<template>
	<view class="tm-propressRound d-inline-block">
		<view class="tm-propressRound-text" :style="{
				width:size+'px',
				height:size+'px'
			}">
			<slot name="default" :value="value">
				<text class="text-black" :class="[black?'text-white':'']">{{value}}%</text>
			</slot>
		</view>
		<view class="tm-propressRound-rk">
			<canvas :canvas-id="cid" :id="cid"
			:style="{
				width:size+'px',
				height:size+'px'
			}"
			></canvas>
		</view>
	</view>
</template>

<script>
	/**
	 * 环形进度条
	 * @property {Number} value = [] 默认0，推荐使用v-model赋值。value.sync等同。
	 * @property {Number} size = [] 默认100，圆环大小。
	 * @property {Number} line-width = [] 默认6，圆环线条宽。
	 * @property {Array} color = [] 默认['#FF9800','#E91E63','#FF5722']，激活颜色
	 * @property {String} bgcolor = [] 默认'#EEEEEE'，背景颜色
	 * @property {Function} input 变化时的值。
	 * @property {Function} change 变化时的值。
	 * @example <tm-propressRound v-model="checked"></tm-propressRound>
	 */
	export default {
		name:"tm-propressRound",
		model:{
			prop:"value",
			event:"input"
		},
		props:{
			black:{
				type:Boolean,
				default:false
			},
			size:{
				type:Number,
				default:100
			},
			lineWidth:{
				type:Number,
				default:10
			},
			value:{
				type:Number,
				default:0
			},
			color:{
				type:Array,
				default:()=>{
					return ['rgb(255,152,0)','rgb(233,30,99)','rgb(255,87,34)']
				}
			},
			bgcolor:{
				type:String,
				default:'rgb(238,238,238)'
			}
		},
		data() {
			return {
				ctx:null,
				timid:null,
				jishu:0,
				cid:'fdd_psd'
			};
		},
		computed:{
			
		},
		created() {
			// #ifdef H5 || APP-VUE || APP-PLUS
			this.cid = uni.$tm.guid();
			// #endif
		},
		mounted() {
			
			this.ctx = uni.createCanvasContext(this.cid,this)
			this.creatShape();
			this.startHuiZhi(this.value,0,true)
		},
		destroyed() {
			clearInterval(this.timid)
		},
		watch:{
			
			value:function(newval,oldval){
				if(newval < 0){
					this.$emit("input",0)
					this.$emit("update:value",0)
					this.$emit("change",0)
					return;
				}else if(newval >100){
					this.$emit("input",100)
					this.$emit("update:value",100)
					this.$emit("change",100)
					return;
				}
				this.$emit("input",newval)
				this.$emit("update:value",newval)
				this.$emit("change",newval)
				let blv = newval - oldval;
				if(newval>=100){
					blv = 100 - oldval;
				}
				
				if(blv >= 0 ){
					this.startHuiZhi(blv,oldval,true)
				}else{
					if(newval<=0){
						blv = oldval;
					}
					
					this.startHuiZhi(Math.abs(blv),oldval,false)
				}
			}
		},
		methods: {
			
			startHuiZhi(val,oldv,type){
				clearInterval(this.timid);
				let i = 0;
				let t = this;

				// #ifdef H5
					this.timid = setInterval(()=>{
						i += 1;
						if(i>=val){
							clearInterval(t.timid);
							return;
						}
						if(type){
							t.huizhired(oldv+i,type);
						}else{
							t.huizhired(oldv-i,type);
						}
					},5)
				// #endif
				// #ifndef H5
					if(type){
						t.huizhired(val+oldv,type);
					}else{
						t.huizhired(oldv-val,type);
					}
				// #endif
			},
			// 重新绘制。
			creatShape() {
				if(!this.ctx) return;
				let ctx= this.ctx;
				// this.ctx.translate(this.size / 2,this.size / 2)
				// this.ctx.rotate(270 * Math.PI / 180)
				let x,y,r ;
				x = y = this.size / 2;
				r = (this.size - this.lineWidth*2) / 2
				
				ctx.beginPath()
				ctx.setLineCap('round')
				ctx.setLineWidth(this.lineWidth-1)
				ctx.setStrokeStyle(this.bgcolor)
				
				ctx.arc(x, y, r, -90, 2 * Math.PI)
				
				ctx.stroke()
				
				ctx.draw(true)
				
			},
			huizhired(end=0,type){
				if(!this.ctx) return;
				let ctx = this.ctx;
				
				if(end>=100) end = 100;
				if(end<=0) end = 0;
				let bl = end * 3.6;
				
				bl = bl-90
				let x,y,r ;
				x = y = this.size / 2;
				r = (this.size - this.lineWidth*2) / 2
				ctx.beginPath()
				ctx.setLineCap('round')
				ctx.setLineWidth(type?this.lineWidth-1:this.lineWidth+1)
				ctx.setStrokeStyle(this.bgcolor)
				ctx.arc(x, y, r, -90, 2 * Math.PI)
				ctx.stroke()
				ctx.draw(true)
				
				ctx.beginPath()
				ctx.setLineCap('round')
				ctx.setLineWidth(this.lineWidth)
				var grd=ctx.createLinearGradient(x,0,0,2*x);
				let colorl = this.color.length;
				
				if(colorl==1){
					grd.addColorStop(1,this.color[0]);
				}else if(colorl>1){
					for(let i=0;i<colorl;i++){
						grd.addColorStop(i/(colorl-1),this.color[i]);
					}
				}
				ctx.setStrokeStyle(grd)
				
				ctx.arc(x, y, r, -90 * (Math.PI / 180), bl * (Math.PI / 180))
				
				ctx.stroke()
				
				ctx.draw(true)
				
			},

		},
	}
</script>

<style lang="scss" scoped>
.tm-propressRound{
	position: relative;
	.tm-propressRound-text{
		position: absolute;

		display: flex;
		justify-content: center;
		align-items: center;
		align-content: center;
	}
}
</style>
