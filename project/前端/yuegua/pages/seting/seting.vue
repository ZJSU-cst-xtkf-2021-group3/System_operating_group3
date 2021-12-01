<template>
	<view>
		<u-collapse>
			<u-collapse-item title="账号设置">
				<u-cell title="修改密码" isLink clickable :border="false">
					<u-icon slot="icon" name="grid-fill" size="20"></u-icon>
				</u-cell>				
			</u-collapse-item>
			<u-collapse-item title="隐私设置">
				<u-cell title="关注的话题">
					<u-switch slot="value" v-model="focustopic"></u-switch>
				</u-cell>			
				<u-cell title="关注的用户" >
					<u-switch slot="value" v-model="focususer"></u-switch>
				</u-cell>	
				<u-cell title="发布的话题">
					<u-switch slot="value" v-model="publishtopic"></u-switch>
				</u-cell>			
				<u-cell title="发布的评论">
					<u-switch slot="value" v-model="comment"></u-switch>
				</u-cell>	
				<u-cell title="发布的节点">
					<u-switch slot="value" v-model="publisnode"></u-switch>
				</u-cell>			
				<u-cell title="关注后可见"  :border="false">
					<u-switch slot="value" v-model="neddfocus"></u-switch>
				</u-cell>	
			</u-collapse-item>
		</u-collapse>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				focustopic:false,
				focususer:false,
				publishtopic:false,
				comment:false,
				publisnode:false,
				neddfocus:false,
			};
		},
		methods:{
		}
	}
</script>

<style lang="scss">

</style>
