<template>
  <div class="container" id="app">
    <h3 style="text-align:center">动物森友会鱼类价格查询</h3>

    <div style="text-align:center">
      <el-input id="search-word" type="text" οnkeydοwn="jump(event);" placeholder />
      <el-button @click="getData">搜索</el-button>
    </div>
  </div>
</template>
