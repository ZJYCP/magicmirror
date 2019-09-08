const WSS_URL = `ws://127.0.0.1:8081`
let Socket = ''
let lockReconnect = false  //避免重复连接
/**建立连接 */
export function createSocket() {
    if (!Socket||Socket.readyState===3) {
        console.log('正在建立websocket连接')
        Socket = new WebSocket(WSS_URL)
        Socket.onopen = onopenWS
        Socket.onmessage = onmessageWS
        Socket.onerror = onerrorWS
        Socket.onclose = oncloseWS
    } else {
        console.log(Socket);
        console.log('websocket已连接')
    }
}

/**打开WS之后发送心跳 */
export function onopenWS() {
    heartCheck.reset().start()
    console.log("websocket连接成功!" + new Date().toUTCString());
}

/**连接失败重连 */
export function onerrorWS() {
    // console.log('websocket错误,正在断开重连' + new Date().toUTCString())
    // Socket.close()
    // reconnect()
}

/**关闭WS */
export function oncloseWS() {
    Socket.close()
    reconnect()
    console.log('websocket已断开,启动重连' + new Date().toUTCString())
}

/**WS数据接收统一处理 */
export function onmessageWS(e) {
    heartCheck.reset().start();
    let receData
    if (e.data !== 'pong') {
        if ((e.data).indexOf('Logout')===1){
            Socket.close()
            // '主动关闭'
            return
        }
        receData = e

    } else {
        receData = '心跳返回'
    }
    window.dispatchEvent(new CustomEvent('onmessageWS', {
        detail: {
            data: receData
        }
    }))
}

/**发送数据
 * @param eventType
 */
export function sendWSPush(eventTypeArr) {
    const obj = {
        appId: 'airShip',
        cover: 0,
        event: eventTypeArr
    }
    if (Socket !== null && Socket.readyState === 3) {
        Socket.close()
        createSocket() //重连
    } else if (Socket.readyState === 1) {
        Socket.send(JSON.stringify(obj))
    } else if (Socket.readyState === 0) {
        setTimeout(() => {
            Socket.send(JSON.stringify(obj))
        }, 3000)
    }
}



export function closeWs(){
    Socket.send('quit')
}

let heartCheck = {
    timeout: 5000,
    timeoutObj: null,
    serverTimeoutObj: null,
    reset() {
        clearTimeout(this.timeoutObj)
        clearTimeout(this.serverTimeoutObj)
        return this;
    },
    start() {
        var _this = this
        this.timeoutObj = setTimeout(() => {
            Socket.send('ping');
            _this.serverTimeoutObj = setTimeout(() => {
                Socket.close
            }, _this.timeout)
        }, this.timeout)
    }
}


function reconnect() {
    if (lockReconnect) return
    lockReconnect = true
    setTimeout(() => {
        createSocket()
        lockReconnect = false
    }, 2000)
}
