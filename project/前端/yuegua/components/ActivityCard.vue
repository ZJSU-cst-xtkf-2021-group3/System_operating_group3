<template>
	<view class="card">
		<view class="textpart">
			<view class="cardheader">
				<u--text :text="title" size="15" lines="2"></u--text>
			</view>
			<view class="content">
				<image v-if="showimg" style="width: 50px; height: 50px;margin-right: 10rpx;" mode="aspectFill" :src="imgsrc"></image>
				<u--text :text="partcontent" size="13" lines="3"></u--text>
			</view>			
		</view>
		<view class="divideline"><u-line length="100%"></u-line></view>
		<view class="cardfooter">
			<view class="rightfooter" v-if="showrightfooter">
				<view><u--text prefixIcon="thumb-up" :text="likecount" size="12"></u--text></view>
				<view><u--text prefixIcon="chat" :text="commentcount" size="12"></u--text></view>
				<view><u--text prefixIcon="share" :text="sharecount" size="12"></u--text></view>
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
			likecnt:{
				type:String,
				default:'0'
			},
			commentcnt:{
				type:String,
				default:'0'
			},
			sharecnt:{
				type:String,
				default:'0'
			}
		},
		computed:{
			likecount:function(){
				return this.computcount(this.likecnt);
			},
			commentcount:function(){
				return this.computcount(this.commentcnt);
			},
			sharecount:function(){
				return this.computcount(this.sharecnt);
			},
			
		},
		methods:{
			computcount(num){
				let n = Number(num);
				console.log(num);
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
			}
		}
	}
</script>

<style lang="scss" scoped>
	@import '@/static/variables.scss';
	.card{
		padding: 10rpx 20rpx 10rpx 20rpx;
		border-bottom: 1rpx;
		border-top: 1rpx;
		border-right: 0;
		border-left: 0;
		border-style: solid;
		border-color: $bordercolor;
		//background-color: #3C9CFF;
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
			.rightfooter{
				margin-left: 10rpx;
				@extend %rightcenter;
				view{
					width: 120rpx;
				}
			}
		}
	}
</style>
