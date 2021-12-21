<template>
	<view class="page">
		<ReviewCard :indexs="2" :showimg="true" :imgsrc="imgsrc" title="薇娅道歉" desc="根据浙江省杭州市事务部消息.." timestamp="2021-12-20"></ReviewCard>
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
				imgsrc:'/static/wy.jpg'
			};
		},
		components:{
			ReviewCard
		}
	}
</script>

<style lang="scss">

</style>
