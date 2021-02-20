import numpy as np 
import pandas as pd 
import os 
import sys 
import requests
import json
import datetime
import time
from pandas.io.json import json_normalize 

Data = pd.read_csv('Tracks.csv')
Data = Data.drop('Unnamed: 0', axis = 1)
    
def getOneLine(id):
    token = 'BQAe39pMdB60gg_dsts7coC8lSkBRVqPyweAKnMNrOZizIF3k3gsNzNVrrfOrGcmbAz4wYpg5wdAGYikqsmftegnliY12vR6FO3LBaBzAEEYm7FCgRw-g9y19UJCyvqDWeiSVqbaPy_YKpSxX5z1Yn7yjUag5Myb-71rJdKy2IcGu_TmymvzcoqodqugCq9gHI-7BVwa1bsMqVUi8QBpQgeGiijyZ9DMuTecOUpyWE8dSO7bWZrshPUA666kJu0l1aGdgHcer6JXHAs'
    myID = '11dFghVXANMlKmJXsNCbNl'
    
    headers = {
    'Accept': 'application/json',
    'response_type': 'code',
    'Authorization': 'Get your own key'
    }
    
    url = 'https://api.spotify.com/v1/audio-features/' + id
    response = requests.get(url, allow_redirects = True, headers=headers)
    #print(response)
    response = str(response.json())
    
    response = response.replace('{','')
    response = response.replace(',','')
    response = response.replace("'","")
    response = response.split()
    
    danceAbility = response[1]
    energy = response[3]
    key = response[5]
    loudness = response[7]
    mode = response[9]
    speechiness = response[11]
    acousticness = response[13]
    instrumentalness = response[15]
    liveness = response[17]
    valence = response[19]
    tempo = response[21]
    time_signature = response[35][0]
    duration_ms = response[33]

    return danceAbility, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, time_signature, duration_ms
    
def getTrackPlayedNum(id):
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Get your own key'
    }
    
    response = requests.get('https://api.spotify.com/v1/tracks/' + id, headers=headers)
    #print(response)
    response = str(response.json())
    
    #Replace everything
    response = response.replace('{','')
    response = response.replace(',','')
    response = response.replace("'","")
    response = response.split()
    
    popularityIndex = response.index('popularity:')
    return response[popularityIndex + 1]

def makeDatasets():
    #df = pd.DataFrame(columns=['artist_name', 'track_id', 'track_name', 'acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'time_signature', 'valence', 'popularity'])
    df = pd.read_csv('Datasets/Data.csv')
    #For loop Start
    for i in range(2380, Data.shape[0]):
        print(i)
        ID = Data.iloc[i]['track_id']
        danceAbility, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, time_signature, duration_ms = getOneLine(ID)
        popularity = getTrackPlayedNum(ID)
        df = df.append({
            'artist_name' : Data.iloc[i]['artist_name'], 
            'track_id' : ID, 
            'track_name': Data.iloc[i]['track_name'], 
            'acousticness': acousticness, 
            'danceability': danceAbility, 
            'duration_ms': duration_ms, 
            'energy': energy, 
            'instrumentalness': instrumentalness, 
            'key': key, 
            'liveness': liveness, 
            'loudness': loudness, 
            'mode': mode, 
            'speechiness': speechiness, 
            'tempo': tempo, 
            'time_signature': time_signature, 
            'valence': valence, 
            'popularity': popularity,
        }, ignore_index = True)
        
        if i % 500 == 0:
            print(df.head())
            print(df.shape)
            df.to_csv('Data.csv')
            
makeDatasets()