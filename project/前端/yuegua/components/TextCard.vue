<template>
	<view class="card">
		<view class="cardheader">
			<u--text :text="title" size="15" lines="2"></u--text>
		</view>
		<view class="content">
			<image v-if="showimg" style="width: 50px; height: 50px;margin-right: 10rpx;" mode="aspectFill" :src="imgsrc"></image>
			<u--text :text="partcontent" size="13" lines="3"></u--text>
		</view>
		<view class="divideline"><u-line length="100%"></u-line></view>
		<view class="cardfooter">
			<view class="leftfooter">
				<u-tag text="标签" size="mini" plain></u-tag>
				<u-avatar :src="avatarsrc" size="22"></u-avatar>
				<u--text style="margin-left: 15rpx;" :text="uname" size="14"></u--text>					
			</view>
			<view class="rightfooter">
				<u--text prefixIcon="eye-fill" :text="readcount" size="14" iconStyle="17px"></u--text>
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
			readcount:{
				type:String,
				default:''
			}
		}
	}
</script>

<style lang="scss" scoped>
	@import '@/static/variables.scss';
	.card{
		padding: 10rpx 40rpx 10rpx 40rpx;
		border-bottom: 1rpx;
		border-top: 1rpx;
		border-right: 0;
		border-left: 0;
		border-style: solid;
		border-color: $bordercolor;
		//background-color: #3C9CFF;
		.cardheader{
			padding-bottom: 10rpx;
		}
		.content{
			display: flex;
			align-items: flex-start;
		}
		.divideline{
			padding-top: 10rpx;
			padding-bottom: 10rpx;
		}
		.cardfooter{
			@extend %betweencenter;
			.leftfooter{
				@extend %leftcenter;
			}
			.rightfooter{
				@extend %rightcenter;
			}
		}
	}
</style>
