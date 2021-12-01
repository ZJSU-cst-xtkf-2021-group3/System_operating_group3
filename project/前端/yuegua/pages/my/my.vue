<template>
	<view>
		<u-popup mode="top" :show="true" :round="true" :overlay="false" :closeOnClickOverlay="false">
			<view class="headerpanel">
				<view class="headerpanel-uinfo">
					<view>
						<view class="headerpanel-uinfo-name">
							<text style="font-size: 45rpx;font-weight: 550;margin-right: 30rpx;">wuji</text>
							<u-icon name="level" size="18" label="4" space="0"></u-icon>
						</view>
						<u--text line="2" text="今天天气很好"></u--text>
					</view>
					<view class="avatar">
						<u-avatar size="80" :src="src"></u-avatar>
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
		</u-popup>
		<view class="controlpanel">
			<u-icon name="edit-pen" size="30" label="草稿" labelPos="bottom" labelSize="10"></u-icon>
			<u-icon name="more-circle" size="30" label="审核进度" labelPos="bottom" labelSize="10"></u-icon>
			<u-icon name="setting" size="30" label="设置" labelPos="bottom" labelSize="10"></u-icon>
		</view>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				src: 'http://pic2.sc.chinaz.com/Files/pic/pic9/202002/hpic2119_s.jpg'
			};
		}
	}
</script>

<style lang="scss">
@import '@/static/variables.scss';
.headerpanel{
	height: 20vh;
	padding: 20rpx;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	background-color: $mypanelbgcolor;
	border-radius: 0 0 60rpx 60rpx;
	.headerpanel-uinfo{
		padding: 0 20rpx 0 20rpx;
		display: flex;
		align-items: flex-start;
		justify-content: space-between;
		.headerpanel-uinfo-name{
			margin-bottom: 10rpx;
			display: flex;
			align-items: flex-start;
		}		
	}
	.headerpanel-udata{
		display: flex;
		padding: 20rpx 40rpx 0 40rpx;
		.datablock{
			margin: 20rpx 40rpx 20rpx 40rpx;
			display: flex;
			flex-direction: column;
			align-items: center;
		}
	}
}
.controlpanel{
	margin-top: 18vh;
	margin-bottom: 20rpx;
	display: flex;
	justify-content: space-around;
}
</style>
