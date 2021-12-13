<template>
	<view :key="cKey" class="tm-lottie flex-center">
		<!-- #ifndef H5 -->

		<canvas :style="{ width: w_w + 'px', height: h_h + 'px' }" id="cid" canvas-id="cid"></canvas>
		<!-- #endif -->
		<!-- #ifdef H5 -->

		<canvas :style="{ width: w_w + 'px', height: h_h + 'px' }" :id="cuid" :canvas-id="cuid"></canvas>
		<!-- #endif -->
	</view>
</template>

<script>
import lottie from 'tm-vuetify/tool/function/lottie.js';
export default {
	name: 'tm-lottie',
	props: {
		width: {
			type: Number | String,
			default: 420
		},
		height: {
			type: Number | String,
			default: 420
		},
		url: {
			type: String||Object,
			default: ()=>{
				return "";
			}
		},
		loop: {
			type: Boolean,
			default: true
		},
		autoplay: {
			type: Boolean,
			default: true
		}
	},
	computed: {
		w_w: function() {
			return uni.upx2px(this.width);
		},
		h_h: function() {
			return uni.upx2px(this.height);
		}
	},
	data() {
		return {
			cuid: 'cid',
			cKey: ''
		};
	},
	created() {
		// #ifdef H5
		this.cuid = this.$tm.guid();
		// #endif
		this.cKey = this.$tm.guid();
	},
	destroyed() {
		// 释放内存。
		lottie.destroy()
	},
	async mounted() {
		if (this.url) {
			this.$nextTick(async function() {
				await this.LoadLottiePlay_Mp();
			});
		}
	},
	methods: {
		async LoadLottiePlay_Mp(url) {
			const canvasContext = uni.createCanvasContext(this.cuid, this);

			//  请求到的lottie json数据
			let animationData=null
			// 请求lottie的路径。注意开启downloadFile域名并且返回格式是json
			const animationPath = url || this.url;// url || this.url
			if(typeof animationPath ==='string'&&animationPath!=''){
				let p = await this.rloadJson(animationPath).catch(e=>{
					uni.$tm.toast(JSON.stringify(e));
				})
				animationData = JSON.parse(p.data.data)
				
			}else{
				animationData = url;
			}
			if(!animationData) return;
			
			// 指定canvas大小
			canvasContext.canvas = {
				width: this.w_w,
				height: this.h_h
			};
			try {
				// 如果同时指定 animationData 和 path， 优先取 animationData
				lottie.loadAnimation({
					renderer: 'canvas', // 只支持canvas
					loop: this.loop,
					autoplay: this.autoplay,
					animationData: animationData,
					path: '',
					rendererSettings: {
						context: canvasContext,
						clearCanvas: true
					}
				});
			} catch (e) {
				console.log(e);
			}
		},
		async LoadLottiePlay_H5(url) {
			const canvasContext = uni.createCanvasContext(this.cuid, this);
		
			//  请求到的lottie json数据
			let animationData=null
			// 请求lottie的路径。注意开启downloadFile域名并且返回格式是json
			const animationPath = url || this.url;// url || this.url
			
			
			// 指定canvas大小
			canvasContext.canvas = {
				width: this.w_w,
				height: this.h_h
			};
			try {
				// 如果同时指定 animationData 和 path， 优先取 animationData
				lottie.loadAnimation({
					renderer: 'canvas', // 只支持canvas
					loop: this.loop,
					autoplay: this.autoplay,
					animationData: '',
					path: animationPath,
					rendererSettings: {
						context: canvasContext,
						clearCanvas: true
					}
				});
			} catch (e) {
				console.log(e);
			}
		},
		play() {
			lottie.play();
		},
		stop() {
			lottie.stop();
		},
		pause() {
			lottie.pause();
		},
		rloadJson(url){
			
			return new Promise((res,rej)=>{
				
				uni.request({
					responseType:'json',
					url:url,
					success: (v) => {
						
						res(v)
					},
					fail: (e) => {
						console.log(e);
						rej(e)
					}
				})
			})
		},
		// type:1正向播放，-1反向
		setDirection(type = 1) {
			lottie.setDirection(type);
		},
		async registerAnimation(url) {
			if (!url) return;
			lottie.destroy();
			this.cKey = this.$tm.guid();
			await this.LoadLottiePlay_Mp(url);
			lottie.resize();
		}
	}
};
</script>

<style lang="scss"></style>
