<template>
	<view class="topic">
		<view class="top">
		    <u--image :showLoading="true" :src="src" width="400px" height="160px" @click="click"></u--image>
		    <u--text text="#今日话题#" :bold="true" :size="20" ></u--text>
			<view class="lead">
			    <u--text  text="导语:" :bold="true"></u--text>
				<view class="content">
		            <mote-lines-divide :line="2" expandText="展开" foldHint="收起">
		                    关于uView的取名来由，首字母u来自于uni-app首字母，uni-app是基Vuejs，Vue和View(延伸为UI、视图之意)同音，同时view组件uni-app中最础最重要的组件，故取名uView，表达源于uni-app和Vue之意，同时在此也对它示感谢。
		            </mote-lines-divide>
				</view>
			</view>
			<u-gap height="10" bgColor="#ffffff"></u-gap>
		</view>
		<view class="middle">
			<u-subsection :list="list_choose" @change="sectionChange" mode="subsection" :current="current" activeColor="#f59189" inactiveColor="#ffffff"></u-subsection>
		    <u-back-top :scrollTop="scrollTop" :mode="mode" :iconStyle="iconStyle" :customStyle="customStyle"></u-back-top>
			<u-gap height="5" bgColor="#ebebeb"></u-gap>
		    <Dynamic v-for="(item,index) in list" key="id" 
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
        shareBtn
    },
    data() {
        return {
            title: 'Hello',
			src: 'https://cdn.uviewui.com/uview/album/1.jpg',
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
                    avatar:'https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1950846641,3729028697&fm=26&gp=0.jpg',
                    name:'小新',
                    publishTime:1617086756,
                    content:'中国外交官这样讽加拿大总理，算不算骂？该不该骂？',
                    imgList:[
                        'https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1976832114,2993359804&fm=26&gp=0.jpg',
                        'https://dss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2369680151,826506100&fm=26&gp=0.jpg',
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
                    avatar:'https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2291332875,175289127&fm=26&gp=0.jpg',
                    name:'小白',
                    publishTime:1617036656,
                    content:'  足不出户享国内核医学领域顶级专家云诊断，“中山-联影”分子影像远程互联融合创新中心揭牌 ',
                    imgList:[
                        'https://dss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2369680151,826506100&fm=26&gp=0.jpg',
                    ],
                    isLike:false,
                    isGiveReward:false,
                    likeNumber:0,
                    giveRewardNumber:0,
                    chatNumber:2,
                    isFocusOn:false,
                },
                {
                    id:3,
                    avatar:'https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1950846641,3729028697&fm=26&gp=0.jpg',
                    name:'小新',
                    publishTime:1617046556,
                    content:'  外交部：一小撮国家和个人编造所谓新疆“强迫劳动”的故事，其心何其毒也！ ',
                    imgList:[
                        'https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1976832114,2993359804&fm=26&gp=0.jpg',
                        'https://dss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2369680151,826506100&fm=26&gp=0.jpg',
                        'https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1976832114,2993359804&fm=26&gp=0.jpg',
                        'https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1976832114,2993359804&fm=26&gp=0.jpg',
                        'https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1976832114,2993359804&fm=26&gp=0.jpg',
                    ],
					isFocusOn:true,
                    isLike:true,
                    isGiveReward:false,
                    likeNumber:4,
                    giveRewardNumber:22,
                    chatNumber:52,
                },
                {
                    id:4,
                    avatar:'https://dss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3717120934,3932520698&fm=26&gp=0.jpg',
                    name:'小龙马',
                    publishTime:1616086456,
                    content:'DCloud有800万开发者,uni统计手机端月活12亿。是开发者数量和案例最丰富的多端开发框架。 欢迎知名开发商提交案例或接入uni统计。 新冠抗疫专区案例 uni-app助力',
                    imgList:[
                        'https://dss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2369680151,826506100&fm=26&gp=0.jpg',
                        'https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1976832114,2993359804&fm=26&gp=0.jpg',
                        'https://dss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2369680151,826506100&fm=26&gp=0.jpg',
                    ],
					isFocusOn:true,
                    isLike:true,
                    isGiveReward:false,
                    likeNumber:25,
                    giveRewardNumber:0,
                    chatNumber:7,
                },
                {
                    id:5,
                    avatar:'https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2590128318,632998727&fm=26&gp=0.jpg',
                    name:'风清扬',
                    publishTime:1607086356,
                    content:'划个水',
                    imgList:[
                        'https://dss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2369680151,826506100&fm=26&gp=0.jpg',
                        'https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1976832114,2993359804&fm=26&gp=0.jpg',
                        'https://dss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2369680151,826506100&fm=26&gp=0.jpg',
                        'https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1976832114,2993359804&fm=26&gp=0.jpg',
                    ],
					isFocusOn:true,
                    isLike:true,
                    isGiveReward:true,
                    likeNumber:3,
                    giveRewardNumber:2,
                    chatNumber:2,
                },
				{
				    id:6,
				    avatar:'https://tse1-mm.cn.bing.net/th/id/OIP-C.DDGRsJiGlIb4VAU2ZH8PjAAAAA?w=186&h=199&c=7&r=0&o=5&dpr=1.25&pid=1.7',
				    name:'墨燃',
				    publishTime:1607086356,
				    content:'今天也撸到猫猫了，开心!',
				    imgList:[
				        'https://tse1-mm.cn.bing.net/th/id/OIP-C.XokdM2VcbovvShghWQ6qEwAAAA?w=125&h=150&c=7&r=0&o=5&dpr=1.25&pid=1.7',
				        'https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1976832114,2993359804&fm=26&gp=0.jpg',
				        'https://dss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2369680151,826506100&fm=26&gp=0.jpg',
				        'https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1976832114,2993359804&fm=26&gp=0.jpg',
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
	
</style>