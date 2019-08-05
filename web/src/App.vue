<template>
    <div id="app">
        <date-time class="date-time"></date-time>
        <weather class="weather"></weather>
        <home class="home"></home>
        <news class="news"></news>
    </div>
</template>

<script>
    import dateTime from './components/DateTime'
    import weather from './components/weather'
    import home from './components/home'
    import news from './components/news'
    import { createSocket, sendWSPush ,closeWs} from './api/websocket'

    export default {
        name: 'app',
        components: {
            dateTime,
            weather,
            home,
            news
        },
        data(){
            return{
            }
        },
        created(){

        },

        mounted(){
            window.onbeforeunload = e => {
                //根据需要，销毁事件监听
                window.removeEventListener('onmessageWS', getDataFunc)
                closeWs()
            };

            createSocket() //创建
            sendWSPush(11111) //发送数据

            //监听ws数据响应
            const getDataFunc = function(e) {
                console.log(e.detail.data)
            }
            window.addEventListener('onmessageWS', getDataFunc)


        },
        methods:{

        }
    }
</script>

<style lang="scss">
    body {
        margin: 0;
    }

    #app {
        width: 100%;
        height: 100vh;
        background-color: black;
        color: white;

        .date-time {
            display: inline-block;
            margin-left: .2rem;
            position: relative;
            top:.2rem
        }

        .weather {
            display: inline-block;
            width: 5rem;
            float: right;
            position: relative;
            top: .2rem;
        }

        .home {
            /*width: ;*/
            position: relative;
            top: 30%;
            margin-left: .2rem;
        }

        .news{
            position: absolute;
            bottom: 1rem;
            width: 100%;
            /*top: 0;*/
        }

    }
</style>
