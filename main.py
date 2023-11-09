
import pandas as pd
import os
import numpy as np
import Levenshtein

def read_excel_sheets(file_path):
    xls = pd.ExcelFile(file_path)
    data_frames = []
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)
        data_frames.append(df)
    return pd.concat(data_frames, ignore_index=True)

df_2014 = read_excel_sheets('bus_2014.xlsx')
df_2015 = read_excel_sheets('bus_2015.xlsx') 
df_2016 = read_excel_sheets('bus_2016.xlsx') 
df_2017 = read_excel_sheets('bus_2017.xlsx') 
df_2018 = read_excel_sheets('bus_2018.xlsx')
df_2018 = df_2018.iloc[:, :-1]
df_2019 = read_excel_sheets('bus_2019.xlsx')
df_2019 = df_2019.iloc[:, :-3]
df_2020 = read_excel_sheets('bus_2020.xlsx')
df_2020 = df_2020.iloc[:, :-3]
df_2020.rename(columns={'Gap': 'Min Gap', 'Delay': 'Min Delay'}, inplace=True)
df_2021 = read_excel_sheets('bus_2021.xlsx')
df_2021.rename(columns={'Date': 'Report Date'}, inplace=True)
df_2021 = df_2021.iloc[:, :-3]
df_2022 = read_excel_sheets('bus_2022.xlsx')
df_2022.rename(columns={'Date': 'Report Date'}, inplace=True)

bus_delay_list = [df_2014,df_2015,df_2016,df_2017,df_2018,df_2019,df_2020,df_2021,df_2022]
df_bus_delay = pd.concat(bus_delay_list)

df_bus_delay['YTime'] = pd.to_datetime(df_bus_delay['Time'], format='%H:%M:%S', errors='coerce').dt.strftime('%H:%M')
df_bus_delay['DateTime'] = df_bus_delay['Report Date'].dt.strftime('%Y-%m-%d')+'-'+ df_bus_delay['YTime']
df_bus_delay['DateTime'] = pd.to_datetime(df_bus_delay['DateTime'])

drop_columns = ['YTime','Time','Report Date','Direction']
df_bus_delay = df_bus_delay.drop(drop_columns, axis = 1)
df_bus_delay = df_bus_delay.dropna(subset=['Route'])

df_bus_delay['copy'] = df_bus_delay['Location'].str.lower()
df_bus_delay['copy'] = df_bus_delay['copy'].str.replace('vp','victoria park')
df_bus_delay['copy'] = df_bus_delay['copy'].str.replace(' to ','$').str.replace('b/w','').str.replace('w/b','').str.replace('e/b','').str.replace('s/b','').str.replace('n/b','')
df_bus_delay['copy'] = df_bus_delay['copy'].str.replace('stn','station').str.replace(' and ','&').str.replace('/','&').str.replace(' ','')
df_bus_delay['copy'] = df_bus_delay['copy'].astype(str)
df_bus_delay = df_bus_delay[~df_bus_delay['copy'].str.isdigit()]
df_bus_delay['copy'] = df_bus_delay['copy'].apply(lambda x: '&'.join(sorted(x.split('&'))) if x.count('&') == 1 else x)

stops = pd.read_csv('stops.txt')
stops['cleaned_stops'] = stops['stop_name'].str.replace('at', '&').str.replace('Rd', '').str.replace('Ave', '').str.replace('Dr', '').str.replace('St', '')
stops['cleaned_stops'] = stops['cleaned_stops'].str.replace(' ', '').str.lower()

def compute_similarity(string1, string2):
    distance = Levenshtein.distance(string1, string2)
    max_length = max(len(string1), len(string2))
    if max_length == 0:
        return 100
    else:
        return 100 - (distance / max_length) * 100
    
def synchronize_locations_ls(location, reference_list):
    # 1) create an array with the similarity scores between the location and each entry in reference list
    similarity_scores = []
    for item in reference_list:
        string=str(item)
        print(location)
        print(string)
        print(compute_similarity(location[0], string))
        similarity_scores.append(compute_similarity(location, string))
    # 2) find the highest score in this list
    max_score = max(similarity_scores)
    # 3) if the score is above the threshold, return the string from the list that corresponds to the highest score
    interpolated = reference_list[similarity_scores.index(max_score)] if max_score <= 70 else "user check"
    return interpolated

np_copy = list(df_bus_delay['copy'])
np_stops = list(stops['cleaned_stops'])

synchronized_values = synchronize_locations_ls(np_copy, np_stops)
df_bus_delay['synchronized'] = synchronized_values