<template>
  <div id="header">
    <el-row>
      <el-col :span="4">
        <span class="headerbox"><h1>LOGO</h1></span>
      </el-col>
      <el-col :span="2">
        <span class="headerbox"><h3>首页</h3></span>
      </el-col>
      <el-col :span="8" offset="2">
        <span class="headerbox">
          <el-input class="searchinput" prefix-icon="el-icon-search" placeholder="请输入内容" v-model="input" >
          </el-input>
        </span>
      </el-col>
      <el-col :span="6" offset="2">
        <span class="headerdata">
          <span class="user">
            <el-dropdown placement="bottom-start">
              <span>
                <el-avatar :size="40" :src="circleUrl"></el-avatar>
                <span class="username">用户名</span>
              </span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item icon="el-icon-user">个人中心</el-dropdown-item>
                <el-dropdown-item icon="el-icon-sort">切换账号</el-dropdown-item>
                <el-dropdown-item icon="el-icon-right">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </span>
          <el-divider direction="vertical"></el-divider>
          <span>
            <el-badge  is-dot class="badgeitem">
              <el-button circle icon="el-icon-bell"></el-button>
            </el-badge>
          </span>
        </span>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "Header",
  data(){
    return{
      input:'',
      circleUrl:'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'
    }
  }
}
</script>

<style lang="scss">
@import "./src/assets/variables";

#header{
  height: 80px;
  background-color: $headercgcolor;
}

.headerbox {
  @extend #header;
  @extend %center;
}

.headerdata{
  @extend #header;
  @extend %rightcenter;
  padding: 0 10px 0 10px;
  .el-divider{
    height:20px;

  }

}

.user{
  width: 40%;
  span{
    @extend %leftcenter;
  }
  .username{
    font-family: "Microsoft YaHei";
    font-size: 15px;
    font-size-adjust: 0.5;
    margin-left: 10px;
  }
}

</style>