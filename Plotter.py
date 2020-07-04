import urllib.request
import pandas as pd
with urllib.request.urlopen('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv') as f:
    #html = f.read().decode('utf-8')
    df = pd.read_csv(f, encoding = 'utf-8')
    df.to_csv("Current.csv", index = False)
    
