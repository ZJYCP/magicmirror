<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Device extends Model
{
    //

    /**
     * 可以被批量赋值的属性。
     *
     * @var array
     */
    protected $fillable = ['device_id','user_id'];
}
