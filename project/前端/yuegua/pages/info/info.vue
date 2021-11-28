<template>
	<view style="padding: 20rpx 30rpx 0 30rpx;">
		<view class="uavatar" @click="clickavatar">
			<text>头像</text>
			<u-avatar :src="src" size="60"></u-avatar>
		</view>
		<view class="uavatar">
			<text style="margin-right: 50rpx;">昵称</text>
			<u--input v-model="uname" border="bottom" maxlength="15" :showWordLimit="true"></u--input>
		</view>
		<view class="uavatar">
			<text style="margin-right: 50rpx;">性别</text>
			<u-radio-group v-model="usex" iconPlacement="left" shape="square" >
				<u-radio style="margin-right: 40rpx;" name="男" label="男"></u-radio>
				<u-radio style="margin-right: 40rpx;" name="女" label="女"></u-radio>
				<u-radio style="margin-right: 40rpx;" name="保密" label="保密"></u-radio>
			</u-radio-group>
		</view>
		<view  style="display: flex;margin-bottom: 30rpx;">
			<text style="margin-right: 50rpx;">生日</text>
			<picker mode="date" :value="date" :start="startDate" :end="endDate" @change="bindDateChange">
				<view class="uni-input" style="border-bottom: 1rpx solid #d6d7d9;">{{date}}</view>
			</picker>
		</view>
		<view class="uavatar">
			<text style="margin-right: 50rpx;">签名</text>
			<u--input v-model="usignature" border="bottom" maxlength="30" :showWordLimit="true"></u--input>
		</view>
		<u-popup :show="showchangeavatar" :round="true" :closeOnClickOverlay="false">
			<view class="ctrlbtn">
				<u-icon name="checkmark" size="27" color="#fff" @click="showchangeavatar = false"></u-icon>
				<u-icon name="close" size="24" color="#fff" @click="showchangeavatar = false"></u-icon>
			</view>
			<view style="height: 500rpx;padding: 30rpx;">
				<u-upload
					:fileList="avatarlist"
					@afterRead="afterRead"
					@delete="deletePic"
					:maxCount="1"
					:previewFullImage="true"
				></u-upload>
			</view>
		</u-popup>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				usex:'保密',
				uname:'wuji',
				date:'2000-11-11',
				usignature:'今天天气真好！',
				src: 'https://cdn.uviewui.com/uview/swiper/1.jpg',
				showchangeavatar:false,
			};
		},
		computed: {
			startDate() {
				return this.getDate('start');
			},
			endDate() {
				return this.getDate('end');
			},
			avatarlist(){
				return [{url: 'https://cdn.uviewui.com/uview/swiper/1.jpg',}]
			}
		},
		methods:{
			bindDateChange: function(e) {
				this.date = e.target.value
			},
			getDate(type) {
				const date = new Date();
				let year = date.getFullYear();
				let month = date.getMonth() + 1;
				let day = date.getDate();
	
				if (type === 'start') {
					year = year - 60;
				} else if (type === 'end') {
					year = year + 2;
				}
				month = month > 9 ? month : '0' + month;
				day = day > 9 ? day : '0' + day;
				return `${year}-${month}-${day}`;
			},
			clickavatar(){
				this.showchangeavatar = true;
			},
			// 删除图片
			deletePic(event) {

			},
			// 新增图片
			async afterRead(event) {
				// 当设置 mutiple 为 true 时, file 为数组格式，否则为对象格式

			},
		}
	}
</script>

<style lang="scss">
@import '@/static/variables.scss';
.uavatar{
	margin-bottom: 30rpx;
	@extend %betweencenter
}
.ctrlbtn{
	padding: 20rpx;
	border-radius: 20rpx 20rpx 0 0;
	background-color: #007AFF;
	@extend %betweencenter
}
</style>
