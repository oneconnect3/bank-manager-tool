<template>
  <div class="prod_info" style="margin-top: 15px;">
    <el-input placeholder="输入产品关键字" v-model="search_keyword.key">
      <el-select v-model="bank_name" slot="prepend" placeholder="发行银行">
        <el-option label="招商银行" value="1"></el-option>
        <el-option label="平安银行" value="2"></el-option>
      </el-select>
      <el-select v-model="prod_type" slot="prepend" style="margin-left: 20px;" placeholder="投资类型">
        <el-option label="结构型" value="1"></el-option>
        <el-option label="混合型" value="2"></el-option>
      </el-select>
      <el-select
        v-model="prod_return"
        slot="prepend"
        style="margin-left: 20px;"
        placeholder="预期收益率"
      >
        <el-option label="3%以下" value="1"></el-option>
        <el-option label="3%~5%" value="2"></el-option>
        <el-option label="5%以上" value="3"></el-option>
      </el-select>
      <el-select v-model="if_sale" slot="prepend" style="margin-left: 20px;" placeholder="是否在售">
        <el-option label="是" value="1"></el-option>
        <el-option label="否" value="2"></el-option>
      </el-select>
      <el-button slot="append" icon="el-icon-search" @click="onsubmit();"></el-button>
    </el-input>

    <el-card class="box-card" v-if="showResults">
      <div slot="header" class="clearfix">
        <span>搜索结果</span>
      </div>
      <div>{{ serverResponse }}</div>
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
      search_keyword: {key:''},
      serverResponse: ""
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
          var msg = response.data.msg.price;
          // 坑二：这里直接按类型解析，若再通过 JSON.stringify(msg) 转，会得到带双引号的字串
          prod.serverResponse = msg;

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
