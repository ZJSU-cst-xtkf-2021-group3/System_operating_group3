<!-- 开关。 -->
<template>
	<view @click="onclick" class="d-inline-block tm-switch " >
		<view class="tm-switch-wk relative ">
			<view class="tm-switch-bg  round-l-24 round-r-24 flex-between"
			:class="[bgColorCusjs,loaddingState?'opacity-7':'']"
			
			>
				<view  class="text-size-xs tm-switch-txt text-align-center flex-center" >
					<text>{{text[0]?text[0]:''}}</text>
				</view>
				<view   class="text-size-xs tm-switch-txt text-align-center text-grey flex-center">
					<text>{{text[1]?text[1]:''}}</text>
				</view>
				
				
			</view>
			<!-- bar -->
			<view :animation="changValue?animationOn:animationOff" class="tm-switch-wk-bar absolute rounded white  flex-center " 
			:class="[changValue?'shadow-'+color+'-10':'',changValue?'on':'']">
				<text v-if="loaddingState" class="iconfont icon-loading" :class="[loaddingState?'load':'',`text-${color_tmeme}`]"></text>
			</view>
		</view>
	</view>
</template>

<script>
	/**
	 * 开关
	 * @property {String|Boolean} value = [true|false] 同v-model一样的值，如果需要双向绑定需要value.sync，推荐使用v-model
	 * @property {String|Number|Boolean|Object} name = [] 自定义数据，change时携带。
	 * @property {Function} change {checked,value:携带的name数据}
	 * @property {Boolean} disabled = [true|false] 默认：false, 禁用
	 * @property {String} color = [] 默认：primary, 主题色
	 * @property {Boolean} black = [true|false] 默认：false, 暗黑模式
	 * @property {Boolean} loadding = [true|false] 默认：false, 是否加载中
	 * @property {Array} text = [true|false] 默认： ['开','关'], 左右两边的字符
	 * @example <tm-switch v-model="checked"></tm-switch>
	 * 
	 */
	export default {
		name: 'tm-switch',
		model: {
			prop: 'value',
			event: 'input'
		},
		props:{
			value:{
				type:String|Boolean,
				default:false
			},
			name:{
				type:String|Number|Boolean|Object,
				default:''
			},
			// 禁用。
			disabled: {
				type:Boolean|String,
				default:false
			},
			loadding: {
				type:Boolean|String,
				default:false
			},
			color:{
				type:String,
				default:'primary'
			},
			// 暗黑
			black: {
				type:Boolean|String,
				default:null
			},
			// 左右两边的字符。
			text:{
				type:Array,
				default:()=>{
					return ['开','关']
				}
			},
			// 跟随主题色的改变而改变。
			fllowTheme:{
				type:Boolean|String,
				default:true
			}
		},
		watch: {
			value: function(newval, oldval) {
				if (newval !== oldval) {
					if (!this.jiancMax()) {
						this.changValue = false;
						return;
					}
		
					this.change();
				}
			}
		},
		computed: {
			black_tmeme: function() {
				if (this.black !== null) return this.black;
				return this.$tm.vx.state().tmVuetify.black;
			},
			color_tmeme:function(){
				if(this.$tm.vx.state().tmVuetify.color!==null&&this.$tm.vx.state().tmVuetify.color && this.fllowTheme){
					return this.$tm.vx.state().tmVuetify.color;
				}
				return this.color;
			},
			changValue: {
				get: function() {
					return this.value;
				},
				set: function(newValue) {
					this.$emit('input', newValue)
					// 如果不想用v-model. 直接使用value,需要:value.sync
					this.$emit('update:value', newValue);
				}
			},
			loaddingState:function(){
				return this.loadding;
			},
			bgColorCusjs(){
				if(this.disabled) {
					if(this.black_tmeme){
						return 'grey-darken-4   bk';
					}else{
						return 'grey-lighten-1 grey';
					}
				}
				
				if(this.black_tmeme){
					if(this.changValue) return this.color_tmeme + ' bk ';
					if(!this.changValue) return 'grey-darken-1 bk ';
					
				}else{
					if(this.changValue) return this.color_tmeme + ' text-white ';
					if(!this.changValue) return 'grey-lighten-2 text-white ';
				}

				
			}
		},
		data() {
			return {
				animationOn:null,
				animationOff:null,
			};
		},
		mounted() {
			this.aniinit();
		},
		methods: {
			aniinit(){
				 var animation = uni.createAnimation({
				      duration: 500,
				        timingFunction: 'ease',
				    })
				    this.animationOn = animation
				    this.animationOn.left('inherit').translateX(uni.upx2px(56)).step()
				    this.animationOn = animation.export()
				
				var animation2 = uni.createAnimation({
				     duration: 500,
				       timingFunction: 'ease',
				   })
				   this.animationOff = animation2
				   this.animationOff.right('inherit').left(uni.upx2px(4)).step()
				   this.animationOff = animation2.export()
				
				    
			},
			// 检查是否超过了最大选择。
			jiancMax() {
				if(this.disabled) return false;
				return true;
			},
			onclick(e) {
				if (this.disabled||this.loaddingState) return;
			
				if (!this.jiancMax()) {
					return;
				}
				this.changValue = !this.changValue;
				
			},
			change() {
				this.$emit('change', {
					checked: this.changValue,
					value: this.name
				});
			
			}
		},
	}
</script>

<style lang="scss" scoped>
.tm-switch{
	vertical-align: middle;
	.tm-switch-wk{
		width: 100upx;
		height: 48upx;
	}
	.tm-switch-bg{
		width: 100%;
		height: 100%;
		transition: all 0.5s;
		
		.tm-switch-txt{
			width: 50upx;
			height: 100%;
			// line-height: 48upx;
		}
	}
	.tm-switch-wk-bar{
		left: 4upx;
		top: 4upx;
		width:40upx;
		height: 40upx;
		transition: all 0.6s;
		.load{
			animation: xhRote 0.8s infinite linear;
		}
	}
}
@keyframes xhRote{
	0%{
		transform: rotate(0deg);
	}
	
	100%{
		transform: rotate(360deg);
	}
}
</style>
