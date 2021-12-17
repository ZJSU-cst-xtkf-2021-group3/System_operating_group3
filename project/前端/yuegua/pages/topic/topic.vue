<template>
	<view class="page">


		<view style="margin-top: 20rpx; margin-left: 20rpx;margin-bottom: 20rpx; font-size: 40rpx;font-weight: 550;">{{basicInfo.title}}</view>
		<view style="margin: 10rpx 0 10rpx 0;display: flex;align-items: center;justify-content: space-between;">
			<view style="display: flex;align-items: center;">
				<u-icon :label="basicInfo.hotPoints" labelColor="#A1A1A1" size="23" name="/static/icons/热搜.png"></u-icon>
				<view style="margin-left: 20rpx;display: flex;align-items: center;">
					<u-tag :text="basicInfo.Tag" size="mini" type="warning" shape="circle"></u-tag>
				</view>				
			</view>
			<view style="display: flex;flex-direction: row; align-items: center;justify-content: space-between;">
				<!-- 举报按钮 -->
				<u-icon @click="set_tip_off_obj(1,TID)" style="margin-right: 20rpx;" name="warning" color="#AEAEAE" size="25"></u-icon>
				<focusbuttom :focus="isfocusauthor" @clicked="subscribe()"style="margin-right: 20rpx;"></focusbuttom>	
			</view>
		</view>

		<view class="udatabar">
			<view style="display: flex;align-items: center; justify-content: space-between" @click="toOthersSpace(basicInfo.UID)">
				<view style="display: flex;align-items: center; justify-content: space-between">
					<u-avatar :src="basicInfo.header" size="20"></u-avatar>
					<text style="margin-left: 15rpx;font-size: 33rpx;">{{basicInfo.Author}}</text>
					
				</view>
			
			</view>
			<view>
					<text style="font-size: 25rpx;color: #A1A1A1;">发布于 {{basicInfo.postTime}} 更新于 {{switchTime(basicInfo.lastUpDateTime)}} </text>
				
			</view>
		</view>

		
		
		<view style="padding: 20rpx 20rpx 0rpx 20rpx;">{{basicInfo.statement}}</view>
			
		<view v-if="votedata.hasvoteOption" style="padding: 10rpx;background-color: #fafafa;border-radius: 20rpx; margin-top: 20rpx;">
			<view>话题投票</view>

			<view v-for="(item,index) in votelist" :key="index" :class="['selectbar',item.selected && !votedata.hasvote?'bar-selected':'bar-normal']" @click="clickedselections(index)">
				<view v-show="votedata.hasvote" :class="['leftbar', item.selected?'bar-active':'bar-inactive']" ></view>
				<text class="lefttext" >{{item.content}}</text>
				<text v-show="votedata.hasvote" class="righttext">{{item.count}} 票 {{item.percent}}%</text>
			</view>
			<view v-show="voteselected && !votedata.hasvote" class="votebtn">
				<tm-button theme="bg-gradient-blue-accent" width="130" height="60" block @click="clickedvote">投票</tm-button>
			</view>
			<view >{{totalVotes}}人参与</view>
		</view>
		<!-- <view style="padding: 10rpx 20rpx 10rpx 20rpx;"><u-line color="#e7e6e4"></u-line></view> -->
		<view class="ctrlbar">
			<u-icon name="clock" size="22" label="时间导航" labelSize="16"></u-icon>
			<tm-button fab icon="../../static/icons/节点.png" icon-size="55" theme="bg-gradient-blue-accent" size="m" @click="addnode=true"></tm-button>
			<!-- <u-icon name="plus" size="22" @click="addnode=true"></u-icon> -->
		</view>
		
		<!-- jdxr -->
		<view class="timenodepanel" >
			<u-row>
				<u-col span="1" >
					<view class="timeline" :style="{height: this.timelineheight + 15 +'px'}">
						<view ><u-icon name="play-circle-fill" color="#1890FF" size="20"></u-icon></view>
						<u-line direction="col" :length="timelineheight-40" hairline color="#1890FF"></u-line>
						<view ><u-icon name="more-circle-fill" color="#1890FF" size="20"></u-icon></view>
					</view>					
				</u-col>
				<u-col span="11">
					<view class="timecontent" >
						<view v-for="(item,index) in nodelist">
							<NodeCard :key="index" :nodedata="item" @clickedPanel="clickednode(item)" @clickedfavor="clickedfavor(item)"></NodeCard>							
						</view>
					</view>
				</u-col>
			</u-row>
		</view>


		<view class="footerbar" >

			<view style="width: 45vw; display: flex;flex-direction: row;align-items: center; " >
				
						<u-search placeholder="请输入评论" searchIcon="" height="60" maxlength="30" :showAction="false" :clearabled="false"
						v-model="inputCommentWords" @search="postComments" style="margin-right: 20rpx;"></u-search>		
			</view>
			
			
			<view class="iconbtn" style="display: flex;flex-direction: row;align-items: center; justify-content: space-around">
				<view style="margin-right: 25rpx;">
				<u-icon @click="Star(1,TID)" :name="isfavor?'thumb-up-fill':'thumb-up'" space="0" :color="isfavor?'#1890FF':'#AEAEAE'" :labelColor="isfavor?'#1890FF':'#AEAEAE'" size="25" :label="basicInfo.star"></u-icon>
					
				</view>
<!-- 				<u-icon @click="Tip_off(1,TID)" :name="isfocus?'heart-fill':'heart'" space="0" :color="isfocus?'#1890FF':'#AEAEAE'" :labelColor="isfocus?'#1890FF':'#AEAEAE'" size="25" :label="basicInfo.tip_off"></u-icon>
 -->				<!-- <u-icon name="heart-fill" space="0" color="#AEAEAE" labelColor="#AEAEAE" label="123" size="23"></u-icon> -->
				<view style="margin-right: 25rpx;">
					<u-icon name="share-square" space="0" color="#AEAEAE" labelColor="#AEAEAE" label="" size="23" @click="Share()"></u-icon>
				</view>
			</view>
		</view>
		

		<!-- <view style="padding: 10rpx 20rpx 10rpx 20rpx;"><u-line color="#e7e6e4"></u-line></view> -->
		<!-- 老评论区 -->
		<tm-gap></tm-gap>
		
			<view class="ctrlbar" style="margin-top: 20rpx 20rpx;">
				<u-icon name="chat" size="24" label="评论" labelSize="16"></u-icon>
				<text style="font-size: 26rpx;color: #999999;">{{totalComments}}条</text>
			</view>
		<tm-gap></tm-gap>
		
			<view v-for="(item,index) in commentslist" :key=index  class="commentcard">
				<view class="commentdatabar">
					<view style="display: flex;align-items: center;justify-content: center;" @click="toOthersSpace(item.UID)">
						<u-avatar :src="item.header" size="20"></u-avatar>
						<view style="margin-left: 10rpx;font-size: 30rpx;">{{item.Uname}}</view>
					</view>
					<view style="font-size: 20rpx;">{{switchTime(item.time)}}</view>
				</view>
				<view class="comment" >
					{{item.value}}
				</view>
				<view class="commentfooterbar">
					<u-icon name="thumb-down" color="#2979ff" :label="item.tip_off" size="20" @click="set_tip_off_obj(4,item.CID)" ></u-icon>
					<u-icon name="thumb-up" color="#2979ff" :label="item.star" size="20"style="margin-right: 20rpx;"@click="Star(4,item.CID)"></u-icon>
				</view>
				<view style="display: flex;align-items: center;justify-content: center;">
					<u-line color="#d6d7d9"></u-line>
				</view>
			</view>
			<tm-gap></tm-gap>
			<tm-gap></tm-gap>
			<tm-gap></tm-gap>
		
		 
		<u-popup mode="bottom" :show="addnode" round closeable @close="addnode=false" :closeOnClickOverlay="false" >

			<view style="height: 1100rpx;">
				<view style="margin-top: 20rpx;display: flex;align-items: center;justify-content: center;">
					<tm-segTabs :round="24" :margin="[32,10]" font-size="s" :list="tabslist" color="white" activeFontColor="blue" bg-color="bg-gradient-blue-lighten" v-model="tabsactive"></tm-segTabs>
				</view>
				<Pulish :types="tabslist[tabsactive]"></Pulish>
			</view>
		</u-popup>
		<u-popup mode="bottom" :show="shownode" round closeOnClickOverlay @close="shownode=false">
			<view style="min-height: 500rpx;padding-bottom: 20rpx;">
				<view style="margin: 8rpx;position: relative;">
					<view style="font-size: 24rpx;color: #1890FF;text-align: center;">{{curnode.nodetime}}</view>
					<view style="position: absolute;top: 2rpx;right: 10rpx;">
						<u-icon @click="set_tip_off_obj(curnode.type,curnode.ID)" style="margin-left: 20rpx;" name="info-circle" color="#AEAEAE" size="20"></u-icon>
					</view>
				</view>
				<view style="margin: 10rpx;font-size: 33rpx;font-weight: 550;">{{curnode.title}}</view>
				<view class="udatabar">
					<view style="display: flex;align-items: center;"@click="toOthersSpace(curnode.UID)">
						<u-avatar :src="curnode.header" size="20"></u-avatar>
						<text style="margin-left: 15rpx;font-size: 33rpx;">{{curnode.Uname}}</text>
						<text style="margin-left: 30rpx;font-size: 25rpx;color: #A1A1A1;">· {{curnode.time}}</text>
					</view>
					<!-- <view>
						<focusbuttom :focus="isfocusnodeauthor" @clicked="isfocusnodeauthor=!isfocusnodeauthor"></focusbuttom>
					</view> -->
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
		<u-popup :show="showreport" mode="center" round :overlay="false" @close="showreport=false">
			<view style="width: 600rpx;border-radius: 20rpx;box-shadow: 0px 0px 2px 1px #D5D5D5;">
				<view style="height: 60rpx;text-align: center;line-height: 60rpx;font-size: 34rpx;">举报</view>
				<view style="padding: 10rpx 20rpx 20rpx 20rpx;">
					<u--textarea v-model="reportdata" placeholder="请输入反馈原因" height="100" maxlength="100" count></u--textarea>
				</view>
				<view style="margin-bottom: 20rpx;display: flex;align-items: center;justify-content: center;">
					<tm-button theme="bg-gradient-blue-accent" width="130" height="60" block @click="Tip_off()">举报</tm-button>
				</view>
			</view>
		</u-popup>
		<tm-message ref="toast"></tm-message>
		<tm-dialog v-model="showLoginAlert" content="需要登录后再操作哦!" confirmColor="bg-gradient-blue-accent":showCancel="false" theme="split"></tm-dialog>
	</view>
</template>

<script>
	import tmMessage from "@/tm-vuetify/components/tm-message/tm-message.vue"
	import Pulish from '../../components/Publish'
	import tmButton from '../../tm-vuetify/components/tm-button/tm-button'
	import tmTimeline from '../../tm-vuetify/components/tm-timeline/tm-timeline'
	import NodeCard from '../../components/NodeCard'
	import focusbuttom from '../../components/focusbuttom'
	import comment from '../../components/comment'
	export default {
		data() {
			return {
				tip_off_selecter:{type:0,id:0},
				TID:0,
				basicInfo:{},
				totalVotes:0,
				totalComments:0,
				voteslist:[],
				commentslist:[],
				percentage:50,
				inputCommentWords:"",
				showLoginAlert:false,
				addnode:false,
				shownode:false,
				isfocusauthor:false,
				showreport:false,
				isfavor:false,
				reportdata:'',
				timelineheight:20,
				src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',
				tabsactive:0,
				tabslist:['引用','爆料'],
				votedata:{hasvoteOption:false,hasvote:false},
				voteselected:false,
				votelist:[
					{content:'同意',count:10,percent:10,selected:false},
					{content:'不同意',count:90,percent:90,selected:false},
				],
				
				curnode:{},
				nodelist:[],
				
			};
		},
		methods:{
			clickedselections(index){
				if(this.votedata.hasvote) return
				let len = this.votelist.length
				if(this.votelist[index].selected) this.voteselected = false
				else this.voteselected = true
				// console.log(this.voteselected)
				for (let i = 0; i < len;++i) {
					if(i === index) this.votelist[index].selected = !this.votelist[index].selected
					else this.votelist[i].selected = false
					
				}
			},
			clickedvote(){
				this.votedata.hasvote = true;
			},
			clickednode(item){
				this.shownode = true
				this.curnode = item
			},

			clickedfavortopic(){
				this.Star(1,this.TID)
			},
			moveHandle(){
				return false
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
			loginAlert(){
				this.showLoginAlert=true
				
			},
			subscribe(){
				console.log("按了subscribe")
				//取消关注
				if(this.isfocusauthor){
					uni.request({
					    url: 'http://101.37.175.115/MyCenter/del/subscribe?TID='+this.TID,
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"GET",
							
					    success: (res) => {
						   if(res.data.res=="ok"){
							   console.log("取消关注")
							   this.$refs.toast.show({model:'success',wait:1000,lable:"取消关注成功"})
							   this.isfocusauthor=false
						   }
						   else{
							   this.toastHandler(res.data.res)
						   }
					    }
							
					});
				}
				if(!this.isfocusauthor){
					uni.request({
					    url: 'http://101.37.175.115/Topic/subscribe?TID='+this.TID,
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"GET",
							
					    success: (res) => {
						   if(res.data.res=="ok"){
							   console.log("关注成功")
							   this.$refs.toast.show({model:'success',wait:1000,label:"取消关注成功"})
							   this.isfocusauthor=true
						   }
						   else{
							   this.toastHandler(res.data.res)
						   }
					    }
							
					});
				}
	
			},
			//发布评论
			postComments(){
				var that =this
			  if(this.inputCommentWords==""){
				  this.$refs.toast.show({model:'disabled',wait:1000,label:"不能发布空内容哦！"})
			  }	
			  else{
				  uni.request({
				      url: 'http://101.37.175.115/Post/comment',
				  	header: {
				  	        'Content-Type': 'application/x-www-form-urlencoded' 
				  	    },
				  		method:"POST",
						data:{
							TID:this.TID,
							value:this.inputCommentWords
						},
				      success: (res) => {
						  if(res.data.res=="ok"){
							  that.$refs.toast.show({model:'success',wait:1000,label:"评论发布成功！"})
							  that.freshData(4)
							  
						  }
						  else{
							  that.toastHandler(res.data.res)
						  }
					  }

				  });
			  }
			},
			//点赞
			Star(type,id){
				//对话题
				if(type==1){
					uni.request({
					    url: 'http://101.37.175.115/Topic/star?TID='+this.TID,
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"GET",
							
					    success: (res) => {
						   if(res.data.res=="ok"){
							   console.log("点赞成功")
							   this.$refs.toast.show({model:'success',wait:1000,label:"EXP +3"})
						   }
						   else{
							   this.toastHandler(res.data.res)
						   }
					    }	
					});
					this.isfavor=true
					this.freshData(1)
					
				}
				//对引用
				if(type==2 || type==3){
					uni.request({
					    url: 'http://101.37.175.115/Event/star?ID='+id+'&type='+type,
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"GET",
							
					    success: (res) => {
						   if(res.data.res=="ok"){
							   console.log("点赞成功")
							   this.$refs.toast.show({model:'success',wait:1000,label:"EXP +3"})
						   }
						   else{
							   this.toastHandler(res.data.res)
						   }
					    }	
					});
					//刷新结点信息
					
				}
				//对评论
				if(type==4){
					uni.request({
					    url: 'http://101.37.175.115/Comments/star?CID='+id,
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"GET",
							
					    success: (res) => {
						   if(res.data.res=="ok"){
							   console.log("点赞成功")
							   this.$refs.toast.show({model:'success',wait:1000,label:"EXP +3"})
						   }
						   else{
							   this.toastHandler(res.data.res)
						   }
					    }	
					});
					this.freshData(4)
				}
				
			},
			//举报
			set_tip_off_obj(type,id){
				this.tip_off_selecter.type=type
				this.tip_off_selecter.id=id
				this.showreport=true
			},
			
			Tip_off(){
				var type=this.tip_off_selecter.type
				var id=this.tip_off_selecter.id
				//对话题
				if(type==1){
					
					uni.request({
					    url: 'http://101.37.175.115/Topic/tip-off?TID='+id,
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"GET",
							
					    success: (res) => {
						   if(res.data.res=="ok"){
							   console.log("举报成功")
							   this.showreport=false
							   
							   this.$refs.toast.show({model:'success',wait:1000,label:"反馈成功！"})
						   }
						   else{
							   this.toastHandler(res.data.res)
						   }
					    }	
					});
					this.freshData(1)
					
				}
				//对引用
					if(type==2 || type==3){
						uni.request({
							url: 'http://101.37.175.115/Event/tip-off?ID='+id+'&type='+type,
							header: {
									'Content-Type': 'application/x-www-form-urlencoded' 
								},
								method:"GET",
								
							success: (res) => {
							   if(res.data.res=="ok"){
								   console.log("举报成功")
								   this.showreport=false
								   this.shownode=false
								   this.$refs.toast.show({model:'success',wait:1000,label:"反馈成功！"})
							   }
							   else{
								   this.toastHandler(res.data.res)
							   }
							}	
						});
						this.freshData(2)
						
					}
				//对评论
				if(type==4){
					uni.request({
					    url: 'http://101.37.175.115/Comments/tip-off?CID='+id,
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"GET",
							
					    success: (res) => {
						   if(res.data.res=="ok"){
							   console.log("举报成功")
							   this.showreport=false
							   this.$refs.toast.show({model:'success',wait:1000,label:"反馈成功！"})
						   }
						   else{
							   this.toastHandler(res.data.res)
						   }
					    }	
					});
					this.freshData(4)
					
				}
			},
			
			//统一处理提示信息显示
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
			},
			//刷新页面数据
			freshData(type){
				if (type==1){
					//刷新基本信息
					uni.request({
					    url: 'http://101.37.175.115/Topic/show_info?TID='+this.TID,
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"GET",
							
					    success: (res) => {
					       if(res.data.res=="ok"){
							   this.basicInfo=res.data.data
							   if (res.data.data.isSubscribe){
								   this.isfocusauthor=true
							   }
							   else{
								   this.isfocusauthor=false
							   }
						   }
						   else{
							   this.toastHandler(res.data.res)
						   }
					    }
						
					});
				}
				if (type==2){
					//刷新话题和评论
				}
				if (type==4){
					//刷新评论
					uni.request({
					    url: 'http://101.37.175.115/Comments/all?TID='+this.TID,
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"GET",
							
					    success: (res) => {
					       if(res.data.res=="ok"){
								this.commentslist=res.data.data
								this.totalComments=res.data.total
						   }else{
							   this.toastHandler(res.data.res)
						   }
					    }
					});
	
				}
			},
			toOthersSpace(uid){
				console.log(uid)
				uni.navigateTo({
					url: '../other/other?uid='+uid
				})
			},
			Share(){
				var Shareconf={
							title: this.basicInfo.title + "快来跟我看看吧", 		// 分享标题[非必填]
							desc: '悦卦，一款次世代追瓜App', 		// 描述[非必填]
							imageUrl: this.basicInfo.mainPic, 	// 分享图片[非必填]
							path: '', 		// 分享路径[非必填]
							copyLink: '', 	// 复制链接[非必填]
							query: {w:123},	// 分享参数[非必填]
						}
				uni.$tm.vx.commit('setWxShare',Shareconf)
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
			//投票数据格式化
			loadVotelist(i,total){
				var obj={
					content:i.item,
					ID:i.ID,
					count:i.counts,
					selected:false,
					percent:parseInt(i.counts*100/total),
				}
				this.votelist.push(obj)
			}
		},
		onLoad(option){
			//接收传参TID
			var tid=option.tid
			this.TID=tid
			console.log(tid)
			
			//加载话题基本信息
			uni.request({
			    url: 'http://101.37.175.115/Topic/show_info?TID='+this.TID,
				header: {
				        'Content-Type': 'application/x-www-form-urlencoded' 
				    },
					method:"GET",
					
			    success: (res) => {
			       if(res.data.res=="ok"){
					   this.basicInfo=res.data.data
					   if (res.data.data.isSubscribe){
						   this.isfocusauthor=true
					   }
					   else{
						   this.isfocusauthor=false
					   }
				   }
				   else{
					   this.toastHandler(res.data.res)
				   }
			    }
				
			});
			// 加载话题投票区
			uni.request({
			    url: 'http://101.37.175.115/Topic/show_votes?TID='+this.TID,
				header: {
				        'Content-Type': 'application/x-www-form-urlencoded' 
				    },
					method:"GET",
					
			    success: (res) => {
			       if(res.data.res=="ok"){
					   if(res.data.data!=[]){
						   this.votedata.hasvoteOption=true
						   this.totalVotes=res.data.total
						   var len=res.data.data.length
						    for (var i=0;i<len;++i){
								this.loadVotelist(res.data.data[i],res.data.total)
							}
								console.log(this.votelist)
					   }
					   else{
						   this.votedata.hasvoteOption=false
					   }
					  
				   }else{
					   this.toastHandler(res.data.res)
				   }
			    }
			});
			//加载评论区
			uni.request({
			    url: 'http://101.37.175.115/Comments/all?TID='+this.TID,
				header: {
				        'Content-Type': 'application/x-www-form-urlencoded' 
				    },
					method:"GET",
					
			    success: (res) => {
			       if(res.data.res=="ok"){
						this.commentslist=res.data.data
						this.totalComments=res.data.total
				   }
				   else{
					   this.toastHandler(res.data.res)
				   }
			    }
			});
			//加载结点
			uni.request({
			    url: 'http://101.37.175.115/Event/all?TID='+this.TID,
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
					   this.toastHandler(res.data.res)
				   }
			    }
			});
			

		},
		onReady() {
			let query = uni.createSelectorQuery().in(this);
			query.select('.timenodepanel').boundingClientRect(data => {
			  // console.log(JSON.stringify(data))
			  this.timelineheight += data.height
			  // console.log(this.timelineheight)
			}).exec();
			
			uni.$on('StarNode',(data)=>{  
					this.Star(data.type,data.id)
			    })
			
		},
		onUnload() {
			uni.$off('StarNode');
		},
		
		components:{

			Pulish,tmButton,tmTimeline,NodeCard,focusbuttom,comment
		}
	}
</script>

<style lang="scss">
@import '@/static/variables.scss';
.udatabar{
	padding: 10rpx;
	@extend %betweencenter;
}

.ctrlbar{
	padding: 10rpx;
	@extend %betweencenter
}
.selectbar{
	display: flex;
	height: 50rpx;
	margin: 10rpx;
	border-radius: 25rpx;
	background-color: #F1F1F1;
	position: relative;
	.leftbar{
		height: 50rpx;width: 40%;
		border-radius: 25rpx;
		display: flex;
		// background: linear-gradient(to left,#50AAFF ,#007AFF );
	}
	.bar-active{
		background-color: #70CAFF;
	}
	.bar-inactive{
		background-color: #cacaca;
	}
	.lefttext{
		position: absolute;
		left: 30rpx;
		line-height: 50rpx;
	}
	.righttext{
		position: absolute;
		right: 20rpx;
		line-height: 50rpx;
	}
}
.bar-selected{
	border: 2rpx solid #007AFF;
	text{
		color: #1890FF;
	}
}
.bar-normal{
	text{
		color: #656565;
	}
}
.votebtn{
	margin: 20rpx 0 0rpx 0;
	@extend %center;
}
.timenodepanel{
	min-height: 50rpx;
	// background-color: #007AFF;
	.timeline{
		position: relative;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.timecontent{
		margin-top: 20rpx;
		// margin-bottom: 20rpx;

	}
}
.footerbar{
	height: 70rpx;
	width: 100%;
	padding: 5rpx 10rpx 5rpx 10rpx;
	position: fixed;
	bottom: 0;
	left: 0;
	display: flex;
	align-items: center;
	background-color: #fff;
	z-index: 999;
	.iconbtn{
		width: 50vw;
		padding: 0 10rpx 0 10rpx;
		@extend %betweencenter;
	}
}
.commentbar{
	margin-top: 20rpx;
	padding: 0 10rpx 0 10rpx;
	@extend %betweencenter;
}
.commentcard{
	padding: 10rpx;
	margin-bottom: 10rpx;
	.commentdatabar{
		display: flex;
		@extend %betweencenter;
	}
	.comment{
		padding: 10rpx;
	}
	.commentfooterbar{
		margin-right: 10rpx;
		margin-bottom: 5rpx;
		display: flex;
		align-items: center;
		justify-content: flex-start;
		flex-direction: row-reverse;
	}	
}

</style>
