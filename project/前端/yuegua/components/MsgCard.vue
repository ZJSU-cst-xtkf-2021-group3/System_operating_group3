<template>
	<view class="cell" @click="seeMsgInfo(Type,typeID)">
		<u-row>
			<u-col span="2">
				<u--image width="50" height="50" radius="27" :src="avtarsrc"></u--image>
			</u-col>
			<u-col span="10">
				<view style="margin-left: 20rpx;">
					<view style="display: flex;align-items: flex-start;">
						<view style="font-size: 30rpx;">{{uname}}</view>
						<view style="margin-left: 30rpx;font-size: 16rpx;color: #AAAAAA;">· {{timestamp}}</view>
					</view>
					<view style="margin-top: 5rpx;color: #A2A2A2;">{{msg}}</view>
				</view>
				
			</u-col>
		</u-row>
		<view style="height: 2rpx;position: absolute;bottom: 0;left: 70px;right: 0;background-color: #EEEEEE;"></view>
	</view>
</template>

<script>
	export default {
		name:"MsgCard",
		props:{
			avtarsrc:{type:String,default:""},
			uname:{type:String},
			msg:{type:String},
			timestamp:{type:String},
			Type:{type:Number},
			typeID:{type:Number},
		},
		data() {
			return {
				
			};
		},
		methods:{
		seeMsgInfo(type,id){
			console.log("type: "+type+"id: "+id)
			//爆料详情
			if(type===3){
				console.log("爆料")
			}
			//引用详情
			if (type===2){
				console.log("引用")
			}
			//话题详情
			if (type===1){
				console.log("话题")
			}
		}	
		},
	}
</script>

<style lang="scss" scoped>
.cell{
	position: relative;
	padding: 15rpx;	
}

</style>
