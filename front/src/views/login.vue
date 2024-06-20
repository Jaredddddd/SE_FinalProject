<template>
  <div class="login">
    <Row
      justify="center"
      align="middle"
      @keydown.enter.native="submitLogin"
      style="height: 100%"
    >
      <div class="loginUp">
        <div class="loginLeft">
          <!-- <img src="../assets/login/logo.png" alt="" srcset=""> -->
          <img
            src="../assets/login/sysu.jpg"
            alt=""
            srcset=""
            style="width: 100px; height: 95px; position: relative; top: -30px"
          />
          <span class="line"></span>
          <span class="title">超市库存管理系统</span>
        </div>
      </div>

      <div class="loginMiddle">
        <div class="login-background">
          <div class="loginBg"></div>
          <div class="loginRight">
            <Row class="loginRow">

              <el-tabs
                v-model="tabName"
                @tab-click="changeTabName"
                class="loginTab"
                style="width: 390px; height: 30px;margin: 0 auto;"
              >
                <el-tab-pane
                  label="账号密码登录"
                  name="userAndPassword"
                  class="zhanghao"
                >
                  <el-form
                    ref="usernameLoginForm"
                    :model="form"
                    :rules="usernameLoginFormRules"
                    class="form"
                  >
                    <el-form-item prop="username" class="loginInput">
                      <el-row>
                        <el-input
                          v-model="form.username"
                          size="large"
                          clearable
                          placeholder="登录账号"
                          autocomplete="off"
                        >
                          <i
                            class="iconfont icon-yonghu"
                            slot="prefix"
                            style="line-height: 50px"
                          ></i>
                        </el-input>
                      </el-row>
                    </el-form-item>
                    <el-form-item prop="password">
                      <el-input
                        style="height: 50px; line-height: 50px"
                        type="password"
                        v-model="form.password"
                        size="large"
                        placeholder="请输入登录密码"
                        password
                        autocomplete="off"
                      >
                        <i
                          class="iconfont icon-mima1"
                          slot="prefix"
                          style="line-height: 50px"
                        ></i>
                      </el-input>
                    </el-form-item>
                  </el-form>
                  <el-row>
                    <el-button
                      class="login-btn"
                      type="primary"
                      size="large"
                      :loading="loading"
                      long
                    >
                      <span
                        v-if="true"
                        style="letter-spacing: 20px; font-weight: bold"
                        ><router-link to="/main" class="link-text">登录</router-link
                        ></span
                      >
                      <span v-else>正在登录...请稍后}</span>
                    </el-button>
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
export default {
  components: {},
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
        password: "123456",
        mobile: "",
        code: "",
      },
      usernameLoginFormRules: {
        username: [
          {
            required: true,
            message: "账号不能为空",
            trigger: "blur",
          },
        ],
        password: [
          {
            required: true,
            message: "密码不能为空",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    changeTabName(e) {
      if (e != "userAndPassword") {
        window.WwLogin({
          id: "qywxsmqywxsm",
          appid: "wwf94bb44e76e308f8",
          agentid: "1000002",
          // redirect_uri: "https://artskyhome.com:8080/%23/login",
          state: "LJW1314520",
          href: "",
        });
      }
    },
    afterLogin(res) {
      let accessToken = res.result;
      this.setStore("accessToken", accessToken);
      userInfo().then((res) => {
        if (res.success) {
          delete res.result.permissions;
          let roles = [];
          res.result.roles.forEach((e) => {
            roles.push(e.name);
          });
          delete res.result.roles;
          this.setStore("roles", roles);
          this.setStore("saveLogin", this.saveLogin);
          if (this.saveLogin) {
            Cookies.set("userInfo", JSON.stringify(res.result), {
              expires: 7,
            });
          } else {
            Cookies.set("userInfo", JSON.stringify(res.result));
          }
          this.setStore("userInfo", res.result);
          this.$store.commit("setAvatarPath", res.result.avatar);
          util.initRouter(this);
          this.$router.push({
            name: "home_index",
          });
        } else {
          this.loading = false;
        }
      });
    },
    submitLogin() {
      // this.$refs.usernameLoginForm.validate((valid) => {
      //   if (valid) {
          this.loading = true;
          login({
            username: this.form.username,
            password: this.form.password,
            // code: this.form.imgCode,
            // captchaId: this.captchaId,
            saveLogin: this.saveLogin,
          }).then((res) => {
            if (res.success) {
              this.afterLogin(res);
            } else {
              this.loading = false;
            }
          });
      //   }
      // });
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

  color: #77c8c6;
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
  background-color: #ffffff;

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
    color: #ffffff;
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
    // width: 560px;
    // height: 560px;
    // margin-top: 20px;
    // // background-image: url(../assets/login/star.png);
    // background-image: url(../assets/login/sysu3.jpg);
    // background-repeat: no-repeat;
    // background-position: left bottom;
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
    height: 420px;
    background-color: rgb(4, 66, 7);
    border: 1px solid rgb(1, 47, 4);
    box-shadow: 0px 2px 15px 1px rgba(0, 0, 0, 0.1);
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
  }
  //账号密码下面横线
  .ivu-tabs-ink-bar {
    height: 4px;
    width: 86px !important;
    border-radius: 2px;
    margin: 0px 142px;
    background-color: #d7d0ff;
  }
  //账号密码样式
  .ivu-tabs-nav .ivu-tabs-tab-active,
  .ivu-tabs-nav .ivu-tabs-tab:hover {
    color: #ffffff;
    margin: 0px 92px;
  }
  .loginInput {
    font-size: 18px;
    font-family: Microsoft YaHei;
    font-weight: bold;
    color: #be3131;
  }

  .ivu-tabs-bar {
    border-bottom: 0px;
  }
  //登陆方框
  .login-btn {
    width: 390px;
    height: 50px;
    background: radial-gradient(circle, rgb(32, 195, 37), rgb(49, 188, 213));
    border: 2px solid #61c8c5;
    box-shadow: 0px 2px 6px 0px rgba(0, 0, 0, 0.21);
    border-radius: 4px;
  }
  .login .login-btn,
  .login .other-login {
    margin-top: 40px;
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
    color: rgba(0, 0, 0, 0.2);

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
}
</style>
