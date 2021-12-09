<template>
	<view class="page">
		<view class="searchbar" @click="clicksearch"><u-icon name="search" size="20"></u-icon><text>搜索</text></view>
		<scroll-view scroll-x scroll-with-animation>
			<u-tabs :list="tabslist" :activeStyle="{ color: '#3c9cff' }" sticky @click="tabclick"></u-tabs>
		</scroll-view>
		<view v-show="showrecommd">
			<u-swiper :list="list3" indicator indicatorMode="dot" interval="4000" circular ></u-swiper>
			<view style="background-color: #fff;">
				<view style="margin: 10rpx 0 0rpx 10rpx;font-size: 30rpx;font-weight: 550;">活动</view>
				<u-scroll-list>
					<view v-for="(item,index) in 10" :key="index" class="actcard">
						<u--image mode="aspectFill" width="140" height="150" radius="6" src="https://cdn.uviewui.com/uview/album/1.jpg" :lazy-load="true"></u--image>
						<view style="color: #fff;">#今天天气真好！#</view>
					</view>
				</u-scroll-list>
			</view>
			<view style="margin: 10rpx 0 0rpx 15rpx;font-size: 30rpx;font-weight: 550;">话题</view>
			<TextCard :imgsrc="src" :avatarsrc="src" partcontent="项目 'yuegua' 编译成功。" 
					   likecnt="712" commentcnt="423432" readcnt="899" title="这是一个标题" uname="wuji"></TextCard>
			<ActivityCard partcontent="项目 'yuegua' 编译成功。"
					   likecnt="712" commentcnt="423432" sharecnt="899" title="这是一个标题"></ActivityCard>			
		</view>
		<view v-show="showrank">
			<view style="display: flex;">
				<u-tag style="margin-left: 20rpx;" text="话题" :bgColor="topicselected?'#1890FF':'#fff'" :color="topicselected?'#fafafa':'#5f5f5f'" shape="circle"
				@click="topicselected=true"></u-tag>
				<u-tag style="margin-left: 15rpx;" text="活动" :bgColor="!topicselected?'#1890FF':'#fff'" :color="!topicselected?'#fafafa':'#5f5f5f'" shape="circle"
				@click="topicselected=false"></u-tag>
			</view>
		</view>
		<view v-show="showfkinds">
			<view>
				<TextCard :imgsrc="src" :avatarsrc="src" partcontent="项目 'yuegua' 编译成功。"
						   likecnt="712" commentcnt="423432" readcnt="899" title="这是一个标题" uname="wuji"></TextCard>
			</view>
		</view>
	</view>
</template>

<script>
	import TextCard from '@/components/TextCard';
	import ActivityCard from '@/components/ActivityCard';
    export default {
		name:'home',
        data() {
            return {
				showrecommd:true,
				showrank:false,
				showfkinds:false,
				topicselected:true,
				src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',
                tabslist: [{name: '推荐',},{name: '热榜',},{name: '娱乐',},{name: '体育',},{name: '二次元'},{name: '日常'},{name: '时政'},{name: '国际'}],
				ranktabslist:[{name: '话题',},{name: '活动'}],
				list3: [
					'https://cdn.uviewui.com/uview/swiper/swiper3.png',
					'https://cdn.uviewui.com/uview/swiper/swiper2.png',
					'https://cdn.uviewui.com/uview/swiper/swiper1.png',
				],
			}
        },
		methods: {
			clicksearch(){
				uni.navigateTo({
					url:'../search/search'
				})
			},
			tabclick(e) {
				if(e.index === 0){
					this.showrecommd = true
					this.showrank = false
					this.showfkinds = false
				}
				else if(e.index === 1){
					this.showrank = true
					this.showrecommd = false
					this.showfkinds = false
				}
				else{
					this.showfkinds = true
					this.showrank = false
					this.showrecommd = false
				}
			}
		},
		components:{
			TextCard,
			ActivityCard
		}
    }
</script>

<style lang="scss" scoped>
@import '@/static/variables.scss';
$tagbgcolor:#fff;
$tagcolor:#5f5f5f;
$tagselectedbgcolor:#1890FF;
$tagselectedcolor:#fafafa;
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
.actpanel{
	background-color: #fff;
}
.actcard{
	width: 140px;
	padding: 5px;
	margin: 10rpx;
	border-radius: 15rpx;
	display: flex;
	flex-direction: column;
	align-items: center;
	background-color: #007AFF;
}

</style>
