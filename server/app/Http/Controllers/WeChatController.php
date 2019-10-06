<?php

namespace App\Http\Controllers;

use Log;

class WeChatController extends Controller
{
    public function serve()
    {
        Log::info('request arrived');

        $app = app('wechat.official_account');
        $app->server->push(function ($message) {
            return "欢迎关注魔镜";
        });

        return $app->server->serve();

    }
}
