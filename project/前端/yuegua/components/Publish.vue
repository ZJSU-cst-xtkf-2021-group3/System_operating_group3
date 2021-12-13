<template>
	<view>
		<view class="bigcell">
			<view class="cell1">
				<text>标题</text>
				<u--input v-model="title" placeholder="请输入标题" border="none"  maxlength="20"></u--input>			
			</view>			
			<view class="cell1">
				<text>链接</text>
				<u--input v-model="link" placeholder="请添加链接" border="none" maxlength="200"></u--input>			
			</view>
			<view v-if="types!='topic'">
				<view class="cell1">
					<text>时间</text>
					<u--input v-model="datetime" placeholder="请输入时间,如:2021-9-21 12:8" border="none" maxlength="20"></u--input>			
				</view>
				<u-alert  title="注:时间为事件发生的时间." fontSize="8" type = "warning"></u-alert>				
			</view>

			<view v-if="types=='topic'" class="selecttype">
				<text>分类</text>
				<uni-combox :candidates="typecandidates" placeholder="请选择分类" v-model="type"></uni-combox>
			</view>
		</view>
		<view class="cell">
			<text>简介</text>
			<u--textarea v-model="desc" placeholder="请输入简介" height="100" maxlength="100" count></u--textarea>			
		</view>
		<view v-if="types=='topic'" class="cell2">
			<text>封面</text>
			<u-upload
				:fileList="coverimg"
				@afterRead="afterRead"
				@delete="deletePic"
				:maxCount="1"
			></u-upload>			
		</view>
		
		<view v-if="types=='topic'" style="padding-right: 20rpx;margin-bottom: 10rpx;display: flex;flex-direction: row-reverse;">
			<text style="color: #1989FA;text-decoration: underline;">添加投票</text>
		</view>
		<view style="position: absolute;bottom: 20rpx;left: 0;right: 0;display: flex;align-items: center;justify-content: center;margin: 20rpx 20rpx 0 20rpx;">
			<view v-if="types=='topic'" style="width: 20%">
				<tm-button  theme="grey-lighten-2" fontColor="grey-darken-2" :round="24" block>保存</tm-button>
			</view>
			<view style="width: 80%">
				<!-- <u-button :hairLine="false" shape="cicle" color="#1890FF" text="发布"></u-button> -->
				<tm-button  theme="bg-gradient-blue-accent" :round="24" block>{{types=='topic'?'发布':'添加'}}</tm-button>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		name:"Publish",
		props:{
			types:{
				type:String,
				default:'topic'
			}
		},
		data() {
			return {
				title:'',
				desc:'',
				type:'',
				link:'',
				datetime:'',
				typecandidates:['娱乐','体育','二次元','日常','时政','国际'],
				coverimg:[]
			};
		}
	}
</script>

<style lang="scss" scoped>
@import '@/static/variables.scss';
text{
	color: #999999;
	font-size: 30rpx;
}
.bigcell{
	margin: 10rpx;
	margin-top: 20rpx;
	padding: 10rpx;
	box-shadow: 0px 0px 2px 1px $shadowcolor;
	border-radius: 20rpx;
	background-color: #fff;
	margin-bottom: 20rpx;
	text{
		margin-right: 15rpx;
	}	
	.cell1{
		padding: 10rpx;
		@extend %center;
	}
	.selecttype{
		padding: 10rpx;
		background-color: #fff;
		border-radius: 20rpx;
		@extend %betweencenter;
	}
}
.cell{
	margin: 10rpx;
	padding: 20rpx;
	border-radius: 20rpx;
	background-color: #fff;
	margin-bottom: 20rpx;
	box-shadow: 0px 0px 2px 1px $shadowcolor;
}

.cell2{
	margin: 10rpx;
	padding: 20rpx;
	background-color: #fff;
	border-radius: 20rpx;
	margin-bottom: 10rpx;
	box-shadow: 0px 0px 2px 1px $shadowcolor;
}

</style>
