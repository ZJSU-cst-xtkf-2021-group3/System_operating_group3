<template>
	<view class="page">
		<view style="margin-top: 10rpx;font-size: 35rpx;font-weight: 550;">全球最大的中文搜索引擎、致力于让网民更便捷地获取信息，找到所求</view>
		<view class="udatabar">
			<view style="display: flex;align-items: center;">
				<u-avatar :src="src" size="20"></u-avatar>
				<text style="margin-left: 15rpx;font-size: 33rpx;">wuji</text>
				<text style="margin-left: 20rpx;font-size: 25rpx;">1天前</text>				
			</view>
			<view>
				<u-button type="primary" text="关注" size="mini"></u-button>
			</view>
		</view>
		<view style="padding: 20rpx;">
			说明：目前经测试(Hbuilder X 2.6.8)，在H5，APP，可以直接对组件监听tap事件，等同组件内部发出的click事件效果，某些HX版本上， 微信小程序对组件使用tap事件可能无效，故建议对按钮组件的点击事件监听统一使用组件内部发出的click事件。
		</view>
		<view style="padding: 10rpx;">
			<view>问题</view>
			<view class="selectbar">
				<text>选项1</text>
				<text>56%</text>
			</view>
			<view class="selectbar">
				<text>选项2</text>
				<text>44%</text>
			</view>
			<view>2008人参与</view>
		</view>
		<view style="padding: 10rpx 20rpx 10rpx 20rpx;"><u-line color="#e7e6e4"></u-line></view>
		<view class="ctrlbar">
			<u-icon name="clock" size="22" label="时间导航"></u-icon>
			<u-icon name="plus" size="22"></u-icon>
		</view>
		<view class="footerbar">
			<view style="width: 44vw;">
				<u-search placeholder="请输入评论" searchIcon="" height="60" maxlength="30" :showAction="false" :clearabled="false"></u-search>
			</view>
			<view class="iconbtn">
				<u-icon name="thumb-up" color="#2979ff" label="123" size="20"></u-icon>
				<u-icon name="chat" color="#2979ff" label="123" size="20"></u-icon>
				<u-icon name="share-square" color="#2979ff" label="123" size="20"></u-icon>
			</view>
		</view>
		<view style="padding: 10rpx 20rpx 10rpx 20rpx;"><u-line color="#e7e6e4"></u-line></view>
		<view style="margin-left: 10rpx;font-weight: 550;">评论</view>
		<view class="commentcard">
			<view class="commentdatabar">
				<view style="display: flex;align-items: center;justify-content: center;">
					<u-avatar :src="src" size="20"></u-avatar>
					<view style="margin-left: 10rpx;font-size: 30rpx;">wuji</view>
				</view>
				<view style="font-size: 20rpx;">1小时前</view>	
			</view>
			<view class="comment">
				天气真好
			</view>
			<view class="commentfooterbar">
				<u-icon name="thumb-up" color="#2979ff" label="123" size="20"></u-icon>
			</view>
			
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',
			};
		},
		methods:{
			clicked(){
				uni.request({
					url:'http://www.baidu.com/',
					success: (res) => {
						console.log(res.data)
					}
				})
			}
		}
	}
</script>

<style lang="scss">
@import '@/static/variables.scss';
.udatabar{
	padding: 10rpx;
	@extend %betweencenter
}
.ctrlbar{
	padding: 10rpx;
	@extend %betweencenter
}
.selectbar{
	margin: 10rpx 20rpx 10rpx 20rpx;
	padding: 0 10rpx 0 10rpx;
	height: 50rpx;
	background-color: #007AFF;
	@extend %betweencenter;
}
.footerbar{
	height: 70rpx;
	width: 100%;
	position: fixed;
	bottom: 0;
	left: 0;
	@extend %center;
}
.iconbtn{
	width: 50vw;
	@extend %betweencenter;
}
.commentcard{
	padding: 10rpx;
	.commentdatabar{
		display: flex;
		@extend %betweencenter;
	}
	.comment{
		padding: 15rpx;
	}
	.commentfooterbar{
		margin-right: 10rpx;
		display: flex;
		align-items: center;
		flex-direction: row-reverse;
	}	
}

</style>
