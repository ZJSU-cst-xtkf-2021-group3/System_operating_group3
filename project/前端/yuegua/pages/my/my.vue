<template>
	<view>
		<u-transition mode="fade-down" :show="true">
			<view class="headerpanel">
				<!-- <view class="bgimg"></view> -->
				<view class="headerpanel-uinfo">
					<view style="padding-top: 20rpx;">
						<view class="headerpanel-uinfo-name">
							<text style="font-size: 45rpx;font-weight: 550;margin-right: 30rpx;">wuji</text>
						</view>
						<u--text line="2" text="今天天气很好"></u--text>
						<view class="levelbar">
							<u-icon style="margin-right: 10rpx;" name="level" size="18" label="4" space="0"></u-icon>
							<u-line-progress :percentage="30" height="8" activeColor="#1890FF" :showText="false"></u-line-progress>
							<text style="font-size: 10rpx;margin-left: 10rpx;">190/24</text>
						</view>
					</view>
					<view class="avatarpanel">
						<u-avatar size="80" :src="src"></u-avatar>
						<text style="margin-top: 20rpx;color: #A1A1A1;" @click="clickeditinfo">编辑资料</text>
					</view>
				</view>
				<view class="headerpanel-udata">
					<view class="datablock">
						<text style="font-size: 35rpx;font-weight: 550;">33445</text>
						<text style="font-size: 20rpx;">关注</text>
					</view>
					<view class="datablock">
						<text style="font-size: 35rpx;font-weight: 550;">765</text>
						<text style="font-size: 20rpx;">粉丝</text>
					</view>
					<view class="datablock">
						<text style="font-size: 35rpx;font-weight: 550;">945</text>
						<text style="font-size: 20rpx;">发布</text>
					</view>
				</view>
			</view>
		</u-transition>
		<view class="controlpanel">
			<u-icon name="/static/icons/草稿.png" size="30" label="草稿" labelPos="bottom" labelSize="10"></u-icon>
			<u-icon name="/static/icons/审核.png" size="30" label="审核进度" labelPos="bottom" labelSize="10"></u-icon>
			<u-icon name="/static/icons/seting.png" size="30" label="设置" labelPos="bottom" labelSize="10" @click="clickset"></u-icon>
		</view>
		<u-sticky>
			<view style="background-color: #fafafa;">
				<u-tabs :list="tabslist" sticky></u-tabs>
			</view>			
		</u-sticky>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',
				tabslist:[{name:'发布的话题'},{name:'发布的节点'}]
			};
		},
		methods:{
			clickset(){
				uni.navigateTo({
					url:'../seting/seting'
				})
			},
			clickeditinfo(){
				uni.navigateTo({
					url:'../info/info'
				})
			}
		}
	}
</script>

<style lang="scss">
@import '@/static/variables.scss';
.headerpanel{
	height: 20vh;
	padding: 20rpx;
	display: flex;
	position:relative;
	flex-direction: column;
	justify-content: space-between;
	background-color: $cardcolor;
	border-radius: 0 0 30rpx 30rpx;
	.bgimg{
		position:absolute;
		left: 0; right: 0; top: 0; bottom: 0;
		background: url('https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png') center;
		background-size: cover;
		filter: blur(50px);
	}
	.headerpanel-uinfo{
		filter: blur(0px);
		padding: 0 20rpx 0 20rpx;
		display: flex;
		align-items: flex-start;
		justify-content: space-between;
		.headerpanel-uinfo-name{
			margin-bottom: 10rpx;
			display: flex;
			align-items: flex-start;
		}		
		.levelbar{
			width: 50vw;
			margin-top: 10rpx;
			@extend %betweencenter;
		}
		.avatarpanel{
			display: flex;
			flex-direction: column;
			align-items: center;
		}
	}
	.headerpanel-udata{
		display: flex;
		padding: 20rpx 40rpx 0 30rpx;
		.datablock{
			margin: 20rpx 40rpx 20rpx 40rpx;
			display: flex;
			flex-direction: column;
			align-items: center;
		}
	}
}

.controlpanel{
	margin-top: 20rpx;
	margin-bottom: 20rpx;
	display: flex;
	justify-content: space-around;
}

</style>
