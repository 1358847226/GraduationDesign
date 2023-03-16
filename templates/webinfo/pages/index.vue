const WOW const WOW
<template>
  <div>
    <div class="banner">
      <div class="banner-text">
        <i class="el-icon-key" />
        <i :class="lock" style="font-size: 180px; display: block" />
        <h1 style="font-size: 51px" class="animate__animated animate__zoomInDown">
          小微软件应用分享平台
        </h1>
        <h3 class="animate__animated animate__bounce animate__slow">
          愿天下计算机系同学顺利毕业
        </h3>
      </div>
    </div>
    <div class="excellence">
      <!--      优秀作品-->
      <h2 class="center-text wow animate__lightSpeedInRight">
        优秀作品
      </h2>
      <div class="wow animate__lightSpeedInLeft">
        <el-carousel :interval="4000" type="card" height="400px">
          <el-carousel-item v-for="item in 6" :key="item">
            <img :src="require('../assets/excellence' + item + '.jpg')" alt="" width="640px">
            <div class="center-text">
              优秀作品{{ item }}
            </div>
          </el-carousel-item>
        </el-carousel>
      </div>
      <h2 class="center-text wow animate__lightSpeedInRight">
        最新分享
      </h2>
      <div class="new-share wow animate__lightSpeedInLeft">
        <el-card v-for="item in 6" :key="item" :body-style="{ padding: '0px' }" style="margin-bottom: 5px">
          <img :src="require('../assets/excellence' + item + '.jpg')" alt="" width="320px">
          <div class="center-text">
            最新分享{{ item }}
          </div>
        </el-card>
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
    }, 3800)
  },
  mounted () {
    this.$nextTick(() => {
      const { WOW } = require('wowjs')
      new WOW({ animateClass: 'animate__animated' }).init()
    })
    this.health()
  },
  methods: {
    health () {
      this.$axios.post('/login', { username: 'jxy', password: 'jxy5753897547' }).then((res) => {
        this.$cookies.set('token', 'jwt ' + res.token)
        this.$axios.get('/Products')
      })
    }
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

.el-carousel__item:nth-child(2n) {
  color: white;
  background-color: #001E1E;
}

.el-carousel__item:nth-child(2n+1) {
  color: white;
  background-color: #001E1E;
}
.excellence {
  width: 1280px;
  margin: 0 auto;
}
.center-text {
  text-align: center;
}
.new-share {
  display: flex;
  justify-content: space-between;
  align-content: space-between;
  flex-flow: row wrap;
  width: 100%;
  margin-top: 5px;
}
</style>
