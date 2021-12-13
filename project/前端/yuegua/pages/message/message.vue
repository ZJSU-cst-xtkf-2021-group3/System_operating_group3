<template>
	<view>
		<view class="cell" @click="focus=true">
			<u-row>
				<u-col span="2">
					<u--image width="50" height="50" radius="27" :src="fanssrc"></u--image>
				</u-col>
				<u-col span="10">
					<view class="rightpart">
						<view style="margin-left: 20rpx;font-size: 32rpx;">粉丝</view>
						<view><u-icon name="arrow-right" color="#999999" size="18"></u-icon></view>
					</view>
				</u-col>
			</u-row>
			<view style="height: 2rpx;position: absolute;bottom: 0;left: 70px;right: 0;background-color: #EEEEEE;"></view>
		</view>
		<view class="cell" @click="fovar=true">
			<u-row>
				<u-col span="2">
					<u--image width="55" height="55" radius="27" :src="favorsrc"></u--image>
				</u-col>
				<u-col span="10">
					<view class="rightpart">
						<view style="margin-left: 20rpx;font-size: 32rpx;">点赞</view>
						<view><u-icon name="arrow-right" color="#999999" size="18"></u-icon></view>
					</view>
				</u-col>
			</u-row>
			<view style="height: 2rpx;position: absolute;bottom: 0;left: 70px;right: 0;background-color: #EEEEEE;"></view>
		</view>

		<view>
			<MsgCard :avtarsrc="msgsrc" uname="用户名" msg="他点赞了你的评论!" timestamp="1天前"></MsgCard>
			<MsgCard :avtarsrc="msgsrc" uname="用户名" msg="他点赞了你的话题!" timestamp="1天前"></MsgCard>
			<MsgCard :avtarsrc="msgsrc" uname="用户名" msg="他关注了你!" timestamp="1天前"></MsgCard>
			<MsgCard :avtarsrc="msgsrc" uname="审核消息" msg="你投稿的话题审核通过." timestamp="1天前"></MsgCard>
		</view>
		<u-popup mode="bottom" :show="fovar" round closeable @close="fovar=false">
			<view :style="{height:'calc(100vh - ' + headerheight +'px)'}"></view>
		</u-popup>
		<u-popup mode="bottom" :show="focus" round closeable @close="focus=false">
			<view :style="{height:'calc(100vh - ' + headerheight +'px)'}"></view>
		</u-popup>
<!-- 		<u-popup mode="bottom" :show="comm" round closeable @close="comm=false">
			<view :style="{height:'calc(100vh - ' + headerheight +'px)'}"></view>
		</u-popup> -->
	</view>
</template>

<script>
import MsgCard from '../../components/MsgCard'
export default {
	data() {
		return {
			fanssrc:"/static/images/粉丝.png",
			favorsrc:"/static/images/点赞.png",
			msgsrc:"/static/images/系统通知.png",
			headerheight:0,
			fovar:false,
			focus:false,
			comm:false
		};
	},
	onLoad() {
		this.headerheight += uni.getStorageSync('headerheight')
	},
	components:{
		MsgCard
	}
}
</script>

<style lang="scss">
@import '@/static/variables.scss';
.cell{
	position: relative;
	padding: 15rpx;
	.rightpart{
		@extend %betweencenter
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
