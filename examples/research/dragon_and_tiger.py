# -*- coding: utf-8 -*-

import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from zvt.api.selector import get_big_players, get_player_success_rate
from zvt.domain import DragonAndTiger
from zvt.utils import next_date, current_date

if __name__ == "__main__":
    provider = "em"
    DragonAndTiger.record_data(provider=provider)
    end_timestamp = next_date(current_date(), -60)
    # recent year
    start_timestamp = next_date(end_timestamp, -400)
    print(f"{start_timestamp} to {end_timestamp}")
    players = get_big_players(start_timestamp=start_timestamp, end_timestamp=end_timestamp)
    print(players)
    df = get_player_success_rate(
        start_timestamp=start_timestamp, end_timestamp=end_timestamp, intervals=[3, 5, 10], players=players
    )
    print(df)
