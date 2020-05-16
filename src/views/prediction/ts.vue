<template>
  <el-main>
    <span>&nbsp 请选择产品：</span>
    <el-select v-model="pred_info.pred_prod" placeholder="搏弈BYAQKF280D">
      <el-option label="日日聚财(1401期)A19003" value="产品1"></el-option>
      <el-option label="翠竹同益3M对公10款(B)19期FGAB15044B" value="产品2"></el-option>
      <el-option label="成长2020年第74期" value="产品3"></el-option>
      <el-option label="安稳2020年第42期" value="产品4"></el-option>
      <el-option label="稳健成长(2020)88期" value="产品5"></el-option>
      <el-option label="合赢2020年第4期" value="产品6"></el-option>
      <el-option label="成长2020年第72期" value="产品7"></el-option>
      <el-option label="金翼宝942号" value="产品8"></el-option>
      <el-option label="安盈268号" value="产品9"></el-option>
      <el-option label="紫气东来稳健1292期" value="产品10"></el-option>
      <el-option label="漓江理财2020-52期" value="产品11"></el-option>
      <el-option label="创赢计划青鑫共享2020年186期" value="产品12"></el-option>
      <el-option label="蒙银财鑫20056期" value="产品13"></el-option>
      <el-option label="农银私行·安心得利·灵珑AD200210" value="产品14"></el-option>
      <el-option label="优选恒利1号2020年第19期" value="产品15"></el-option>
    </el-select>
    <span>&nbsp&nbsp&nbsp&nbsp 预测天数：</span>
    <el-input-number v-model="pred_info.pred_days" @change="handleChange" :min="1" :max="100" label="描述文字"></el-input-number>&nbsp&nbsp&nbsp&nbsp
    <el-button type="primary" @click="onsubmit();">一键预测</el-button>
    <div style="margin-top: 20px">
      <ve-line :data="chartData" :settings="chartSettings"></ve-line>
    </div>

  </el-main>
</template>


<style>
</style>

<script>
import axios from "axios";
import VCharts from "v-charts";

export default {
  data() {
    return {
      pred_info: {
          pred_prod: "产品1",
          pred_days: 5
      },
      chartData: {
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
      const path = "http://127.0.0.1:5000/getTS";
      axios
        .post(path, prod.pred_info)
        .then(response => {
          var rs = response.data;
          prod.chartData.columns = ['时间', '预测值', '置信下限', '置信上限'];
          prod.chartData.rows = rs.result;
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
