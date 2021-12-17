<template>
	<view class="page">


		<view style="margin-top: 10rpx;font-size: 33rpx;font-weight: 550;">{{basicInfo.title}}</view>
		<view style="margin: 10rpx 0 10rpx 0;display: flex;align-items: center;justify-content: space-between;">
			<view style="display: flex;align-items: center;">
				<u-icon :label="basicInfo.hotPoints" labelColor="#A1A1A1" size="23" name="/static/icons/热搜.png"></u-icon>
				<view style="margin-left: 20rpx;display: flex;align-items: center;">
					<u-tag :text="basicInfo.Tag" size="mini" type="warning" shape="circle"></u-tag>
				</view>				
			</view>
			<view>
				<u-icon @click="showreport=true" style="margin-left: 20rpx;" name="info-circle" color="#AEAEAE" size="22"></u-icon>
			</view>
		</view>

		<view class="udatabar">
			<view style="display: flex;align-items: center;" @click="toOthersSpace(basicInfo.UID)">
				<u-avatar :src="basicInfo.header" size="20"></u-avatar>
				<text style="margin-left: 15rpx;font-size: 33rpx;">{{basicInfo.Author}}</text>
				<text style="margin-left: 10rpx;font-size: 25rpx;color: #A1A1A1;">发布于 {{basicInfo.postTime}} 更新于 {{switchTime(basicInfo.lastUpDateTime)}} </text>
				
			</view>
			<view>

				<focusbuttom :focus="isfocusauthor" @clicked="isfocusauthor=!isfocusauthor"></focusbuttom>
			</view>
		</view>

		<view style="margin: 10rpx 10rpx 20rpx 10rpx;display: flex;align-items: center;justify-content: center;">
			<view style="padding: 10rpx 25rpx 10rpx 25rpx;border-radius: 50rpx;background-color: #fff;display: flex;align-items: center;justify-content: center;box-shadow: 0px 0px 2px 1px #e5e5e5;">
				<uni-link color="#1890FF" href="https://uniapp.dcloud.io/" text="前往浏览"></uni-link>
				<u-icon color="#1890FF" size="15"  name="arrow-rightward"></u-icon>
			</view>				
		</view>
		
		<view style="padding: 20rpx 20rpx 0rpx 20rpx;">{{basicInfo.statement}}</view>
			
		<view v-if="votedata.isvote" style="padding: 10rpx;background-color: #fafafa;border-radius: 20rpx; margin-top: 20rpx;">
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
		<view>
			<!-- <tm-timeline :list="list" model="left" ></tm-timeline> -->
		</view>
		<view class="timenodepanel" >
			<u-row>
				<u-col span="1" >
					<view class="timeline" :style="{height: timelineheight + 15 +'px'}">
						<view ><u-icon name="play-circle-fill" color="#1890FF" size="20"></u-icon></view>
						<u-line direction="col" :length="timelineheight-40" hairline color="#1890FF"></u-line>
						<view ><u-icon name="more-circle-fill" color="#1890FF" size="20"></u-icon></view>
					</view>					
				</u-col>
				<u-col span="11">
					<view class="timecontent" >
						<view v-for="(item,index) in nodelist">
							<NodeCard :nodedata="item" @clickedPanel="clickednode(item)" @clickedfavor="clickedfavor(item)"></NodeCard>							
						</view>
					</view>
				</u-col>
			</u-row>
		</view>
		<view class="ctrlbar">
			<u-icon name="chat" size="24" label="评论" labelSize="16"></u-icon>
			<text style="font-size: 26rpx;color: #999999;">12312条</text>
		</view>

		<view style="margin-bottom: 70rpx;">
			<comment v-for="item in commentlist" :commentdata="item" @clickedfavor="clickedfavor(item)"></comment>
			<view style="display: flex;align-items: center;justify-content: center;">
				<u-loadmore isDot line status="nomore"></u-loadmore>
			</view>
		</view>

		<view class="footerbar" >

			<view style="width: 45vw;">
				<u-search placeholder="请输入评论" searchIcon="" height="60" maxlength="30" :showAction="false" :clearabled="false" 
				v-model="inputCommentWords" @search="postComments"></u-search>
			</view>
			<view class="iconbtn">

				<u-icon @click="Star(1,TID)" :name="isfavor?'thumb-up-fill':'thumb-up'" space="0" :color="isfavor?'#1890FF':'#AEAEAE'" :labelColor="isfavor?'#1890FF':'#AEAEAE'" size="25" :label="basicInfo.star"></u-icon>
				<u-icon @click="Tip_off(1,TID)" :name="isfocus?'heart-fill':'heart'" space="0" :color="isfocus?'#1890FF':'#AEAEAE'" :labelColor="isfocus?'#1890FF':'#AEAEAE'" size="25" :label="basicInfo.tip_off"></u-icon>
				<!-- <u-icon name="heart-fill" space="0" color="#AEAEAE" labelColor="#AEAEAE" label="123" size="23"></u-icon> -->
				<u-icon name="share-square" space="0" color="#AEAEAE" labelColor="#AEAEAE" label="123" size="23"></u-icon>
			</view>
		</view>
		

		<!-- <view style="padding: 10rpx 20rpx 10rpx 20rpx;"><u-line color="#e7e6e4"></u-line></view> -->
		<view class="commentbar">
			<text style="font-weight: 550;">评论</text>
			<u-icon name="chat" color="#2979ff" :label="totalComments" size="20"></u-icon>
		</view>
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
				<u-icon name="thumb-down" color="#2979ff" :label="item.tip_off" size="20" @click="Tip_off(4,item.CID)" ></u-icon>
				<u-icon name="thumb-up" color="#2979ff" :label="item.star" size="20"style="margin-right: 20rpx;"@click="Star(4,item.CID)"></u-icon>
				
			</view>
			
		</view>
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
						<u-icon @click="showreport=true" style="margin-left: 20rpx;" name="info-circle" color="#AEAEAE" size="20"></u-icon>
					</view>
				</view>
				<view style="margin: 10rpx;font-size: 33rpx;font-weight: 550;">{{curnode.title}}</view>
				<view class="udatabar">
					<view style="display: flex;align-items: center;">
						<u-avatar :src="src" size="20"></u-avatar>
						<text style="margin-left: 15rpx;font-size: 33rpx;">wuji</text>
						<text style="margin-left: 30rpx;font-size: 25rpx;color: #A1A1A1;">· {{curnode.time}}</text>
					</view>
					<view>
						<focusbuttom :focus="isfocusnodeauthor" @clicked="isfocusnodeauthor=!isfocusnodeauthor"></focusbuttom>
					</view>
				</view>
				<view style="padding: 20rpx 20rpx 20rpx 20rpx;">
					<view style="margin-bottom: 10rpx;">{{curnode.content}}</view>
					<view v-if="curnode.type == '引用'" style="margin-top: 20rpx;">
						<u--text type="info" :text="curnode.src" lines=3 size="10"></u--text>
					</view>
					<view v-if="curnode.type == '爆料' && curnode.imglist.length > 0"><u-album :urls="curnode.imglist" multipleSize="75"></u-album></view>
				</view>
				<view v-if="curnode.type == '引用'" style="margin: 10rpx 10rpx 0rpx 10rpx;display: flex;align-items: center;justify-content: center;">
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
					<tm-button theme="bg-gradient-blue-accent" width="130" height="60" block @click="">举报</tm-button>
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
				TID:0,
				basicInfo:{},
				totalVotes:0,
				totalComments:0,
				voteslist:[],
				commentslist:[],
				eventslist:[],
				percentage:50,
				inputCommentWords:"",
				hasvoteOption:false,
				showLoginAlert:false,
				addnode:false,
				shownode:false,
				isfocusauthor:true,
				isfocusnodeauthor:false,
				showreport:false,
				isfavor:false,
				favorcnt:98,
				isfocus:false,
				focuscnt:653,
				reportdata:'',
				timelineheight:20,
				src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',
				tabsactive:0,
				tabslist:['引用','爆料'],
				votedata:{isvote:true,hasvote:false},
				voteselected:false,
				votelist:[
					{content:'同意',count:10,percent:10,selected:false},
					{content:'不同意',count:90,percent:90,selected:false},
				],
				list:[
						{
							title:'',
							content:'我是内容我是内容我是内容',
							time:"2020年7月",
							color:"blue",
							borderColor:'blue'
						},
						{
							title:'说明文字',
							content:'我是内容我是内容我是内容',
							time:"2019年7月",
							color:"blue",
							borderColor:'blue',
						},
						{
							title:'说明文字',
							content:'我是内容我是内容我是内容',
							time:"2018年7月",
							color:"blue",
							borderColor:'blue',
						},
						{
							title:'说明文字',
							content:'我是内容我是内容',
							time:"2017年7月",
							color:"blue",
							borderColor:'blue',
						},
					],
				curnode:{},
				nodelist:[
					{title:'标题1',content:'这是内容1',nodetime:'2021年12月12日',time:'12:08',type:'爆料',imglist:['https://cdn.uviewui.com/uview/album/1.jpg',
                    'https://cdn.uviewui.com/uview/album/2.jpg',
                    'https://cdn.uviewui.com/uview/album/3.jpg',
                    'https://cdn.uviewui.com/uview/album/4.jpg',
                    'https://cdn.uviewui.com/uview/album/5.jpg',
                    'https://cdn.uviewui.com/uview/album/6.jpg',
                    'https://cdn.uviewui.com/uview/album/7.jpg',
                    'https://cdn.uviewui.com/uview/album/8.jpg',
                    'https://cdn.uviewui.com/uview/album/9.jpg',
                    'https://cdn.uviewui.com/uview/album/10.jpg',],isfavor:false,favorcnt:142},
					{title:'标题2',content:'这是内容2',nodetime:'2021年12月18日',time:'12:08',type:'爆料',imglist:['https://cdn.uviewui.com/uview/album/1.jpg'],isfavor:true,favorcnt:142},
					{title:'标题3',content:'这是内容3',nodetime:'2021年12月12日',time:'13:08',type:'引用',src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',isfavor:false,favorcnt:142},
					{title:'标题3',content:'这是内容3',nodetime:'2021年12月12日',time:'13:08',type:'引用',src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',isfavor:false,favorcnt:142},
					{title:'标题3',content:'这是内容3',nodetime:'2021年12月12日',time:'13:08',type:'引用',src:'https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png',isfavor:false,favorcnt:142},
				],
				commentlist:[
					{imgsrc:'https://cdn.uviewui.com/uview/album/5.jpg',uname:'wuji1',time:'12:06',isfavor:false,favorcnt:987,comment:'天气真好1'},
					{imgsrc:'https://cdn.uviewui.com/uview/album/8.jpg',uname:'wuji2',time:'1天前',isfavor:false,favorcnt:54,comment:'天气真好2天气真好2天气真好2天气真好2天气真好2'},
					{imgsrc:'https://cdn.uviewui.com/uview/album/3.jpg',uname:'wuji3',time:'12月11日',isfavor:false,favorcnt:127,comment:'天气真好3'},
				],
				albumsrcs:[
                    'https://cdn.uviewui.com/uview/album/1.jpg',
                    'https://cdn.uviewui.com/uview/album/2.jpg',
                    'https://cdn.uviewui.com/uview/album/3.jpg',
                    'https://cdn.uviewui.com/uview/album/4.jpg',
                    'https://cdn.uviewui.com/uview/album/5.jpg',
                    'https://cdn.uviewui.com/uview/album/6.jpg',
                    'https://cdn.uviewui.com/uview/album/7.jpg',
                    'https://cdn.uviewui.com/uview/album/8.jpg',
                    'https://cdn.uviewui.com/uview/album/9.jpg',
                    'https://cdn.uviewui.com/uview/album/10.jpg',
                ],
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

			clickedfavor(item){
				item.isfavor=!item.isfavor
				item.favorcnt+=(item.isfavor?1:-1)
			},
			clickedfavortopic(){
				this.Star(1,this.TID)
			},
			clickedfocustopic(){
				this.isfocus=!this.isfocus
				this.focuscnt+=(this.isfocus?1:-1)
				this.Tip_off(1,this.TID)
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
				if(this.isfocus){
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
							   this.isfocus=false
						   }
						   else{
							   this.toastHandler(res.data.res)
						   }
					    }
							
					});
				}
				if(!this.isfocus){
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
							   this.isfocus=true
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
			Tip_off(type,id){
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
					    url: 'http://101.37.175.115/Event/tip-off??ID='+id+'&type='+type,
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"GET",
							
					    success: (res) => {
						   if(res.data.res=="ok"){
							   console.log("举报成功")
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
								   this.isfocus=true
							   }
							   else{
								   this.isfocus=false
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
						   this.isfocus=true
					   }
					   else{
						   this.isfocus=false
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
						   this.voteslist=res.data.data
						   this.totalVotes=res.data.total
						   this.hasvoteOption=true
						   
					   }
					   else{
						   this.hasvotes=false
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
						this.eventslist=res.data.data
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
	margin-bottom: 30px;
	.commentdatabar{
		display: flex;
		@extend %betweencenter;
	}
	.comment{
		padding: 15rpx;
	}
	.commentfooterbar{
		margin-right: 10rpx;
		display: flex;
		align-items: center;
		justify-content: flex-start;
		flex-direction: row-reverse;
	}	
}

</style>
