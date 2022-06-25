# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))
print(sys.path)

# nohup python examples/recorders/eastmoney_data_runner1.py > /dev/null 2>&1 &
# nohup python examples/recorders/eastmoney_data_runner2.py > /dev/null 2>&1 &
# nohup python examples/recorders/em_data_runner.py > /dev/null 2>&1 &
# nohup python examples/recorders/sina_data_runner.py > /dev/null 2>&1 &