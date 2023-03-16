<template>
  <div>
    <el-form :model="loginForm" status-icon ref="ruleForm" label-width="100px" class="loginForm">
      <div class="logo">
        <SvgIcon icon-class="ITHelpYou" />
<!--        <embed src="../assets/icons/svg/ITHelpYou.svg" type="image/svg+xml" width="200"/>-->
      </div>
      <el-form-item label="用户名" prop="username">
        <el-input v-model="loginForm.username" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input type="password" v-model="loginForm.password" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm()">提交</el-button>
        <el-button @click="register()">注册</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'login',
  data () {
    return {
      loginForm: {}
    }
  },
  methods: {
    submitForm () {
      this.$cookies.set('token', '')
      this.$axios.post('/login', this.loginForm).then((res) => {
        this.$cookies.set('token', 'jwt ' + res.token)
      })
    },
    register () {
      this.$router.push({ path: 'register' })
    }
  }
}
</script>

<style scoped>
.loginForm {
  width: 400px;
  /*height: 200px;*/
  border: white 1px solid;
  padding: 20px 20px 20px 0;
  position: absolute;
  transform: translateX(-50%) translateY(-50%);
  left: 50%;
  top: 50%;
}
.logo {
  width: 400px;
  height: 180px;
}
</style>
