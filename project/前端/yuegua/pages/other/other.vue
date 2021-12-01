<template>
	<view>
		<view class="headerpanel-uinfo">
			<view>
				<view class="headerpanel-uinfo-name">
					<text style="font-size: 45rpx;font-weight: 550;margin-right: 30rpx;">wuji</text>
					<u-icon name="level" size="18" label="4" space="0"></u-icon>
				</view>
				<u--text line="2" text="今天天气很好"></u--text>
			</view>
			<view>
				<u-button type="primary" size="mini" text="取消关注"></u-button>
			</view>
		</view>
		<u-popup :show="true" :round="true" :overlay="false" :closeOnClickOverlay="false">
			<view class="datapanel">
				<view class="dataheader">

						<u-button type="primary" shape="circle" text="投稿"></u-button>
						<u-button type="primary" shape="circle" text="关注话题"></u-button>					

					<view class="headerpanel-udata">
						<view class="datablock">
							<text style="font-size: 35rpx;font-weight: 550;">33445</text>
							<text style="font-size: 20rpx;">关注</text>
						</view>
						<view class="datablock">
							<text style="font-size: 35rpx;font-weight: 550;">765</text>
							<text style="font-size: 20rpx;">粉丝</text>
						</view>
						<view class="datablock">
							<text style="font-size: 35rpx;font-weight: 550;">945</text>
							<text style="font-size: 20rpx;">发布</text>
						</view>
					</view>
				</view>
			</view>
		</u-popup>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			};
		}
	}
</script>

<style lang="scss">
	
.headerpanel-uinfo{
	padding: 20rpx 40rpx 20rpx 40rpx;
	display: flex;
	align-items: center;
	justify-content: space-between;
	.headerpanel-uinfo-name{
		margin-bottom: 10rpx;
		display: flex;
		align-items: flex-start;
	}		
}
.datapanel{
	height: 83vh;
	border-radius: 100rpx 100rpx 0 0;
	.dataheader{
		display: flex;
		align-items: center;
		padding: 10rpx;
		.headerpanel-udata{
			display: flex;
			
			.datablock{
				margin: 20rpx;
				display: flex;
				flex-direction: column;
				align-items: center;
			}
		}		
	}

}

</style>
