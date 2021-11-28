<template>
	<view class="content">
		
		<!-- <view class="login_img"><image mode="aspectFill" src="/static/image/iamhe.png"></image></view> -->
		
		<view class="login_from">
			
			<view class="login_from_input">
				<view class="login_from_name">用户名</view>
				<view class="login_from_fun"><input type="text" placeholder="请输入用户名(6个字符之内)"></view>
			</view>

			<view class="login_from_input">
				<view class="login_from_name">密码</view>
				<view class="login_from_fun"><input type="digit" password="true" placeholder="请输入登录密码"></view>
			</view>

			<view class="login_from_input">
				<view class="login_from_name">邀请码</view>
				<view class="login_from_fun">
					<input type="text" placeholder="请输入邀请码">
					<label class="cuIcon-scan cuicon"></label>
				</view>
			</view>
				
			
			<view class="login_from_dl">
				<button @click="denglu">确定</button>
			</view>
			
			<view class="logo_xieyi">
				<label @click="moutcl" :class="gouxSta?'cuIcon-squarecheckfill':'cuIcon-square'"></label>
				<view class="logo_text">请勾选并阅读<text>《注册协议》</text>及<text>《隐私协议》</text></view>
			</view>
			
		</view>
		
	</view>
</template>
<script>
	
	



   export default {

   data(){
     return {
		//value3: [],
		//label3: '',
		//list1: areaData,
		
		gouxSta:false,
		times:60,
		yzmbotshou:true,
		yzmbothide:false
		 
	}
	   },
    onLoad(){
     },
    methods: {
		
		moutcl(){
			if( this.gouxSta == false){
				this.gouxSta = true
			}else{
				this.gouxSta = false
			}
		},
		
		denglu(){
			if( this.gouxSta == false){
				uni.showToast({
					"title":"请阅读并勾选用户协议",
					"icon":'none'
				})				
			}else{
				uni.showToast({
					"title":"账号不存在",
					"icon":'none'
				})
			}		
		},
		
		
			
     }
 }
</script>
<style>
	
	page{ background: #fff; }
	
	.login_img{ width: 100%; height: auto; margin-top: 90upx; }
	.login_img image{ width: 170upx; height: 170upx; display: block; margin: 0px auto; border-radius: 50%; }
	
	.login_from{ width: 100%; height: auto; box-sizing: border-box; padding: 20upx 8%; }
	
	.login_from_input{ width: 100%; height:auto; display: flex; flex-direction: row; justify-content: space-between; align-items: center; border-bottom: 1px #eee solid; padding: 40upx 0px; margin: 0px auto;  } 
		
	.login_from_name{ width: 20%; }
	.login_from_fun{ width: 80%; display: flex; flex-direction: row; justify-content: flex-end; align-items: center;  }
	.login_from_fun input{ width: 100%; text-align: left; font-size: 14px;  }
	
	
	.login_from_dl{ width: 100%; height: 50px; line-height: 50px; margin-top: 150upx;   }
	.login_from_dl button{ width: 100%; height: 50px; line-height: 50px; background: #000000; color: #fff; border-radius: 50px; }
	
	.logo_xieyi{ width: 100%; height: 40px; line-height: 40px; display: flex; flex-direction: row; margin-top: 30upx; align-items: center; color: #444; font-size: 14px; justify-content: center; }
	.logo_xieyi label{ font-size: 18px; margin-right: 1%; }
	
	.cuIcon-squarecheckfill{ color: #000000; }
	.logo_text text{ color: #FF3B00; }
	
	.getyzm{ width: 60%; display: flex; flex-direction: row; justify-content: flex-end; color: #FF3B00; }
	.cuicon{ font-size: 18px; }  
	
</style>
