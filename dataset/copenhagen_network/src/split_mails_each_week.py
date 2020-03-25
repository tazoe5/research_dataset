import sys, os
from pathlib import Path
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
DATASET_PATH = Path('~/research_other/dataset/copenhagen_network').expanduser()
DATA_NAME = ['bt_symmetric.csv', 'calls.csv', 'sms.csv', 'fb_friends.csv', 'genders.csv']

data = [bt_data, calls_data, sms_data, fb_data, genders_data] = \
    [pd.read_csv(str(DATASET_PATH/d_n)) for d_n in DATA_NAME]
# タイムスタンプ
ts_minute = 60
ts_hour = 60*60
ts_day = 24 * ts_hour
ts_week = 7 * ts_day
print(f'1時間: {ts_hour}, 1日: {ts_day}, 1週間：　{ts_week}, 全期間：　{4*ts_week}')


mails_processed = sms_data.rename(columns={'sender': 'user_a', 'recipient': 'user_b'})

week1 = mails_processed.query('0 < timestamp <= @ts_week')
week2 = mails_processed.query('@ts_week < timestamp <= 2*@ts_week')
week3 = mails_processed.query('@ts_week*2 < timestamp <= 3*@ts_week')
week4 = mails_processed.query('@ts_week*3 < timestamp <= 4*@ts_week')
weeks = [week1, week2, week3, week4]


save_path = DATASET_PATH/'processed'/'mails_weeks'
save_path.mkdir(parents=True, exist_ok=True)

print(f'save dir: {str(save_path)}')
print('file_name...')
for i, week in enumerate(weeks):
    i += 1
    fname = f'week{i}.csv'
    print(fname)
    week.to_csv(save_path/fname)
print('done')
    
