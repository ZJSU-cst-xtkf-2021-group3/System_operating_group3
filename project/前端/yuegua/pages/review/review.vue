<template>
	<view class="page">
		<u-alert title="审核不通过的投稿可在草稿箱中继续编辑." type = "warning"></u-alert>
		<ReviewCard v-for="index in 10" :key="index" :indexs="1" :showimg="true" :imgsrc="imgsrc" title="这是标题" desc="这是简介" timestamp="2021-12-13"></ReviewCard>
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

<style lang="scss" scoped>
@import '@/static/variables.scss';

</style>
