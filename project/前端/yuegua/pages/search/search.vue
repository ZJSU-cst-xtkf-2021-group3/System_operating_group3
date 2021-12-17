<template>
	<view class="page">
		<view class="searchbar">
			<u-search placeholder="请输入内容" v-model="searchkeyword" height="60" maxlength="30" :focus="true" @search="onsearch" @custom="onsearch"></u-search>
		</view>
		<tm-gap></tm-gap>
		<tm-gap></tm-gap>
		<view class="hotsearch">
			<u-icon label="热搜榜" size="25" name="/static/icons/热搜.png"></u-icon>
			<view style="padding: 5rpx 30rpx 5rpx 30rpx;"><u-line color="#d6d7d9"></u-line></view>
			
			<view class="hotlist">
				<view v-for="(item,index) in rankData" :key="index" style="width: 50%;margin: 5rpx 0 5rpx 0;" @click="seeMore(item.TID)">
					<text style="margin-right: 30rpx;font-size: 35rpx;font-weight:bold;font-style: italic;">{{index + 1}}</text><text>{{item.title}}</text>
				</view>
				
			</view>
		</view>
		<tm-gap></tm-gap>
		<tm-gap></tm-gap>
		<view class="searchhistory">
			<view>
				<text>搜索记录</text>
			</view>
			<!--  -->
			<view class="footer" >
				<u-tag v-for="(item,index) in searchHistory" :kry=index :text="item" shape="circle" size="mini" bgColor="#45aaf2" style="margin-left: 10rpx;" @click="tagclick(item)"></u-tag>
			</view>
			
			<view style="display: flex;align-items: center;justify-content: center;margin-top: 50rpx;" @click="removeHistory()">
				<u-icon name="trash" color="#a5a5a5" label="清除搜索记录" size="22" labelSize="12"></u-icon>
			</view>
		</view>
		<u-popup mode="bottom" :show="showres" round closeable @close="showres=false" :overlay="false" :closeOnClickOverlay="false"  >
			<view :style="{height:'calc(100vh - ' + headerheight +'px)'}" @touchmove.stop.prevent="moveHandle">
				
				 <scroll-view scroll-y="true" class="scroll-Y" style="height: 80vh;" @scrolltolower="onReachScollBottom" >
					  <TextCard v-for="(item,index) in searchData" :key=index :imgsrc="item.mainPic" :avatarsrc="item.header" :partcontent="item.statement" :showimg="true"
							   :likecnt="String(item.star)" :readcnt="String(item.Fcounts)" :title="item.title" :uname="item.Uname" :dislikecnt="String(item.tip_off)"
							   :time=switchTime(item.lastUpDateTime) :tag=item.Tag :ID="item.TID "
							  v-bind:key="index" style="margin-top: 70rpx;"></TextCard>
									  
				 </scroll-view>
				
				
			</view>
			
		</u-popup>
		<u-toast ref="uToast"></u-toast>
	</view>
	
</template>

<script>
	import TextCard from '@/components/TextCard';
	export default {
		data() {
			return {
				searchkeyword:'',
				headerheight:0,
				showres:false,
				rankData:null,
				searchData:null,
				searchHistory:[],
				has_next:false,
				has_previous:false,
				current_page:1,
			};
		},
		methods:{
			onsearch(){
				if(this.searchkeyword === ''){
					this.$refs.uToast.show({
						type:'error',
						message: "搜索内容为空！",
					})
				}
				else{
					//搜索记录
					this.searchHistory.push(this.searchkeyword)
					uni.setStorage({
					    key: 'searchHistory',
					    data: this.searchHistory,
					    success: function () {
					        console.log('success');
					    }
					});
					
						uni.request({
						    url: 'http://101.37.175.115/HomePage/search', 
						    data: {
						        key: this.searchkeyword,
								page:this.current_page
						    },
						    header: {
						         'Content-Type': 'application/x-www-form-urlencoded' 
						    },
						    success: (res) => {
								if (res.data.res=='ok'){
									if(res.data.data[0] != null){
										this.searchData=res.data.data
										this.showres = true
		
									}
									else{
										this.$refs.uToast.show({
											type:'default',
											message: "暂时没有相关内容哦",
										})
									}
									
									
								}
						        
						    }
						});
				}
				
			},
			seeMore(e){
				console.log(e)
				
				//navigate
			},
			removeHistory(){
				this.searchHistory=[]
				uni.setStorage({
				    key: 'searchHistory',
				    data: this.searchHistory,
				    success: function () {
				        console.log('removed');
				    }
				});
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
			tagclick(e){
				var that= this
				uni.request({
				    url: 'http://101.37.175.115/HomePage/search', 
				    data: {
				        key: e,
						page:1
				    },
				    header: {
				         'Content-Type': 'application/x-www-form-urlencoded' 
				    },
				    success: (res) => {
						if (res.data.res=='ok'){
							if(res.data.data[0] != null){
								that.showres = true
								that.searchData=res.data.data		
						
							}
							else{
								this.$refs.uToast.show({
									type:'default',
									message: "暂时没有相关内容哦",
								})
							}
	
						}
				        
				    }
				});
			},
			moveHandle(){
				return false
			},
			
			onReachScollBottom(){
				var that=this
					console.log("触底刷新")
					if (that.has_next!="no" && that.searchkeyword!=""){
						
					var next=this.current_page+=1
					uni.request({
					    url: 'http://101.37.175.115/HomePage/search', 
					    data: {
					        key: that.searchkeyword,
							page:next
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
							   that.searchData=that.searchData.concat(res.data.data)
							   
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
		mounted() {
				const query = uni.createSelectorQuery().in(this);
				query.select('.searchbar').boundingClientRect(data => {
					this.headerheight = data.height;
				}).exec();
				
				uni.getSystemInfo({
					success: (e) => {
						this.headerheight += e.windowTop + 6
					}
				})
		
			},
			onLoad() {
				var that =this
				uni.getStorage({
				    key: 'searchHistory',
				    success: function (res) {
				        that.searchHistory=res.data
				    }
				});
				
				
				uni.request({
				    url: 'http://101.37.175.115/HomePage/rank', 
				    
					header: {
					        'Content-Type': 'application/x-www-form-urlencoded' 
					    },
						method:"GET",
						
				    success: (res) => {
				       if(res.data.res=="ok"){
						  
						   that.rankData=res.data.data
						   
					   }
				    }
					
				});
			},
			
			
			components:{
				TextCard,
			
			}
	}
</script>

<style lang="scss" scoped>
@import '@/static/variables.scss';
.page{
	.searchbar{
		height: 60rpx;
		margin: 10rpx 30rpx 10rpx 30rpx;
		@extend %center;
	}	
	.searchhistory{
		padding: 0rpx 20rpx 0rpx 20rpx;
		margin: 10rpx 0 10rpx 0;	
		.footer{
			padding: 10rpx 0 10rpx 0;
			display: flex;
			flex-wrap: wrap;
		}
	}
	.hotsearch{
		background-color: #fefefe;
		
		
		.hotlist{
			padding: 10rpx 20rpx 10rpx 20rpx;
			display: flex;
			margin-left: 80rpx;
			margin-right: 20rpx;
			flex-wrap: wrap;
		}
	}
	
}

</style>
