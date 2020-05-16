<template>
  <el-row :gutter="40" class="panel-group">
    <el-col :xs="8" :sm="8" :lg="8" class="card-panel-col">
      <el-card class="box-card" >
      <div class="card-panel">
        <div class="card-panel-icon-wrapper icon-day">
          <svg-icon icon-class="day" class-name="card-panel-icon" />
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
            今日新售
          </div>
          <count-to :start-val="0" :end-val="new_prod_day" :duration="2000" class="card-panel-num" />
        </div>
      </div>
      </el-card>
    </el-col>

    <el-col :xs="8" :sm="8" :lg="8" class="card-panel-col">
      <el-card class="box-card" >
      <div class="card-panel">
        <div class="card-panel-icon-wrapper icon-month">
          <svg-icon icon-class="week" class-name="card-panel-icon" />
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
            本周新售
          </div>
          <count-to :start-val="0" :end-val="new_prod_week" :duration="2000" class="card-panel-num" />
        </div>
      </div>
      </el-card>
    </el-col>

    <el-col :xs="8" :sm="8" :lg="8" class="card-panel-col">
      <el-card class="box-card" >
      <div class="card-panel">
        <div class="card-panel-icon-wrapper icon-total">
          <svg-icon icon-class="total" class-name="card-panel-icon" />
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
            目前在售
          </div>
          <count-to :start-val="0" :end-val="prod_total" :duration="2000" class="card-panel-num" />
        </div>
      </div>
      </el-card>
    </el-col>

  </el-row>
</template>

<script>
import CountTo from 'vue-count-to'

export default {
  components: {
    CountTo
  },
  data(){
    return {
      new_prod_day: 33,
      new_prod_week: 372,
      prod_total: 8536
    }
  },
  methods: {

  }
}
</script>

<style lang="scss" scoped>
.panel-group {
  margin-top: 18px;
  padding:16px 16px 0;

  .card-panel-col {
    margin-bottom: 32px;
  }

  .card-panel {
    height: 108px;
    cursor: pointer;
    font-size: 24 px;
    position: relative;
    overflow: hidden;

    .card-panel-icon-wrapper {
      float: left;
      margin: 14px 0 0 14px;
      padding: 16px;
      transition: all 0.38s ease-out;
      border-radius: 6px;
    }

    .card-panel-icon {
      float: left;
      font-size: 48px;
    }

    .card-panel-description {
      float: right;
      font-weight: bold;
      margin: 26px;
      margin-left: 0px;

      .card-panel-text {
        line-height: 18px;
        color: rgba(0, 0, 0, 0.45);
        font-size: 24px;
        margin-bottom: 24px;
      }

      .card-panel-num {
        font-size: 24px;
      }
    }
  }
}

@media (max-width:550px) {
  .card-panel-description {
    display: none;
  }

  .card-panel-icon-wrapper {
    float: none !important;
    width: 100%;
    height: 100%;
    margin: 0 !important;

    .svg-icon {
      display: block;
      margin: 14px auto !important;
      float: none !important;
    }
  }
}
</style>