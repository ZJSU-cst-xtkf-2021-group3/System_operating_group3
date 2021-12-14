<script>
	export default {
		onLaunch: function() {
			console.warn('当前组件仅支持 uni_modules 目录结构 ，请升级 HBuilderX 到 3.1.0 版本以上！')
			console.log('App Launch')
		},
		onShow: function() {
			// var that = this
			console.log('App Show')
	// 		   setInterval(function () {
				   
	// 			   uni.request({
	// 			       url: 'http://101.37.175.115/Message/RTMSG', 
				       
	// 			   	header: {
	// 			   	        'Content-Type': 'application/x-www-form-urlencoded' 
	// 			   	    },
	// 			   		method:"GET",
				   		
	// 			       success: (res) => {
				   		
	// 			          if(res.data.res=="ok"){
	// 			   			if(res.data.isEmpty==false){
	// 			   				uni.setStorage({
	// 			   				    key: 'RTMSG',
	// 			   				    data: res.data.data,
	// 			   				    success: function () {
	// 			   				        console.log('msg arrive');
	// 			   				    }
	// 			   				});
	// 							that.$options.globalData.hasNotify=true
	// 			   			}
	// 						else{
	// 							that.$options.globalData.hasNotify=false
	// 						}
							
							
	// 			   	   }
	// 			       }		   	
	// 			   });
	
	// 			   }, 21000)

			
		},
		onHide: function() {
			console.log('App Hide')
		},
		globalData:{
			hasNotify:false
		},
	}
</script>

<style lang="scss">
	/*每个页面公共css */
	@import "@/tm-vuetify/mian.min.css";
	// <!-- 主题包 -->
	
	@import "@/uview-ui/index.scss";
	@import '@/static/variables.scss';
	/*每个页面公共css */
	@import '@/uni_modules/uni-scss';
	/* #ifndef APP-NVUE */
	@import '@/static/customicons.css';
	
	// 设置整个项目的背景色
	
	page {
		background-color: #f6f7f8;
	}

	/* #endif */
	.page{
		@extend %basepage
	}

</style>
