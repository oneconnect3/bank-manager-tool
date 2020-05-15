<template>
  <el-main>
    <span>&nbsp 请选择产品：</span>
    <el-select v-model="bank.bank1" placeholder="本行">
      <el-option label="招商银行" value="招商银行"></el-option>
      <el-option label="光大银行" value="光大银行"></el-option>
      <el-option label="兴业银行" value="兴业银行"></el-option>
      <el-option label="平安银行" value="平安银行"></el-option>
      <el-option label="浙商银行" value="浙商银行"></el-option>
      <el-option label="民生银行" value="民生银行"></el-option>
      <el-option label="浦发银行" value="浦发银行"></el-option>
      <el-option label="中信银行" value="中信银行"></el-option>
      <el-option label="广发银行" value="广发银行"></el-option>
      <el-option label="华夏银行" value="华夏银行"></el-option>
    </el-select>
    <span>&nbsp&nbsp&nbsp&nbsp 预测天数：</span>
    <el-select v-model="bank.bank2" placeholder="对标行">
      <el-option label="招商银行" value="招商银行"></el-option>
      <el-option label="光大银行" value="光大银行"></el-option>
      <el-option label="兴业银行" value="兴业银行"></el-option>
      <el-option label="平安银行" value="平安银行"></el-option>
      <el-option label="浙商银行" value="浙商银行"></el-option>
      <el-option label="民生银行" value="民生银行"></el-option>
      <el-option label="浦发银行" value="浦发银行"></el-option>
      <el-option label="中信银行" value="中信银行"></el-option>
      <el-option label="广发银行" value="广发银行"></el-option>
      <el-option label="华夏银行" value="华夏银行"></el-option>
    </el-select>&nbsp&nbsp&nbsp&nbsp
    <el-button type="primary" @click="onsubmit();">一键预测</el-button>
    <div style="margin-top: 20px"></div>
  </el-main>
</template>


<style>
</style>

<script>
import axios from "axios";
import VCharts from "v-charts";

export default {
  data() {
    this.chartSettings0 = {
      stack: {},
      yAxisName: ["占比（%）"]
    };
    this.chartExtend = {
      series: {
        barMaxWidth: 150
      },
      toolip: {
        trigger: "axis",
        formatter(params) {
          for (x in params) {
            return params[x].x + "%";
          }
        }
      }
    };
    this.chartSettings1 = {
      metrics: [],
      dimension: ["类别"],
      xAxisName: [""],
      yAxisName: ["占比（%）"]
    };
    return {
      showResults: false,
      bank: {
        bank1: "",
        bank2: ""
      },
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
    onsubmit() {
      var prod = this;
      // var that = this;
      // 对应 Python 提供的接口，这里的地址填写下面服务器运行的地址，本地则为127.0.0.1，外网则为 your_ip_address
      const path = "http://127.0.0.1:5000/getPred";
      axios
        .post(path, prod.bank)
        .then(response => {
          var rs = response.data;
          this.chartSettings0.stack = rs.stack_dict;
          this.chartSettings1.metrics = rs.bank_names;
          prod.chartData1.columns = rs.struct_columns;
          prod.chartData1.rows = rs.struct_data;
          prod.chartData2.columns = rs.interest_columns;
          prod.chartData2.rows = rs.interest_data;
          prod.chartData3.columns = rs.contract_columns;
          prod.chartData3.rows = rs.contract_data;
          // alert(
          //   "Success " + response.status + ", " + response.data + ", " + msg
          // );
        })
        .catch(function(error) {
          alert("Error " + error);
        });
      this.showResults = true;
    },
    downloadWithCSS() {
      const doc = new jsPDF();
      /** WITH CSS */
      var canvasElement = document.createElement("canvas");
      html2canvas(this.$refs.content, { canvas: canvasElement }).then(function(
        canvas
      ) {
        const img = canvas.toDataURL("image/jpeg", 1.0);
        doc.addImage(img, "JPEG", 0.5, 2);
        doc.save("sample.pdf");
      });
    }
  },
  mounted: function() {
    this.onsubmit();
  }
};
</script>
