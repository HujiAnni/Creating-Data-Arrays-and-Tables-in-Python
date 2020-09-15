import pandas as pd
import numpy as np
dfc = pd.read_csv('IthacaDailyClimate2018.csv')

minvals=np.min(dfc)
print(minvals)

meanvals=np.mean(dfc)
print(meanvals)

sumvals=np.sum(dfc)
print(sumvals)

dfcdesc=dfc.describe()
print(dfcdesc)

print(dfc.quantile())
