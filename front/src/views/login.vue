<template>
  <div class="login">
    <Row justify="center" align="middle" @keydown.enter.native="submitLogin" style="height: 100%">
      <div class="loginUp">
        <div class="loginLeft">
          <img src="../assets/login/sysu.jpg" alt="" style="width: 100px; height: 95px; position: relative; top: -30px" />
          <span class="line"></span>
          <span class="title">超市库存管理系统</span>
        </div>
      </div>
      <div class="loginMiddle">
        <div class="login-background">
          <div class="loginBg"></div>
          <div class="loginRight">
            <Row class="loginRow">
              <el-tabs v-model="tabName" @tab-click="changeTabName" class="loginTab" style="width: 390px; height: 30px;margin: 0 auto">
                <el-tab-pane label="账号密码登录" name="userAndPassword" class="zhanghaomima">
                  <el-form ref="usernameLoginForm" :model="form" :rules="usernameLoginFormRules" class="form">
                    <el-form-item prop="username" class="loginInput">
                      <el-row>
                        <el-input v-model="form.username" size="large" clearable placeholder="登录账号" autocomplete="off">
                          <i class="iconfont icon-yonghu" slot="prefix" style="line-height: 50px"></i>
                        </el-input>
                      </el-row>
                    </el-form-item>
                    <el-form-item prop="password">
                      <el-input v-model="form.password" size="large" type="password" placeholder="请输入登录密码" autocomplete="off" style="margin-top: 55px">
                        
                      <!-- <el-input style="height: 50px; line-height: 50px" type="password" v-model="form.password" size="large" placeholder="请输入登录密码" autocomplete="off"> -->
                        <i class="iconfont icon-mima1" slot="prefix" style="line-height: 50px"></i>
                      </el-input>
                    </el-form-item>
                  </el-form>
                  <el-row>
                    <el-button class="login-btn" type="primary" size="large" :loading="loading" long @click="submitLogin">
                      <span v-if="!loading" style="letter-spacing: 20px; font-weight: bold">登录</span>
                      <span v-else>正在登录...请稍后</span>
                    </el-button>
                  </el-row>
                  <el-row v-if="errorMessage" style="color: red; margin-top: 10px;">
                    {{ errorMessage }}
                  </el-row>
                </el-tab-pane>
                <el-tab-pane label="注册" name="register">
                  <el-form ref="registerForm" :model="registerForm" :rules="registerFormRules" class="form">
                    <el-form-item prop="identity">
                      <el-select v-model="registerForm.identity" placeholder="请选择身份">
                        <el-option label="管理员" value="manager"></el-option>
                        <el-option label="进货员" value="buyer"></el-option>
                        <el-option label="销售员" value="saler"></el-option>
                      </el-select>
                    </el-form-item>
                    <el-form-item prop="username">
                      <el-input v-model="registerForm.username" size="large" clearable placeholder="注册账号" autocomplete="off">
                        <i class="iconfont icon-yonghu" slot="prefix" style="line-height: 50px"></i>
                      </el-input>
                    </el-form-item>
                    <el-form-item prop="password">
                      <el-input type="password" v-model="registerForm.password" size="large" placeholder="请输入密码" autocomplete="off">
                        <i class="iconfont icon-mima1" slot="prefix" style="line-height: 50px"></i>
                      </el-input>
                    </el-form-item>
                    <el-form-item prop="confirmPassword">
                      <el-input type="password" v-model="registerForm.confirmPassword" size="large" placeholder="确认密码" autocomplete="off">
                        <i class="iconfont icon-mima1" slot="prefix" style="line-height: 50px"></i>
                      </el-input>
                    </el-form-item>
                  </el-form>
                  <el-row class="register-btn-row">
                    <el-button class="register-btn" type="primary" size="large" :loading="loading" long @click="submitRegister">
                      <span v-if="!loading" style="letter-spacing: 20px; font-weight: bold">注册</span>
                      <span v-else>正在注册...请稍后</span>
                    </el-button>
                  </el-row>
                  <el-row v-if="registerErrorMessage" style="color: red; margin-top: 10px;">
                    {{ registerErrorMessage }}
                  </el-row>
                </el-tab-pane>
              </el-tabs>
            </Row>
            <p class="loginBottom">欢迎来到无为超市</p>
          </div>
        </div>
      </div>
    </Row>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      saoMaFx: false,
      captchaId: "",
      captchaImg: "",
      loadingCaptcha: false,
      error: false,
      tabName: "userAndPassword",
      saveLogin: false,
      loading: false,
      form: {
        username: "admin",
        password: "",
        mobile: "",
        code: "",
      },
      registerForm: {
        username: "",
        password: "",
        confirmPassword: ""
      },
      usernameLoginFormRules: {
        username: [
          { required: true, message: "账号不能为空", trigger: "blur" },
        ],
        password: [
          { required: true, message: "密码不能为空", trigger: "blur" },
        ],
      },
      registerFormRules: {
        username: [
          { required: true, message: "账号不能为空", trigger: "blur" },
        ],
        password: [
          { required: true, message: "密码不能为空", trigger: "blur" },
        ],
        confirmPassword: [
          { required: true, message: "确认密码不能为空", trigger: "blur" },
          { validator: (rule, value, callback) => {
            if (value !== this.registerForm.password) {
              callback(new Error('两次输入的密码不一致'));
            } else {
              callback();
            }
          }}
        ],
      },
      errorMessage: null,
      registerErrorMessage: null,
    };
  },
  methods: {
    changeTabName(e) {
      if (e != "userAndPassword") {
        window.WwLogin({
          id: "qywxsmqywxsm",
          appid: "wwf94bb44e76e308f8",
          agentid: "1000002",
          state: "LJW1314520",
          href: "",
        });
      }
    },
    submitLogin() {
      this.$axios.post("/login", this.form).then((res) => {
        if (res.code == 200) {
          this.$notify.success({ title: "成功", message: res.msg, duration: 2000 });
          // 打印放回的数据
          // console.log(res.data);
          // 根据用户身份跳转到不同页面
          if (res.data.identity === 'manager') {
            this.$router.push('/manager');
          } else if (res.data.identity === 'buyer') {
            this.$router.push('/buyer');
          } else if (res.data.identity === 'saler') {
            this.$router.push('/saler');
          } else {
            // 默认跳转到 main 页面
            this.$router.push('/main');
          }
        } else {
          this.$notify.error({ title: "错误", message: res.msg, duration: 2000 });
        }
      });
    },
    submitRegister() {
      this.$axios.post("/register", this.registerForm).then((res) => {
        if (res.code == 200) {
          this.$notify.success({ title: "成功", message: res.msg, duration: 2000 });
          // this.$router.push('/');
          setTimeout(() => {
            location.reload(); // 注册成功后重新加载页面
          }, 1000);
        } else {
          this.$notify.error({ title: "错误", message: res.msg, duration: 2000 });
        }
      }).catch((err) => {
        this.registerErrorMessage = err.response.data.message || '注册失败';
      });
    },
  },
};
</script>

<style lang="less">
html,
body {
  background: #ffffff !important;
  font-family: Microsoft YaHei;
  font-weight: 400;
}
a {
  font-family: Microsoft YaHei;

  color: #ffffff !important;
}
input::-webkit-input-placeholder {
  font-size: 14px;
}
.ivu-checkbox-wrapper.ivu-checkbox-large {
  font-size: 14px;
}
a:hover {
  font-family: Microsoft YaHei;
  color: #77c8c6;
}
.login {
  height: 100%;
  background-color: #ffffff !important;

  .ivu-tabs-nav-container {
    line-height: 2;
    font-size: 17px;
    box-sizing: border-box;
    white-space: nowrap;
    overflow: hidden;
    position: relative;
    zoom: 1;
  }
  .loginUp {
    width: 1200px;
    min-height: 80px;
    background-color: rgb(255, 255, 255);
    margin: 0 auto;
    overflow: hidden;
  }
  .loginLeft {
    margin-top: 20px;
    height: 50px;
    display: flex;
  }
  .line {
    display: inline-block;
    width: 2px;
    height: 25px;
    background: url(../assets/login/line.png);
    margin: 0px 10px;
    margin-top: 15px;
  }
  //超市库存管理系统颜色字体
  .title {
    line-height: 58px;
    font-size: 18px;
    font-family: Microsoft YaHei;
    font-weight: 500;
    color: #8a2525;
  }
  //是否自动登陆字体
  .zhanghao {
    color: #f6f6f6 !important;
  }
  .loginMiddle {
    width: 100%;
    height: 780px;
    margin: 0 auto;
    background-color: rgb(255, 255, 255);
    overflow: hidden;
    // background: linear-gradient(45deg, rgba(2, 173, 168, 0.17), rgba(0, 221, 215, 0.17));
  }
  .login-background {
    width: 1300px;
    height: 780px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
  }

  .loginBg {
    width: 560px;
    height: 560px;
    margin-top: 20px;
    background-image: url(../assets/login/sysu100.png);
    background-repeat: no-repeat;
    background-position: left bottom;
    background-size: contain;
  }
  //账号密码的方框
  .loginRight {
    width: 450px;
    height: 490px;
    background-color: rgba(128, 118, 118, 0.184);
    border: 1px solid rgb(117, 174, 117);
    box-shadow: 0px 2px 15px 1px rgba(240, 239, 239, 0.1);
    border-radius: 5px;
    margin-top: 95px;
    margin-right: 100px;
    position: relative;
  }
  .loginRow {
    padding: 0px 30px;
    color: #8a2525;
  }
  .loginDown {
    width: 1200px;
    height: auto;
    margin: 0 auto;
  }
  .loginTab {
    margin-top: 20px;
  }
  .ivu-tabs-tab {
    color: #333333;
    font-size: 18px;
    font-family: Microsoft YaHei;
    font-weight: bold;
  }
  .ivu-tabs-nav .ivu-tabs-tab {
    padding: 8px 42px;
    margin-right: 0px;
    color: #fff8f8;
  }
  //账号密码下面横线
  .ivu-tabs-ink-bar {
    height: 4px;
    width: 86px !important;
    border-radius: 2px;
    margin: 0px 142px;
    background-color: #fafafa;
  }

  .loginInput {
    position: relative; /* 相对定位 */
    top: 45px; /* 向下移动50像素 */
    font-size: 18px;
    font-family: Microsoft YaHei;
    font-weight: bold;
    color: #be3131;
  }

  // .login-password {
  //   position: relative; /* 相对定位 */
  //   top: 55px; /* 向下移动50像素 */
  //   // margin-top: 65px; /* 根据需要调整这个值 */
  // }
  .ivu-tabs-bar {
    border-bottom: 0px;
    color: #f6f6f6;
  }
  //登陆方框
  .login-btn {
    position: relative; /* 相对定位 */
    top: 0px; /* 向下移动50像素 */
    width: 390px;
    height: 50px;
    background: radial-gradient(circle, rgba(7, 90, 29, 0.992), rgb(6, 85, 37));
    border: 2px solid #dde8e8;
    box-shadow: 0px 2px 6px 0px rgba(0, 0, 0, 0.21);
    border-radius: 4px;
    margin-top: 5px; /* 调整登录按钮的位置 */
  }
  .register-btn {
    width: 390px;
    height: 50px;
    background: radial-gradient(circle, rgba(7, 90, 29, 0.992), rgb(6, 85, 37));
    border: 2px solid #e1e8e8;
    box-shadow: 0px 2px 6px 0px rgba(0, 0, 0, 0.21);
    border-radius: 4px;
    margin-top: 5px; /* 调整注册按钮的位置 */
  }

  .login .login-btn,
  .login .other-login {
    margin-top: 40px;
    color: #fcfafa;
  }

  .loginBottom {
    width: 448px;
    height: 60px;
    background: #f9f9f9;
    border-radius: 0px 0px 5px 5px;
    padding: 0px;
    position: absolute;
    bottom: 0px;
    font-size: 16px;
    font-weight: bold;
    color: #aa1313;
    text-align: center;
    line-height: 60px;
  }
  .loginDown p {
    text-align: center;
    font-size: 12px;
    font-family: Microsoft YaHei;
    color: #420d0d;
    line-height: 22px;
  }
  //是否自动登陆框
  .ivu-checkbox-checked .ivu-checkbox-inner {
    background-color: #d7d0ff;
    border-color: #d7d0ff;
  }
  .ivu-form-item {
    margin-bottom: 24px;
    color: #f6f6f6;
  }
  .ivu-input-wrapper-large .ivu-input-icon {
    line-height: 50px;
  }
  .loginInput input:nth-of-type(1) {
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    font-family: Microsoft YaHei;
    color: #520909;
    line-height: 50px;
  }
  .ivu-input-large {
    height: 50px;
    color: #cfcfcf;
    line-height: 50px;
  }
  .ivu-input-large {
    font-size: 14px;
  }
  .ivu-btn-large {
    height: 50px;
  }
  .form {
    padding-top: 2vh;

    .input-verify {
      width: 67%;
    }
  }

  .code-image {
    .ivu-spin-fix .ivu-spin-main {
      height: 20px;
    }
  }

  .forget-pass,
  .other-way {
    font-size: 14px;
  }

  .login-btn,
  .other-login {
    margin-top: 40px;
  }

  .icons {
    display: flex;
    align-items: center;
  }

  .other-icon {
    cursor: pointer;
    margin-left: 10px;
    display: flex;
    align-items: center;
    color: rgba(252, 252, 252, 0.2);

    :hover {
      color: #0d4887;
    }
  }

  .layout {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 368px;
    height: 100%;
  }

  .register-btn-row {
    display: flex;
    justify-content: center; /* 调整注册按钮位置 */
  }
}

.zhanghaomima {
  color: #f6f6f6 !important;
}

.el-tabs__content {
  overflow: visible !important; /* 或者使用 'visible'，根据你的需求 */
}


// //账号密码样式
// .ivu-tabs-nav .ivu-tabs-tab-active,
// .ivu-tabs-nav .ivu-tabs-tab:hover {
//   color: #ffffff !important;
//   margin: 0px 92px;
// }


// //默认颜色
// .ivu-tabs-nav .ivu-tabs-tab {
//   border: none;
//   background-color: transparent;
// }
// //鼠标选中的颜色
// .ivu-tabs-nav .ivu-tabs-tab-active {
//  color: #26bca8;
// }
// //鼠标移上去的颜色
// .ivu-tabs-nav .ivu-tabs-tab:hover{
//  color: #26bca8;
// }



</style>
