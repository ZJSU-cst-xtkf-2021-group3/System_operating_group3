<template>
	<view>
		<view class="commentcard">
			<view style="display: flex;align-items: center;justify-content: space-between;">
				<view class="commentdatabar">
					<view style="display: flex;align-items: center;justify-content: center;">
						<u-avatar :src="commentdata.imgsrc" size="20"></u-avatar>
						<view style="margin-left: 10rpx;font-size: 30rpx;">{{commentdata.uname}}</view>
					</view>
					<view style="margin-left: 30rpx;font-size: 18rpx;color: #999999;">{{commentdata.time}}</view>
				</view>
				<view class="commentrightbar">
					<u-icon @click="clickedfavor" :name="commentdata.isfavor?'thumb-up-fill':'thumb-up'" space="0" :color="commentdata.isfavor?'#1890FF':'#AEAEAE'" labelColor="#AEAEAE" size="23" :label="commentdata.favorcnt"></u-icon>
					<!-- <u-icon name="thumb-up" space="0" color="#AEAEAE" labelColor="#AEAEAE" labelSize="13" size="20" :label="commentdata.favorcnt"></u-icon> -->
				</view>				
			</view>
			<view class="comment">
				{{commentdata.comment}}
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		name:"comment",
		emits:['clickedfavor'],
		props:{
			commentdata:Object
		},
		data() {
			return {
				
			};
		},
		methods:{
			clickedfavor(){
				this.$emit('clickedfavor')
			}
		}
	}
</script>

<style lang="scss" scoped>
.commentcard{
	// border-top: 2rpx solid #EAEAEA;
	border-bottom: 2rpx solid #EAEAEA;
	padding: 10rpx 20rpx 10rpx 20rpx;
	.commentdatabar{
		display: flex;
		align-items: center;
	}
	.comment{
		padding: 10rpx 10rpx 0 10rpx;
		color: #343434;
	}
	.commentrightbar{
		width: 90rpx;
	}	
}
</style>
