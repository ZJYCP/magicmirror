<template>
    <div>
        <div class="envir">
            <div class="title">室内环境</div>
            <p>室内温度 4℃</p>
            <p>湿度 78%</p>
            <p>噪声强度 50dB</p>
            <p>光照强度 1000Lux</p>
        </div>
        <div class="emer">
            <div class="title">异常情况</div>
            <p>于8月10日05时9分检测到火焰</p>
            <p>于8月11日18时2分检测到烟雾</p>
            <p>于8月12日03时37分检测到异常人物走动</p>

        </div>
    </div>
</template>

<script>
export default {
    name: "home",
    methods: {
        get_data(){

        }
    }
}
</script>

<style scoped lang="scss">

    .envir {

    }

    .emer {
        p {
            color: red;
        }
    }

    p {
        margin: 0;
    }

    .title {
        font-size: .3rem;
        font-weight: bold;
    }
</style>
