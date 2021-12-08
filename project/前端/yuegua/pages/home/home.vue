<template>
	<view class="page">
		<view class="searchbar" @click="clicksearch"><u-icon name="search" size="20"></u-icon><text>搜索</text></view>
		<u-tabs :list="tabslist" @click="tabclick" sticky></u-tabs>
		    <u-swiper :list="list3" indicator indicatorMode="dot" interval="4000" circular ></u-swiper>
		<TextCard :imgsrc="src" :avatarsrc="src" partcontent="项目 'yuegua' 编译成功。" 
				   likecnt="712" commentcnt="423432" readcnt="899" title="这是一个标题" uname="wuji"></TextCard>
		<ActivityCard partcontent="项目 'yuegua' 编译成功。"
				   likecnt="712" commentcnt="423432" sharecnt="899" title="这是一个标题"></ActivityCard>
	</view>
</template>

<script>
	import TextCard from '@/components/TextCard';
	import ActivityCard from '@/components/ActivityCard';
    export default {
		name:'home',
        data() {
            return {
				src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',
                tabslist: [{name: '推荐',},{name: '娱乐',},{name: '体育',},{name: '二次元'},{name: '日常'},{name: '时政'},{name: '国际'}],
				list3: [
					'https://cdn.uviewui.com/uview/swiper/swiper3.png',
					'https://cdn.uviewui.com/uview/swiper/swiper2.png',
					'https://cdn.uviewui.com/uview/swiper/swiper1.png',
				],
			}
        },
		methods: {
			clicksearch(){
				
			},
			tabclick(item) {
				//console.log('item', item);
			}
		},
		components:{
			TextCard,
			ActivityCard
		}
    }
</script>

<style lang="scss">
@import '@/static/variables.scss';
.page{
	.searchbar{
		height: 60rpx;
		margin: 10rpx 30rpx 10rpx 30rpx;
		border-radius: 30rpx;
		background-color: $searchbarcolor;
		box-shadow: 0px 0px 2px 1px $shadowcolor;
		// box-shadow: -2px -2px 2px 1px $shadowcolor;
		@extend %center;
	}	
}


</style>
