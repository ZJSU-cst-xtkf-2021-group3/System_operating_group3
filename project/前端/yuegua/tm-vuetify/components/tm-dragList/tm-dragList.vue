<template>
	<view class="tm-dragList ">
		<view :style="{height:height*list.length+'rpx',width:w+'px'}" class="relative"
			:class="[disabled?'opacity-7':'']">
			<view class="fulled-height "
				:class="[index!==0?'border-t-1':'',bgColor,black_tmeme?'grey-darken-4 bk':'','absolute','tm-dragList-item','shadow-'+(nowMove_index==index?16:0),'flex-between']"
				v-for="(item,index) in listData" :key="index"
				:style="{transition: nowMove_index==index||endDrage?'all 0s':'all 0.1s',top:item.top+'px',height:height+'rpx',width:w+'px',zIndex:nowMove_index==index?5:0}">
				<view class="fulled fulled-height flex-start">
					<view v-if="item['icon']" class="flex-shrink pl-32 fulled-height flex-center">
						<tm-icons :black="black_tmeme" :color="item['color']||'black'" :fllowTheme="fllowTheme" dense
							:name="item['icon']" :size="40"></tm-icons>

					</view>
					<view class="pl-32 text-size-n" :class="[black_tmeme?'bk':'']">{{item.text}}</view>
				</view>
				<view @touchstart="m_start($event,index)" @mousedown="m_start($event,index)"
					@touchmove.stop.prevent="m_move($event,index)" @mousemove.stop.prevent="m_move($event,index)"
					@touchend="m_end($event,index)" @mouseup="m_end($event,index)"
					class="flex-shrink flex-end fulled-height" style="width: 100rpx;">
					<text class="iconfont icon-menu pr-32  text-size-n"
						:class="[black_tmeme?' bk text-grey-darken-2':'text-grey']"></text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	/**
	 * 拖放排序
	 * @property {String | Boolean} black = [true|false] 默认：null，是否开启暗黑模式
	 * @property {String | Boolean} disabled = [true|false] 默认：false，是否禁用，禁用后无法操作。
	 * @property {Number} width = [] 默认：0，组件的宽度，rpx,可不提供，默认为父组件的宽度。
	 * @property {Number} height = [] 默认：120，列表项目的高度，rpx,
	 * @property {String} bgColor = [] 默认：white，项目的背景色
	 * @property {String} right-icon = [] 默认：''，项目右边可拖动的图标
	 * @property {String} rang-key = [] 默认：'text'，列表项目读取文本的key
	 * @property {String} list = [] 默认：[]，列表数据[{text: "菜单选项",icon: 'icon-menu',color:'red'}]
	 * @param {Function} change 拖动排序后，触发，返回新的排序后list数据。
	 */
	import tmIcons from '@/tm-vuetify/components/tm-icons/tm-icons.vue';
	export default {
		name: "tm-dragList",
		components: {
			tmIcons
		},
		props: {
			disabled: {
				type: String | Boolean,
				default: false
			},
			// 跟随主题色的改变而改变。
			fllowTheme: {
				type: Boolean | String,
				default: true
			},
			// 是否开启暗黑模式
			black: {
				type: String | Boolean,
				default: null
			},
			width: {
				type: Number,
				default: 0
			},
			height: {
				type: Number,
				default: 120
			},
			list: {
				type: Array,
				default: () => {
					return []
				}
			},
			rangKey: {
				type: String,
				default: 'text'
			},
			rightIcon: {
				type: String,
				default: "icon-menu"
			},
			bgColor: {
				type: String,
				default: "white"
			},

		},
		destroyed() {
			clearTimeout(999)
		},
		watch: {
			list: {
				deep: true,
				handler() {
					this.jishunTopData();
				}
			}
		},
		data() {
			return {
				w: 0,
				h: 0,
				totalH: 0,
				y: 0,
				listData: [], //被处理过的数据。
				new_index: null, //即将被替换的索引（实质性被替换）
				nowMove_index: null, //现在正在移动的索引
				olde_Data: null, //即将被替换的数据
				olde_index: null, //即将被替换的索引（虚拟，用来调整顺序位置，实质不会被替换）
				max_bottom: 0, //不能超过移动底部的位置。
				new_item: [], //虚拟列表，内部排列好，但未在页面中渲染。
				endDrage: false,

			};
		},
		computed: {
			black_tmeme: function() {
				if (this.black !== null) return this.black;
				return this.$tm.vx.state().tmVuetify.black;
			},
		},
		async mounted() {
			let t = this;
			this.jishunTopData();
		},
		methods: {
			jishunTopData() {
				this.$nextTick(async function() {
					this.listData = [];

					let p = await this.$Querey(".tm-dragList", this).catch(e => {})
					this.w = uni.upx2px(this.width) || p[0].width;
					this.h = uni.upx2px(this.height)
					this.max_bottom = p[0].height - this.h
					this.totalH = this.h * this.list.length
					let list = [];
					for (let i = 0; i < this.list.length; i++) {
						let p = this.list[i];
						p['top'] = i * this.h;
						this.listData.push(p)
					}

				})
			},
			m_start(event, index) {
				event.preventDefault()
				event.stopPropagation()
				if (this.disabled) return;
				this.olde_Data = this.listData[index];
				this.nowMove_index = index;
				this.olde_index = index;
				this.endDrage = false;
				this.new_item = this.listData;
				if (event.type.indexOf('mouse') == -1 && event.changedTouches.length == 1) {
					var touch = event.changedTouches[0];

					this.y = touch.pageY - event.currentTarget.offsetTop - this.listData[index].top
				} else {
					this.y = event.pageY - event.currentTarget.offsetTop - this.listData[index].top
				}

				// #ifdef MP || APP
				uni.vibrateShort({})
				// #endif
			},
			m_move(event, index) {
				if (this.disabled) return;
				let t = this
				event.preventDefault()
				event.stopPropagation()

				if (t.nowMove_index == null) return;
				if (event.type.indexOf('mouse') == -1 && event.changedTouches.length == 1) {
					var touch = event.changedTouches[0];
					let ch = touch.pageY - t.y

					// if (t.listData[index].top >= 0 && t.listData[index].top <= t.max_bottom) {
						
					// }
					
					t.listData.splice(index, 1, {
						...t.listData[index],
						top: ch
					})
					let top =t.listData[index].top
					let oldtop =t.olde_Data.top
					if(top<=0) top =0;
					if(top>=t.max_bottom) top=t.max_bottom;
					
					let dirvect = top - t.olde_Data.top;
					
					let num = Math.round(Math.abs(dirvect) / t.h);
					
					if (dirvect >= 0) {
						t.new_index = index + num;
					} else {
						t.new_index = index - num;
					}

					if (t.new_index !== index && t.olde_index != t.new_index) {
						t.listData.splice(t.new_index, 1, {
							...t.listData[t.new_index],
							top: t.olde_index * t.h
						})

						let newItems = [...t.listData];
						newItems.splice(index, 1)
						newItems.splice(t.new_index, 0, t.listData[index])
						t.new_item = [...newItems];
						// #ifdef MP || APP
						uni.vibrateShort({})
						// #endif
					} else if (t.new_index === t.olde_index && index == t.olde_index) {
						let orindex = t.olde_index + 1;
						if (dirvect > t.h) {
							orindex = t.new_index;
						}

						t.listData.splice(orindex, 1, {
							...t.listData[orindex],
							top: orindex * t.h
						})
						let newItems = [...t.listData];
						newItems.splice(orindex, 1)
						newItems.splice(orindex, 0, t.listData[orindex])
						t.new_item = [...newItems];
						// #ifdef MP || APP
						uni.vibrateShort({})
						// #endif

					}

					t.olde_index = t.new_index



				} else {
					let ch = event.pageY - t.y
					if (event.currentTarget.offsetTop >= 0 && event.currentTarget.offsetTop <= t.max_bottom) {
						t.listData.splice(index, 1, {
							...t.listData[index],
							top: ch
						})
					}
					let dirvect = t.listData[index].top - t.olde_Data.top;
					let num = Math.round(Math.abs(dirvect) / t.h);
					if (dirvect >= 0) {
						t.new_index = index + num;
					} else {
						t.new_index = index - num;
					}

					if (t.new_index !== index && t.olde_index != t.new_index) {
						t.listData.splice(t.new_index, 1, {
							...t.listData[t.new_index],
							top: t.olde_index * t.h
						})

						let newItems = [...t.listData];
						newItems.splice(index, 1)
						newItems.splice(t.new_index, 0, t.listData[index])
						t.new_item = [...newItems];

					} else if (t.new_index === t.olde_index && index == t.olde_index) {
						let orindex = t.olde_index + 1;
						if (dirvect > t.h) {
							orindex = t.new_index;
						}

						t.listData.splice(orindex, 1, {
							...t.listData[orindex],
							top: orindex * t.h
						})
						let newItems = [...t.listData];
						newItems.splice(orindex, 1)
						newItems.splice(orindex, 0, t.listData[orindex])
						t.new_item = [...newItems];


					}

					t.olde_index = t.new_index

				}



			},
			m_end(event, index) {
				if (this.disabled) return;
				let t = this;
				event.preventDefault()
				event.stopPropagation()
				this.nowMove_index = null;
				this.endDrage = true;
				if (this.new_index == null) return;
				if (event.type.indexOf('mouse') == -1 && event.changedTouches.length == 1) {
					let tid = 999
					clearTimeout(tid)
					let now_index = index;
					tid = setTimeout(function() {

						let newItems = [...t.new_item];

						for (let i = 0; i < newItems.length; i++) {
							let p = newItems[i];
							p['top'] = i * t.h;
							p['zIndex'] = 0;
						}
						t.listData = [...newItems]
						t.moveChange();
						// #ifdef MP || APP
						uni.vibrateShort({})
						// #endif
					}, 50);
				} else {
					let tid = 999
					clearTimeout(tid)
					let now_index = index;
					tid = setTimeout(function() {
						let newItems = [...t.new_item];

						for (let i = 0; i < newItems.length; i++) {
							let p = newItems[i];
							p['top'] = i * t.h;
							p['zIndex'] = 0;
						}
						t.listData = [...newItems]
						t.moveChange();
					}, 50);
				}
			},
			
			moveChange(e, index) {
				if (this.disabled) return;
				//change后修改的数据 。
				this.$emit('change', this.listData);
			}
		},
	}
</script>

<style lang="scss">
	.tm-dragList-item {}
</style>
