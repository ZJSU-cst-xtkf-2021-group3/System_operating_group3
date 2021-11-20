<template>
<div class="container" >
  <el-row>
    <el-col :span="2" offset="2"><div class="navi">

  <el-menu default-active="/" router>
    <el-menu-item index="/">
      <span class="menuitem"><span slot="title">推荐</span></span>
    </el-menu-item>
    <el-menu-item index="/attention/topic">
      <span class="menuitem"><span slot="title">关注</span></span>

    </el-menu-item>
  </el-menu>

    </div></el-col>
    <el-col :span="16"><div class="content">
      <router-view></router-view>
    </div></el-col>
    <el-col :span="3"><div class="rank">
      <div class="ranktitle">热点</div>
      <div class="rankcontent" v-for="index in 10" :key="index" > <span>{{index}}.</span><span>热点事件{{index}}</span> </div>
      <div class="rankmore"> <el-link type="primary">查看更多</el-link> </div>
    </div></el-col>
  </el-row>
</div>
</template>

<script>
export default {
  name: "Home"
}
</script>

<style lang="scss">
@import "src/assets/variables";

.container{
  margin: 10px;
  .navi{
    //background-color: aqua;
  }
  .content{
    height: 500px;
    //background-color: aqua;
  }
  .rank{
    font-family: "Microsoft YaHei";
    background-color: aliceblue;
    .ranktitle{
      @extend %center;
      padding: 10px 0 0 0;
      font-size: 18px;
    }
    .rankcontent{
      margin: 10px;
      font-size: 15px;
    }
    .rankmore{
      @extend %center;
      padding-bottom: 10px;
    }
  }
  .menuitem{
    @extend %center;
    span{
      font-family: "Microsoft YaHei";
      font-size: 20px;
    }
  }

}


</style>