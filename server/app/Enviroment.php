<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Enviroment extends Model
{
    //

    /**
     * 可以被批量赋值的属性。
     *
     * @var array
     */
    protected $fillable = ['temp','humid','sound'];
}
