<template>
	<view class="tm-stepper  d-inline-block" >
		<view class="flex-center" :style="{minWidth: 200+'rpx',width:`${width}rpx`}">
			<tm-button @touchcancel="endlongpressEvent" 
			@touchend="endlongpressEvent"
			 @touchstart="$emit('touchstart','minus')"
			  @longpress="longpressEvent('-')" 
			  :fllowTheme="fllowTheme" 
			  :disabled="isJianDisabled||disabled?true:false" 
			  :shadow="(isJianDisabled||disabled)?0:shadwo_num" 
			  :black="black_tmeme"  @click="setStep('-')" :item-class="` round-l-${round} `" icon-size="24"  height="40" round="0"
			:theme="disabled?'':color_tmeme "  style="width:70rpx;" :height="height" block icon="icon-minus"></tm-button>
			<input @blur="jianchData" @input="inputVal" :disabled="disabled" v-model="setVal" type="number" :style="{height:`${height}rpx`,width:'calc(100% - 140rpx)'}" 
			class="text-align-center grey-lighten-4 text-size-n fulled"
			:class="[
				`text-${font_color}`,
				black_tmeme?'grey-darken-4 bk':''
			]"
			 />
			<tm-button @touchcancel="endlongpressEvent" @touchend="endlongpressEvent" @touchstart="$emit('touchstart','add')" @longpress="longpressEvent('+')" :fllowTheme="fllowTheme" :shadow="(isJianDisabled||disabled)?0:shadwo_num" :black="black_tmeme"  @click="setStep('+')"  :item-class="` round-r-${round} `" icon-size="24" height="40"   round="0" 
			:theme="disabled?'':color_tmeme " :disabled="isAddDisabled||disabled?true:false" style="width:70rpx;" :height="height"  block icon="icon-plus"></tm-button>
		</view>
	</view>
</template>

<script>
	/**
	 * 步进器
	 * @property {String|Number} value = [] 默认：''，值，推荐使用value.sync或者v-model
	 * @property {Boolean} disabled = [] 默认：false，是否禁用
	 * @property {Boolean} black = [] 默认：false，是否暗黑模式。
	 * @property {Number|String} step = [] 默认：1， 步幅。
	 * @property {String} color = [] 默认：primary， 主题色。
	 * @property {String} fontColor = [] 默认：black， 输入框的文字主题色。
	 * @property {String|Number} round = [] 默认：3， 圆角。
	 * @property {String|Number} shadow = [] 默认：3， 圆角。
	 * @property {String|Number} max = [] 默认：999， 最大值。
	 * @property {String|Number} min = [] 默认：0， 最小值。
	 * @property {String|Number} width = [] 默认：200， 宽度，单位rpx。
	 * @property {String|Number} height = [] 默认：70， 高度，单位rpx。
	 * @property {String} name = [] 默认：''，提交表单时的的字段名称标识
	 * @example <tm-stepper  value="50"></tm-stepper>
	 */
	import tmButton from "@/tm-vuetify/components/tm-button/tm-button.vue"
	
	export default {
		components:{tmButton},
		name:"tm-stepper",
		model:{
			prop:"value",
			event:'input'
		},
		props:{
			
			value:{
				type:Number|String,
				default:0
			},
			//提交表单时的的字段名称
			name:{
				type:String,
				default:''
			},
			disabled:{
				type:Boolean,
				default:false
			},
			black:{
				type:Boolean|String,
				default:null
			},
			// 步幅，默认1
			step:{
				type:Number,
				default:1
			},
			color:{
				type:String,
				default:'primary'
			},
			fontColor:{
				type:String,
				default:'black'
			},
			round:{
				type:String|Number,
				default:3
			},
			shadow:{
				type:String|Number,
				default:3
			},
			// 跟随主题色的改变而改变。
			fllowTheme:{
				type:Boolean|String,
				default:true
			},
			max:{
				type:Number|String,
				default:999
			},
			min:{
				type:Number|String,
				default:0
			},
			height:{
				type:Number|String,
				default:60
			},
			width:{
				type:Number|String,
				default:180
			}
		},
		data() {
			return {
				setVal:'',
				timeid:598985656,
			};
		},
		mounted() {
			this.setVal = this.value;
		},
		computed: {
			isJianDisabled(){
				if(isNaN(parseInt(this.setVal))) return false;
				if(parseInt(this.setVal) <=this.min) return true;
				return false
			},
			isAddDisabled(){
				if(isNaN(parseInt(this.setVal))) return false;
				if(parseInt(this.setVal) >=this.max) return true;
				return false
			},
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
			font_color:function(){
				if(this.fontColor) return this.fontColor;
				return this.color;
			},
			shadwo_num:function(){
				if(typeof this.shadow !== 'undefined') return this.shadow;
				return 3;
			}
		},
		destroyed() {
			clearInterval(this.timeid)
		},
		methods: {
			setStep(ty) {
				if(this.disabled) return;
				// if(isNaN(parseInt(this.value))) return;
				
				let pval = parseInt(this.value);
				if(isNaN(parseInt(this.value))) pval=0
				if(ty=='+'){
					pval += parseInt(this.step)
				}else{
					pval -= parseInt(this.step)
				}
				if(pval<0){
					if(pval <= this.min){
						pval=this.min;
					}
					clearInterval(this.timeid)
				}else if(pval >= this.max){
					pval=this.max;
					clearInterval(this.timeid)
					
				}
				this.$nextTick(function(){
					this.setVal =  String(pval)=='NaN'?'':String(pval);
					this.$emit('input',this.setVal)
					this.$emit('update:value',this.setVal)
				})
				
			},
			inputVal(e){
				let val = parseInt(e.detail.value);
				
				if(val < this.min){
					val= this.min;
				}
				if(val > this.max){
					this.setVal = ""
					val= String(this.max);
				}
				
				
				this.$nextTick(function(){
					this.setVal = String(val)=='NaN'?'':String(val);
					this.$emit('input',this.setVal);
					this.$emit('update:value',this.setVal);
				})
				
			},
			jianchData(){
				let val = parseInt(this.setVal);
				if(val <= this.min){
					val= this.min;
				}
				if(val >= this.max){
					val= this.max;
				}
				this.setVal = String(val)=='NaN'?'':String(val);
				this.$emit('input',this.setVal);
				this.$emit('update:value',this.setVal);
			},
			longpressEvent(ty){
				if(this.disabled) return;
				let t =this;
				clearInterval(this.timeid)
				this.timeid = setInterval(function(){
					t.setStep(ty)
				},250)
			},
			endlongpressEvent(ty){
				clearInterval(this.timeid)
			}
		},
		
	}
</script>

<style lang="scss">

</style>
