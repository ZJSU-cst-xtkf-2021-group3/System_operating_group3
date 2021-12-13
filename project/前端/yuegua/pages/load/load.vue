<template>
	<view class="container" :style="(ispdFocus || isuserFocus)?containerHeight.focus:containerHeight.blur">
		<view class="welcome-text">
			<text class="intro">欢迎来到阅卦</text>
		</view>
		<view class="input-area">
			<view class="user-icon">
				<image :src="userImg" :style="isDisabledBtn?'opacity:1':'opacity:1'"></image>
			</view>
			<!-- 用户名输入框 -->
			<view class="input-text" :style="isuserFocus?input_boder_style.focus:input_boder_style.blur">
				<view :style="isuserFocus?label_style.focus:label_style.blur">
					帐 号
				</view>

				<u-input :focus="un" v-model="userLoginInfo.userName" type="text" :height="100" placeholder="" :custom-style="customStyle"
				 :clearable="false" @focus="userFocus" @blur="userBlur" />

				<view class="clear" @click="clearInput('userName')" v-show="userLoginInfo.userName!=='' && isuserFocus">
					<image :src="clearImg" class="img"></image>
				</view>
			</view>
			<!-- 密码输入框 -->
			<view class="input-text" :style="ispdFocus?input_boder_style.focus:input_boder_style.blur">
				<view :style="ispdFocus?label_style.focus:label_style.blur">
					密 码
				</view>

				<u-input :focus="pd" v-model="userLoginInfo.password" type="password" :password-icon="false" :height="100"
				 placeholder="" :maxlength="pdMaxLength" :custom-style="customStyles" :clearable="false" @focus="pdFocus" @blur="pdBlur" />

				<view class="clear" @click="clearInput('password')" v-show="userLoginInfo.password!=='' && ispdFocus">
					<image :src="clearImg" class="img"></image>
				</view>
			</view>

			<!-- 登录按钮 -->
			<view class="btn">
				<u-button size="default" :loading="isLogining" :ripple="true" :custom-style="isDisabledBtn?login_btn_style.disabled:login_btn_style.able"
				 :disabled="isDisabledBtn" @click="login">{{isLogining?'':'登 录'}}</u-button>
			</view>
            <view style="text-align: right;margin-top: 10rpx;">
                <text>如果你没有账户，请点击</text>
				<text style="color: #007AFF;text-decoration: underline;" @click="clickzhuce">注册账号</text>
            </view>
			<u-toast ref="uToast"></u-toast>
		</view>
		<view class="copy-right"></view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// ------------- 其他 -------------
				userLoginInfo: {
					userName: '',
					password: ''
				},

				// 整体容器高度，单位 rpx

				// containerHeight: 1000,
				containerHeight: {
					focus: 'height:800rpx;transition:0.2s',
					blur: 'height:1300rpx;transition:0.2s'
				},

				// 获取焦点时，整体上移的动画效果
				animationData: {},

				// 登录界面的用户图标
				userImg: '../../static/icons/用户-圆.png',

				// 是否正在清除
				isClearing: false,

				// ------------- 输入框 -------------
				pdMaxLength: 10,
				// 输入框是否获取到焦点
				isuserFocus: false,
				ispdFocus: false,

				// 输入框自定义样式
				customStyles: {
					"padding-left": "40rpx",
					// 使光标消失（iOS无效果）
					"color": "transparent",
					"text-shadow": "0 0 0 #000"
				},

				// 清除按钮图标
				clearImg: '../../static/img/clear.png',

				// 输入框 label 样式
				label_style: {
					focus: 'width:100rpx;display:flex;justify-content:center;color:#1890FF;font-weight:bold;transform:scale(1.1)',
					blur: 'width:100rpx;display:flex;justify-content:center;color:#aaaaaa;transform:scale(1)'
				},

				input_boder_style: {
					focus: 'border-bottom: 1px solid #1890FF;',
					blur: 'border-bottom: 1px solid #e4e4e4;'
				},

				// ------------- 登录按钮 -------------
				// 登录按钮自定义样式
				login_btn_style: {
					able: {
						"width": "100%",
						"height": "100rpx",
						"border-radius": "20rpx",
						"border": "#e4e4e4",
						"background-color": "#1890FF",
						"color": "#fff",
						"font-size":"35rpx",
					},
					disabled: {
						"width": "100%",
						"height": "100rpx",
						"border-radius": "20rpx",
						"border": "#e4e4e4",
						"background-color": "#000000",
						"color": "#fff",
						"opacity": "0.5",
						"font-size":"35rpx",
					}
				},

				// 点击登录按钮后，接口返回数据前，对该操作上锁
				isLogining: false,

				un: false,
				pd: false,

				isDisabledBtn: true
			}
		},
		methods: {
			userFocus() {
				// 是否在焦点上
				this.isuserFocus = true
			},
			userBlur() {
				setTimeout(() => {
					this.isuserFocus = false
				}, 1)
			},

			pdFocus() {
				this.ispdFocus = true
			},
			pdBlur() {
				// 失去焦点事件先于清除事件触发，因此让其延迟即可先触发 clearInput 事件
				setTimeout(() => {
					this.ispdFocus = false
				}, 1)
			},
			clickzhuce(){
				uni.navigateTo({
					url:'../zhuce/zhuce'
				})
			},
			// 清除 input 内容
			clearInput(value) {
				switch (value) {
					case 'userName':
						// setTimeout(() => {
							this.userLoginInfo.userName = ''
							// 清空内容之后保持焦点
							this.un = false
							this.$nextTick(() => {
								this.un = true
							})
						// }, 2)
						break
					case 'password':
						// setTimeout(() => {
							this.userLoginInfo.password = ''
							this.pd = false
							this.$nextTick(() => {
								this.pd = true
							})
						// }, 2)
						break
				}
			},

			login() {
				var that = this
				    uni.request({
					    header:{
						    "Content-Type":"application/x-www-form-urlencoded",
						    },
					    url:"http://101.37.175.115/UserAccess/login",
						data:{
							username:that.userLoginInfo.userName,
							password:that.userLoginInfo.password,
							
						},
						method:"POST",
					    success(res){
						    if(res.data.res=='check passed'){
								console.log("ok")
								this.isLogining = true
				                setTimeout(()=>{
					            this.isLogining = false
					            this.$refs.uToast.show({
						                 title: '登录成功',
						                 type: 'success'
					              })
				                },2000)
				                uni.switchTab({
					                    url:"../home/home"
				                 })
							}
							console.log(res.data.res)
							console.log(that.userLoginInfo.userName)
						   
					    }
				})
			}
			
		},
		watch: {
			userLoginInfo: {
				handler(newVal, oldVal) {
					if ((newVal.userName !== '') && (newVal.password !== '')) {
						this.isDisabledBtn = false
					} else {
						this.isDisabledBtn = true
					}
				},
				deep: true
			}
		}
	}
</script>

<style lang="scss" scoped>
	// $screen-height:1330rpx;

	.container {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		align-items: flex-end;
		width: 100%;

        .welcome-text{
             width: 100%;
             font-size: 20px;
             display: flex;
             justify-content: center;
            }
		.input-area {
			width: 80%;
			.user-icon {
				width: 100%;
				display: flex;
				justify-content: center;

				>image {
					width: 150rpx;
					height: 150rpx;
				}
			}

			.input-text {
				display: flex;
				flex-wrap: nowrap;
				align-items: center;
				margin-top: 20rpx;

				.clear {
					height: 100rpx;
					display: flex;
					align-items: center;

					.img {
						height: 36rpx;
						width: 36rpx;
					}
				}
			}

			.btn {
				margin-top: 40rpx;

				.login-btn {
					width: 100%;
					border-radius: 20rpx;
					border: $uni-color-primary;
					background-color: $uni-color-primary;
					color: $uni-text-color-inverse;
				}
				.enroll{
					// width: 100%;

			    }
			}
			
		}

		.copy-right {
			// bottom: 100rpx;
			bottom: 0;
			width: 100%;
			color: $uni-text-color-grey;
			text-align: center;
			font-size: 24rpx;
		}
	}
</style>