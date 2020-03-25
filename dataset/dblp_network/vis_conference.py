from pathlib import Path
import json
# from zipfile import ZipFile
import pandas as pd
import numpy as np
from tqdm import tqdm

DATA_PATH = Path('./processing_data/size200/').expanduser()
if not DATA_PATH.is_dir():
    raise ValueError

pvis_str = ''
eurovis_str = ''
tvcg_str = ''
print(f'#FILE: {len(list(DATA_PATH.iterdir()))}')
for d_path in tqdm(DATA_PATH.iterdir()):
    with d_path.open() as f:
        lines = f.readlines()
    for line in lines:
        paper = json.loads(line)
        try:
            venue = paper['venue']
            raw = venue['raw']
        except KeyError:
            continue
        '''
        if 'pacific visualization' in raw:
            pvis_str += line
        elif 'EuroVis' in raw:
            eurovis_str += line
        '''
        if 'IEEE Transactions on Visualization and Computer Graphics' == raw:
            tvcg_str += line
# 保存処理
SAVE_DIR = Path('./processing_data/vis_papers').expanduser()
if not SAVE_DIR.is_dir():
    print('保存先ディレクトリが見つかりません.')
    SAVE_DIR.mkdir(parents=True)
TVCG_FILE = 'tvcg_papers.json'
TVCG_PATH = SAVE_DIR/TVCG_FILE
TVCG_PATH.write_text(tvcg_str)
'''
PVIS_FILE = 'pvis_papers.json'
EUROVIS_FILE = 'eurovis_papers.json'
PVIS_PATH = SAVE_DIR/PVIS_FILE
EUROVIS_PATH = SAVE_DIR/EUROVIS_FILE
PVIS_PATH.write_text(pvis_str)
EUROVIS_PATH.write_text(eurovis_str)
'''
