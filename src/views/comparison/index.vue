<template>
  <el-main>
    <span>&nbsp 请选择本行：</span>
    <el-select v-model="bank.bank1" placeholder="平安银行">
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
    <el-select v-model="bank.bank2" placeholder="招商银行">
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
    <el-button type="warning" @click="downloadWithCSS">下载报告</el-button>

    <div ref="content" style="margin-top: 50px">
      <el-row :gutter="26" style="display: flex; justify-content: center; align-items: center">
        <el-col :span="11">
          <el-card
            class="grid-content bg-purple"
            shadow="hover"
            style="height: 500px; background: #E2F0FA"
          >
            <div slot="header" class="clearfix">
              <span>产品结构对比</span>
            </div>
            <ve-histogram :data="chartData1" :settings="chartSettings0" :extend="chartExtend"></ve-histogram>
          </el-card>
        </el-col>
        <el-col :span="1">
          <i
            class="el-icon-d-arrow-right"
            style="display: flex; justify-content: center; font-size: 24px"
          ></i>
        </el-col>
        <el-col :span="11">
          <el-card
            class="grid-content bg-purple"
            shadow="hover"
            style="height: 500px; background: #FFEBDD"
          >
            <div slot="header" class="clearfix">
              <span>主要观察</span>
            </div>
            <div>
              <el-row>
                <el-tag>{{ insights.insight1_1_title }}</el-tag>
                <p>{{ insights.insight1_1 }}</p>
              </el-row>
              <el-row style="margin-top: 15px">
                <el-tag>{{ insights.insight1_2_title }}</el-tag>
                <p>{{ insights.insight1_2 }}</p>
                <p id="insight1_2"></p>
              </el-row>
              <el-row style="margin-top: 15px">
                <el-tag>{{ insights.insight1_3_title }}</el-tag>
                <p>{{ insights.insight1_3 }}</p>
              </el-row>
            </div>
          </el-card>
        </el-col>
      </el-row>
      <el-divider></el-divider>
      <el-row style="display: flex; justify-content: center; align-items: center" :gutter="26">
        <el-col :span="11">
          <el-card
            class="grid-content bg-purple"
            shadow="hover"
            style="height: 450px; background: #E2F0FA"
          >
            <div slot="header" class="clearfix">
              <span>产品利率对比</span>
            </div>
            <ve-histogram :data="chartData2" :settings="chartSettings1"></ve-histogram>
          </el-card>
        </el-col>
        <el-col :span="1">
          <i
            class="el-icon-d-arrow-right"
            style="display: flex; justify-content: center; font-size: 24px"
          ></i>
        </el-col>
        <el-col :span="11">
          <el-card
            class="grid-content bg-purple"
            shadow="hover"
            style="height: 450px; background: #FFEBDD"
          >
            <div slot="header" class="clearfix">
              <span>主要观察</span>
            </div>
            <div>
              <el-row>
                <el-tag>{{ insights.insight3_1_title }}</el-tag>
                <p>{{ insights.insight3_1 }}</p>
              </el-row>
              <el-row style="margin-top: 15px">
                <el-tag>{{ insights.insight3_2_title }}</el-tag>
                <p>{{ insights.insight3_2 }}</p>
              </el-row>
            </div>
          </el-card>
        </el-col>
      </el-row>
      <el-divider></el-divider>
      <el-row style="display: flex; justify-content: center; align-items: center" :gutter="26">
        <el-col :span="11">
          <el-card
            class="grid-content bg-purple"
            shadow="hover"
            style="height: 450px; background: #E2F0FA"
          >
            <div slot="header" class="clearfix">
              <span>产品期限对比</span>
            </div>
            <ve-histogram :data="chartData3" :settings="chartSettings1"></ve-histogram>
          </el-card>
        </el-col>
        <el-col :span="1">
          <i
            class="el-icon-d-arrow-right"
            style="display: flex; justify-content: center; font-size: 24px"
          ></i>
        </el-col>
        <el-col :span="11">
          <el-card
            class="grid-content bg-purple"
            shadow="hover"
            style="height: 450px; background: #FFEBDD"
          >
            <div slot="header" class="clearfix">
              <span>主要观察</span>
            </div>
            <div>
              <el-row>
                <el-tag>{{ insights.insight2_1_title }}</el-tag>
                <p>{{ insights.insight2_1 }}</p>
              </el-row>
              <el-row style="margin-top: 15px">
                <el-tag>{{ insights.insight2_2_title }}</el-tag>
                <p>{{ insights.insight2_2 }}</p>
              </el-row>
            </div>
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

.span {
  font-weight: bold;
}

p {
  line-height: 24px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.el-tag {
  font-weight: bold;
  font-size: 16px;
}

.clearfix {
  font-weight: bold;
  font-size: 18px;
}
</style>

<script src="../../assets/js/jquery-3.1.1.min.js"></script>

<script>
import axios from "axios";
import VCharts from "v-charts";
import jsPDF from "jspdf";
import html2canvas from "html2canvas";

export default {
  data() {
    this.grid = {
      show: true,
      top: 50,
      left: 10,
      backgroundColor: "#E2F0FA"
      // borderColor: '#000'
    };
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
      },
      insights: {}
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
          prod.insights = rs.insights;

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
      var bk = this;
      const doc = new jsPDF();
      /** WITH CSS */
      var canvasElement = document.createElement("canvas");
      // window.html2canvas = html2canvas;
      html2canvas(this.$refs.content, {
        canvas: canvasElement,
        scale: 0.4
      }).then(function(canvas) {
        const img = canvas.toDataURL("image/jpeg", 1);
        doc.addImage(img, "PNG", 5, 8);
        var bank1 = bk.bank.bank1;
        var bank2 = bk.bank.bank2;
        var timestamp = new Date().getTime();
        doc.save(bank1 + "_" + bank2 + "_银行对标报告_" + timestamp + ".pdf");
      });
    }
  },
  mounted: function() {
    this.onsubmit();
  }
};
</script>
