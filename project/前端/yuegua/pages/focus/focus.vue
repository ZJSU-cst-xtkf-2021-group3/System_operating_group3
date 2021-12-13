<template>
	<view>
<!-- 		<u-scroll-list :indicator="false" style="margin-top: 20rpx;">
			<view class="avatarblock" v-for="index in 8" :key="index">
				<u-avatar :src="src"></u-avatar>
				<text class="unametext">今天天天天气真好</text>
			</view>
		</u-scroll-list> -->
<!-- 		<view style="margin: 0 30rpx 0 30rpx;">
			<u-line color="#d7d6d4"></u-line>
		</view> -->
		<!-- <u-tabs style="box-shadow: 0px -4px 8px 4px #d2d2d2; ;" :list="tabslist" :activeStyle="{ color: '#3c9cff' }"></u-tabs> -->
		<tm-tabs v-model="activeIndex" color="blue" :list="tabslist" ></tm-tabs>
	</view>
</template>

<script>
	import tmTabs from '@/tm-vuetify/components/tm-tabs/tm-tabs'
	export default {
		components:{tmTabs},
		data() {
			return {
				activeIndex:0,
				src:'https://cdn.uviewui.com/uview/swiper/1.jpg',
				tabslist:['全部','话题','用户'],
			};
		}
	}
</script>

<style lang="scss">
.avatarblock{
	margin: 0 10rpx 0 10rpx;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
}

.unametext{
	width: 120rpx;
	font-size: 15rpx;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
</style>
