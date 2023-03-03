<template>
  <div class="header">
    <el-menu
      :default-active="activeIndex"
      class="nav"
      mode="horizontal"
      background-color="#001E1E"
      text-color="#fff"
      active-text-color="#ffd04b"
    >
      <div class="logo">
        <img class="logo-img" src="../assets/ITHelpYou.png" alt="it help you, it帮你">
      </div>
      <el-menu-item index="1" @click="$router.push({path: '/'})">
        主页
      </el-menu-item>
      <el-menu-item index="2" @click="$router.push({path: 'Product'})">
        关于我们
      </el-menu-item>
      <el-menu-item index="3" @click="$router.push({path: 'Product'})">
        作品大全
      </el-menu-item>
      <el-menu-item index="4" @click="$router.push({path: 'Product'})">
        自助投稿
      </el-menu-item>
      <el-menu-item index="5" @click="$router.push({path: 'Product'})">
        联系我们
      </el-menu-item>
      <el-input
        v-model="search"
        class="search"
        placeholder="请输入内容"
        prefix-icon="el-icon-search"
        size="medium"
      />
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'NavMenu',
  data () {
    return {
      activeIndex: '1',
      search: ''
    }
  },
  methods: {
  }
}
</script>

<style scoped>
.logo {
  width: 200px;
  height: 60px;
  float: left;
}
.logo-img {
  margin-top: 5px;
}
.header{
  top:0;
  position: sticky;
  background-color: #001E1E;
  opacity: 0.8;
  z-index: 999;
}
.nav {
  border: black;
  text-align: center;
  margin: 0 320px;
}
.search {
  width: 200px;
  float: right;
  margin-top: 12px;
}
</style>
