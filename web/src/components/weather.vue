<template>
    <div id="weather">
        <div class="title">今日天气</div>
        <div>{{wea}}</div>
        <div>当前温度:{{temp}}</div>
        <div>天气质量等级为{{air}}</div>
        <img class="weatherImg" src="/image/cloud.png" alt="">
        <div>紫外线{{radio.level}} {{radio.desc}}</div>
        <div>穿衣指数:{{cloth.desc}}</div>
        <div id="myChart"></div>
    </div>
</template>

<script>
    export default {
        name: "weather",
        data() {
            return {
                temp: '',
                wea: '',
                air: '',
                airtip:'',
                radio: '',
                cloth: '',
                tempToday:[]
            }
        },
        methods: {
            async getWeather() {
                this.tempToday=[]
                let res = await this.$http.get('https://www.tianqiapi.com/api/', 'version=v1&city=上海')
                let data=res.data[0]
                console.log(res.data[0]);
                [this.temp,this.wea,this.air,this.airtip,this.radio,this.cloth]=[data.tem,data.wea,data.air_level,data.air_tips,data.index[0],data.index[3]]
                data.hours.forEach((item)=>{
                    this.tempToday.push(parseInt((item.tem).replace('℃','')))
                })

                this.drawLine()
            },
            drawLine() {
                // 基于准备好的dom，初始化echarts实例
                let _this=this
                let myChart = this.$echarts.init(document.getElementById('myChart'))
                // 绘制图表
                myChart.setOption({
                    color: '#fff',
                    title: {
                        show:false,
                        text: '一日天气变化',
                        textStyle: {
                            color: '#fff'
                        }
                    },
                    tooltip: {},
                    grid: {
                        x: 50,
                        y: 25,
                        x2: 30,
                        y2: 35
                    },
                    xAxis: {
                        // boundaryGap: false,
                        axisLabel: {
                            color: '#fff'
                        },
                        axisLine: {
                            lineStyle: {
                                color: '#fff'
                            }
                        },
                        data: ["8时", "11", "14", "17", "20", "23", "02", "05"]
                    },
                    yAxis: {
                        min: 20,
                        interval: 4,
                        axisLabel: {
                            color: '#fff',
                            formatter: '{value} ℃'
                        },
                        axisLine: {
                            lineStyle: {
                                color: '#fff'
                            }
                        },
                    },
                    series: [{
                        name: '销量',
                        type: 'line',
                        smooth: true,
                        data: _this.tempToday,
                        markPoint: {
                            symbolSize: 30,

                            label: {
                                show: true,
                                color: '#ddd'
                            },
                            data: [
                                {
                                    type: 'max',
                                    name: '最大值',
                                    itemStyle:{
                                        color:'rgba(204,0,51,0.7)'
                                    },
                                },
                                {
                                    type: 'min',
                                    name: '最小值',
                                    itemStyle:{
                                        color:'rgba(0,153,255,0.6)'
                                    },
                                },
                            ]
                        }
                    }]
                });
                window.addEventListener('resize', function () {
                    myChart.resize()
                });

            }
        },
        created() {
            this.getWeather()
        },
        mounted() {

        }
    }
</script>

<style scoped lang="scss">
    #weather {
        font-size: .24rem;

        .weatherImg{
            height: 1.2rem;
            position: absolute;
            top: 0;
            right: .6rem;
        }
        .title {
            /*font-size: 4rem;*/
        }

        #myChart {
            height: 150px;
            width: 100%;
        }
    }

</style>
