import pandas as pd
dfp=pd.read_excel('PizzaSheet.xlsx')
print(dfp)
print(dfp.shape)

dfc=pd.read_csv('IthacaDailyClimate2018.csv')
print(dfc)
print(dfc.head())
dfc.columns
