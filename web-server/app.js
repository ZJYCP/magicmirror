const Koa = require('koa');
const Router=require('koa-router');
const bodyParser = require('koa-bodyparser');
const app = new Koa();
const router=new Router();


//微信验证
router.get('/wx',async (ctx,next)=>{
    // console.log(ctx.query);
    const {signature,timestamp,nonce,echostr}=ctx.query
    //直接返回
    ctx.body=echostr
})

router.post('/wx',async (ctx,next)=>{
    console.log(ctx.request.body);
    ctx.body=ctx.request.body.echostr
})

app.use(bodyParser())
app.use(router.routes())
app.use(router.allowedMethods())

// 监听端口、启动程序
app.listen(3000, err => {
    if (err) throw err;
    console.log('runing...');
})
