<template>
	<view class="card" @click="seeInfo(ID)">
		<view class="textpart">
			<view class="cardheader">
				<u--text :text="title" size="15" lines="2"></u--text>
			</view>
			<view class="content">
				<image v-if="showimg" style="width: 50px; height: 50px;margin-right: 10rpx;" mode="aspectFill" :src="imgsrc"></image>
				<u--text :text="partcontent" size="15" lines="3"></u--text>
			</view>			
		</view>
		<view class="divideline"><u-line color="#e5e5e5" length="100%"></u-line></view>
		<view class="cardfooter">
			<view class="leftfooter">
				<u-tag :text="tag" size="mini" plain></u-tag>
				<u-avatar :src="avatarsrc" size="16"></u-avatar>
				<text style="margin-left: 15rpx;font-size: 15rpx;">{{uname}}</text>		
				<text style="margin-left: 15rpx;font-size: 15rpx;">{{time}}</text>
			</view>
			<view class="rightfooter" v-if="showrightfooter">
				<view><u--text prefixIcon="eye" :text="readcnt" size="12"></u--text></view>
				<view><u--text prefixIcon="thumb-up" :text="likecount" size="12"></u--text></view>
				<view><u--text prefixIcon="thumb-down" :text="dislikecnt" size="12"></u--text></view>
			</view>
		</view>
		
	</view>
</template>

<script>
	export default {
		name:'TextCard',
		props:{
			title:{
				type:String,
				default:''
			},
			showimg:{
				type:Boolean,
				default:false
			},
			showrightfooter:{
				type:Boolean,
				default:true
			},
			partcontent:{
				type:String,
				default:''
			},
			imgsrc:{
				type:String,
				default:''
			},
			avatarsrc:{
				type:String,
				default:''
			},
			uname:{
				type:String,
				default:''
			},
			dislikecnt:{
					type:String,
					default:'0'
			},
			likecnt:{
				type:String,
				default:'0'
			},
			commentcnt:{
				type:String,
				default:'0'
			},
			readcnt:{
				type:String,
				default:'0'
			},
			time:{
				type:String,
				default:'刚刚'
			},
			tag:{
				type:String,
				default:""
			},
			ID:{
				type:Number,
				default:0
			}
		},
		computed:{
			likecount:function(){
				return this.computcount(this.likecnt);
			},
			commentcount:function(){
				return this.computcount(this.commentcnt);
			},
			readcount:function(){
				return this.computcount(this.readcnt);
			},
			
		},
		methods:{
			computcount(num){
				let n = Number(num);
				if(n < 1000){
					return num;
				}
				else if(n >= 1000 && n < 10000){
					let a = n/1000;
					return a.toFixed(1).toString() + 'k';
				}
				else{
					let a = n/10000;
					return a.toFixed(1).toString() + 'w';
				}
			},
			
			seeInfo:function(e){
				// console.log("clicked")
				// console.log(e)
				uni.navigateTo({
				    url: '../topic/topic?tid='+e,
				});
			},
		}
	}
</script>

<style lang="scss" scoped>
@import '@/static/variables.scss';
.card{
	padding: 10rpx 20rpx 10rpx 20rpx;
	margin: 10rpx 0 10rpx 0;
	border-radius: 10rpx;
	background-color: $cardcolor;
	.textpart{
		padding: 0 10rpx 0 10rpx;
		.cardheader{
			padding-bottom: 10rpx;
		}
		.content{
			display: flex;
			align-items: flex-start;
		}			
	}
	.divideline{
		padding-top: 5rpx;
	}
	.cardfooter{
		@extend %betweencenter;
		.leftfooter{
			@extend %leftcenter;
		}
		.rightfooter{
			@extend %rightcenter;
			view{
				width: 120rpx;
			}
		}
	}
}
</style>
