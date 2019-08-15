import pandas as pd
import glob
from scipy import stats
import numpy as np
import functionTools as tools


# import and dataframe cleaning
"""appendData = []
cleanData = pd.DataFrame(columns=['Series', 'Tournament', 'Round', 'B365W', 'B365L', 'Year', 'Spread'])
for f in list(glob.glob('/Users/emmanuelmakonga/Desktop/projet/tennis/data/20*.xls*')):
    try:
        tempData = pd.read_excel(f)
        yearFile = tools.extractNumberFromString(f)
        tempData['Year'] = ''.join(yearFile)
        tempData = tempData[['Series', 'Tournament', 'Round', 'B365W', 'B365L', 'Year']]
        tempData['Spread'] = tempData['B365W'] - tempData['B365L']
        tempData['OWin'] = np.where(tempData['Spread']>=0, 'Yes', 'No')
        appendData.append(tempData)
    except:
        pass

cleanData = pd.concat(appendData)
cleanData = cleanData.reset_index(drop=True)"""

cleanData = pd.read_excel('cleanData.xlsx')

#args
OddMax= 3 #test by year
#by year
"""for t in cleanData['Year'].unique():
    #filter
    data = cleanData[cleanData['Year'] == t]
    data = data[(data['B365W'] < OddMax) & (data['B365L'] < OddMax)]

    #check if when odds are at .50 difference outisder win or not
    spreadData = pd.DataFrame(columns=['thresholdSpread', 'freq', 'nbOutWin', 'nbOutLoss'])
    x = np.arange(0.05, OddMax, .05)
    for i in x:
        tempData = data[(data['Spread'] <= i) & (data['Spread'] > -i)]
        spreadData = spreadData.append({'thresholdSpread' : i, 'freq' : float(len(tempData[tempData['OWin'] == 'Yes']))/float(len(tempData)), 'nbOutWin' : len(tempData[tempData['OWin'] == 'Yes']), 'nbOutLoss': len(tempData[tempData['OWin'] == 'No']), 'WinOddAvg' : np.mean(tempData['B365W']) }, ignore_index=True)

    #xlpath = t + '_spreadData.xlsx'
    #spreadData.to_excel(xlpath)"""

#by series
"""for s in cleanData['Series'].unique():
    # filter
    data = cleanData[cleanData['Series'] == s]
    data = data[(data['B365W'] < OddMax) & (data['B365L'] < OddMax)]

    # check if when odds are at .50 difference outisder win or not
    spreadData = pd.DataFrame(columns=['thresholdSpread', 'freq', 'nbOutWin', 'nbOutLoss'])
    x = np.arange(0.05, OddMax, .05)
    for i in x:
        tempData = data[(data['Spread'] <= i) & (data['Spread'] > -i)]
        spreadData = spreadData.append(
            {'thresholdSpread': i, 'freq': float(len(tempData[tempData['OWin'] == 'Yes'])) / float(len(tempData)),
             'nbOutWin': len(tempData[tempData['OWin'] == 'Yes']), 'nbOutLoss': len(tempData[tempData['OWin'] == 'No']),
             'WinOddAvg': np.mean(tempData['B365W'])}, ignore_index=True)

    #xlpath = s + '_spreadData.xlsx'
    #spreadData.to_excel(xlpath)"""

#by round
"""for r in cleanData['Round'].unique():
    # filter
    data = cleanData[cleanData['Round'] == r]
    data = data[(data['B365W'] < OddMax) & (data['B365L'] < OddMax)]

    # check if when odds are at .50 difference outisder win or not
    spreadData = pd.DataFrame(columns=['thresholdSpread', 'freq', 'nbOutWin', 'nbOutLoss'])
    x = np.arange(0.05, OddMax, .05)
    for i in x:
        tempData = data[(data['Spread'] <= i) & (data['Spread'] > -i)]
        spreadData = spreadData.append(
            {'thresholdSpread': i, 'freq': float(len(tempData[tempData['OWin'] == 'Yes'])) / float(len(tempData)),
             'nbOutWin': len(tempData[tempData['OWin'] == 'Yes']), 'nbOutLoss': len(tempData[tempData['OWin'] == 'No']),
             'WinOddAvg': np.mean(tempData['B365W'])}, ignore_index=True)

    #xlpath = r + '_spreadData.xlsx'
    #spreadData.to_excel(xlpath)"""