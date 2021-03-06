# -*- coding: utf-8 -*-
"""Covid19IndiaLocator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/punit0087/Covid19India.Org-Tracker/blob/master/Covid19IndiaLocator.ipynb
"""

##Code written by Punit Rathore (prathore@mit.edu)
import numpy as np
import pandas as pd
import requests
from math import sin, cos, sqrt, atan2, radians

import warnings
warnings.filterwarnings("ignore")

#https://drive.google.com/drive/folders/1ynC5CBEpb9ipZuFvEiJnbqvf-f8-iKHI?usp=sharing
def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)


if __name__ == "__main__":
    file_id1 = '1FBbr9zubK4VsB6gmNzj4fvE204ngvCeZ'
    destination1 = 'IndiaPostalCodes.csv'
    
    #If file is not present in current directory, then download file from google_drive.
    files_in_dir = os.listdir()
    if 'IndiaPostalCodes.csv' not in files_in_dir :
        download_file_from_google_drive(file_id, destination)
        
        

import covid19main_Copy
from covid19main_Copy import *

def get_nearest_case_with_pincode(query_pincode):
    g = int(query_pincode)
    #print('call_received at script 2')
    validPIN = True;
    if g in city_wise_coordinates.PIN.values:
        query_info= city_wise_coordinates[city_wise_coordinates.PIN == int(g)]
        #print('No error in script 2')
        (mindist, cases, district, state , Lat, Lng) = get_nearest_covid19_stats_pincode(query_info,corona_db_with_latlng)
        return (validPIN ,mindist, cases, district, state , Lat, Lng)
    else:
        validPIN = False;
        return (validPIN ,None,None,None,None,None,None)

def get_nearest_case_with_geoloc(Lats,Lngs):  
    Latitude = float(Lats)
    Longitude = float(Lngs)
    query_info = {'Lat':Latitude , 'Lng' : Longitude}
    (mindist, cases, district, state , Lat, Lng) = get_nearest_covid19_stats_lat_lng(query_info,corona_db_with_latlng)
    return (mindist, cases, district, state , Lat, Lng)
