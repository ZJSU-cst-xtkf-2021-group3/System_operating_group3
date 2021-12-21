<template>
	<view class="page">
		<u-alert title="审核不通过的投稿可在草稿箱中继续编辑." type = "warning"></u-alert>
		<ReviewCard v-for="(item,index) in Data" :key="index" :indexs="1" :showimg="true" :imgsrc="item.imgsrc" :title="item.title" :desc="item.desc" timestamp="2021-12-13"></ReviewCard>
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
				Data:[
				{
					imgsrc:'/static/luo.jpg',
					title:"罗永浩",
					desc:"被怀疑漏税"	
				},
					{
						imgsrc:'/static/EDG.jpg',
						title:"EDG",
						desc:"我们是冠军"	
					},
					{
						imgsrc:'/static/lh.jpg',
						title:"王力宏",
						desc:"致歉"	
					}
				],
				// imgsrc:'https://cdn.uviewui.com/uview/album/1.jpg'
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
