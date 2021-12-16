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
				<focusbuttom :focus="isfocusauthor" @clicked="isfocusauthor=!isfocusauthor"></focusbuttom>
			</view>
		</view>
		<u-popup :show="true" :round="true" :overlay="false" :closeOnClickOverlay="false">
			<view class="datapanel">
				<view class="dataheader">
					<view class="ctrltabs">
						<view v-for="(item,index) in tabslist" :class="['tab',activetab===index?'selected':'unselected']" @click="activetab=index">
							<text>{{item.name}}</text>
							<view style="height: 6rpx;width: 50rpx;border-radius: 50rpx;"></view>
						</view>
					</view>
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
			<view class="datalist">
				<view></view>
			</view>
		</u-popup>

	</view>
</template>

<script>
	import focusbuttom from '../../components/focusbuttom'
	export default {
		data() {
			return {
				activetab:0,
				isfocusauthor:false,
				colors:['#007AFF','#00000000'],
				tabslist:[{name:'他的投稿'},{name:'他的关注'}]
			};
		},
		methods:{

		},
		components:{focusbuttom}
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
		justify-content: space-between;
		padding: 10rpx;
		.ctrltabs{
			display: flex;
			.tab{
				margin-left: 20rpx;
				display: flex;
				flex-direction: column;
				align-items: center;
				justify-content: flex-end;		

			}
			.selected{
				text{
					font-size: 32rpx;
					color: #007AFF;
				}
				view{
					margin-top: 12rpx;
					background-color: #007AFF;
				}
			}
			.unselected{
				text{
					font-size: 32rpx;
					color: #858585;
				}
				view{
					margin-top: 12rpx;
					background-color: #00000000;
				}
			}
		}
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
