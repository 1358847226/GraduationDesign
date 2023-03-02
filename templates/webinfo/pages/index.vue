<template>
  <div>
    <div class="banner">
      <div class="banner-text">
        <i class="el-icon-key" />
        <i :class="lock" style="font-size: 180px; display: block" />
        <h1 style="font-size: 51px">
          小微软件应用分享平台
        </h1>
        <h3>愿天下计算机系同学顺利毕业</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  layout: 'header',
  data () {
    return {
      childName: '',
      lock: 'el-icon-lock'
    }
  },
  created () {
    const that = this
    setTimeout(function () {
      that.lock = 'el-icon-unlock'
    }, 4000)
  }
}
</script>
<style scoped>
.banner-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform:translate(-50%,-60%);
  color: darkred;
  opacity: 0.8;
  text-align: center;
}
.banner {
  width: 100%;
  height: 1068px;
  background-image: url("../assets/computer.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}
.el-icon-key {
  font-size: 180px;
  position: relative;
  animation-name: example;
  animation-duration: 4s;
  visibility: hidden;
}
@keyframes example {
  0%   {left:500px; top:0;visibility: visible}
  25%  {left:500px; top:500px;visibility: visible}
  50%  {left:0; top:500px;visibility: visible}
  100%  {left:0; top:300px;visibility: hidden}
}
</style>
