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
    setOptions({ prod1,prod2,prod3,prod4 } = {}) {
    // setOptions({ prod1,prod2} = {}) {
      this.chart.setOption({
        xAxis: {
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
          boundaryGap: true,
          axisTick: {
            show: false
          }
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
            type: 'cross'
          },
          padding: [5, 10]
        },
        yAxis: {
          axisTick: {
            show: false
          }
        },
        legend: {
        //   data: ['固定收益类','权益类']
          data: ['固定收益类','权益类','衍生品类','混合类']
        },
        series: [
            {
                name: '固定收益类',
                itemStyle: {
                    normal: {
                    // color: "#2ec7c9",
                    lineStyle: {
                        // color: '#2ec7c9',
                        width: 2
                    }
                    }
                },
                smooth: true,
                type: 'line',
                data: prod1,
                animationDuration: 2800,

            },
            {
                name: '权益类',
                smooth: true,
                type: 'line',
                itemStyle: {
                normal: {
                    // color: '#b6a2de',
                    lineStyle: {
                    // color: '#b6a2de',
                    width: 2
                    },
                }
                },
                data: prod2,
                animationDuration: 2800,

            },
        {
            name: '衍生品类',
            smooth: true,
            type: 'line',
            itemStyle: {
                normal: {
                // color: '#5ab1ef',
                lineStyle: {
                    // color: '#5ab1ef',
                    width: 2
                }
                }
            },
            data: prod3,
            animationDuration: 2800,
        },
        {
            name: '混合类',
            smooth: true,
            type: 'line',
            itemStyle: {
                normal: {
                // color: '#ffb980',
                lineStyle: {
                    // color: '#ffb980',
                    width: 2
                }
                }},
            data: prod4,
            animationDuration: 2800,
        }
    ]
      })
    }
  }
}
</script>
