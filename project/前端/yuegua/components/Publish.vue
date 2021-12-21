<template>
	<view>
		<view class="bigcell">
			<view class="cell1">
				<text>标题</text>
				<u--input v-model="title" placeholder="请输入标题" border="none"  maxlength="20"></u--input>			
			</view>			
			<view v-if="types === '引用'" class="cell1">
				<text>链接</text>
				<u--input v-model="link" placeholder="请添加链接" border="none" maxlength="200"></u--input>			
			</view>
			<view v-if="types!='topic'">
				<view class="cell1" style="display: flex;flex-direction: row;justify-content: space-between;">
					<text>时间</text>
					<view>
						<tm-pickersDate  @confirm="dateSe_1" btn-color="blue"
						:show-detail="{year:true,month:true,day:true,hour:true,min:true,sec:false}"
						>
							<tm-button theme="blue">事件发生时间</tm-button>
						</tm-pickersDate>							
						</view>
					<!-- <u--input v-model="datetime" placeholder="请输入时间,如:2021-9-21 12:8" border="none" maxlength="20"></u--input>	 -->		
				</view>
				<u-alert title="注:时间为事件发生的时间." fontSize="8" type = "warning"></u-alert>				
			</view>
			<view v-if="types=='topic'" class="cell1">
				<text>标签</text>
				<u--input v-model="tag" placeholder="请输入标签" border="none"  maxlength="5"></u--input>			
			</view>		
			<view v-if="types=='topic'" class="selecttype">
				<text>分类</text>
				<uni-combox :candidates="typecandidates" placeholder="请选择分类" v-model="type"></uni-combox>
			</view>
		</view>
		<view class="cell">
			<text>简介</text>
			<u--textarea v-model="desc" placeholder="请输入简介" height="100" maxlength="100" count></u--textarea>			
		</view>
		<view v-if="types=='topic'" class="cell2">
			<text>封面</text>
			<!-- <tm-upload :filelist.sync="coverimg" color="blue" max="1" @change="change"></tm-upload> -->
			<u-upload
				:fileList="fileListtopic"
				@afterRead="afterRead"
				@delete="deletePic"
				:maxCount="2"
				name="topic"
			></u-upload>			
		</view>
		<view v-if="types=='爆料'" class="cell2">
			<text @click="test()">图片</text>
	<robby-image-upload v-model="imageData"  :enable-drag="false" :enable-del="true" :enable-add="true" :limit="9"></robby-image-upload>
		</view>
		<view v-if="types=='topic'" class="bigcell">
			<view style="padding: 10rpx;display: flex;align-items: center;">
				<text>投票</text>
				<tm-switch v-model="addvote" :text="[]"></tm-switch>				
			</view>
			<view v-show="addvote">
<!-- 				<view class="cell1">
					<text>问题</text>
					<u--input v-model="quesion" placeholder="请输入问题" border="none"  maxlength="20"></u--input>			
				</view>	 -->
				<view v-for="(item,index) in selections" class="cell1">
					<text>选项{{index+1}}</text>
					<u--input v-model="selections[index]" :placeholder="'请输入选项'+(index+1)" border="none"  maxlength="20"></u--input>			
				</view>
				<view style="display: flex;justify-content: space-between;">
					<view style="width: 40vw;">
						<tm-button height="60" theme="grey-lighten-2" fontColor="grey-darken-1" :round="4" block @click="clickeddelselection">删除选项</tm-button>
					</view>
					<view style="width: 40vw;">
						<tm-button height="60" theme="grey-lighten-2" fontColor="grey-darken-1" :round="4" block @click="clickedaddselection">添加选项</tm-button>
					</view>						
				</view>

				
			</view>
			
		</view>
		<view style="margin-top: 40rpx;margin-bottom: 40rpx;display: flex;align-items: center;justify-content: center;margin: 20rpx 20rpx 0 20rpx;">
			<view v-if="types=='topic'" style="width: 20%">
				<tm-button  theme="grey-lighten-2" fontColor="grey-darken-2" :round="24" block @click="clicked">保存</tm-button>
			</view>
			<view style="width: 80%">
				<!-- <u-button :hairLine="false" shape="cicle" color="#1890FF" text="发布"></u-button> -->
				<tm-button theme="bg-gradient-blue-accent" :round="24" block @click="clickedpublish">{{types=='topic'?'发布':'添加'}}</tm-button>
			</view>
		</view>
		<tm-message ref="toast"></tm-message>
		
	</view>
</template>

<script>
	import robbyImageUpload from '@/components/robby-image-upload/robby-image-upload.vue'
	export default {
		name:"Publish",
		props:{
			types:{
				type:String,
				default:'topic'
			},
			TID:{
				type:String,
				default:0
			}
		},
		data() {
			return {
				title:'',
				desc:'',
				link:'',
				type:'',
				tag:'',
				quesion:'',
				c:[''],
				coverimg:[],
				selections:[''],
				datetime:Number(new Date()),
				addvote:false,
				typecandidates:['娱乐','体育','日常','二次元','数码','国际时政'],
				fileListtopic:[],
				tempimage:'',
				imageData:[],
				showTimePicker:false
			};
		},
		methods:{
			close(){
				this.showTimePicker=false
			},
			clickedaddselection(){
				this.selections.push('')
			},
			clickeddelselection(){
				let index=this.selections.length-1
				if(index>=0){
					this.selections.splice(index,1)
				}
			},
			deletePic(event) {
				this[`fileList${event.name}`].splice(event.index, 1)
			},
			afterRead(event) {
				let lists = [].concat(event.file)
				lists.map((item) => {
					this[`fileList${event.name}`].push({
						...item,
					})
				})
				this.tempimage = event.file.url
			},
			publishtopic(){
				return new Promise((resolve,reject)=>{
					let index=0;
					for(let i=0;i<6;++i){
						if(this.typecandidates[i]===this.type){
							index=i
						}
					}
					uni.uploadFile({
						url: 'http://101.37.175.115/Post/topic', 
						filePath: this.tempimage,
						name: 'mainPic',
						formData: {
							'category': index,
							'statement': this.desc,
							'title':this.title,
							'tag':this.tag,
						},
						success: (res) => {
							resolve(JSON.parse(res.data).TID)
						},
					});	
				})
			},
			async clickedpublish(){
				let that=this
				if(this.types === 'topic'){
					if(this.title && this.desc && this.link && this.type){
						if(!this.addvote){
							let tid = await this.publishtopic()
							// console.log(tid)
							uni.redirectTo({
								url:`../topic/topic?tid=${tid}`,
							})
						}
						else{
							let flag=true
							for(let i=0;i<that.selections.length;++i){
								if(that.selections[i]===''){
									flag=false
									break
								}
							}
							if(flag){
								let tid = await this.publishtopic()
								let data={TID:tid,items:that.selections}
								console.log(data)
								uni.request({
									url: 'http://101.37.175.115/Post/topic_vote',
									method:"POST",
									header: {'Content-Type': 'application/json'},
									data,
									success(res) {
										// console.log(res)
										uni.redirectTo({
											url:`../topic/topic?tid=${tid}`,
										})
									}
								})								
							}
							else{
								this.$refs.toast.show({model:'warn',wait:1000,label:"请填写完成必需内容"})
							}
						}

					}
					else{
						this.$refs.toast.show({model:'warn',wait:1000,label:"请填写完成必需内容"})
					}
				}
				if(this.types==='爆料'){
					var tmplist=[]
					let len=this.imageData.length
					console.log(len)
					for(let i=0;i<len;++i){
						var obj={
							'name':'imgs',
							'uri':this.imageData[i]
						}	
									tmplist.push(obj)
					}
					console.log(tmplist)
					uni.uploadFile({
					            url: 'http://101.37.175.115/Post/revelation', 
								// url: 'http://yuegua.fgimax.vipnps.vip/Post/revelation', 
					            files:tmplist,
					            
					            formData: {
					                'TID' : parseInt(this.TID),
									'title':this.title,
									'statement':"xxx",
									'eventTime':this.datetime,
									'text':this.desc
									
					            },
					            success: (res) => {
					              
									console.log(res.data);
									// this.toastHandler(tmp)
									uni.$emit('posted',JSON.parse(res.data).res)
					            }
					        });
				}
				if(this.types==='引用'){
					uni.request({
					    url: 'http://101.37.175.115/Post/event',
						header: {
						        'Content-Type': 'application/x-www-form-urlencoded' 
						    },
							method:"POST",
							data:{
								'TID' : parseInt(this.TID),
								'title':this.title,
								'statement':this.desc,
								'eventTime':this.datetime,
								'url':this.link
							},
					   success: (res) => {
					       console.log(res.data);
						   
					   	uni.$emit('posted',res.data.res)
					   }
						
					});
				}
			},
			clickedsave(){
				
			},
			test(){
				
				
			},
			dateSe_1(e){
				// {year: 2021, month: 8, day: 23}
				this.datetime = e.year+'-'+e.month + '-' + e.day+" "+e.hour+":"+e.min;
				console.log(this.datetime)
			},
			clicked(){
				
			}
			
		},
		
		components: {robbyImageUpload}
	}
</script>

<style lang="scss" scoped>
@import '@/static/variables.scss';
text{
	color: #999999;
	font-size: 30rpx;
}
.bigcell{
	margin: 10rpx;
	margin-top: 20rpx;
	padding: 10rpx;
	box-shadow: 0px 0px 2px 1px $shadowcolor;
	border-radius: 20rpx;
	background-color: #fff;
	margin-bottom: 20rpx;
	text{
		margin-right: 15rpx;
	}	
	.cell1{
		padding: 10rpx;
		@extend %center;
	}
	.selecttype{
		padding: 10rpx;
		background-color: #fff;
		border-radius: 20rpx;
		@extend %betweencenter;
	}
}
.cell{
	margin: 10rpx;
	padding: 20rpx;
	border-radius: 20rpx;
	background-color: #fff;
	margin-bottom: 20rpx;
	box-shadow: 0px 0px 2px 1px $shadowcolor;
}

.cell2{
	margin: 10rpx;
	padding: 20rpx;
	background-color: #fff;
	border-radius: 20rpx;
	margin-bottom: 10rpx;
	box-shadow: 0px 0px 2px 1px $shadowcolor;
}

</style>
