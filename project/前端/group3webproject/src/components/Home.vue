<template>
<div class="container" >
  <el-row>
    <el-col :span="5" offset="1"><div class="navi"></div></el-col>
    <el-col :span="12"><div class="content"></div></el-col>
    <el-col :span="5"><div class="rank"></div></el-col>
  </el-row>
</div>
</template>

<script>
export default {
  name: "Home"
}
</script>

<style lang="scss">

.container{
  margin: 10px;
  .navi{
    height: 100px;
    background-color: #42b983;
  }
  .content{
    height: 500px;
    background-color: aqua;
  }
  .rank{
    height: 200px;
    background-color: aliceblue;
  }
}


</style>