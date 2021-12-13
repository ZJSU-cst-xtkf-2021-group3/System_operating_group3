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
				
				<!-- <uni-tag text="关注" type="error" circle :inverted="isfocus" @click="isfocus=!isfocus"></uni-tag> -->
				<u-tag :text="isfocus?'取消关注':'关注'" shape="circle" size="mini" :plain="isfocus" borderColor="#f00" @click="isfocus=!isfocus" icon=""></u-tag>
			</view>
		</view>
		<view style="padding: 20rpx 20rpx 0rpx 20rpx;">
			说明：目前经测试(Hbuilder X 2.6.8)，在H5，APP，可以直接对组件监听tap事件，等同组件内部发出的click事件效果，某些HX版本上， 微信小程序对组件使用tap事件可能无效，故建议对按钮组件的点击事件监听统一使用组件内部发出的click事件。
		</view>
		<view style="margin: 10rpx 10rpx 20rpx 10rpx;display: flex;align-items: center;justify-content: center;">
			<view style="padding: 10rpx 25rpx 10rpx 25rpx;border-radius: 50rpx;background-color: #fff;display: flex;align-items: center;justify-content: center;box-shadow: 0px 0px 2px 1px #e5e5e5;">
				<uni-link color="#1890FF" href="https://uniapp.dcloud.io/" text="前往浏览"></uni-link>
				<u-icon color="#1890FF" size="15"  name="arrow-rightward"></u-icon>
			</view>				
		</view>

		<view style="padding: 10rpx;background-color: #fafafa;border-radius: 20rpx;">
			<view>问题</view>
			<view class="selectbar"> 
				<text>选项1</text>
				<text>123</text>
			</view>
			<view class="selectbar">
				<text>选项2</text>
				<text>535</text>
			</view>
			<view>2008人参与</view>
		</view>
		<!-- <view style="padding: 10rpx 20rpx 10rpx 20rpx;"><u-line color="#e7e6e4"></u-line></view> -->
		<view class="ctrlbar">
			<u-icon name="clock" size="22" label="时间导航" labelSize="16"></u-icon>
			<tm-button fab icon="../../static/icons/节点.png" icon-size="55" theme="bg-gradient-blue-accent" size="m" @click="addnode=true"></tm-button>
			<!-- <u-icon name="plus" size="22" @click="addnode=true"></u-icon> -->
		</view>
		<view>
			<tm-timeline :list="list" model="left"></tm-timeline>
		</view>
		
		<view class="footerbar">
			<view style="width: 45vw;">
				<u-search placeholder="请输入评论" searchIcon="" height="60" maxlength="30" :showAction="false" :clearabled="false"></u-search>
			</view>
			<view class="iconbtn">
				<u-icon name="thumb-up" color="#2979ff" label="123" size="20"></u-icon>
				<u-icon name="heart-fill" color="#2979ff" label="123" size="20"></u-icon>
				<u-icon name="share-square" color="#2979ff" label="123" size="20"></u-icon>
			</view>
		</view>
		<!-- <view style="padding: 10rpx 20rpx 10rpx 20rpx;"><u-line color="#e7e6e4"></u-line></view> -->
		<view class="commentbar">
			<text style="font-weight: 550;">评论</text>
			<u-icon name="chat" color="#2979ff" label="123" size="20"></u-icon>
		</view>
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
		<u-popup mode="bottom" :show="addnode" round closeable @close="addnode=false" :closeOnClickOverlay="false">
			<view style="height: 900rpx;">
				<view style="height: 90rpx;font-size: 32rpx;margin-bottom: 20rpx;text-align: center;line-height: 90rpx;">
					添加节点
				</view>
				<Pulish types="node"></Pulish>
			</view>
		</u-popup>
	</view>
</template>

<script>
	import Pulish from '../../components/Publish.vue'
	import tmButton from '../../tm-vuetify/components/tm-button/tm-button'
	import tmTimeline from '../../tm-vuetify/components/tm-timeline/tm-timeline'
	export default {
		data() {
			return {
				headerheight:0,
				addnode:false,
				isfocus:false,
				src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',
				list:[
						{
							title:'',
							content:'我是内容我是内容我是内容',
							time:"2020年7月",
							color:"blue",
							borderColor:'blue'
						},
						{
							title:'说明文字',
							content:'我是内容我是内容我是内容',
							time:"2019年7月",
							color:"blue",
							borderColor:'blue',
						},
						{
							title:'说明文字',
							content:'我是内容我是内容我是内容',
							time:"2018年7月",
							color:"blue",
							borderColor:'blue',
						},
						{
							title:'说明文字',
							content:'我是内容我是内容',
							time:"2017年7月",
							color:"blue",
							borderColor:'blue',
						},
					]
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
			},
		},
		onLoad() {
			this.headerheight = uni.getStorageSync('headerheight')
		},
		components:{
			Pulish,
			tmButton,
			tmTimeline
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
	// margin-top: 15rpx;
	padding: 10rpx;
	@extend %betweencenter
}
.selectbar{
	margin: 10rpx 20rpx 10rpx 20rpx;
	padding: 0 10rpx 0 10rpx;
	height: 50rpx;
	background-color: #EEEEEE;
	@extend %betweencenter;
}
.footerbar{
	height: 70rpx;
	width: 100%;
	position: fixed;
	bottom: 0;
	left: 0;
	display: flex;
	align-items: center;
	background-color: #fff;
	z-index: 999;
	.iconbtn{
		width: 50vw;
		@extend %betweencenter;
	}
}
.commentbar{
	padding: 0 10rpx 0 10rpx;
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
