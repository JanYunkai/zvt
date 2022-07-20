# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../examples")))


# nohup python examples/data_runner/actor_runner.py > /dev/null 2>&1 &
# nohup python examples/data_runner/finance_runner.py > /dev/null 2>&1 &
# nohup python examples/data_runner/index_runner.py > /dev/null 2>&1 &
# nohup python examples/data_runner/joinquant_kdata_runner.py > /dev/null 2>&1 &
# nohup python examples/data_runner/kdata_runner.py > /dev/null 2>&1 &
# nohup python examples/data_runner/sina_data_runner.py > /dev/null 2>&1 &
# nohup python examples/data_runner/trading_runner.py > /dev/null 2>&1 &