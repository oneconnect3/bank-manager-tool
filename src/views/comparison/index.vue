<template>
  <el-main>
    <span>&nbsp 请选择本行：</span>
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
    <span>&nbsp&nbsp&nbsp&nbsp 对标行：</span>
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
    <el-button type="primary" @click="onsubmit();">一键对比</el-button>
    <el-button @click="download">Download PDF</el-button>

    <div ref="content" style="margin-top: 20px">
      <el-row type="flex">
        <el-col :span="12">
          <el-card shadow="hover">
            <div slot="header" class="clearfix">
              <span>产品结构对比</span>
            </div>
            <ve-histogram :data="chartData1" :settings="chartSettings0" :extend="chartExtend"></ve-histogram>
          </el-card>
        </el-col>
        <el-col :span="12">
          <el-card shadow="hover">
            <div slot="header" class="clearfix">
              <span>卡片名称</span>
            </div>
            <div v-for="o in 4" :key="o" class="text item">{{'列表内容 ' + o }}</div>
          </el-card>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <el-card shadow="hover">
            <div slot="header" class="clearfix">
              <span>产品利率对比</span>
            </div>
            <ve-histogram :data="chartData2" :settings="chartSettings1"></ve-histogram>
          </el-card>
        </el-col>
        <el-col :span="12">
          <el-card shadow="hover">
            <span>结论</span>
          </el-card>
        </el-col>
      </el-row>

      <el-row type="flex">
        <el-col :span="12">
          <el-card shadow="hover">
            <div slot="header" class="clearfix">
              <span>产品期限对比</span>
            </div>
            <ve-histogram :data="chartData3" :settings="chartSettings1"></ve-histogram>
          </el-card>
        </el-col>
        <el-col :span="12">
          <el-card shadow="hover">
            <span>结论</span>
          </el-card>
        </el-col>
      </el-row>
    </div>
  </el-main>
</template>


<style>
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
</style>

<script>
import axios from "axios";
import VCharts from "v-charts";
import jsPDF from "jspdf";
import html2canvas from "html2canvas";

export default {
  data() {
    this.chartSettings0 = {
      stack: {},
      series: [
        {
          barWidth: 10
        }
      ],
      yAxisName: ["占比（%）"]
    };
    this.chartExtend = {
      series: {
        barMaxWidth: 150
      },
      dataZoom: [
        {
          type: "inside"
        }
      ]
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
      const path = "http://127.0.0.1:5000/getCmp";
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
        const img = canvas.toDataURL("image/jpeg", 0.8);
        doc.addImage(img, "JPEG", 20, 20);
        doc.save("sample.pdf");
      });
    },
    download() {
      const doc = new jsPDF();
      /** WITHOUT CSS */
      const contentHtml = this.$refs.content.innerHTML;
      doc.fromHTML(contentHtml, 15, 15, {
        width: 170
      });
      doc.save("sample.pdf");
    }
  },
  mounted: function() {
    this.onsubmit();
  }
};
</script>
