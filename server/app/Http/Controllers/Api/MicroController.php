<?php

namespace App\Http\Controllers\Api;

use App\Device;
use App\Enviroment;
use Illuminate\Http\Request;
use Log;

class MicroController extends Controller
{
    //

    function __construct()
    {
    }


    /**
     * 获取符合条件的用户列表
     * @param int $device_id
     * @return mixed
     */
    private function getUserOpenid($device_id = 520)
    {
        return Device::select('user_id')->where('device_id', $device_id)->get();
    }

    /**
     * 发送微信模板消息
     * @param $touser
     * @param $template_id
     * @param $data
     * @return mixed
     */
    private function send_template($touser, $template_id, $data)
    {
        $app = app('wechat.official_account');

        $res = $app->template_message->send([
            'touser' => $touser,
            'template_id' => $template_id,
            'url' => 'https://blog.emx6.com',
            'scene' => 1000,
            'data' => $data
        ]);

        return $res;
    }

    /**
     * 温度、湿度、噪声强度数据新增
     * @param Request $request
     * @return mixed
     */
    public function temp(Request $request)
    {

        Log::info('insert enviroment data');

        $envData = $request->post();
        Log::info($envData);
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
     * 警报
     * @param $type
     * @return mixed
     */
    public function alarm($type)
    {


        $users = $this->getUserOpenid(520);
        if ($type == 'infrared') {

            //触发广播事件
            event(new \App\Events\PushAlarmEvent(['time'=>time(),'alarmType'=>$type]));

            $template_id = 'ywUbmiyxDXBMD13qsv7yNTqW7kNQK_hXyRfbmog-U-c';
            $data = [
                'temp' => '23.3',  //TODO 从数据库拿
                'level' => date('Y-m-d h:i:s', time()),
            ];
            $res_flag = 1;
            foreach ($users as $value) {
                $res = $this->send_template($value['user_id'], $template_id, $data);
                if ($res['errcode'] != 0) {
                    $res_flag = 0;
                }
            }

            if ($res_flag){
                Log::info('send infrared alarm successfully');

                return $this->success('红外模板消息发送成功'.'共有'.count($users).'人');
            }else{
                return $this->failed('模板发送失败',400,1002);
            }
        }

    }

    public function get_data()
    {

    }
}
