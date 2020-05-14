<template>
  <div class="dashboard-container">
    <panel-group/>
    <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:16px;">
      <el-card class="box-card" >
        <line-chart :chart-data="lineChartData"/>
      </el-card>
    </el-row>
    <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:16px;">
      <el-card class="box-card" >
        <bar-chart :chart-data="barChartData"/>
      </el-card>
    </el-row>
    <el-row :gutter="40" style="background:#fff;padding:16px 16px 0;margin-bottom:16px;">
      <el-col :xs="8" :sm="8" :lg="8" class="card-panel-col">
        <el-card class="box-card" >
          <pie-chart :chart-data="pieChartData1"/>
        </el-card>
      </el-col>
      <el-col :xs="8" :sm="8" :lg="8" class="card-panel-col">
        <el-card class="box-card" >
          <pie-chart :chart-data="pieChartData2"/>
        </el-card>
      </el-col>
      <el-col :xs="8" :sm="8" :lg="8" class="card-panel-col">
        <el-card class="box-card" >
          <pie-chart :chart-data="pieChartData3"/>
        </el-card>
      </el-col>
    </el-row>
    
    <!-- <div class="dashboard-text">name: {{ name }}</div> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import PanelGroup from './components/PanelGroup'
import LineChart from './components/LineChart'
import BarChart from './components/BarChart'
import PieChart from './components/PieChart'

const lineChartData = {
  prod1:[200, 192, 120, 144, 160, 130, 140],
  prod2:[180, 160, 151, 106, 145, 150, 130],
  prod3:[120, 82, 91, 154, 162, 140, 145],
  prod4:[130, 140, 141, 142, 145, 150, 160]
};
const barChartData = {
    bankNames:["招商银行","光大银行","兴业银行","平安银行","浙商银行","民生银行","浦发银行","中信银行","广发银行","华夏银行"],
    prodData:[
    {name:"结构性存款",data:[6,2,2,7,3,3,4,10,8,5]},
    {name:"大额存单",data:[17,4,15,5,1,1,10,7,6,6]},
    {name:"定期存款",data:[2,4,3,2,10,1,9,4,5,6]},
    {name:"外币理财",data:[2,1,20,2,5,5,4,6,7,8]},
    {name:"活期理财",data:[5,2,20,1,16,20,7,5,17,15]},
    {name:"贵金属理财",data:[3,2,18,17,15,12,17,14,11,2]},
    {name:"权益类理财",data:[10,3,10,9,2,6,17,15,2,15]}
    ]
};
const pieChartData1 = {
    title:'日分布',
    legendData:['固定收益类','权益类','衍生品类','混合类'],
    seriesData:[
      {name:'结构性存款',value:10},
      {name:'权益类',value:8},
      {name:'衍生品类',value:14},
      {name:'混合类',value:16}
      ]
};
const pieChartData2 = {
    title:'月分布',
    legendData:['固定收益类','权益类','衍生品类','混合类'],
    seriesData:[
      {name:'固定收益类',value:10},
      {name:'权益类',value:8},
      {name:'衍生品类',value:14},
      {name:'混合类',value:16}
      ]
};
const pieChartData3 = {
    title:'年分布',
    legendData:['固定收益类','权益类','衍生品类','混合类'],
    seriesData:[
      {name:'固定收益类',value:10},
      {name:'权益类',value:8},
      {name:'衍生品类',value:14},
      {name:'混合类',value:16}
      ]
};

export default {
  name: 'Dashboard',
  components: { 
    PanelGroup,
    LineChart,
    BarChart,
    PieChart
  },
  data() {
    return {
      lineChartData,
      barChartData,
      pieChartData1,
      pieChartData2,
      pieChartData3
    }
  },
  // created() {
  //   this.fetchData()
  // },

  computed: {
    ...mapGetters([
      'name'
    ])
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
