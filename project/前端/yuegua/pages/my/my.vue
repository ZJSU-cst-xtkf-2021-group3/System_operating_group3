<template>
	<view>
		<u-transition mode="fade-down" :show="true">
			<view class="headerpanel">
				<!-- <view class="bgimg"></view> -->
				<view class="headerpanel-uinfo">
					<view style="padding-top: 20rpx;">
						<view class="headerpanel-uinfo-name">
							<text style="font-size: 45rpx;font-weight: 550;margin-right: 30rpx;">wuji</text>
							<u-icon color="#FFC53D" style="margin-right: 10rpx;" name="level" size="18" label="4" space="0"></u-icon>
						</view>
						<u--text line="2" text="今天天气很好"></u--text>
						<view class="levelbar">
							<u-line-progress :percentage="70" height="8" activeColor="#1890FF" :showText="false"></u-line-progress>
							<view style="font-size: 10rpx;margin-left: 10rpx;text-align: center;">49/555</view>
						</view>
					</view>
					<view class="avatarpanel">
						<u-avatar size="80" :src="src"></u-avatar>
						<view style="margin-top: 20rpx;display: flex;align-items: center;" @click="clickeditinfo">
							<u-icon name="edit-pen-fill" size="19" color="#A1A1A1"></u-icon>
							<text style="color: #A1A1A1;" >编辑资料</text>
						</view>
						
					</view>
				</view>
				<view class="headerpanel-udata">
					<view class="datablock" @click="focus=true">
						<text style="font-size: 35rpx;font-weight: 550;">33445</text>
						<text style="font-size: 20rpx;">关注</text>
					</view>
					<view class="datablock" @click="fans=true">
						<text style="font-size: 35rpx;font-weight: 550;">765</text>
						<text style="font-size: 20rpx;">粉丝</text>
					</view>
					<view class="datablock">
						<text style="font-size: 35rpx;font-weight: 550;">945</text>
						<text style="font-size: 20rpx;">发布</text>
					</view>
				</view>
			</view>
		</u-transition>
		<view class="controlpanel">
			<u-icon name="/static/icons/草稿.png" size="30" label="草稿" labelPos="bottom" labelSize="10" @click="clickdraft"></u-icon>
			<u-icon name="/static/icons/审核.png" size="30" label="审核进度" labelPos="bottom" labelSize="10" @click="clickreview"></u-icon>
			<u-icon name="/static/icons/seting.png" size="30" label="设置" labelPos="bottom" labelSize="10" @click="clickset"></u-icon>
		</view>
		<u-sticky>
			<view style="display: flex;align-items: center;justify-content: center;">
				<tm-segTabs :round="24" :margin="[32,10]" font-size="s" :list="tabslist" color="white" activeFontColor="blue" bg-color="bg-gradient-blue-lighten" v-model="active"></tm-segTabs>
			</view>
		</u-sticky>
		<view class="contpanel">
			
		</view>
		<u-popup mode="bottom" :show="focus" round :overlay="false" @close="focus=false">
			<view :style="{height:'calc(100vh - ' + headerheight +'px)'}">
				<view class="popupheader">
					关注-33445
					<u-icon style="position: absolute;right: 20rpx;top: 15rpx;" name="close" color="#fafafa" size="25" @click="focus=false"></u-icon>
				</view>
				<view style="">
					<UserCard :avtarsrc="src" uname="用户名" desc="他点赞了你的评论!"></UserCard>
				</view>
			</view>
		</u-popup>
		<u-popup mode="bottom" :show="fans" round :overlay="false" @close="fans=false">
			<view :style="{height:'calc(100vh - ' + headerheight +'px)'}">
				<view class="popupheader">
					粉丝-33445
					<u-icon style="position: absolute;right: 20rpx;top: 15rpx;" name="close" color="#fafafa" size="25" @click="fans=false"></u-icon>
				</view>
			</view>
		</u-popup>
	</view>
</template>

<script>
	import UserCard from '@/components/UserCard'
	import tmSegTabs from '@/tm-vuetify/components/tm-segTabs/tm-segTabs.vue'
	export default {
		data() {
			return {
				active:0,
				focus:false,
				fans:false,
				headerheight:0,
				src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',
				tabslist:['发布的话题','发布的节点']
			};
		},
		onLoad() {
			this.headerheight = uni.getStorageSync('headerheight')
		},
		methods:{
			clickset(){
				uni.navigateTo({
					url:'../seting/seting'
				})
			},
			clickeditinfo(){
				uni.navigateTo({
					url:'../info/info'
				})
			},
			clickreview(){
				uni.navigateTo({
					url:'../review/review'
				})
			},
			clickdraft(){
				uni.navigateTo({
					url:'../draft/draft'
				})
			},
		},
		components:{
			UserCard,
			tmSegTabs
		}
	}
</script>

<style lang="scss">
@import '@/static/variables.scss';
.headerpanel{
	height: 21vh;
	padding: 20rpx;
	display: flex;
	position:relative;
	flex-direction: column;
	justify-content: space-between;
	background: linear-gradient(to top,$cardcolor 60%, #1890FFA0 );
	border-radius: 0 0 30rpx 30rpx;
	.bgimg{
		position:absolute;
		left: 0; right: 0; top: 0; bottom: 0;
		background: url('https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png') center;
		background-size: cover;
		filter: blur(50px);
	}
	.headerpanel-uinfo{
		filter: blur(0px);
		padding: 0 20rpx 0 20rpx;
		display: flex;
		align-items: flex-start;
		justify-content: space-between;
		.headerpanel-uinfo-name{
			margin-bottom: 10rpx;
			display: flex;
			align-items: flex-start;
		}		
		.levelbar{
			width: 60vw;
			margin-top: 10rpx;
		}
		.avatarpanel{
			display: flex;
			flex-direction: column;
			align-items: center;
		}
	}
	.headerpanel-udata{
		display: flex;
		padding: 20rpx 40rpx 10rpx 30rpx;
		.datablock{
			margin: 20rpx 40rpx 20rpx 40rpx;
			display: flex;
			flex-direction: column;
			align-items: center;
		}
	}
}

.controlpanel{
	margin-top: 20rpx;
	margin-bottom: 20rpx;
	display: flex;
	justify-content: space-around;
}
.popupheader{
	position: relative;font-size: 35rpx;line-height: 80rpx;text-align: center;color: #fafafa;height: 80rpx;background-color: #1890FF;border-radius: 20rpx 20rpx 0 0;
}
.contpanel{
	height: 300rpx;
	margin: 10rpx;
	margin-top: 15rpx;
	padding: 20rpx;
	border-radius: 20rpx;
	background-color: #fafafa;
}
</style>
