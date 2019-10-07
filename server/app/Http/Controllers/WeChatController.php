<?php

namespace App\Http\Controllers;

use function GuzzleHttp\Psr7\str;
use Log;

class WeChatController extends Controller
{

    /**************************************************************
     *
     *  将数组转换为JSON字符串（兼容中文）
     *  @param  array   $array      要转换的数组
     *  @return string      转换得到的json字符串
     *  @access public
     *
     *************************************************************/
    function JSON($array) {
        $this->arrayRecursive($array, 'urlencode', true);
        $json = json_encode($array);
        return urldecode($json);
    }


    public function serve()
    {
        Log::info('request arrived');

        $app = app('wechat.official_account');

        $app->server->push(function ($message) {
            switch ($message['MsgType']) {
                case 'event':
                    return '收到事件消息';
                    break;
                case 'text':
                    if(strstr($message['Content'],'绑定')){
                        $pattern="/([^#]+)$/";
                        preg_match($pattern,$message['Content'],$deviceId);
                        $bind_res=$this->bindDevice($deviceId[0],$message['FromUserName']);
                        return $bind_res;
                    }
                    break;
                case 'image':
                    return '收到图片消息';
                    break;
                case 'voice':
                    return '收到语音消息';
                    break;
                case 'video':
                    return '收到视频消息';
                    break;
                case 'location':
                    return '收到坐标消息';
                    break;
                case 'link':
                    return '收到链接消息';
                    break;
                case 'file':
                    return '收到文件消息';
                default:
                    return '收到其它消息';
                    break;
            }
        });
        return $app->server->serve();
    }


    public function bindDevice($device_id,$user_openid){
        return '绑定设备号为'.$device_id.'的魔镜成功';
    }
}
