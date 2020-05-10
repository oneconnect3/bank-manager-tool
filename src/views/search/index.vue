<template>
  <div class="prod_info" style="margin-top: 15px;">
    <el-input placeholder="输入产品关键字" v-model="search_keyword.prod_name">
      <el-select v-model="search_keyword.bank_name" slot="prepend" placeholder="发行银行">
        <el-option label="中国银行" value="中国银行"></el-option>
        <el-option label="民生银行" value="民生银行"></el-option>
      </el-select>
      <el-select
        v-model="search_keyword.prod_type"
        slot="prepend"
        style="margin-left: 15px;"
        placeholder="投资类型"
      >
        <el-option label="结构型" value="结构型"></el-option>
        <el-option label="混合型" value="混合型"></el-option>
      </el-select>
      <el-select
        v-model="search_keyword.prod_return"
        slot="prepend"
        style="margin-left: 15px;"
        placeholder="收益率(%)"
      >
        <el-option label="1.5%以下" value="1.5%以下"></el-option>
        <el-option label="1.5%~2%" value="1.5%~2%"></el-option>
        <el-option label="2%~2.5%" value="2%~2.5%"></el-option>
        <el-option label="2.5%~3%" value="2.5%~3%"></el-option>
        <el-option label="3%~3.5%" value="3%~3.5%"></el-option>
        <el-option label="3.5%~4%" value="3.5%~4%"></el-option>
        <el-option label="4%~4.5%" value="4%~4.5%"></el-option>
        <el-option label="4.5%~5%" value="4.5%~5%"></el-option>
        <el-option label="5%以上" value="5%以上"></el-option>
      </el-select>
      <el-select
        v-model="search_keyword.duration"
        slot="prepend"
        style="margin-left: 50px;"
        placeholder="产品期限(月)"
      >
        <el-option label="3个月以下" value="3个月以下"></el-option>
        <el-option label="3~6个月" value="3~6个月"></el-option>
        <el-option label="6~12个月" value="6~12个月"></el-option>
        <el-option label="12个月以上" value="12个月以上"></el-option>
      </el-select>
      <el-button slot="append" icon="el-icon-search" @click="onsubmit();"></el-button>
    </el-input>

    <el-card class="box-card" v-if="showResults">
      <div slot="header" class="clearfix">
        <span>搜索结果</span>
      </div>
      <div>{{ serverResponse }}</div>
      <el-table :data="prod_list" stripe border fit>
        <el-table-column prop="name" label="产品名称" width="350"></el-table-column>
        <el-table-column prop="bank" label="发行银行" width="200"></el-table-column>
        <el-table-column prop="type" label="投资类型" width="200"></el-table-column>
        <el-table-column prop="profit" label="预期收益率" width="200"></el-table-column>
        <el-table-column prop="duration" label="产品期限" width="200"></el-table-column>
        <el-table-column prop="detail" label="查看详情" width="200"></el-table-column>        
      </el-table>
    </el-card>
  </div>
</template>

<style>
.el-select .el-input {
  width: 130px;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
</style>

<script>
import axios from "axios";

export default {
  data() {
    return {
      showResults: false,
      // bank_name: "",
      // prod_type: "",
      // prod_return: "",
      // if_sale: "",
      search_keyword: {
        bank_name: "",
        prod_type: "",
        prod_return: "",
        duration: "",
        prod_name: "",
        detail: ""
      },
      serverResponse: "",
      prod_list: []
    };
  },

  methods: {
    onsubmit() {
      var prod = this;
      // var that = this;
      // 对应 Python 提供的接口，这里的地址填写下面服务器运行的地址，本地则为127.0.0.1，外网则为 your_ip_address
      const path = "http://127.0.0.1:5000/getProd";
      axios
        .post(path, prod.search_keyword)
        .then(response => {
          // 这里服务器返回的 response 为一个 json object，可通过如下方法需要转成 json 字符串
          // 可以直接通过 response.data 取key-value
          // 坑一：这里不能直接使用 this 指针，不然找不到对象
          // var msg = response.data.msg.price;

          // 坑二：这里直接按类型解析，若再通过 JSON.stringify(msg) 转，会得到带双引号的字串
          // prod.serverResponse = msg;

          var rs = response.data.msg;
          prod.prod_list = rs;

          // alert(
          //   "Success " + response.status + ", " + response.data + ", " + msg
          // );
        })
        .catch(function(error) {
          alert("Error " + error);
        });
      this.showResults = true;
    }
  }
};
</script>
