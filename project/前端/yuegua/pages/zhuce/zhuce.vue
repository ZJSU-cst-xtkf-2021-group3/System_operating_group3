<template>
	<view class="content">
		
		<!-- <view class="login_img"><image mode="aspectFill" src="/static/image/iamhe.png"></image></view> -->
		
		<view class="login_from">
			
			<view class="login_from_input">
				<view class="login_from_name">用户名</view>
				<view class="login_from_fun"><input v-model="username" type="text" placeholder="请输入用户名(6个字符之内)"></view>
			</view>

			<view class="login_from_input">
				<view class="login_from_name">密码</view>
				<view class="login_from_fun"><input v-model="password" type="digit" password="true" placeholder="请输入登录密码"></view>
			</view>

			<view class="login_from_input">
				<picker @change="bindPickerChange" :value="index" :range="array" range-key="age">
					<view style="padding: 20rpx;background-color: white;">{{ array[index].age }}</view>
				</picker>					
			</view>
				
			
			<view class="login_from_dl">
				<button @click="denglu">注册</button>
			</view>
			
		</view>
		
	</view>
</template>
<script>
	
   export default {

   data(){
     return {
		username:"",
		password:"",
		array: [{ age: '15~25岁' }, { age: '26~35岁' }, { age: '36~50岁' }, { age: '50岁以上' }],
		index: 2,
 
	}
	   },
    onLoad(){
     },
    methods: {
		bindPickerChange: function(e) {
					this.index = e.detail.value;
				},
		denglu(){
			var that = this
			    uni.request({
				    header:{
					    "Content-Type":"application/x-www-form-urlencoded",
					    },
				    url: "http://101.37.175.115/UserAccess/register",
					data:{
						username:that.username,
						password:that.password,
						age:"1",
						wechat:"2",
						introduction:"3",
						header:"file:///Users/lishengdi/Downloads/IMG_3531.JPG"
						
					},
					method:"POST",
				    success(res){
					    if(res.data.res=='ok'){
							console.log("ok")
							uni.showToast({
			                          title: '注册成功',
				                      icon:'success',
			                          duration: 2000
			                       }),
			                uni.redirectTo({
				                      url:"../load/load"
			              })
						}
						console.log(res.data.res)
						console.log(that.username)
					   
				    }
			})
			
		},
		
		
			
     }
 }
</script>
<style scoped>
	
	page{ background: #fff; }
	
	.login_from{ width: 100%; height: auto; box-sizing: border-box; padding: 20upx 8%; }
	
	.login_from_input{ width: 100%; height:auto; display: flex; flex-direction: row; justify-content: space-between; align-items: center; border-bottom: 1px #eee solid; padding: 40upx 0px; margin: 0px auto;  } 
		
	.login_from_name{ width: 20%; }
	.login_from_fun{ width: 80%; display: flex; flex-direction: row; justify-content: flex-end; align-items: center;  }
	.login_from_fun input{ width: 100%; text-align: left; font-size: 14px;  }
	
	
	.login_from_dl{ width: 100%; height: 50px; line-height: 50px; margin-top: 150upx;   }
	.login_from_dl button{ width: 100%; height: 50px; line-height: 50px; background: #000000; color: #fff; border-radius: 50px; }
	
	
	.cuIcon-squarecheckfill{ color: #000000; }
	.logo_text text{ color: #FF3B00; }
	
	.getyzm{ width: 60%; display: flex; flex-direction: row; justify-content: flex-end; color: #FF3B00; }
	.cuicon{ font-size: 18px; }  
	
</style>
