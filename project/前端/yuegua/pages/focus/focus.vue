<template>
	<view>
		<tm-tabs v-model="activeIndex" color="blue" :list="tabslist" ></tm-tabs>
		<view>
			<view v-show="activeIndex===0">
<!-- 				<TextCard v-for="(item,index) in topicList" :imgsrc="item.mainPic" :partcontent="item.statement" :showimg="true"
						   :likecnt="String(item.star)" :title="item.title" :dislikecnt="String(item.tip_off)"
						   :time=switchTime(item.lastUpDateTime) :ID="item.TID"
						  v-bind:key="index" ></TextCard> -->
				<TextCard v-for="(item,index) in topicList" :imgsrc="item.mainPic" :partcontent="item.statement" 
						   :likecnt="String(item.star)" :title="item.title" :dislikecnt="String(item.tip_off)"
						   :time=switchTime(item.lastUpDateTime) :ID="item.TID" :showimg="true"
						  v-bind:key="index" :uname=item.Uname :tag=item.Tag :avatarsrc=item.header ></TextCard>
		
			</view>
			<view v-show="activeIndex===1">
				<view v-for="(item,index) in userList" @click="clickedUser(item)">
					<UserCard :avtarsrc="item.header" :uname="item.Uname" :desc="item.introduction" ></UserCard>
				</view>
				
			</view>
		</view>
	</view>
</template>

<script>
	import tmTabs from '@/tm-vuetify/components/tm-tabs/tm-tabs'
	import TextCard from '@/components/TextCard';
	import UserCard from '@/components/UserCard';
	export default {
		components:{tmTabs,TextCard,UserCard},
		data() {
			return {
				topicList:[],
				userList:[],
				activeIndex:0,
				src:'https://cdn.uviewui.com/uview/swiper/1.jpg',
				tabslist:['话题','用户'],
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
			clickedUser(item){
				uni.navigateTo({
					url:`../other/other?UID=${item.UID}`,
				})
			}
		},
		onShow() {
			let that = this
			uni.request({
				url:'http://101.37.175.115/MyCenter/cat/my/subscribe',
				success(e) {
					// console.log(e)
					that.topicList = e.data.data
					console.log(that.topicList)
				},
				fail() {
					
				}
			})
			uni.request({
				url:'http://101.37.175.115/MyCenter/cat/my/follow',
				success(e) {
					console.log(e.data.data)
					that.userList = e.data.data
					
				},
				fail() {
					
				}
			})
		}
	}
</script>

<style lang="scss">
.avatarblock{
	margin: 0 10rpx 0 10rpx;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
}

.unametext{
	width: 120rpx;
	font-size: 15rpx;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
</style>
