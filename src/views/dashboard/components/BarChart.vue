<template>
    <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from './mixins/resize'

export default {
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '350px'
    },
    autoResize: {
      type: Boolean,
      default: true
    },
    chartData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      chart: null
    }
  },
  watch: {
    chartData: {
      deep: true,
      handler(val) {
        this.setOptions(val)
      }
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart()
    })
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')
      this.setOptions(this.chartData)
    },
    setOptions( {bankNames,prodData} = {}) {
    // setOptions( chartData = {}) {
    // var bankNames = chartData.map(obj=>obj.bankName);
    // var prodNames = Object.keys(chartData[0].data)
    // var prodSeries = prodNames.map(
    //     prodName=>({
    //             name:prodName,
    //             type: 'bar',
    //             stack:'销量',
    //             data:cD2.map(obj=>obj.data[prodName]),
    //             animationDuration: 2000
    //              })
    // )
    // setOptions({ dataSeries1,dataSeries2} = {}) {
      var prodNames = prodData.map(prod=>prod.name);
      this.chart.setOption({
        xAxis: {
          type: 'category',
          data: bankNames,
          boundaryGap: true,
          axisTick: {
            alignWithLabel: true
          }
        },
        legend: {
        data: prodNames,
        },
        grid: {
          left: 10,
          right: 10,
          bottom: 20,
          top: 30,
          containLabel: true
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        yAxis: {
          axisTick: {
            show: false
          }
        },
        series: prodData.map(prod=>(
            {
            name:prod.name,
            type: 'bar',
            stack:'销量',
            barWidth: '30%',
            data:prod.data,
            animationDuration: 1500,
            label: {
            show: true,
            position: 'inside'}
            }
            )
        )



        
      })
    }
  }
}
</script>