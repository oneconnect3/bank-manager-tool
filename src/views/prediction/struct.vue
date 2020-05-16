<template>
  <el-main>
    <div>
      <div style="margin-top: 20px;">
        <div>
          <p>请选择您的银行，根据你的输入，我们将自动匹配您所在银行的规模，大小，成立年限等数据，以达更精准的预测效果。</p>
        </div>
        <span>银行：</span>
        <el-select v-model="args.arg1" placeholder="平安银行" style="width: 200px">
          <el-option label="农业银行" value="农业银行"></el-option>
          <el-option label="中信银行" value="中信银行"></el-option>
          <el-option label="交通银行" value="交通银行"></el-option>
          <el-option label="兴业银行" value="兴业银行"></el-option>
          <el-option label="宁波银行" value="宁波银行"></el-option>
          <el-option label="华夏银行" value="华夏银行"></el-option>
          <el-option label="招商银行" value="招商银行"></el-option>
          <el-option label="上海银行" value="上海银行"></el-option>
          <el-option label="平安银行" value="平安银行"></el-option>
          <el-option label="工商银行" value="工商银行"></el-option>
          <el-option label="中国银行" value="中国银行"></el-option>
          <el-option label="建设银行" value="建设银行"></el-option>
          <el-option label="民生银行" value="民生银行"></el-option>
          <el-option label="杭州银行" value="杭州银行"></el-option>
          <el-option label="广州农商" value="广州农商"></el-option>
        </el-select>
      </div>
      <!-- <div style="margin-top: 20px">
            <span>参数2：</span>
            <el-select v-model="args.arg2" placeholder="请选择" style="width: 200px">
              <el-option label="招商银行" value="招商银行"></el-option>
              <el-option label="光大银行" value="光大银行"></el-option>
              <el-option label="兴业银行" value="兴业银行"></el-option>
              <el-option label="平安银行" value="平安银行"></el-option>
            </el-select>
      </div>-->
    </div>

    <div style="margin-top: 20px">
      <span>预计收益率（%）：</span>
      <el-input v-model="args.arg2" placeholder="请输入内容"></el-input>
    </div>
    <div style="margin-top: 20px">
      <span>起投金额（RMB）：</span>
      <el-input v-model="args.arg3" placeholder="请输入内容"></el-input>
    </div>
    <div style="margin-top: 20px">
      <span>产品期限（月）：</span>
      <el-input v-model="args.arg4" placeholder="请输入内容"></el-input>
    </div>
    <el-button type="primary" @click="subBtn();" style="margin-top: 30px">提交</el-button>

    <div style="margin-top: 20px" v-if="showResults">
      <div>
        <p>根据您指定的相关参数，预估该产品将在 {{ pred_rs }} 个月内售罄。</p>
      </div>
      <el-row>
        <el-col :span="8">
          <div class="grid-content bg-purple">
            <ve-line :data="chartData1" :settings="chartSettings1"></ve-line>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="grid-content bg-purple-light">
            <ve-line :data="chartData2" :settings="chartSettings2"></ve-line>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="grid-content bg-purple">
            <ve-line :data="chartData3" :settings="chartSettings3"></ve-line>
          </div>
        </el-col>
      </el-row>
    </div>
  </el-main>
</template>

<script>
import axios from "axios";
import VCharts from "v-charts";

export default {
  data() {
    this.chartSettings1 = {
      stack: {},
      xAxisName: ["预计收益率（%）"],
      // yAxisName: ["售罄时长（月）"],
    };    
    this.chartSettings2 = {
      stack: {},
      xAxisName: ["起投金额（RMB）"],
      // yAxisName: ["售罄时长（月）"]
    };  
    this.chartSettings3 = {
      stack: {},
      xAxisName: ["产品期限（月）"],
      // yAxisName: ["售罄时长（月）"]
    };          
    return {
      showResults: false,
      pred_rs: "",
      args: {
        arg1: "",
        arg2: 6,
        arg3: 6,
        arg4: 6
      },
      result: "",
      chartData1: {
        columns: [],
        rows: []
      },
      chartData2: {
        columns: [],
        rows: []
      },
      chartData3: {
        columns: [],
        rows: []
      }
    };
  },
  methods: {
    subBtn() {
      this.showResults = true;
      var prod = this;
      // var that = this;
      // 对应 Python 提供的接口，这里的地址填写下面服务器运行的地址，本地则为127.0.0.1，外网则为 your_ip_address
      const path = "http://127.0.0.1:5000/getPred";
      axios
        .post(path, prod.args)
        .then(response => {
          var rs = response.data;
          prod.pred_rs = rs.result.origin_y;
          prod.chartData1.columns = ['预计收益率（%）', '售罄时长（月）'];
          prod.chartData1.rows = rs.result.rate_series;
          prod.chartData2.columns = ['起投金额（RMB）', '售罄时长（月）'];
          prod.chartData2.rows = rs.result.start_amount_series;
          prod.chartData3.columns = ['产品期限（月）', '售罄时长（月）'];
          prod.chartData3.rows = rs.result.term_series;
          // alert(prod.chartData1.rows)
        })
        .catch(function(error) {
          alert("Error " + error);
        });
    }
  }
};
</script>