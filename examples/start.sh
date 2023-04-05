#!/bin/bash

BASEDIR=/home/yunkai/workspace/zvt
PYTHONPATH=$BASEDIR/examples:$BASEDIR/src
export PYTHONPATH

start(){
    nohup python $BASEDIR/examples/data_runner/actor_runner.py > /dev/null 2>&1 & \
    nohup python $BASEDIR/examples/data_runner/finance_runner.py > /dev/null 2>&1 & \
    nohup python $BASEDIR/examples/data_runner/index_runner.py > /dev/null 2>&1 & \
    # nohup python $BASEDIR/examples/data_runner/joinquant_kdata_runner.py > /dev/null 2>&1 & \
    nohup python $BASEDIR/examples/data_runner/kdata_runner.py > /dev/null 2>&1 & \
    nohup python $BASEDIR/examples/data_runner/sina_data_runner.py > /dev/null 2>&1 & \
    nohup python $BASEDIR/examples/data_runner/trading_runner.py > /dev/null 2>&1 & \
    # recorders
    nohup python $BASEDIR/examples/recorders/eastmoney_data_runner1.py > /dev/null 2>&1 & \
    nohup python $BASEDIR/examples/recorders/eastmoney_data_runner2.py > /dev/null 2>&1 & \
    nohup python $BASEDIR/examples/recorders/em_data_runner.py > /dev/null 2>&1 & \
    nohup python $BASEDIR/examples/recorders/sina_data_runner.py > /dev/null 2>&1 & \
}

  
case "$1" in
    start)
    start
    ;;
    *)
    printf 'Usage: %s {start}\n'
    exit 1
    ;;
esac

exit "0"