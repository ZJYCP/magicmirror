<?php

namespace App\Http\Controllers\Api;

use App\Enviroment;
use Illuminate\Http\Request;
use Log;

class MicroController extends Controller
{
    //

    /**
     *
     */
    public function temp(Request $request)
    {

        Log::info('insert enviroment data');
//        $app = app('wechat.official_account');
//
//
////        $res=$app->template_message->getPrivateTemplates();
//        $res=$app->template_message->send([
//            'touser' => 'oLCjis0yxRyqcoeMGbC57g-BQiKY',
//            'template_id' => 'ywUbmiyxDXBMD13qsv7yNTqW7kNQK_hXyRfbmog-U-c',
//            'url' => 'https://blog.emx6.com',
//            'scene' => 1000,
//            'data' => [
//                'temp' => '23.3',
//                'level' => 'high',
//        ],
//    ]);
//        dd($res);

//        $ress=Enviroment::all();
        $envData=$request->post();
        $enviroment=new Enviroment;

        $enviroment->fill($envData);

        if($enviroment->save()){
            return $this->success('新增环境数据成功 ');
        }else{
            return $this->failed('有错误');
        }

    }
}
