import sys, os
from pathlib import Path
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
DATASET_PATH = Path('~/research_other/dataset/copenhagen_network').expanduser()
DATA_NAME = ['bt_symmetric.csv', 'calls.csv', 'sms.csv', 'fb_friends.csv', 'genders.csv']

data = [bt_data, calls_data, sms_data, fb_data, genders_data] = \
    [pd.read_csv(str(DATASET_PATH/d_n)) for d_n in DATA_NAME]
facebook_processed = fb_data.rename(columns={'# user_a': 'user_a'})


save_path = DATASET_PATH/'processed'/'facebook'
save_path.mkdir(parents=True, exist_ok=True)

print(f'save dir: {str(save_path)}')
print('file_name...')
fname = f'data.csv'
print(fname)
facebook_processed.to_csv(save_path/fname)
print('done')
    
