#Downloading data using News API, opening the data file and converting a JSON file as a csv

#Download and save the API data as a JSON file, while using the terminal curl command:
#curl -o nyt.json "https://newsapi.org/v2/top-headlines?sources=the-new-york-times&apiKey=INSERT_YOUR_KEY"

#In the relevant directory, run the following script to convert to CSV (using Pandas):

import pandas as pd
df_json_raw = pd.read_json('nyt.json')

df_json = df_json_raw.apply( lambda x: pd.Series([x[0]['title'],x[0]['description'],x[0]['publishedAt']]), axis = 1 ) # Add variables as desired e.g. 'source'
df_json.columns=['Title','Description','Published At']               # Label columbs for csv file, to reflect variables (format as desired)

print (df_json)                                       # Show file in workspace

df_json.to_csv('nyt.csv')                            # Export json file as .csv
