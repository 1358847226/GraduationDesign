<template>
  <div class="header">
    <el-menu
      :default-active="activeIndex2"
      class="el-menu-demo"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
    >
      <el-menu-item index="1" @click="$router.push({path: '/'})">主页</el-menu-item>
      <el-submenu index="2">
        <template slot="title">我的工作台</template>
        <el-menu-item index="2-1">选项1</el-menu-item>
        <el-menu-item index="2-2">选项2</el-menu-item>
        <el-menu-item index="2-3">选项3</el-menu-item>
        <el-submenu index="2-4">
          <template slot="title">选项4</template>
          <el-menu-item index="2-4-1">选项1</el-menu-item>
          <el-menu-item index="2-4-2">选项2</el-menu-item>
          <el-menu-item index="2-4-3">选项3</el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-menu-item index="3" @click="$router.push({path: 'Product'})">产品中心</el-menu-item>
    </el-menu>
  </div>

</template>

<script>
export default {
  name: 'NavMenu',
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1',
      childName: 'ChildIndex'
    }
  },
  methods: {
  }
}
</script>

<style scoped>
.header{
  top:0;
  position: sticky;
}
</style>
