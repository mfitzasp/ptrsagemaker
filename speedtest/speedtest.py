# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:08:50 2024

@author: mfitz
"""

import os
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import time
#import json
import numpy as np
from astropy.io import fits
#import psutil


def download_frames_from_ptrarchive(location='.', frames=[]):
    
    
    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=2.0, allowed_methods=frozenset(['GET', 'POST']))
    #retry = Retry(connect=5, backoff_factor=2.0)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    #frames='(509954,507152,509116,507858,508370,508106,510918,509917,508897,508196,507674,507629,507970,510577,510612,507818,508289,509879,507344,507890,509137,510364,508233,507389,508701,507714,508178,508138,507637,508114,508307,507994,507605,510686,507210,507597,507698,510591,509082,509458,509014,510768,508082,507224,507423,508668,507668,507954,509968,510161,507738,510125,510413,507730,507312,508273,508623,507866,509000,508034,507778,508881,509063,510472,509683,507328,508968,508800,508313,507469,508910,508759,508653,509651,508281,509425,508130,507908,508074,507240,510854,509514)'
    
    
    authtoken="AUTHTOKEN"
    frame_url="https://archiveapi.photonranch.org/frames/"
    frames=frames.replace('(','').replace(')','')
    frames=frames.split(',')
    
    if not os.path.exists(location):
        os.makedirs(location)
        
    for frame in frames:
        response=session.get(frame_url + frame)
        download_url=response.json()['url']
        print ("Downloading: " + str(response.json()['filename']))
        with open(location + '/' + response.json()['filename'],'wb') as f:
            f.write(session.get(download_url).content)
        
    #breakpoint()
    
    #print ("Download_frames_from_ptrarchive")
    
def download_frame_from_ptrarchive(location='.', frame=''):
    
    
    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=2.0, allowed_methods=frozenset(['GET', 'POST']))
    #retry = Retry(connect=5, backoff_factor=2.0)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    #frames='(509954,507152,509116,507858,508370,508106,510918,509917,508897,508196,507674,507629,507970,510577,510612,507818,508289,509879,507344,507890,509137,510364,508233,507389,508701,507714,508178,508138,507637,508114,508307,507994,507605,510686,507210,507597,507698,510591,509082,509458,509014,510768,508082,507224,507423,508668,507668,507954,509968,510161,507738,510125,510413,507730,507312,508273,508623,507866,509000,508034,507778,508881,509063,510472,509683,507328,508968,508800,508313,507469,508910,508759,508653,509651,508281,509425,508130,507908,508074,507240,510854,509514)'
    
    
    authtoken="AUTHTOKEN"
    frame_url="https://archiveapi.photonranch.org/frames/"
    # frames=frames.replace('(','').replace(')','')
    # frames=frames.split(',')
    
    if not os.path.exists(location):
        os.makedirs(location)
        
    #for frame in frames:
    response=session.get(frame_url + frame)
    #breakpoint()
    download_url=response.json()['url']
    print ("Downloading: " + str(response.json()['filename']))
    with open(location + '/' + response.json()['filename'],'wb') as f:
        f.write(session.get(download_url).content)
        
    #breakpoint()
    
    #print ("Download_frames_from_ptrarchive")
    return  str(response.json()['filename'])
    
# Frame numbers of npy files
#npyframes='2190439,2190207,2189557,2189727,2189260,2189099,2166275,2165713,2164600,2164834,2163605,2163492,2163389,2163268,2163144,2163080,2162981,2162889,2162816,2162715,2162656,2162542,2162424,2162336,2162187,2162110,2162036,2161971,2161898,2161833,2161808,2161767'
npyframes='2190439'#,2190207,2189557,2189727,2189260,2189099,2166275,2165713,2164600,2164834,2163605,2163492,2163389,2163268,2163144,2163080,2162981,2162889,2162816,2162715,2162656,2162542,2162424,2162336,2162187,2162110,2162036,2161971,2161898,2161833,2161808,2161767''



npyframes=npyframes.replace('(','').replace(')','')
npyframes=npyframes.split(',')

#npyframes=[]

if len(npyframes) > 0:
    # download_timer=time.time()
    # npyfilenames=[]
    # location='npyfiles'
    # #download_timer=time.time()
    # for dbentry in npyframes:
    #     file_to_do=download_frame_from_ptrarchive(location=location, frame=dbentry)
    #     npyfilenames.append(file_to_do)
    #     #breakpoint()
    # time_it_took_to_download=time.time()-download_timer
    # time_per_image_to_download_npy = time_it_took_to_download / len(npyfilenames)
        
    
    counter=0
    timer=time.time()
    
    npydownloadingtimes=[]
    npyopeningtimes=[]
    npyoperationtimes=[]
    npysavingtimes=[]
    
    while counter < 1:
        for frame in npyframes:
            #breakpoint()
            
            download_timer=time.time()
            fitsfilenames=[]
            #fits_download_times=[]
            location='npyfiles'
            #download_timer=time.time()
            #for dbentry in fitsframes:
            npyfile=download_frame_from_ptrarchive(location=location, frame=frame)
                #fitsfilenames.append(file_to_do)
                #breakpoint()
            npydownloadingtimes.append(time.time()-download_timer)
            
            open_overhead=time.time()
            # Open the npy
            tempfile=np.load(location +'/' + npyfile)
            npyopeningtimes.append(time.time()-open_overhead)
            #print (psutil.virtual_memory().percent)
            
            operation_overhead=time.time()
            # pointless operation 1
            np.nanmedian(tempfile)
            
            # pointless operation 2
            np.add(tempfile,2)
            
            # pointless operation 3
            np.divide(tempfile,tempfile)
            
            # pointless operation 4
            np.multiply (tempfile, tempfile)
            
            # pointless operation 5
            np.nanstd(tempfile)
            
            npyoperationtimes.append(time.time()-operation_overhead)
            
            # Save the npy
            saving_overhead=time.time()
            np.save(location +'/saved_' + npyfile, tempfile)
            npysavingtimes.append(time.time()-saving_overhead)
            
            #breakpoint()
            print (npyfile)
            
            try:
                os.remove(location +'/saved_' + npyfile)
            except:
                pass
            try:
                os.remove(location +'/' + npyfile)
            except:
                pass
            
        counter=counter+1

# Frame numbers of same fits files


#fitsframes='2190815,2190430,2190814,2190818,2190216,2190816,2189566,2189718,2190812,2189269,2190817,2189108,2190813,2166266,2168588,2168591,2165729,2164591,2168602,2164825,2168579,2168595,2163614,2168597,2163504,2168598,2163407,2163259,2168603,2163153,2168580,2163089'
fitsframes='2190430'#',2190430,2190814,2190818,2190216,2190816,2189566,2189718,2190812,2189269,2190817,2189108,2190813,2166266,2168588,2168591,2165729,2164591,2168602,2164825,2168579,2168595,2163614,2168597,2163504,2168598,2163407,2163259,2168603,2163153,2168580,2163089'

fitsframes=fitsframes.replace('(','').replace(')','')
fitsframes=fitsframes.split(',')




#time_per_image_to_download_fits = time_it_took_to_download / len(npyfilenames)

if len(fitsframes) > 0:
    counter=0
    timer=time.time()
    fitsdownloadingtimes=[]
    fitsopeningtimes=[]
    fitsoperationtimes=[]
    fitssavingtimes=[]
    
    while counter < 1:
        for frame in fitsframes:
            #breakpoint()
            
            download_timer=time.time()
            fitsfilenames=[]
            #fits_download_times=[]
            location='fitsfiles'
            #download_timer=time.time()
            #for dbentry in fitsframes:
            fitsfile=download_frame_from_ptrarchive(location=location, frame=frame)
                #fitsfilenames.append(file_to_do)
                #breakpoint()
            fitsdownloadingtimes.append(time.time()-download_timer)
            
            open_overhead=time.time()
            # Open the npy
            try:        
                tempfileopen=fits.open(location +'/' + fitsfile, ignore_missing_simple=True)[0]
            except:
                breakpoint()
            tempfile=np.array(tempfileopen.data) # Has to be plonked into an array for a fair comparison, a straight load doesn't actually bring it into memory
            fitsopeningtimes.append(time.time()-open_overhead)
            #print (psutil.virtual_memory().percent)
            
            operation_overhead=time.time()
            # pointless operation 1
            np.nanmedian(tempfile)
            
            # pointless operation 2
            np.add(tempfile,2)
            
            # pointless operation 3
            np.divide(tempfile,tempfile)
            
            # pointless operation 4
            np.multiply (tempfile, tempfile)
            
            # pointless operation 5
            np.nanstd(tempfile)
            
            fitsoperationtimes.append(time.time()-operation_overhead)
            
            # Save the npy
            saving_overhead=time.time()
            fits.writeto(location +'/saved_' + fitsfile, tempfile, tempfileopen.header, overwrite=True)
            #np.save(location +'/saved_' + fitsfile)
            fitssavingtimes.append(time.time()-saving_overhead)
            
            #breakpoint()
            print (fitsfile)
            
            try:
                os.remove(location +'/saved_' + fitsfile)
            except:
                pass
            try:
                os.remove(location +'/' + fitsfile)
            except:
                pass
            
        counter=counter+1



#download_frames_from_ptrarchive(location='fits', frames='2190815,2190430,2190814,2190818,2190216,2190816,2189566,2189718,2190812,2189269,2190817,2189108,2190813,2166266,2168588,2168591,2165729,2164591,2168602,2164825,2168579,2168595,2163614,2168597,2163504,2168598,2163407,2163259,2168603,2163153,2168580,2163089')
print ("npy median download time: " + str(np.median(npydownloadingtimes)))
print ("npy median open time: "+ str(np.median(npyopeningtimes)))
print ("npy median operation time: "+ str(np.median(npyoperationtimes)))
print ("npy median save time: "+ str(np.median(npysavingtimes)))

print ("fits median download time: "+ str(np.median(fitsdownloadingtimes)))
print ("fits median open time: " + str(np.median(fitsopeningtimes)))
print ("fits median operation time: " + str(np.median(fitsoperationtimes)))
print ("fits median save time: "+ str(np.median(fitssavingtimes)))


#breakpoint()