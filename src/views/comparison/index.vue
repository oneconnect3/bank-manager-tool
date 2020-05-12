<template>
  <div class="prod_info" style="margin-left:10px; margin-top: 15px; margin-right: 10px">
    <el-select v-model="bank.bank1" placeholder="本行">
      <el-option label="发行银行" value="不限"></el-option>
      <el-option label="中国银行" value="中国银行"></el-option>
      <el-option label="招商银行" value="招商银行"></el-option>
      <el-option label="华夏银行" value="华夏银行"></el-option>
      <el-option label="平安银行" value="平安银行"></el-option>
      <el-option label="民生银行" value="民生银行"></el-option>
      <el-option label="建设银行" value="建设银行"></el-option>
      <el-option label="广州农商" value="广州农商"></el-option>
      <el-option label="农业银行" value="农业银行"></el-option>
      <el-option label="交通银行" value="交通银行"></el-option>
      <el-option label="兴业银行" value="兴业银行"></el-option>
      <el-option label="晋商银行" value="晋商银行"></el-option>
      <el-option label="工商银行" value="工商银行"></el-option>
      <el-option label="吉林银行" value="吉林银行"></el-option>
      <el-option label="青岛银行" value="青岛银行"></el-option>
    </el-select>

    <el-select v-model="bank.bank2" placeholder="对标行">
      <el-option label="发行银行" value="不限"></el-option>
      <el-option label="中国银行" value="中国银行"></el-option>
      <el-option label="招商银行" value="招商银行"></el-option>
      <el-option label="华夏银行" value="华夏银行"></el-option>
      <el-option label="平安银行" value="平安银行"></el-option>
      <el-option label="民生银行" value="民生银行"></el-option>
      <el-option label="建设银行" value="建设银行"></el-option>
      <el-option label="广州农商" value="广州农商"></el-option>
      <el-option label="农业银行" value="农业银行"></el-option>
      <el-option label="交通银行" value="交通银行"></el-option>
      <el-option label="兴业银行" value="兴业银行"></el-option>
      <el-option label="晋商银行" value="晋商银行"></el-option>
      <el-option label="工商银行" value="工商银行"></el-option>
      <el-option label="吉林银行" value="吉林银行"></el-option>
      <el-option label="青岛银行" value="青岛银行"></el-option>
    </el-select>

    <el-button type="primary" round @click="onsubmit();">一键对比</el-button>

    <el-card class="box-card" v-if="showResults" style="margin-top: 10px">
      <div slot="header" class="clearfix">
          <div style="margin-bottom: 20px">
        <span>产品结构对比结果：</span>
          </div>
        <el-row>
          <el-col :span="12">
            <el-card>
              <span>{{ test_val }}</span>
            </el-card>
          </el-col>
          <el-col :span="12">
            <el-card>
              <span>{{ test_val }}</span>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </el-card>
  </div>
</template>


<style>
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
      bank: {
        bank1: "",
        bank2: ""
      },
      test_val: ""
    };
  },

  methods: {
    onsubmit() {
      var prod = this;
      // var that = this;
      // 对应 Python 提供的接口，这里的地址填写下面服务器运行的地址，本地则为127.0.0.1，外网则为 your_ip_address
      const path = "http://127.0.0.1:5000/getCmp";
      axios
        .post(path, prod.bank)
        .then(response => {
          var rs = response.data.msg;
          prod.test_val = rs;

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
