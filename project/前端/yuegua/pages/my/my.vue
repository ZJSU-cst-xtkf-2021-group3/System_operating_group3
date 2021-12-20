<template>
	<view>
		<u-transition mode="fade-down" :show="true">
			<view class="headerpanel">
				<!-- <view class="bgimg"></view> -->
				<view class="headerpanel-uinfo">
					<view style="padding-top: 20rpx;">
						<view class="headerpanel-uinfo-name">
							<text style="font-size: 45rpx;font-weight: 550;margin-right: 30rpx;">{{basicInfo.Uname}}</text>
							<u-icon color="#FFC53D" style="margin-right: 10rpx;margin-top: 5rpx; " name="level" size="18" :label="basicInfo.rank" space="0"></u-icon>
						</view>
						<!-- xxxxx -->
						<u--text line="2" :text="basicInfo.statement"></u--text>
						<view class="levelbar">
							<u-line-progress :percentage="basicInfo.percent" height="8" activeColor="#1890FF" :showText="false"></u-line-progress>
							<!-- <view style="font-size: 10rpx;margin-left: 10rpx;text-align: center;">EXP</view> -->
						</view>
					</view>
					<view class="avatarpanel">
						<u-avatar size="80" :src="basicInfo.header"></u-avatar>
						<view style="margin-top: 20rpx;display: flex;align-items: center;" @click="clickeditinfo">
							<u-icon name="edit-pen-fill" size="19" color="#A1A1A1"></u-icon>
							<text style="color: #A1A1A1;" >编辑资料</text>
						</view>
						
					</view>
				</view>
				<view class="headerpanel-udata">
					<view class="datablock">
						<text style="font-size: 35rpx;font-weight: 550;">{{basicInfo.EXP}}</text>
						<text style="font-size: 25rpx;">EXP</text>
					</view>
					<view class="datablock">
						<text style="font-size: 35rpx;font-weight: 550;">{{basicInfo.Fcounts}}</text>
						<text style="font-size: 25rpx;">粉丝</text>
					</view>
					<view class="datablock">
						<text style="font-size: 35rpx;font-weight: 550;">{{identity}}</text>
						<text style="font-size: 25rpx;">认证</text>
					</view>
				</view>
			</view>
		</u-transition>
		<view class="controlpanel">
			<u-icon name="/static/icons/草稿.png" size="30" label="草稿" labelPos="bottom" labelSize="10" @click="clickdraft"></u-icon>
			<u-icon name="/static/icons/审核.png" size="30" label="审核进度" labelPos="bottom" labelSize="10" @click="clickreview"></u-icon>
			<u-icon name="/static/icons/seting.png" size="30" label="设置" labelPos="bottom" labelSize="10" @click="clickset"></u-icon>
		</view>
		<u-sticky>
			<view style="display: flex;align-items: center;justify-content: center;">
				<tm-segTabs :round="24" :margin="[32,10]" font-size="s" :list="tabslist" color="white" activeFontColor="blue" bg-color="bg-gradient-blue-lighten" v-model="active"></tm-segTabs>
			</view>
		</u-sticky>
		<view class="contpanel">
			<scroll-view scroll-y="true" class="scroll-Y" style="height: 58vh;"   @touchmove.stop.prevent="false">
				<view v-if="active===0">
					<TextCard v-for="(item,index) in topicList" :imgsrc="item.mainPic" :avatarsrc="item.header" :partcontent="item.statement" :showimg="true"
							   :likecnt="String(item.star)" :readcnt="String(item.Fcounts)" :title="item.title" :uname="item.Uname" :dislikecnt="String(item.tip_off)"
							   :time=switchTime(item.lastUpDateTime) :tag=item.Tag :ID="item.TID"
							  v-bind:key="index" ></TextCard>
				</view>
				<view v-if="active===1" class="timecontent">
					<view v-for="(item,index) in nodelist">
						<NodeCard :key="index" :nodedata="item" @clickedPanel="clickednode(item)" ></NodeCard>							
					</view>
				</view>
				
			</scroll-view>
			
		</view>
		
		<u-popup mode="bottom" :show="shownode" round closeOnClickOverlay @close="shownode=false">
			<view style="min-height: 500rpx;padding-bottom: 20rpx; margin-left: 10rpx;">
				<view style="margin: 8rpx;position: relative;">
					<view style="font-size: 24rpx;color: #1890FF;text-align: center;">{{curnode.nodetime}}</view>
					
				</view>
				<view style="margin: 10rpx;font-size: 33rpx;font-weight: 550;">{{curnode.title}}</view>
				<view class="udatabar">
					<view style="display: flex;align-items: center;">
						<u-avatar :src="curnode.header" size="20"></u-avatar>
						<text style="margin-left: 15rpx;font-size: 33rpx;">{{curnode.Uname}}</text>
						<text style="margin-left: 30rpx;font-size: 25rpx;color: #A1A1A1;">· {{curnode.time}}</text>
					</view>
					
				</view>
				<view style="padding: 20rpx 20rpx 20rpx 20rpx;">
					<view style="margin-bottom: 10rpx;">{{curnode.content}}</view>
					<view v-if="curnode.typeName == '引用'" style="margin-top: 20rpx;">
						<u--text type="info" :text="curnode.src" lines=3 size="20"></u--text>
					</view>
					<view v-if="curnode.typeName == '爆料' && curnode.imglist.length > 0"><u-album :urls="curnode.imglist" multipleSize="75"></u-album></view>
				</view>
				<view v-if="curnode.typeName == '引用'" style="margin: 10rpx 10rpx 0rpx 10rpx;display: flex;align-items: center;justify-content: center;">
					<view style="padding: 10rpx 25rpx 10rpx 25rpx;border-radius: 50rpx;background-color: #fff;display: flex;align-items: center;justify-content: center;box-shadow: 0px 0px 2px 1px #e5e5e5;">
						
						<uni-link color="#1890FF" :href="curnode.src" text="前往浏览"></uni-link>
						<u-icon color="#1890FF" size="15"  name="arrow-rightward"></u-icon>
					</view>
				</view>
			</view>
		</u-popup>
	
		
		
	<tm-message ref="toast"></tm-message>
	<tm-dialog v-model="showLoginAlert" content="需要登录后再操作哦!" confirmColor="bg-gradient-blue-accent":showCancel="false" theme="split"></tm-dialog>
	
	
	</view>
	
</template>

<script>
	import NodeCard from '../../components/NodeCard'
	import UserCard from '@/components/UserCard'
	import TextCard from '@/components/TextCard';
	import tmSegTabs from '@/tm-vuetify/components/tm-segTabs/tm-segTabs.vue'
	export default {
		data() {
			return {
				active:0,
				headerheight:0,
				src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',
				tabslist:['发布的话题','发布的节点'],
				basicInfo:{},
				identity:"",
				topicList:[],
				curnode:{},
				nodelist:[],
				shownode:false,
				showLoginAlert:false
			};
		},
		onLoad() {
			var that=this
			this.headerheight = uni.getStorageSync('headerheight')
			//基本信息
			uni.request({
			    url: 'http://101.37.175.115/MyCenter/basicInfo', 
			    
				header: {
				        'Content-Type': 'application/x-www-form-urlencoded' 
				    },
					method:"GET",
				
			    success: (res) => {
			       if(res.data.res=="ok"){
					  that.basicInfo=res.data.data
						that.identity="注册用户"
						if(res.data.data.ifPassedExam){
							that.identity="会员用户"
						}
					  
						if(res.data.data.isEditor){
							that.identity="编辑"
						}			
				   }
				   else{
					   console.log(res.data)
					    this.toastHandler(res.data.res)
				   }
			    }
				
			});
			//发布的话题
			uni.request({
			    url: 'http://101.37.175.115/MyCenter/cat/mypost/topics', 
			    
				header: {
				        'Content-Type': 'application/x-www-form-urlencoded' 
				    },
					method:"GET",
				
			    success: (res) => {
			       if(res.data.res=="ok"){
					  that.topicList=res.data.data
				   }
				   else{
					   console.log(res.data)
					    this.toastHandler(res.data.res)
				   }
			    }
				
			});
			
			//加载结点
			uni.request({
			    url: 'http://101.37.175.115/MyCenter/cat/mypost/events',
				header: {
				        'Content-Type': 'application/x-www-form-urlencoded' 
				    },
					method:"GET",
					
			    success: (res) => {
			       if(res.data.res=="ok"){
					   var len= res.data.data.length
					   
						for(var i = 0; i < len; i++){
							this.format2list(res.data.data[i])
						}
				   }
				   else{
					   console.log(res.data)
					   this.toastHandler(res.data.res)
				   }
			    }
			});
			
		},
		methods:{
			clickset(){
				uni.navigateTo({
					url:'../seting/seting'
				})
			},
			clickeditinfo(){
				uni.navigateTo({
					url:'../info/info'
				})
			},
			clickreview(){
				uni.navigateTo({
					url:'../review/review'
				})
			},
			clickdraft(){
				uni.navigateTo({
					url:'../draft/draft'
				})
			},
			clickednode(item){
				this.shownode = true
				this.curnode = item
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
			format2list(i){
				if(i.type==2){
					var tmp =this.switchTime(i.time)
					var obj={title:i.title,
							content:i.statement,
							nodetime:i.eventTime,
							time:tmp,
							typeName:'引用',
							type:2,
							ID:i.ID,
							imglist:[],
							favorcnt:i.star,
							header:i.header,
							src:i.url,
							star:i.star,
							Uname:i.Uname,
							UID:i.UID,
							tip_off:i.tip_off
							}
							
					this.nodelist.push(obj)
				}
				if(i.type==3){
					var tmp =this.switchTime(i.time)
					var obj={title:i.title,
							content:i.text,
							nodetime:i.eventTime,
							time:tmp,
							typeName:'爆料',
							type:3,
							ID:i.ID,
							imglist:i.pics,
							favorcnt:i.star,
							header:i.header,
							src:i.url,
							Uname:i.Uname,
							star:i.star,
							tip_off:i.tip_off
							}
							
					this.nodelist.push(obj)
				}
			},
			
			toastHandler(e){
				if(e=="login please"){
					this.showLoginAlert=true
					return
				}
				if(e=="refused"){
					this.$refs.toast.show({model:'error',wait:1000,label:"本人回避，或已完成操作！"})
					return
				}
				if(e=="failed"){
					this.$refs.toast.show({model:'error',wait:1000,label:"阿偶，出错啦！"})
					return
				}
				if(e=="permission denied"){
					this.$refs.toast.show({model:'error',wait:1000,label:"您还无此权限！"})
					return
				}
				if(e=="ok"){
					this.$refs.toast.show({model:'success',wait:1000,label:"发布成功！"})
					return
				}	
			},
		},
		components:{
			UserCard,
			tmSegTabs,
			TextCard,
			NodeCard,
		}
	}
</script>

<style lang="scss">
@import '@/static/variables.scss';

.headerpanel{
	height: 21vh;
	padding: 20rpx;
	display: flex;
	position:relative;
	flex-direction: column;
	justify-content: space-between;
	background: linear-gradient(to top,$cardcolor 60%, #1890FFA0 );
	border-radius: 0 0 30rpx 30rpx;
	.bgimg{
		position:absolute;
		left: 0; right: 0; top: 0; bottom: 0;
		background: url('https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png') center;
		background-size: cover;
		filter: blur(50px);
	}
	.headerpanel-uinfo{
		filter: blur(0px);
		padding: 0 20rpx 0 20rpx;
		display: flex;
		align-items: flex-start;
		justify-content: space-between;
		.headerpanel-uinfo-name{
			margin-bottom: 10rpx;
			display: flex;
			align-items: flex-start;
		}		
		.levelbar{
			width: 60vw;
			margin-top: 10rpx;
		}
		.avatarpanel{
			display: flex;
			flex-direction: column;
			align-items: center;
		}
	}
	.headerpanel-udata{
		display: flex;
		padding: 0rpx 40rpx 10rpx 30rpx;
		.datablock{
			margin: 0rpx 40rpx 20rpx 40rpx;
			display: flex;
			flex-direction: column;
			align-items: center;
		}
	}
}

.controlpanel{
	margin-top: 20rpx;
	margin-bottom: 20rpx;
	display: flex;
	justify-content: space-around;
}
.popupheader{
	position: relative;font-size: 35rpx;line-height: 80rpx;text-align: center;color: #fafafa;height: 80rpx;background-color: #1890FF;border-radius: 20rpx 20rpx 0 0;
}
.contpanel{
	height: 300rpx;
	margin: 10rpx;
	margin-top: 15rpx;
	padding: 20rpx;
	border-radius: 20rpx;
	background-color: #fafafa;
}
.timecontent{
		margin-top: 20rpx;
		margin-left: 25rpx;
		// margin-bottom: 20rpx;

	}
</style>
