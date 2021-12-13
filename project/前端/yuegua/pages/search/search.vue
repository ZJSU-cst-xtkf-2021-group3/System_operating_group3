<template>
	<view class="page">
		<view class="searchbar">
			<u-search placeholder="请输入内容" v-model="searchkeyword" height="60" maxlength="30" :focus="true" @search="onsearch" @custom="onsearch"></u-search>
		</view>
		<view class="hotsearch">
			<u-icon label="热搜榜" size="25" name="/static/icons/热搜.png"></u-icon>
			<view style="padding: 5rpx 30rpx 5rpx 30rpx;"><u-line color="#d6d7d9"></u-line></view>
			
			<view class="hotlist">
				<view v-for="(item,index) in 10" :key="index" style="width: 50%;margin: 5rpx 0 5rpx 0;">
					<text style="margin-right: 30rpx;font-size: 35rpx;font-weight:bold;font-style: italic;">{{index + 1}}</text><text>热搜{{index}}</text>
				</view>
				
			</view>
		</view>
		<view class="searchhistory">
			<view>
				<text>搜索记录</text>
			</view>
			<view class="footer">
				<u-tag style="margin: 10rpx;" text="标签" shape="circle" size="mini" bgColor="#c5c5c5" ></u-tag>
				<u-tag style="margin: 10rpx;" text="标签" shape="circle" size="mini" bgColor="#c5c5c5" ></u-tag>
				<u-tag style="margin: 10rpx;" text="标签" shape="circle" size="mini" bgColor="#c5c5c5" ></u-tag>
			</view>
			<view style="display: flex;align-items: center;justify-content: center;">
				<u-icon name="trash" color="#a5a5a5" label="清除搜索记录" size="22" labelSize="12"></u-icon>
			</view>
		</view>
		<u-popup mode="bottom" :show="showres" round closeable @close="showres=false" :overlay="false" :closeOnClickOverlay="false" >
			<view :style="{height:'calc(100vh - ' + headerheight +'px)'}">
				<scroll-view scroll-y>
					<view v-for="(item,index) in 15" style="height: 100rpx;margin: 10rpx;background-color: #007AFF;"></view>
				</scroll-view>
			</view>
		</u-popup>
		<u-toast ref="uToast"></u-toast>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				searchkeyword:'',
				headerheight:0,
				showres:false
			};
		},
		methods:{
			onsearch(){
				if(this.searchkeyword === ''){
					this.$refs.uToast.show({
						type:'error',
						message: "搜索内容为空！",
					})
				}
				else{
					this.showres = true
					console.log(this.searchkeyword)					
				}

			},
		},
		mounted() {
			const query = uni.createSelectorQuery().in(this);
			query.select('.searchbar').boundingClientRect(data => {
				this.headerheight += data.height;
			}).exec();
		},
		onLoad() {
			this.headerheight += uni.getStorageSync('headerheight') + 10
		}
	}
</script>

<style lang="scss" scoped>
@import '@/static/variables.scss';
.page{
	.searchbar{
		height: 60rpx;
		margin: 10rpx 30rpx 10rpx 30rpx;
		@extend %center;
	}	
	.searchhistory{
		padding: 0rpx 20rpx 0rpx 20rpx;
		margin: 10rpx 0 10rpx 0;	
		.footer{
			padding: 10rpx 0 10rpx 0;
			display: flex;
			flex-wrap: wrap;
		}
	}
	.hotsearch{
		background-color: #fefefe;
		
		.hotlist{
			padding: 10rpx 20rpx 10rpx 20rpx;
			display: flex;
			flex-wrap: wrap;
		}
	}
}

</style>
