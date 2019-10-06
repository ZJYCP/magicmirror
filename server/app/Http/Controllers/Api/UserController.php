<?php

namespace App\Http\Controllers\Api;

use App\Enviroment;
use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use Log;

class UserController extends Controller
{
    //

    public function index()
    {

        Log::info('api-users');
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

        $ress=Enviroment::all();
        dd($ress);

    }
}
