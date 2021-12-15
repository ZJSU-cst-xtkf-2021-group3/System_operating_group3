<template>

	<view class="page">
		<tm-alerts v-if="haveMsg" :margin=[32,0] color="blue" left-icon="icon-paperplane-fill"
					:label="this.Msg" close></tm-alerts>
		<view class="searchbar" @click="clicksearch"><u-icon name="search" size="20"></u-icon><text>搜索</text></view>
		<scroll-view scroll-x scroll-with-animation>
			<u-tabs :list="tabslist" :activeStyle="{ color: '#3c9cff' }" sticky @click="tabclick"></u-tabs>
		</scroll-view>
		<view v-show="showrecommd">
			
			<!-- <tm-alerts v-if="haveMsg" :label="this.Msg" left-icon="icon-paperplane-fill" close></tm-alerts> -->
			<u-swiper :list="list3" indicator indicatorMode="dot" interval="4000" circular ></u-swiper>
			<scroll-view scroll-y="true" class="scroll-Y" style="height: 50vh;"   @touchmove.stop.prevent="moveHandle">
				<TextCard v-for="(item,index) in topicList" :imgsrc="item.mainPic" :avatarsrc="item.header" :partcontent="item.statement" :showimg="true"
						   :likecnt="String(item.star)" :readcnt="String(item.Fcounts)" :title="item.title" :uname="item.Uname" :dislikecnt="String(item.tip_off)"
						   :time=switchTime(item.lastUpDateTime) :tag=item.Tag :ID="item.TID"
						  v-bind:key="item.TID" ></TextCard>
			</scroll-view>
			
			
		
		</view>
		<view v-show="showrank">
			<!-- <view style="display: flex;">
				<u-tag style="margin-left: 20rpx;" text="话题" :bgColor="topicselected?'#1890FF':'#fff'" :color="topicselected?'#fafafa':'#5f5f5f'" shape="circle"
				@click="topicselected=true"></u-tag>
				<u-tag style="margin-left: 15rpx;" text="活动" :bgColor="!topicselected?'#1890FF':'#fff'" :color="!topicselected?'#fafafa':'#5f5f5f'" shape="circle"
				@click="topicselected=false"></u-tag>
			</view> -->
			
			<scroll-view scroll-y="true" class="scroll-Y" style="height: 70vh;"  @scrolltolower="onReachScollBottom(0)" @touchmove.stop.prevent="moveHandle">
				<TextCard v-for="(item,index) in topicList" :imgsrc="item.mainPic" :avatarsrc="item.header" :partcontent="item.statement" :showimg="true"
						   :likecnt="String(item.star)" :readcnt="String(item.Fcounts)" :title="item.title" :uname="item.Uname" :dislikecnt="String(item.tip_off)"
						   :time=switchTime(item.lastUpDateTime) :tag=item.Tag :ID="item.TID"
						  v-bind:key="item.TID" ></TextCard>
			</scroll-view>
			
		</view>
		
		<view v-show="showfkinds">
			<scroll-view scroll-y="true" class="scroll-Y" style="height: 70vh;"  @scrolltolower="onReachScollBottom(1)" @touchmove.stop.prevent="moveHandle">
				<TextCard v-for="(item,index) in topicList" :imgsrc="item.mainPic" :avatarsrc="item.header" :partcontent="item.statement" :showimg="true"
						   :likecnt="String(item.star)" :readcnt="String(item.Fcounts)" :title="item.title" :uname="item.Uname" :dislikecnt="String(item.tip_off)"
						   :time=switchTime(item.lastUpDateTime) :tag=item.Tag :ID="item.TID"
						  v-bind:key="item.TID" ></TextCard>
			</scroll-view>
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
				topicList:{},
				has_next:false,
				has_previous:false,
				current_page:1,
				recommendList:{},
				haveMsg:false,
				Msg:[],
				current_category:0,
				
				
				src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',
                tabslist: [{name: '推荐',},{name: '热榜',},{name: '娱乐',},{name: '体育',},{name: '日常'},{name: '二次元'},{name: '数码'},{name: '国际时事'}],
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
					
					uni.request({
					    url: 'http://101.37.175.115/HomePage/recommend', 
					    
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"GET",
							
					    success: (res) => {
					       if(res.data.res=="ok"){
							   
							   this.topicList=res.data.data
							   
						   }
					    }
						
					});
					
				}
				else if(e.index === 1){
					this.showrank = true
					this.showrecommd = false
					this.showfkinds = false
					
					uni.request({
					    url: 'http://101.37.175.115/HomePage/default', 
					    data: {
					        page: 1
					    },
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"GET",
							
					    success: (res) => {
					       if(res.data.res=="ok"){
							   this.has_next=res.data.has_next
							   this.has_previous=res.data.has_previous
							   this.current_page=res.data.current_page
							   this.topicList=res.data.data
							   
						   }
					    }
						
					});
					
				}
				else{
					console.log("分类"+e.index)
					this.showfkinds = true
					this.showrank = false
					this.showrecommd = false
					
					
					uni.request({
					    url: 'http://101.37.175.115/HomePage/category?category='+(e.index-1), 
					    data: {
					        page: 1
					    },
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"GET",
							
					    success: (res) => {
					       if(res.data.res=="ok"){
							   this.has_next=res.data.has_next
							   this.has_previous=res.data.has_previous
							   this.current_page=res.data.current_page
							   this.topicList=res.data.data
							   
						   }
					    }
						
					});
					
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
			
			moveHandle(){
				return false
			},
		onReachScollBottom(e){
			var mainURL='http://101.37.175.115/'
			if (e===0){
				mainURL+="HomePage/default"
			}
			else{
				mainURL=mainURL+"HomePage/category"+"?category="+this.current_category
			}
				console.log(mainURL)
				var that=this
				console.log("触底刷新")
				if (that.has_next!="no"){
					
					
				var next=that.current_page+=1
				uni.request({
				    url: mainURL, 
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
					console.log("no more")
					return 
				}
				
		},

		},
		onLoad() {
			var that =this
			uni.request({
			    url: 'http://101.37.175.115/HomePage/recommend', 
			    
				header: {
				        'Content-Type': 'application/x-www-form-urlencoded' 
				    },
					method:"GET",
					
			    success: (res) => {
			       if(res.data.res=="ok"){
					   
					   that.topicList=res.data.data
					   
				   }
			    }
				
			});
		},
		
		onReady(){
			var that=this
				setInterval(function () {
								   
					   uni.request({
						   url: 'http://101.37.175.115/Message/RTMSG', 
						   
						header: {
								'Content-Type': 'application/x-www-form-urlencoded' 
							},
							method:"GET",
							
						   success: (res) => {
							
							  if(res.data.res=="ok"){
								if(res.data.isEmpty==false){
									console.log("msg arrived")
									that.haveMsg=true
									that.Msg=res.data.data
								}
								else{
									that.haveMsg=false
								}
		
						   }
						   }		   	
					   });
		
				}, 20000)
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
