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
		</view>
		<view class="cell">
			<text>*内容</text>
			<u--textarea v-model="desc" placeholder="请输入内容(必填)" height="100" maxlength="100" count></u--textarea>			
		</view>
		<view v-if="types=='topic'" class="cell2">
			<text>图片</text>
			<u-upload
				:fileList="coverimg"
				@afterRead="afterRead"
				@delete="deletePic"
				:maxCount="1"
			></u-upload>			
		</view>
		<view style="position: absolute;bottom: 20rpx;left: 0;right: 0;display: flex;align-items: center;justify-content: center;margin: 20rpx 20rpx 0 20rpx;">
			<view style="width: 80%">
				<!-- <u-button :hairLine="false" shape="cicle" color="#1890FF" text="发布"></u-button> -->
				<tm-button @click="push" theme="bg-gradient-blue-accent" :round="24" block>{{types=='topic'?'发布':'添加'}}</tm-button>
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
				content:'',
				link:'',
				coverimg:[],
				desc:","
			};
		},
		methods:{
			change_tt:function(){
				console.log(this.title)		
			},
			change_de:function(){
				console.log(this.desc)		
			},
			change_link:function(){
				console.log(this.link)		
			},
			push:function(){
				var that = this
				if(that.content == "")
				{
					uni.showToast({
						title:"内容不得为空!（｀へ´）",
						icon:"error",
						duration:2000
					}),
					uni.switchTab({
						url:"../activity/activity"
					})
				}
				else{uni.request({
						header:{
							"Content-Type":"application/x-www-form-urlencoded",
							},
						url:"http://yuegua.fgimax.vipnps.vip/Post/topic",
						data:{
							title:that.title,
							statement:that.content,
							link:that.link,
							'uid':3
							},
						method:"POST",
						success(res){
							if(res.data.res=='ok'){
								console.log("ok")
							}
							console.log(that.title)
									   
						}
				})
				uni.switchTab({
					url:"../activity/activity"
				})
			}
			}
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
