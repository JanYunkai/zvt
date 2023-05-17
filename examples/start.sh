#!/bin/bash

BASEDIR=/home/yunkai/workspace/zvt
PYTHONPATH=$BASEDIR/examples:$BASEDIR/src
export PYTHONPATH

start(){
    nohup python $BASEDIR/examples/data_runner/actor_runner.py > /dev/null 2>&1 &
    nohup python $BASEDIR/examples/data_runner/finance_runner.py > /dev/null 2>&1 &
    nohup python $BASEDIR/examples/data_runner/index_runner.py > /dev/null 2>&1 &
    # nohup python $BASEDIR/examples/data_runner/joinquant_kdata_runner.py > /dev/null 2>&1 &
    nohup python $BASEDIR/examples/data_runner/kdata_runner.py > /dev/null 2>&1 &
    nohup python $BASEDIR/examples/data_runner/sina_data_runner.py > /dev/null 2>&1 &
    nohup python $BASEDIR/examples/data_runner/trading_runner.py > /dev/null 2>&1 &
    nohup python $BASEDIR/examples/reports/report_bull.py > /dev/null 2>&1 &
    nohup python $BASEDIR/examples/reports/report_tops.py > /dev/null 2>&1 &
    nohup python $BASEDIR/examples/reports/report_vol_up.py > /dev/null 2>&1 &
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