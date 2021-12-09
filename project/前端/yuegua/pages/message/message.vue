<template>
	<view>
		<view class="ctrlheader">
			<view class="ctrlblock" @click="fovar=true">
				<u-icon name="thumb-up-fill" color="#fff" labelColor="#fff" label="点赞" labelSize="12" size="25"></u-icon>
				<view class="badge"></view>
			</view>
			<view class="ctrlblock" @click="focus=true">
				<u-icon name="plus-people-fill" color="#fff" labelColor="#fff" label="关注" labelSize="12" size="25"></u-icon>
				<view class="badge"></view>
			</view>
			<view class="ctrlblock" @click="comm=true">
				<u-icon name="chat-fill" color="#fff" labelColor="#fff" label="评论" labelSize="12" size="25"></u-icon>
				<view class="badge"></view>
			</view>
		</view>
		<view class="msgbar">
			<u-icon label="全部消息" labelPos="left" size="16" labelSize="16" name="/static/icons/laba.png"></u-icon>
		</view>
		<view>
			<MsgCard :avtarsrc="src" uname="用户名" msg="他点赞了你的评论!"></MsgCard>
			<MsgCard :avtarsrc="src" uname="用户名" msg="他点赞了你的话题!"></MsgCard>
			<MsgCard :avtarsrc="src" uname="用户名" msg="他关注了你!"></MsgCard>
			<MsgCard uname="审核消息" msg="你投稿的话题审核通过."></MsgCard>
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
	padding: 20rpx 60rpx 20rpx 60rpx;
	@extend %betweencenter;
	.ctrlblock{
		padding: 10rpx 20rpx 10rpx 20rpx;
		border-radius: 50rpx;
		background-color: #1890FF;
		position: relative;
		.badge{
			position: absolute;
			width: 20rpx;height: 20rpx;
			border-radius: 10rpx;
			top: 0;right: 0;
			background-color: #f00;
		}
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
