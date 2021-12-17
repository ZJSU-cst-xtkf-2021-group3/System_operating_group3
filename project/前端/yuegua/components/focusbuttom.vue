<template>
	<view @click="clickedbtn">
		<view :class="[focus?'hasfocus':'nofocus','focusbtn']" >
			<u-icon v-if="!focus" name="plus" color="#fff" size="8"></u-icon>
			<text class="focustext" style="margin-left: 5rpx;font-size: 20rpx;">{{focus?'取消关注':'关注'}}</text>
		</view>		
	</view>

</template>

<script>
	export default {
		name:"focusbuttom",
		emits:['clicked'],
		props:{focus:Boolean},
		data() {
			return {

			};
		},
		methods:{
			clickedbtn(){
				this.$emit('clicked')
			}
		}
	}
</script>

<style lang="scss" scoped>
	.focusbtn{
		padding: 2rpx 12rpx 2rpx 12rpx;
		display: flex;align-items: center;
	}
	.nofocus{
		border-radius: 25rpx;
		background: linear-gradient(to right,#0D92F6, #0DAFF2);
		.focustext{
			color: #fff;
		}
	}
	.hasfocus{
		border-radius: 5rpx;
		background-color: #EAEAEA;
		.focustext{
			color: #909193;
		}
	}
</style>
