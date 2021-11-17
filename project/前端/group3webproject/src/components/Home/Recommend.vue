<template>
  <div class="content">
    <div class="carousel">
      <el-carousel trigger="click" height="200px">
        <el-carousel-item v-for="item in 4" :key="item">
        </el-carousel-item>
      </el-carousel>
    </div>

  </div>
</template>

<script>
export default {
  name: "Recommand"
}
</script>

<style lang="scss" scoped>

.content{
  margin-left: 20px;
  margin-right: 20px;
  .carousel{
    margin-left: 200px;
    margin-right: 200px;
  }
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}

</style>