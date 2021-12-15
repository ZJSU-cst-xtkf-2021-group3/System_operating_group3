<template>
	
	<view>
		
		<view class="cell" @click="showMyFans()">
			
			<u-row>
				<u-col span="2">
					<u--image width="50" height="50" radius="27" :src="fanssrc"></u--image>
				</u-col>
				<u-col span="10">
					<view class="rightpart">
						<view style="margin-left: 20rpx;font-size: 32rpx;">关注我的</view>
						<view><u-icon name="arrow-right" color="#999999" size="18"></u-icon></view>
					</view>
				</u-col>
			</u-row>
			<view style="height: 2rpx;position: absolute;bottom: 0;left: 70px;right: 0;background-color: #EEEEEE;"></view>
		</view>
		<view class="cell" @click="showMyStar()">
			<u-row>
				<u-col span="2">
					<u--image width="55" height="55" radius="27" :src="favorsrc"></u--image>
				</u-col>
				<u-col span="10">
					<view class="rightpart">
						<view style="margin-left: 20rpx;font-size: 32rpx;">点赞</view>
						<view><u-icon name="arrow-right" color="#999999" size="18"></u-icon></view>
					</view>
				</u-col>
			</u-row>
			<view style="height: 2rpx;position: absolute;bottom: 0;left: 70px;right: 0;background-color: #EEEEEE;"></view>
		</view>

		<view>
			<!-- <MsgCard :avtarsrc="msgsrc" uname="用户名" msg="他点赞了你的评论!" timestamp="1天前"></MsgCard> -->
			<MsgCard v-for="(item,index) in sysMessage":key=index :avtarsrc="msgsrc" uname="审核消息" :msg="item.value" :timestamp="switchTime(item.postTime)" :Type="item.type" :typeID="item.typeID" ></MsgCard>
		</view>
		<u-popup mode="bottom" :show="fovar" round closeable @close="fovar=false">
			<!-- <view :style="{height:'calc(100vh - ' + headerheight +'px)'}"></view> -->
			<scroll-view scroll-y="true" class="scroll-Y" style="height: 80vh;" >
				<UserCard v-for="(item,index) in myStarlist " :key=index :avtarsrc="item.header" :uname="item.msg" :desc="item.time"></UserCard>	
			</scroll-view>
			
			
		</u-popup>
		<u-popup mode="bottom" :show="focus" round closeable @close="focus=false">
			<!-- <view :style="{height:'calc(100vh - ' + headerheight +'px)'}"></view> -->
			<scroll-view scroll-y="true" class="scroll-Y" style="height: 80vh;" >
				<view v-for="(item,index) in myFocuslist " :key=index @click="toOthersSpace(item.UID)">
					<UserCard :avtarsrc="item.header" :uname="item.uname" :desc="item.introduction" ></UserCard>
				</view>
					
			</scroll-view>
			
		</u-popup>
<!-- 		<u-popup mode="bottom" :show="comm" round closeable @close="comm=false">
			<view :style="{height:'calc(100vh - ' + headerheight +'px)'}"></view>
		</u-popup> -->
	</view>
</template>

<script>
import MsgCard from '../../components/MsgCard'
import UserCard from '../../components/UserCard'
export default {
	data() {
		return {
			fanssrc:"/static/images/粉丝.png",
			favorsrc:"/static/images/点赞.png",
			msgsrc:"/static/images/系统通知.png",
			headerheight:0,
			fovar:false,
			focus:false,
			comm:false,
			sysMessage:null,
			myStarlist:{},
			myFocuslist:{}
		};
	},
	methods:{
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
		showMyStar(){
				var that =this
					uni.request({
					    url: 'http://101.37.175.115/Message/stars', 
					    
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"GET",
							
					    success: (res) => {
					       if(res.data.res=="ok"){
								that.myStarlist=res.data.data
								that.fovar=true
						   }
					    }
						
					});
		},
		
		showMyFans(){
			var that =this
				uni.request({
				    url: 'http://101.37.175.115/Message/followers', 
				    
					header: {
					        'Content-Type': 'application/x-www-form-urlencoded' 
					    },
						method:"GET",
						
				    success: (res) => {
						
				       if(res.data.res=="ok"){
							that.myFocuslist=res.data.data
							that.focus=true
					   }
				    }
					
				});
		},
		moveHandle(){
			return false
		},
		toOthersSpace(uid){
			console.log(uid)
			uni.navigateTo({
				url: '../other/other?uid='+uid
			})
		},
	},
	onLoad() {
		this.headerheight += uni.getStorageSync('headerheight')
		var that =this
			uni.request({
			    url: 'http://101.37.175.115/Message/sysNotes', 
			    
				header: {
				        'Content-Type': 'application/x-www-form-urlencoded' 
				    },
					method:"GET",
					
			    success: (res) => {
			       if(res.data.res=="ok"){
					  that.sysMessage=res.data.data
					   
				   }
			    }
				
			});
		},
		
	
	components:{
		MsgCard,
		UserCard,
	},
	

}
</script>

<style lang="scss">
@import '@/static/variables.scss';
.cell{
	position: relative;
	padding: 15rpx;
	.rightpart{
		@extend %betweencenter
	}
}
.msgbar{
	height: 60rpx;margin: 10rpx 0 10rpx 0;padding-left: 30rpx;font-size: 30rpx;background-color: #fafafa;
	display: flex;
	align-items: center;
}
.popuppanel{
	height: calc();
	background-color: #007AFF;
}


</style>
