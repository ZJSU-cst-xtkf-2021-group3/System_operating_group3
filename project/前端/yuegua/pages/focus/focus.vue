<template>
	<view>
		<u-scroll-list :indicator="false" style="margin-top: 20rpx;">
			<view class="avatarblock" v-for="index in 8" :key="index">
				<u-avatar :src="src"></u-avatar>
				<text class="unametext">今天天天天气真好</text>
			</view>
		</u-scroll-list>
		<view style="margin: 0 30rpx 0 30rpx;">
			<u-line color="#d7d6d4"></u-line>
		</view>
		<u-tabs :list="tabslist" ></u-tabs>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				src:'https://cdn.uviewui.com/uview/swiper/1.jpg',
				tabslist:[{name:'全部'},{name:'话题'},{name:'用户'}],
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
