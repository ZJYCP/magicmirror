<?php

namespace App\Http\Controllers\Api;

use App\Enviroment;
use Illuminate\Http\Request;
use Log;

class MicroController extends Controller
{
    //

    /**
     * 温度、湿度、噪声强度数据新增
     * @param Request $request
     * @return mixed
     */
    public function temp(Request $request)
    {

        Log::info('insert enviroment data');

        $envData = $request->post();
        if (count($envData) != 3) {
            return $this->failed('数据错误', 400, 1003);
        }
        $enviroment = new Enviroment;

        $enviroment->fill($envData);

        if ($enviroment->save()) {
            return $this->success('新增环境数据成功 ');
        } else {
            return $this->failed('有错误');
        }

    }


    /**
     * @param $type
     * @return mixed
     */
    public function alarm($type)
    {
        $app = app('wechat.official_account');

        if($type=='infrared'){
            $res = $app->template_message->send([
                'touser' => 'oLCjis0yxRyqcoeMGbC57g-BQiKY',
                'template_id' => 'ywUbmiyxDXBMD13qsv7yNTqW7kNQK_hXyRfbmog-U-c',
                'url' => 'https://blog.emx6.com',
                'scene' => 1000,
                'data' => [
                    'temp' => '23.3',
                    'level' => 'high',
                ],
            ]);
            if($res['errcode']==0){
                Log::info('send infrared alarm successfully');
                return $this->success('红外模板消息发送成功');
            }
        }

    }
}
