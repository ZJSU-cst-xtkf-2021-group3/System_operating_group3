<template>
	<view class="page">
		<u-alert title="审核不通过的投稿可在草稿箱中继续编辑." type = "warning"></u-alert>
		<ReviewCard v-for="index in 10" :key="index" :indexs="1"></ReviewCard>
	</view>
</template>

<script>
	import ReviewCard from '../../components/ReviewCard'
	export default {
		data() {
			return {

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
