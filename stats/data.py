import os
import glob
import pandas as pd
import numpy as np
os.chdir('../games/')
game_files = glob.glob('*.EVE')
list.sort(game_files)
counter = 0
game_frames=[]
while counter < len(game_files):
    path = game_files[counter]
    names = ['type','multi2','multi3','multi4','multi5','multi6','event']
    game_frame = pd.read_csv(path, names = names)
    game_frames.append(game_frame)
    counter = counter + 1
games = pd.concat(game_frames, ignore_index = True)
games['multi5'] = games['multi5'].replace("??", np.NaN)
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
identifiers = identifiers.fillna(method='ffill')
identifiers.columns=(['game_id','year'])
games = pd.concat([games, identifiers], axis=1, sort=False)
games = games.fillna('')
games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])
print (games.head())
