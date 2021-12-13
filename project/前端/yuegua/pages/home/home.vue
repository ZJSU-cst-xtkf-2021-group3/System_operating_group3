<template>
	<view class="page">
		<view class="searchbar" @click="clicksearch"><u-icon name="search" size="20"></u-icon><text>搜索</text></view>
		<scroll-view scroll-x scroll-with-animation>
			<u-tabs :list="tabslist" :activeStyle="{ color: '#3c9cff' }" sticky @click="tabclick"></u-tabs>
		</scroll-view>
		<view v-show="showrecommd">
			<u-swiper :list="list3" indicator indicatorMode="dot" interval="4000" circular ></u-swiper>
			
			
			<TextCard v-for="(item,index) in topicList" :imgsrc="item.mainPic" :avatarsrc="item.header" :partcontent="item.statement" :showimg="true"
					   :likecnt="String(item.star)" :readcnt="String(item.Fcounts)" :title="item.title" :uname="item.Uname" :dislikecnt="String(item.tip_off)"
					   :time=switchTime(item.lastUpDateTime) :tag=item.Tag :ID="item.TID"
					  v-bind:key="item.TID" ></TextCard>
		
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
				<TextCard  :imgsrc="src" :avatarsrc="src" partcontent="项目 'yuegua' 编译成功。" :showimg="true"
						   likecnt="x" commentcnt="x" readcnt="x" title="这是一个标题" uname="wuji"></TextCard>
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
				topicList:null,
				has_next:false,
				has_previous:false,
				current_page:1,
				
				
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
			},
			switchTime(time){
				var now = parseInt(new Date().getTime()/1000);
				var Dvalue=parseInt((now-parseInt(time))/3600)
				if (Dvalue<=24){
					return Dvalue+"小时前"
				}
				else{
					var days=parseInt(Dvalue/24)
					return days+"天前"
				}
			},
			
		},
		onLoad() {
			var that =this
			uni.request({
			    url: 'http://101.37.175.115/HomePage/default', 
			    data: {
			        page: this.current_page
			    },
				header: {
				        'Content-Type': 'application/x-www-form-urlencoded' 
				    },
					method:"GET",
					
			    success: (res) => {
			       if(res.data.res=="ok"){
					   that.has_next=res.data.has_next
					   that.has_previous=res.data.has_previous
					   that.current_page=res.data.current_page
					   that.topicList=res.data.data
					   
				   }
			    }
				
			});
		},
		onReachBottom(){
				var that=this
				console.log("触底刷新")
				if (that.has_next!="no"){
					
				var next=that.current_page+=1
				uni.request({
				    url: 'http://101.37.175.115/HomePage/default', 
				    data: {
				        page: next
				    },
					header: {
					        'Content-Type': 'application/x-www-form-urlencoded' 
					    },
						method:"GET",
						
				    success: (res) => {
				       if(res.data.res=="ok"){
						   that.has_next=res.data.has_next
						   that.has_previous=res.data.has_previous
						   that.current_page=res.data.current_page
						   that.topicList=that.topicList.concat(res.data.data)
						   
					   }
				    }
					
					});
				}
				
				else
				{
					return 
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
