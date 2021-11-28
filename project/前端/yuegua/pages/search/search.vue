<template>
	<view class="page">
		<view class="searchbar">
			<u-search placeholder="请输入内容" v-model="searchkeyword" height="60" maxlength="30" :focus="true"></u-search>
		</view>
		<view class="searchhistory">
			<view class="header">
				<text>搜索记录</text>
				<u-icon name="trash" color="#2979ff" size="22"></u-icon>
			</view>
			<view class="footer">
				<u-tag text="标签" shape="circle" size="mini" ></u-tag>
				<u-tag text="标签" plain size="mini" type="warning"></u-tag>
				<u-tag text="标签" shape="circle" size="mini" plain></u-tag>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				searchkeyword:'',
			};
		},
		methods:{
			tagclose(index){
				console.log(index)
			}
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
		padding: 0 20rpx 0 20rpx;
		.header{
			@extend %betweencenter
		}		
		.footer{
			padding: 10rpx 0 10rpx 0;
			display: flex;
			flex-wrap: wrap;
		}
	}

}

</style>
