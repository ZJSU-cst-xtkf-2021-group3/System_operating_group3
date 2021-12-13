<template>
	<view>
		<view class="reviewcard">
			<view v-if="showimg">
				<u--image v-if="true" radius="10" width="60" height="60" :src="imgsrc" mode="aspectFill"></u--image>
			</view>
			<view>
				<view class="rightpart">
					<view style="font-size: 35rpx;">{{title}}</view>
					<u--text color="#7A7B7E" lines="1" :text="desc"></u--text>
				</view>
			</view>
			<view class="itemtime">{{timestamp}}</view>
			<view class="itemtags" :style="{backgroundColor: `${kinds[indexs].color}`}">{{kinds[indexs].data}}</view>
		</view>
	</view>
</template>

<script>
	export default {
		name:"ReviewCard",
		props:{
			title:{
				type:String,
			},
			desc:{
				type:String
			},
			showimg:{
				type:Boolean,
				default:false
			},
			imgsrc:{
				type:String,
				default:''
			},
			indexs:{
				type:Number,
			},
			timestamp:{
				type:String,
			}
		},
		data() {
			return {
				kinds:[
					{data:'已通过',color:'#05cc05'},
					{data:'审核中',color:'#007AFF'},
					{data:'未通过',color:'#f05050'},
					{data:'草稿',color:'#748596'},
				]
			};
		}
	}
</script>

<style lang="scss">
.reviewcard{
	min-height: 120rpx;
	display: flex;
	padding: 10rpx;
	margin: 10rpx 0 10rpx 0;
	border-radius: 20rpx;
	background-color: #fff;
	position: relative;
	.rightpart{
		padding: 5rpx 0 5rpx 20rpx;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
	}
	.itemtags{
		width: 100rpx;height: 40rpx;color: #fff;position: absolute;right: 0;top: 0;
		border-radius: 0 20rpx 0 20rpx;
		text-align:center;line-height:40rpx;
		font-size: 16rpx;
	}
	.itemtime{
		font-size: 10rpx;
		color: #aAaBaE;text-align: right;
		position: absolute;right: 20rpx;bottom: 0;
	}
}
</style>
