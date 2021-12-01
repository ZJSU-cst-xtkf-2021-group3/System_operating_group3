<template>
	<view class="constainer">
		<view class="cell">
			<text>标题</text>
			<u--input v-model="title" placeholder="请输入标题" border="bottom" ></u--input>			
		</view>
		<view class="cell">
			<text>简介</text>
			<u--textarea v-model="desc" placeholder="请输入简介" height="100" maxlength="100" count></u--textarea>			
		</view>
		<view class="cell">
			<text>添加连接</text>
			<u--input v-model="title" placeholder="请输入链接" border="bottom" ></u--input>			
		</view>
		<view class="selecttype">
			<text>选择分类</text>
			<uni-combox :candidates="typecandidates" placeholder="请选择分类" v-model="type"></uni-combox>
		</view>
		<view class="cell2">
			<text>添加封面</text>
			<u-upload
				:fileList="coverimg"
				@afterRead="afterRead"
				@delete="deletePic"
				:maxCount="1"
			></u-upload>			
		</view>
		<view style="padding-right: 20rpx;margin-bottom: 10rpx;display: flex;flex-direction: row-reverse;">
			<text style="text-decoration: underline;">添加投票</text>
		</view>
		<view style="display: flex;margin-top: 50rpx;">
			<u-button text="保存" :hairLine="false" plain></u-button>
			<u-button text="发布" :hairLine="false" plain></u-button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				title:'',
				desc:'',
				type:'',
				typecandidates:['娱乐','体育'],
				coverimg:[]
			};
		},
		methods:{

		}
	}
</script>

<style lang="scss" scoped>
@import '@/static/variables.scss';
text{
	font-size: 30rpx;
}
.cell{
	padding: 10rpx;
	background-color: #fff;
	margin-bottom: 20rpx;
}
.cell2{
	padding: 10rpx;
	background-color: #fff;
	margin-bottom: 10rpx;
}
.selecttype{
	padding: 10rpx;
	background-color: #fff;
	margin-bottom: 20rpx;
	@extend %betweencenter;
}
</style>
