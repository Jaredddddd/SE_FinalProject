<template>
  <el-container>
    <el-header>
      <el-menu
        :default-active="activeIndex2"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="rgb(1, 67, 36)"
        text-color="#fff"
        active-text-color="#ffd04b"
      >
        <el-menu-item class="fr" index="1">
        <img src="../assets/login/sysu.jpg" alt="图片" width="70" height="50"></el-menu-item>

        <!-- <el-menu-item index="2"><router-link to="/home" class="link-text">企业介绍</router-link></el-menu-item> -->
        <el-menu-item class="fr" index="3"><router-link to="/" class="link-text">登陆页面</router-link></el-menu-item>

        <!-- <el-menu-item index="4">图标</el-menu-item> -->
      </el-menu>
    </el-header>
    <el-container>
      
      <el-aside :width="'165px'">
        <el-row class="tac">
          <el-col :span="19">
            <el-menu
              default-active="2"
              class="el-menu-vertical-demo"
              @select="handleOpen"
              background-color="rgb(1, 67, 36)"
              text-color="#fff"
              active-text-color="#ffd04b"
            >
              <el-menu-item index="1">
                <i class="el-icon-location"></i>
                <span slot="title"><router-link to="/staff" class="link-text">员工信息表</router-link></span>
              </el-menu-item>

              <el-menu-item index="2">
                <i class="el-icon-menu"></i>
                <span slot="title"><router-link to="/client" class="link-text">客户信息表</router-link></span>
              </el-menu-item>

              <el-menu-item index="3">
                <i class="el-icon-document"></i>
                <span slot="title"><router-link to="/commodity" class="link-text">商品信息表</router-link></span>
              </el-menu-item>

              <el-menu-item index="4">
                <i class="el-icon-setting"></i>
                <span slot="title"><router-link to="/purchase" class="link-text">进货信息表</router-link></span>
              </el-menu-item>

              <el-menu-item index="5">
                <i class="el-icon-setting"></i>
                <span slot="title"><router-link to="/sale" class="link-text">销售信息表</router-link></span>
              </el-menu-item>

            </el-menu>
          </el-col>
        </el-row>
      </el-aside>

      <el-main class="main-container">
        <!-- 子路由从这里出去 -->

      <router-view/>
      </el-main>
    </el-container>
  </el-container>
</template>  
 
<script>
export default {
  name: "App",
  data() {
    return {
      activeIndex2: "1",
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>  

<style>

/* background-size: 1500px 900px;  width height */
.main-container {
  background-image: url('../assets/sysu3.jpg');
  /* background-size: 1400px 900px;    */
  background-size: 100% 100%;
  /* background-image: url('../assets/sysu100.png');
  background-size: 400px 400px;  
  background-position: 40% 50%;  */
  background-repeat: no-repeat;
}

.el-container {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0px;
  left: 0;
  bottom: 0;
}
.el-header {
  padding: 0;
  width: 101%;
  height: 100%;
  z-index: 1000;
}

/* header菜单需要靠右的添加.fr即可(如：<el-menu-item class="fr" index="3">消息中心</el-menu-item>) */
.el-header .fr {
  float: right;
}
.el-header .el-menu {
  border-bottom: none;

}
.el-aside,
.el-main {
  padding-top: 60px;
}
.el-aside {
  /* background: rgb(1, 67, 36); */
  background: rgb(1, 67, 36); 
}
.el-aside .el-menu {
  border-right: none;
}

.link-text {
  color: rgb(245, 245, 245); /* 修改为你需要的颜色 */
  text-decoration: none;
}

</style>