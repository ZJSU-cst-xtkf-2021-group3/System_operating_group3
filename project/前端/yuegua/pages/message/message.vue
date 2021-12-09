<template>
	<view>
		<view class="ctrlheader">
			<view class="ctrlblock">
				<u-icon name="thumb-up-fill" color="#fff" labelColor="#fff" label="点赞" labelSize="12" size="25"></u-icon>
			</view>
			<view class="ctrlblock">
				<u-icon name="plus-people-fill" color="#fff" labelColor="#fff" label="关注" labelSize="12" size="25"></u-icon>
			</view>
			<view class="ctrlblock">
				<u-icon name="chat-fill" color="#fff" labelColor="#fff" label="评论" labelSize="12" size="25"></u-icon>
			</view>
		</view>
		<view class="msgbar">
			<u-icon label="全部消息" labelPos="left" size="16" labelSize="16" name="/static/icons/laba.png"></u-icon>
		</view>
		<view>
			<MsgCard :avtarsrc="src" uname="订阅号" msg="天气真好"></MsgCard>
		</view>
		<u-popup mode="bottom" :show="fovar" round closeable @close="fovar=false">
			<view :style="{height:'calc(100vh - ' + headerheight +'px)'}"></view>
		</u-popup>
		<u-popup mode="bottom" :show="focus" round closeable @close="focus=false">
			<view :style="{height:'calc(100vh - ' + headerheight +'px)'}"></view>
		</u-popup>
		<u-popup mode="bottom" :show="comm" round closeable @close="comm=false">
			<view :style="{height:'calc(100vh - ' + headerheight +'px)'}"></view>
		</u-popup>
	</view>
</template>

<script>
import MsgCard from '../../components/MsgCard'
export default {
	data() {
		return {
			src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',
			headerheight:0,
			fovar:false,
			focus:false,
			comm:false
		};
	},
	mounted() {
		const query = uni.createSelectorQuery().in(this);
		query.select('.ctrlheader').boundingClientRect(data => {
			//this.headerheight = data.height;
		}).exec();
		
		uni.getSystemInfo({
			success: (e) => {
				// console.log(e)
				this.headerheight += e.windowTop
			}
		})

	},
	components:{
		MsgCard
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
		background-color: #1890FF;
	}	
}
.msgbar{
	height: 60rpx;margin: 10rpx 0 10rpx 0;padding-left: 30rpx;font-size: 30rpx;background-color: #fafafa;
	display: flex;
	align-items: center;
}
.popuppanel{
	height: calc();
	background-color: #007AFF;
}

</style>
