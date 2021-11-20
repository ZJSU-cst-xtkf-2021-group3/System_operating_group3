<template>
  <div class="content">
    <el-menu default-active="/attention/topic" mode="horizontal" router>
      <el-menu-item index="/attention/topic">追踪事件</el-menu-item>
      <el-menu-item index="/attention/people">关注的人</el-menu-item>
    </el-menu>
    <div>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: "Attention"
}
</script>

<style lang="scss" scoped>
.content{
  margin-left: 20px;
  margin-right: 20px;
}
</style>