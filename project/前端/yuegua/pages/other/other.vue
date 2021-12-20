<template>
	<view>
		<tm-message ref="toast"></tm-message>
		<view class="headerpanel-uinfo">
			<view style="display: flex;align-items: center;">
				<view>
					<u-avatar size="50" :src="basicinfo.header"></u-avatar>
				</view>
				<view style="margin-left: 20rpx;">
					<view class="headerpanel-uinfo-name">
						<text style="font-size: 38rpx;font-weight: 550;margin-right: 30rpx;">{{basicinfo.Uname}}</text>
						<u-icon color="#FFC53D" name="level" size="18" :label="basicinfo.rank" space="0"></u-icon>
					</view>
					<u--text size="12" lines="1" color="#999999" :text="basicinfo.introduction"></u--text>
				</view>				
			</view>

			<view>
				<focusbuttom :focus="isfocusauthor" @clicked="clickedfocus"></focusbuttom>
			</view>
		</view>
		<u-transition :show="true" mode="slide-up">
			<view class="datapanel">
				<u-sticky bgColor="#fafafa">
					<view class="dataheader">
						<view class="ctrltabs">
							<view v-for="(item,index) in tabslist" :class="['tab',activetab===index?'selected':'unselected']" @click="activetab=index">
								<text style="font-size: 30rpx;">{{item.name}}</text>
								<view style="height: 6rpx;width: 50rpx;border-radius: 50rpx;"></view>
							</view>
						</view>
						<view class="headerpanel-udata">
							<view class="datablock">
								<text style="font-size: 33rpx;font-weight: 550;">{{basicinfo.EXP}}</text>
								<text style="font-size: 20rpx;">EXP</text>
							</view>
							<view class="datablock">
								<text style="font-size: 33rpx;font-weight: 550;">{{basicinfo.Fcounts}}</text>
								<text style="font-size: 20rpx;">粉丝</text>
							</view>
							<view class="datablock">
								<text style="font-size: 33rpx;font-weight: 550;">{{identity}}</text>
								<text style="font-size: 20rpx;">认证</text>
							</view>
						</view>
					</view>
				</u-sticky>

				<view>
					<view v-show="activetab===0">
						<TextCard v-for="(item,index) in ptopiclist" :imgsrc="item.mainPic" :avatarsrc="item.header" :partcontent="item.statement" :showimg="true"
								   :likecnt="String(item.star)" :readcnt="String(item.Fcounts)" :title="item.title" :uname="item.Uname" :dislikecnt="String(item.tip_off)"
								   :time=switchTime(item.lastUpDateTime) :tag=item.Tag :ID="item.TID"
								  v-bind:key="index" ></TextCard>
					</view>
					<view v-show="activetab===1">
						<TextCard v-for="(item,index) in ftopiclist" :imgsrc="item.mainPic" :avatarsrc="item.header" :partcontent="item.statement" :showimg="true"
								   :likecnt="String(item.star)" :readcnt="String(item.Fcounts)" :title="item.title" :uname="item.Uname" :dislikecnt="String(item.tip_off)"
								   :time=switchTime(item.lastUpDateTime) :tag=item.Tag :ID="item.TID"
								  v-bind:key="index" ></TextCard>
					</view>
				</view>
			</view>
		</u-transition>
	</view>
</template>

<script>
	import focusbuttom from '../../components/focusbuttom'
	import TextCard from '@/components/TextCard';
	export default {
		data() {
			return {
				UID:',',
				basicinfo:{},
				identity:'',
				ptopiclist:[],
				ftopiclist:[],
				activetab:0,
				isfocusauthor:false,
				colors:['#007AFF','#00000000'],
				tabslist:[{name:'发布话题'},{name:'关注话题'}]
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
			clickedfocus(){
				let that=this
				that.isfocusauthor=!that.isfocusauthor
				if(that.isfocusauthor){
					uni.request({
						url:`http://101.37.175.115/Space/follow?UID=${that.UID}`,
						success(res) {
							// console.log(res)
							that.$refs.toast.show({model:'success',wait:1000,label:"关注成功"})
						}
					})
				}else{
					uni.request({
						url:`http://101.37.175.115/MyCenter/del/follow?UID=${that.UID}`,
						success(res) {
							// console.log(res)
							that.$refs.toast.show({model:'success',wait:1000,label:"取消关注成功"})
						}
					})
				}
			}
		},
		onLoad(op) {
			let that = this
			that.UID=op.UID
			uni.request({
				url:`http://101.37.175.115/Space/basicInfo?UID=${op.UID}`,
				success(res) {
					// console.log(res)
					that.isfocusauthor=res.data.isFouse
					that.basicinfo=res.data.data
					that.identity="注册用户"
					if(res.data.data.ifPassedExam){
						that.identity="会员用户"
					}
					if(res.data.data.isEditor){
						that.identity="编辑"
					}
				}
			})
			uni.request({
				url:`http://101.37.175.115/Space/cat/others/Ptopiclist?UID=${op.UID}`,
				success(res) {
					that.ptopiclist = res.data.data
					// console.log(res)
				}
			})
			uni.request({
				url:`http://101.37.175.115/Space/cat/others/Ftopiclist?UID=${op.UID}`,
				success(res) {
					that.ftopiclist = res.data.data
					// console.log(res)
				}
			})
		},
		components:{focusbuttom,TextCard}
	}
</script>

<style lang="scss">
	
.headerpanel-uinfo{
	padding: 20rpx 40rpx 20rpx 40rpx;
	display: flex;
	align-items: center;
	justify-content: space-between;
	.headerpanel-uinfo-name{
		margin-bottom: 10rpx;
		display: flex;
		align-items: flex-start;
	}		
}
.datapanel{
	background-color: #FAFAFA;
	border-radius: 60rpx 60rpx 0 0;
	.dataheader{
		display: flex;
		align-items: flex-end;
		justify-content: space-between;
		padding: 10rpx;
		.ctrltabs{
			display: flex;
			.tab{
				margin-left: 20rpx;
				display: flex;
				flex-direction: column;
				align-items: center;
				justify-content: flex-end;		

			}
			.selected{
				text{
					font-size: 32rpx;
					color: #007AFF;
				}
				view{
					margin-top: 12rpx;
					background-color: #007AFF;
				}
			}
			.unselected{
				text{
					font-size: 32rpx;
					color: #858585;
				}
				view{
					margin-top: 12rpx;
					background-color: #00000000;
				}
			}
		}
		.headerpanel-udata{
			display: flex;
			.datablock{
				margin: 10rpx 30rpx 10rpx 30rpx;
				display: flex;
				flex-direction: column;
				align-items: center;
			}
		}		
	}

}

</style>
