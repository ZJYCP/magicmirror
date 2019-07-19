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
    import { createSocket, sendWSPush } from './api/websocket'

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
                websock: null,
            }
        },
        created(){
            // this.initWebSocket();

        },
        mounted(){
            createSocket() //创建
            sendWSPush(11111) //发送数据
            //监听ws数据响应
            const getDataFunc = function(e) {
                console.log('11');
                console.log(e.detail.data)
            }
            window.addEventListener('onmessageWS', getDataFunc)

            //根据需要，销毁事件监听
            window.removeEventListener('onmessageWS', getDataFunc)
        },
        methods:{

            // initWebSocket(){ //初始化weosocket
            //     const wsuri = "ws://127.0.0.1:8081";
            //     this.websock = new WebSocket(wsuri);
            //     this.websock.onmessage = this.websocketonmessage;
            //     this.websock.onopen = this.websocketonopen;
            //     this.websock.onerror = this.websocketonerror;
            //     this.websock.onclose = this.websocketclose;
            // },
            // websocketonopen(){ //连接建立之后执行send方法发送数据
            //     let actions = {"test":"12345"};
            //     this.websocketsend(JSON.stringify(actions));
            // },
            // websocketonerror(){//连接建立失败重连
            //     this.initWebSocket();
            // },
            // websocketonmessage(e){ //数据接收
            //     console.log(e.data);
            //     // const redata = JSON.parse(e.data);
            //     const redata = e.data;
            // },
            // websocketsend(Data){//数据发送
            //     this.websock.send(Data);
            // },
            // websocketclose(e){  //关闭
            //     console.log('断开连接',e);
            // },
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
