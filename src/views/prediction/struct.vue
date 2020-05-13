<template>
  <el-main>
    <el-tabs v-model="activeName" type="border-card" @tab-click="handleClick">
      <el-tab-pane label="第一步" name="firstTab">
        <div>
          <div style="margin-top: 20px">
            <span>参数1：</span>
            <el-select v-model="args.arg1" placeholder="请选择" style="width: 200px">
              <el-option label="招商银行" value="招商银行"></el-option>
              <el-option label="光大银行" value="光大银行"></el-option>
              <el-option label="兴业银行" value="兴业银行"></el-option>
              <el-option label="平安银行" value="平安银行"></el-option>
            </el-select>
          </div>
          <div style="margin-top: 20px">
            <span>参数2：</span>
            <el-select v-model="args.arg2" placeholder="请选择" style="width: 200px">
              <el-option label="招商银行" value="招商银行"></el-option>
              <el-option label="光大银行" value="光大银行"></el-option>
              <el-option label="兴业银行" value="兴业银行"></el-option>
              <el-option label="平安银行" value="平安银行"></el-option>
            </el-select>
          </div>

          <el-button type="primary" @click="firstBtn();" style="margin-top: 30px">下一步</el-button>
        </div>
      </el-tab-pane>
      <el-tab-pane label="第二步" name="secondTab">
                  <div style="margin-top: 20px">
            <span>参数3：</span>
            <el-select v-model="args.arg3" placeholder="请选择" style="width: 200px">
              <el-option label="招商银行" value="招商银行"></el-option>
              <el-option label="光大银行" value="光大银行"></el-option>
              <el-option label="兴业银行" value="兴业银行"></el-option>
              <el-option label="平安银行" value="平安银行"></el-option>
            </el-select>
          </div>
        <div style="margin-top: 20px">
          <span>参数4：</span>
          <el-input v-model="input" placeholder="请输入内容" style="width: 200px"></el-input>
        </div>
        <el-button type="primary" @click="secondBtn();" style="margin-top: 30px">下一步</el-button>
      </el-tab-pane>
      <el-tab-pane label="第三步" name="thirdTab">
        <div style="margin-top: 20px">
          <span>参数5：</span>
          <el-checkbox v-model="checked">备选项</el-checkbox>
        </div>
        <div style="margin-top: 20px">
          <span>参数6：</span>
          <el-checkbox v-model="checked">备选项</el-checkbox>
        </div>        
        <el-button type="primary" @click="subBtn();" style="margin-top: 30px">提交</el-button>
      </el-tab-pane>
      <el-tab-pane label="结果" name="result" href="#result">
        <div style="margin-top: 20px">
          <span> {{ result }}</span>
        </div>
      </el-tab-pane>      
    </el-tabs>
  </el-main>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      activeName: "firstTab",
      args: {
        arg1: "",
        arg2: "",
        arg3: ""
      },
      result: ""
    };
  },
  methods: {
    firstBtn() {
      this.activeName = "secondTab";

    },

    secondBtn() {
      this.activeName = "thirdTab";
    },

    subBtn() {
      this.activeName = "result";
      var prod = this;
      // var that = this;
      // 对应 Python 提供的接口，这里的地址填写下面服务器运行的地址，本地则为127.0.0.1，外网则为 your_ip_address
      const path = "http://127.0.0.1:5000/getPred";
      axios
        .post(path, prod.args)
        .then(response => {
          var rs = response.data;
          prod.result = rs.args;

        })
        .catch(function(error) {
          alert("Error " + error);
        });       
    }
  }
};
</script>