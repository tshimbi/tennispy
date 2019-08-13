import pandas as pd
import glob
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

path = '/Users/emmanuelmakonga/Desktop/projet/tennis/data/2018.xlsx'

filenames=list(glob.glob('/Users/emmanuelmakonga/Desktop/projet/tennis/data/20*.xls*'))
#data = [pd.read_excel(filename) for filename in filenames]
data = pd.read_excel(filenames[2])
print(filenames[2])
print(data.columns)

data = data[data['Series'] == 'Grand Slam']
#data = data[(data['Round'] <> 'The Final') & (data['Round'] <> 'Semifinals')& (data['Round'] <> 'Quarterfinals') & (data['Round'] <> '4th Round') & (data['Round'] <> '3th Round')]

vectround = data['Round'].unique()

rootData= data

for i in rootData['Round'].unique():
    data = rootData.loc[rootData['Round'] == i]
    print(i)
    print('Nombre de match', len(data))
    #print(data.head())
    # winner spread
    data_fav_win = data[(data['B365W'] < data['B365L'])]
    data_out_win = data[(data['B365W'] > data['B365L'])]
    oddSpreadWin = abs(data_fav_win['B365W'] - data_fav_win['B365L'])
    oddSpreadSpecialWin = 1 / oddSpreadWin
    oddSpreadOut = abs(data_out_win['B365W'] - data_out_win['B365L'])
    oddSpreadSpecialOut = 1 / oddSpreadOut
    #stats
    #print('Ecart moyen Fav win : mean', round(np.mean(oddSpreadWin), 2))
    #print('Ecart moyen Out win : mean', round(np.mean(oddSpreadOut), 2))
    #sns.distplot(oddSpreadWin, hist=False, label='Winner')
    #sns.distplot(oddSpreadOut, hist=False, label='Outsider')
    #plt.savefig('imagedist.png')
    data_fav_win_xpd = data_fav_win.copy()
    data_fav_win_xpd.loc['oddSpread'] = oddSpreadWin
    data_out_win_xpd = data_out_win.copy()
    data_out_win_xpd.loc['oddSpread'] = oddSpreadOut
    #freq
    print('Frequence victoire outsider :', round(float(len(data_out_win))/float(len(data)), 2))
    print('cote moyenne :', round(np.mean(data_out_win['B365W']), 2))
    print('esperance :', round(float(len(data_out_win))/float(len(data))*np.mean(data_out_win['B365W'])-1, 2))