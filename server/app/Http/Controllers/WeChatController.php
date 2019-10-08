<?php

namespace App\Http\Controllers;

use App\Device;
use Log;

class WeChatController extends Controller
{

    /**************************************************************
     *
     *  将数组转换为JSON字符串（兼容中文）
     * @param array $array 要转换的数组
     * @return string      转换得到的json字符串
     * @access public
     *
     *************************************************************/
    protected function JSON($array)
    {
        $this->arrayRecursive($array, 'urlencode', true);
        $json = json_encode($array);
        return urldecode($json);
    }

    /**
     * @param string $device_id 设备编号
     * @param string $user_openid 用户openid
     * @return string 回复信息
     */
    private function bindDevice($device_id, $user_openid)
    {
        if ($device_id != '520') {
            return '没有该编号的设备';
        }

        if (Device::where('user_id', $user_openid)->exists()) {
            return '该账号已绑定设备号为520的魔镜';// TODO：之后再改 编号写死
        }

        $device = Device::firstOrNew(['user_id' => $user_openid, 'device_id' => $device_id]);
        $res = $device->save();

        if ($res) {
            return '绑定设备号为' . $device_id . '的魔镜成功';
        } else {
            return '绑定失败';
        }
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
                    if (strstr($message['Content'], '绑定')) {

                        $pattern = "/([^#]+)$/";
                        preg_match($pattern, $message['Content'], $deviceId);
                        $bind_res = $this->bindDevice($deviceId[0], $message['FromUserName']);
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

}
