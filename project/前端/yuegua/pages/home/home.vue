<template>
	<view>
		<view class="searchbar"><u-icon name="search" size="20"></u-icon><text>搜索</text></view>
		<!-- <uni-search-bar :v-model="searchtext" placeholder="搜索" :radius="100" maxlength="30" @confirm="search"></uni-search-bar> -->
		<u-tabs :list="tabslist" @click="tabclick" sticky></u-tabs>	
		<TextCard :imgsrc="src" :avatarsrc="src" partcontent="项目 'yuegua' 编译成功。" readcount="1879" title="这是一个标题" uname="wuji"></TextCard>
	</view>

</template>

<script>
	import TextCard from '@/components/TextCard'
    export default {
		name:'home',
        data() {
            return {
				src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',
				searchtext:"",
                tabslist: [{
                    name: '娱乐',
                },{
                    name: '体育',
                },{
                    name: '二次元'
                },{
                    name: '日常'
                },{
				    name: '时政'
				},{
                    name: '国际'
                }],
            }
        },
		methods: {
			search(){
				
			},
			tabclick(item) {
				//console.log('item', item);
			}
		},
		components:{
			TextCard
		}
    }
</script>

<style lang="scss">
@import '@/static/variables.scss';
.searchbar{
	height: 70rpx;
	margin: 10rpx 30rpx 10rpx 30rpx;
	border-radius: 40rpx;
	background-color: $searchbarcolor;
	box-shadow: 0px 0px 2px 1px $shadowcolor;
	// box-shadow: -2px -2px 2px 1px $shadowcolor;
	@extend %center;
}

</style>
