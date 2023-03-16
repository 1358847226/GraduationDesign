<template>
  <div class="footer">
    <div style="margin: auto">
      <div class="footer-children">
        <div class="footer-title">
          联系我们
        </div>
        <div class="footer-text">
          <br>
          邮箱:1358847226@qq.com
          <br>
          电话:17855827804
          <br>
          微信:jxyhelpyou
        </div>
      </div>
      <div class="footer-children center">
        <div class="footer-title">
          作品分类
        </div>
        <div class="footer-text">
          <br>
          <a @click="$router.push({path: 'Product', query: {label: 'JAVA'}})">JAVA</a>
          <a @click="$router.push({path: 'Product', query: {label: 'SSM'}})">SSM</a>
          <a @click="$router.push({path: 'Product', query: {label: 'SpringBoot'}})">SpringBoot</a>
          <br>
          <a @click="$router.push({path: 'Product', query: {label: 'Python'}})">Python</a>
          <a @click="$router.push({path: 'Product', query: {label: 'Django'}})">Django</a>
          <a @click="$router.push({path: 'Product', query: {label: 'Flask'}})">Flask</a>
          <br>
          <a @click="$router.push({path: 'Product', query: {label: 'C#'}})">C#</a>
          <br>
          <a @click="$router.push({path: 'Product', query: {label: '前端'}})">前端</a>
        </div>
      </div>
      <div class="footer-children">
        <div class="footer-title">
          意见反馈
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FooterDefault'
}
</script>

<style scoped>
.footer {
  background-color: #001E1E;
  width: 100%;
  height: 200px;
  display: flex;
  margin-top: 10px;
}
.footer-children {
  float: left;
  width: 427px;
  height: 200px;
  color: cornsilk;
}
.center {
  border: cornsilk solid;
  border-width: 0 1px;
}
.footer-title {
  margin-top: 10px;
  height: 30px;
  font-size: 20px;
  text-align: center;
}
.footer-text {
  text-align: center;
}
.footer-text a {
  text-decoration: underline;
  cursor: pointer;
}
</style>
