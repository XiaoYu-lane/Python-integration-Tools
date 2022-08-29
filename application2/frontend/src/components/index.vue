<template>
  <div>
    <el-container>
      <el-header>
        <el-row>
          <el-col :span="24">
            <div class="grid-content bg-purple-dark">
              <el-menu
                :default-active="activeIndex"
                class="el-menu-demo"
                mode="horizontal"
              >
                <el-menu-item index="1">漏洞工具</el-menu-item>
                <el-submenu index="2">
                  <template slot="title">网络爬虫</template>
                  <el-menu-item index="2-1">图片爬取</el-menu-item>
                </el-submenu>
                <el-menu-item index="3">CMS识别</el-menu-item>
                <el-menu-item index="4">信息收集工具</el-menu-item>
              </el-menu>
            </div>
          </el-col>
        </el-row>
      </el-header>
      <el-main>Main</el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Index",
  data() {
    return {};
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
