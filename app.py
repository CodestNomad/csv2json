import pandas as pd

# read the csv data
df = pd.read_csv('data.csv')

# conver cvs to json
json_data = df.to_json(orient='records')

# save it to a file result.json
with open('result.json', 'w') as f:
    f.write(json_data)
