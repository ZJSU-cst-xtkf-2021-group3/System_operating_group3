<template>
	<view class="topic">
		<view class="top">
		    <u--image :showLoading="true" :src="src" width="400px" height="160px" @click="click"></u--image>
		    <u--text text="#戴耳机听歌睡觉致耳聋#" :bold="true" :size="20" style="margin-top: 40rpx; margin-left: 40rpx;"></u--text>
			<u-gap height="10" bgColor="#ffffff"></u-gap>
			<view class="lead ">
			    <u--text  text="导语:" :bold="true" ></u--text>
				<view class="content">
		            <mote-lines-divide :line="2" expandText="展开" foldHint="收起">
						武汉的樊女士今年33岁，由于存在神经衰弱的毛病，睡眠一直不太好。为此，她想到了戴耳机听歌睡觉。最近半个多月，樊女士发现自己的耳朵总是有“嗡嗡嗡”的鸣音，听力也变差，就医后诊断为突发性耳聋。你每天戴耳机多久？医生建议连续使用耳机听歌不超60分钟，如何缓解久戴耳机的不舒适感？教你一个动作：①双手捂住耳朵；②双手食指叩击后脑勺。
					</mote-lines-divide>
				</view>
			</view>
			<u-gap height="20" bgColor="#ffffff"></u-gap>
		</view>
		<view class="middle">
			<u-subsection :list="list_choose" @change="sectionChange" mode="subsection" :current="current" activeColor="#f59189" inactiveColor="#ffffff"></u-subsection>
		    <u-back-top :scrollTop="scrollTop" :mode="mode" :iconStyle="iconStyle" :customStyle="customStyle"></u-back-top>
			<u-gap height="5" bgColor="#ebebeb"></u-gap>
		    <Dynamic v-for="(item,index) in list" :key="index" 
			    :imgList="item.imgList" 
			    :avatar="item.avatar"
			    :name="item.name"
			    :publishTime="item.publishTime"
				:isFocusOn="item.isFocusOn"
			    :content="item.content"
			    :isLike="item.isLike"
			    :isGiveReward="item.isGiveReward"
			    :likeNumber="item.likeNumber"
			    :giveRewardNumber="item.giveRewardNumber"
			    :chatNumber="item.chatNumber"
			    @clickDynamic="clickDynamic(index)"
			    @clickUser="clickUser(item.id)"
			    @clickFocus="clickFocus(index)"
			    @clickThumbsup="clickThumbsup(item.id)"
			    @clickGiveReward="clickGiveReward(item.id)"
			    @clickChat="clickChat(item.id)">
		    </Dynamic>
		</view>	
		<view class="ctrlbar">
				<uni-fab
					:pattern="pattern"
					:content="content"
					horizontal="right"
					vertical="bottom"
					direction="horizontal"
					:popMenu="true"
					@trigger="trigger"
				/>
			</view>
		<uni-popup ref="sharepopup" type="bottom">
			<share-btn :sharedataTemp="sharedata"></share-btn>
		</uni-popup>
	</view>
</template>

<script>
import Dynamic from '../../components/qizai-dynamic/Dynamic.vue'
import MoteLinesDivide from "@/components/mote-lines-divide/mote-lines-divide"
import uniPopup from "@/components/uni-popup2/uni-popup2.vue"
import shareBtn from '../../components/share-btn/share-btn.vue'
export default {
    components: {
        Dynamic,
		MoteLinesDivide,
		uniPopup,
        shareBtn,
    },
    data() {
        return {
			sharedata:"",
			desc:"",
            title: 'Hello',
			src: 'https://www.wsm.cn/uploads/allimg/160625/37-1606251F049.jpg',
			scrollTop: 0,
			mode: 'circle',
			iconStyle: {
					fontSize: '32rpx',
					color: '#000000'
			},
			customStyle: {
					color: '#ff8585'
			},
			list_choose: ['热门', '实时'],
			current: 0,
			pattern: {
							color: 'gray',
							backgroundColor: '#FFFFFF',
							selectedColor: '#007AFF',
							buttonColor:'orange'
						},
			content: [
			{
				iconPath: '../../static/icons/关注.png',
				selectedIconPath: '/static/componentHL.png',
				text: '关注',
				active: false
			},
			{
				iconPath: '../../static/icons/发布.png',
				selectedIconPath: '/static/apiHL.png',
				text: '发布',
				active: false
			},
			{
				iconPath: '../../static/icons/分享.png',
				selectedIconPath: '/static/apiHL.png',
				text: '分享',
				active: false
			},
			],
            list:[
				{
				    id:1,
				    avatar:'https://tse1-mm.cn.bing.net/th/id/R-C.a53938fecfc8a85da80b9129306e8093?rik=ayTEVU0sEvR1zg&riu=http%3a%2f%2ftupian.qqw21.com%2farticle%2fUploadPic%2f2012-8%2f2012869524112329.jpg&ehk=MvRYdkOCH2Lj2Z7UPpIENQ2wgmwDLzbvxctsFg1ViHM%3d&risl=&pid=ImgRaw&r=0',
				    name:'一粒沙就一粒沙',
				    publishTime:1617086756,
				    content:'你的耳朵还“年轻”吗？哪些常见行为其实很伤耳？拯救你的听力还有什么实用招数？戳图了解↓↓ ​​​​',
				    imgList:[
				        'https://wx3.sinaimg.cn/bmiddle/006vD6Yely1gxjgwib91vj30dw0hqdg8.jpg',
				        'https://wx2.sinaimg.cn/bmiddle/006vD6Yely1gxjgwijir2j30dw0m8tb7.jpg',
						'https://wx2.sinaimg.cn/bmiddle/006vD6Yely1gxjgwiqbjaj30dw0ktmzn.jpg',
						'https://wx3.sinaimg.cn/bmiddle/006vD6Yely1gxjgwj0f23j30dw0m8diu.jpg',
						'https://wx2.sinaimg.cn/bmiddle/006vD6Yely1gxjgwjqet9j30dw0dwaa9.jpg',
						'https://wx1.sinaimg.cn/bmiddle/006vD6Yely1gxjgwi3wlij30dw0m8acm.jpg',
						'https://wx4.sinaimg.cn/bmiddle/006vD6Yely1gxjgwkmh8ej30dw0m8mzj.jpg',
						'https://wx1.sinaimg.cn/bmiddle/006vD6Yely1gxjgwkvc13j30dw0h8aag.jpg',
						'https://wx3.sinaimg.cn/bmiddle/006vD6Yely1gxjgwl1ymij30dw0h8mxl.jpg',
				    ],
				    isLike:true,
				    isGiveReward:true,
				    likeNumber:2,
				    giveRewardNumber:2,
				    chatNumber:2,
				    isFocusOn:true,
				},
				
                {
                    id:2,
                    avatar:'https://tse1-mm.cn.bing.net/th/id/OIP-C.WsVs_1wXmbVZ1543fXUHbwAAAA?pid=ImgDet&rs=1',
                    name:'少年伯爵',
                    publishTime:1617086500,
                    content:'经常佩戴耳机听歌，的确会对耳朵产生一定的伤害，很多年以前，我就是喜欢戴着耳机听歌睡觉，之后就导致耳朵患上了中耳炎，耳朵经常不舒服，而且有耳鸣的一个情况。所以建议大家佩戴耳机听歌的时候，一定要将音量适当的开小一点，并且不要连续听歌超过60分钟，最好是听30分钟，就把耳机摘下来，让耳朵休息一下。',
                    imgList:[
                        'https://wx3.sinaimg.cn/bmiddle/541b030dly1gxjgk2pj5nj20wi1nzwo0.jpg',
                        'https://wx3.sinaimg.cn/bmiddle/541b030dly1gxjgj17f4kj23402c0hdv.jpg',
                    ],
                    isLike:true,
                    isGiveReward:true,
                    likeNumber:2,
                    giveRewardNumber:2,
                    chatNumber:2,
                    isFocusOn:true,
                },

                {
                    id:3,
                    avatar:'https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2291332875,175289127&fm=26&gp=0.jpg',
                    name:'小白',
                    publishTime:1617036656,
                    content:'  长时间戴耳机出现类似“耳鸣”“突发性耳聋” 情况的人好像不在少数啊，有些娃喜欢睡前戴耳机听歌，有些娃不得已为了考试、工作也会长时间戴耳机，太难了，最好还是听医生60-60原则吧，你一次戴多长时间的耳机呢。',
                    imgList:[
                        'https://wx2.sinaimg.cn/bmiddle/007ovWLRgy1gxk2fea7tpj30ku0xiafs.jpg',
                    ],
                    isLike:false,
                    isGiveReward:false,
                    likeNumber:0,
                    giveRewardNumber:0,
                    chatNumber:2,
                    isFocusOn:false,
                },
                {
                    id:4,
                    avatar:'https://wx4.sinaimg.cn/thumb300/0065BsZggy1gqde59akdpj309s09sdfy.jpg',
                    name:'是猫猫猫啊',
                    publishTime:1617046556,
                    content:' 道理我都懂😑😑 但是公共场合使用耳机很难不超过60分钟 o(TヘTo)',
                    imgList:[
                        'https://wx1.sinaimg.cn/orj360/003f1kwGly1gv9abent14g60go0go0zi02.jpg',
                        'https://wx1.sinaimg.cn/orj360/6e41d499gy1gxjjmfvgcej218410ygor.jpg',
                    ],
					isFocusOn:true,
                    isLike:true,
                    isGiveReward:false,
                    likeNumber:4,
                    giveRewardNumber:22,
                    chatNumber:52,
                },
                {
                    id:5,
                    avatar:'https://wx3.sinaimg.cn/thumb300/0065BsZggy1gpou3rvc37j30zk0mwdjx.jpg',
                    name:'最幸福的小橘子',
                    publishTime:1616086456,
                    content:'我可以左耳朵戴一个小时，右耳朵戴一个小时么！？🤣🤣🤣 ​',
                    imgList:[
                        'https://tse4-mm.cn.bing.net/th/id/OIP-C.fcXOozrywkY6o8Bs12LCggHaHY?pid=ImgDet&rs=1',
                        'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1278672224,2880561485&fm=15&gp=0.jpg',
                    ],
					isFocusOn:true,
                    isLike:true,
                    isGiveReward:false,
                    likeNumber:25,
                    giveRewardNumber:0,
                    chatNumber:7,
                },
                {
                    id:6,
                    avatar:'https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2590128318,632998727&fm=26&gp=0.jpg',
                    name:'风清扬',
                    publishTime:1617086500,
                    content:'使用耳机一定要在时长、音量方面进行控制。通常使用耳机不宜超过1小时，否则会损伤我们的听力，最好每小时让耳朵休息15分钟为佳。同时建议不要将耳机音量调的过高，这对我们的听力会造成不可逆转的危害，不会像是皮肉伤一样快速愈合。⚠️此外，大家也要避免在睡觉时和刚洗完澡时使用耳机，更容易对我们的耳道造成伤害，也容易滋生细菌，平时大家也要注意对耳机卫生的维护，避免伤害耳膜。',
                    imgList:[
                        'https://wx3.sinaimg.cn/mw600/ebd57867ly1gxk2mke8vmj20dw0hqwew.jpg',
                        'https://wx4.sinaimg.cn/mw600/e7a2eb42ly1gxk2ewbej8j20tj0gfta8.jpg',
                        'https://wx1.sinaimg.cn/mw600/0069PkFsgy1gxk2undntlj30qy0sctaj.jpg',
                    ],
					isFocusOn:true,
                    isLike:true,
                    isGiveReward:true,
                    likeNumber:3,
                    giveRewardNumber:2,
                    chatNumber:2,
                },
				{
				    id:7,
				    avatar:'https://tse1-mm.cn.bing.net/th/id/R-C.efdb268bb841fb60073dbae826bf2b9f?rik=Ufo6V0eAyp3IkQ&riu=http%3a%2f%2fscimg.jianbihuadq.com%2f202009%2f202009162308095.jpg&ehk=thgEdzkXNa5AqjDy3cJ5aAHwMPSGcbOS7CKvuxvNo3w%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1',
				    name:'丢丢小仙女',
				    publishTime:1617086500,
				    content:'ԅ(¯﹃¯ԅ)本仙女耳朵已聋 ',
				    imgList:[
				        'https://tse1-mm.cn.bing.net/th/id/R-C.0d5ed5da54980c86dff059477b07684e?rik=eGgyatCU4Vryxg&riu=http%3a%2f%2fwww.biaoqingb.com%2fuploads%2fimg1%2f20191215%2f3547027059cfd6a563c0f60479b73cee.jpg&ehk=CAZBIDKu0%2bSd1ze0PNSESIiq9tVUW3RFY6l07xUFAok%3d&risl=&pid=ImgRaw&r=0',
				        'https://wx3.sinaimg.cn/bmiddle/89a3891fly1gxk1ccwlohj21400u0wlj.jpg',
				        'https://wx1.sinaimg.cn/orj360/006Su3SYly1gxk14gt3ruj30hs0hs755.jpg',
				 ],
					isFocusOn:true,
				    isLike:true,
				    isGiveReward:true,
				    likeNumber:3,
				    giveRewardNumber:2,
				    chatNumber:2,
				}
        ]
        }
    },
	onPageScroll(e) {
			this.scrollTop = e.scrollTop;
		},
		
		onShow: function() {
		        uni.request({
		             header:{
		              "Content-Type":"application/x-www-form-urlencoded",
		              },
		             url: "http://101.37.175.115/Activity/show_contributes",
		          data:{
		           A_CID:"1"
		          },
		          method:"GET",
		             success(res){
		              if(res.data.res=='ok'){
		            console.log("ok")
		                        console.log(res.data.data)
		           }
		           console.log(res.data.res)      
		             }
		        })
		      },
		
    methods:{
		sectionChange(index) {
						this.current = index;
					},
		trigger(e) {
			if(e.index == 0)
				{uni.showModal({
					title: '提示',
					content:`欢迎关注该活动´･∀･)乂(･∀･｀`,
					success(res) {
					if (res.confirm) {
						console.log('用户点击确定');
					} else if (res.cancel) {
						console.log('用户点击取消');
						}
					}
				});}
				else if(e.index == 1){
					uni.navigateTo({
						url:"../activity_publish/activity_publish"
					}),
					console.log("ok")
				}
				else if(e.index == 2){
					this.$refs.sharepopup.open();
				}
				},
        clickDynamic(e){
            console.log('childDynamic');
        },
        // 点击用户信息
        clickUser(e){
            console.log(e);
            console.log('childUser');
        },
        // 点击关注
        clickFocus(e){
            this.list[e].isFocusOn = this.list[e].isFocusOn ? false : true;
            console.log(e);
            console.log('childUser');
        },
        // 点赞
        clickThumbsup(e){
            console.log(e);
            console.log('childThumbsup');
        },
        // 点击打赏
        clickGiveReward(e){
            console.log(e);
            console.log('clickGiveReward');
        },
        // 点击聊天
        clickChat(e){
            console.log(e);
            console.log('clickChat');
        }
    }
}
</script>

<style lang="scss" scoped>
@import '@/static/variables.scss';
.ctrlbar{
	margin-top: 100rpx;
}
.lead{
	padding: 20rpx;
}	
</style>