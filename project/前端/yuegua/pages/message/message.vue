<template>
	<view>
		<view class="ctrlheader">
			<view class="ctrlblock">
				<u-icon name="thumb-up-fill" label="点赞" labelSize="18" size="30"></u-icon>
			</view>
			<view class="ctrlblock">
				<u-icon name="thumb-up-fill" label="点赞" labelSize="18" size="30"></u-icon>
			</view>
			<view class="ctrlblock">
				<u-icon name="thumb-up-fill" label="点赞" labelSize="18" size="30"></u-icon>
			</view>
		</view>
		<view style="margin: 0 30rpx 0 30rpx;">
			<u-line color="#d7d6d4"></u-line>
		</view>
		<view style="margin: 10rpx 20rpx 0 20rpx;font-size: 30rpx;">全部消息</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			};
		}
	}
</script>

<style lang="scss">
@import '@/static/variables.scss';
.ctrlheader{
	padding: 20rpx 40rpx 20rpx 40rpx;
	@extend %betweencenter;
	.ctrlblock{
		padding: 10rpx 20rpx 10rpx 20rpx;
		border-radius: 50rpx;
		background-color: #007AFF;
	}	
}

</style>
