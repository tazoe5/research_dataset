import sys, os
from pathlib import Path
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from tqdm import tqdm
ts_minute = 60
ts_hour = 60*60
ts_day = 24 * ts_hour
ts_week = 7 * ts_day
DATASET_PATH = Path('~/research_other/dataset/copenhagen_network').expanduser()
DATA_NAME = ['bt_symmetric.csv', 'calls.csv', 'sms.csv', 'fb_friends.csv', 'genders.csv']
PROCESSED_BLUETOOTH_DIR = DATASET_PATH/'processed'/'bluetooth_proximity_weeks'

def remove_duplicated(df: pd.DataFrame) -> pd.DataFrame:
    df_users = df[['user_a', 'user_b']].get_values()
    num_items = len(df_users)
    bools = [True for _ in np.arange(len(df_users))] # 重複が確認されたら False
    for i in np.arange(num_items):
        if bools[i] == False:
            continue
        ai, bi = df_users[i]
        for j in np.arange(i+1, num_items):
            if bools[j] == False:
                continue
            aj, bj = df_users[j]
            if (ai==aj and bi==bj) or (ai==bj and bi==aj):
                bools[j] = False
    df_unduplicated = df[bools]
    return df_unduplicated

four_hour = ts_hour*4
d = 1
plt.figure(figsize=(10, 13))

for (i, path) in enumerate(PROCESSED_BLUETOOTH_DIR.iterdir()):
    week = pd.read_csv(path)
    counters = []
    blocks = np.arange(int(np.ceil(ts_week / four_hour)))
    for block in tqdm(blocks):
        start = block*four_hour + i*ts_week
        end = start + four_hour
        bins = week.query('@start < timestamp <= @end')
        bins = remove_duplicated(bins)
        counters.append(len(bins))
    plt.subplot(4, 1, i+1)
    plt.title(f'week{i+1}')
    # 目盛りの設定
    for x in np.arange(0, 43, 6):
        plt.plot([x, x], [0, 60000], linestyle='-.', alpha=0.7, color='black')
    for x in np.arange(0, 40, 6):
        plt.plot([x+3, x+3], [0, 60000], linestyle=':', alpha=0.5, color='red')        
    plt.xticks(np.arange(0, 43, 3), labels)
    plt.plot(blocks, counters)
plt.suptitle('bluetooth proximity')
plt.show()

print(f'1時間: {ts_hour}, 1日: {ts_day}, 1週間：　{ts_week}, 全期間：　{4*ts_week}')
