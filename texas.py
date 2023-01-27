import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

#Accessing data from API endpoint
api_url = "http://api.eia.gov/series/?api_key=9UJ2btvdkqq7jjkc8NMV79JsZa8hsdY4RBsFjPct&series_id=EBA.ERCO-ALL.NG.WND.HL"
response = requests.get(api_url)
x = response.json()

#create a Pandas 2 dimensional data frame and rename the columns
df = pd.DataFrame(x['series'][0]['data'])
df = df.rename(columns = {0:"Month", 1:"Value"})

#data manipulation
df.sort_values(by=['Month'],ascending=True,inplace=True)
df['Month_new'] = df['Month'].astype(str).str[4:6]
df.drop('Month',axis=1,inplace=True)
df = df.rename(columns = {"Month_new":"Month"})
new_df = df.groupby(['Month']).mean().reset_index()

# plot bar chart 
new_df.plot.bar(x = "Month", y = "Value", color = "r")
plt.title("Texas Wind Energy By Month")
plt.xlabel("Month")
plt.ylabel("Energy Level")
plt.xticks(rotation = 0)
