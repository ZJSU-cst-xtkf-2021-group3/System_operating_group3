<template>
	<view class="page">
		<ReviewCard :indexs="2" :showimg="true" :imgsrc="imgsrc" title="这是标题" desc="这是简介" timestamp="2021-12-13"></ReviewCard>
		<view style="display: flex;align-items: center;justify-content: center;">
			<u-loadmore isDot line status="nomore"></u-loadmore>
		</view>
	</view>
</template>

<script>
	import ReviewCard from '../../components/ReviewCard'
	export default {
		data() {
			return {
				imgsrc:'https://cdn.uviewui.com/uview/album/1.jpg'
			};
		},
		components:{
			ReviewCard
		}
	}
</script>

<style lang="scss">

</style>
