import pandas as pd
import numpy as np

def find_anomaly(path='Book1.xlsx',sheet_name='Anomaly-1',span=4): #can add limits as inputs too
    df=pd.read_excel('Book1.xlsx',sheet_name=sheet_name,index_col=0, header=0)
    observations=['Blood Pressure', 'Oxygen Level','Temperature', 'Hydration','Glucose Level','TV Time','Phone Time','Heart Rate']
    flags=[bp(df),o2(df),temperature(df),hydration(df),glucose(df),tv(df),phone(df),heartrate(df)]
    danger_level=0
    danger=[]
    for i in range(len(flags)):
        if flags[i]:
            danger.append(observations[i])
            danger_level+=1
    if danger_level>=4:
        return danger
    else:
        return None

df=pd.read_excel('Book1.xlsx',index_col=0, header=0)

def bp(df,limits=[110,130,70,90]): #[110-130,70-90]   within range of 4 problem is there
    i=0
    j=0
    flag=False
    low_sys,high_sys,low_dia,high_dia=limits
    for sys,dia in df[['bpsys_mmHg','bpdia_mmHg']].values:
        if i>=4 or j>=4:
            flag=True
            return flag
        if sys> high_sys or sys<low_sys:
            i+=1
        else:
            i=0
        if dia >high_dia or dia<low_dia:
            j+=1
        else:
            j=0
    return False

def o2(df,limits=[95,99]): #[95-99] allowed   within range of 4 problem is there
    i=0
    flag=False
    low,high=limits
    for item in df['o2level_%'].values:
        if i>=4:
            flag=True
            return flag
        if item> high or item<low:
            i+=1
        else:
            i=0
    return False

def temperature(df,limits=[97,99]): #[97-99] allowed   within range of 4 problem is there
    i=0
    flag=False
    low,high=limits
    for item in df['temperature_F'].values:
        if i>=4:
            flag=True
            return flag
        if item> high or item<low:
            i+=1
        else:
            i=0
    return False

def hydration(df,limits=[45,75]): #[95-99] allowed   within range of 4 problem is there
    i=0
    flag=False
    low,high=limits
    for item in df['hydration_L'].values:
        if i>=4:
            flag=True
            return flag
        if item> high or item<low:
            i+=1
        else:
            i=0
    return False

def glucose(df,limits=[5,11]): #[5-11] allowed   within range of 4 problem is there
    i=0
    flag=False
    low,high=limits
    for item in df['glucose_mmol/L'].values:
        if i>=4:
            flag=True
            return flag
        if item> high or item<low:
            i+=1
        else:
            i=0
    return False

def tv(df,limit=4): #4 hrs on bad
    i=0
    flag=False
    for tv_on,sleep_on in df[['tv','sleepstatus']].values:
        if i>=4:
            flag=True
            return flag
        if tv_on or (tv_on and sleep_on):
            i+=1
        else:
            i=0
    return False

def phone(df,limit=4): #4 hrs on bad
    i=0
    flag=False
    for phone_on,sleep_on in df[['smartphone','sleepstatus']].values:
        if i>=4:
            flag=True
            return flag
        if phone_on or (phone_on and sleep_on):
            i+=1
        else:
            i=0
    return False

def heartrate(df,limits=[40,50,60,100]): #[sleeping allowed-40-50 ,  awake allowed-60-100] hrs on bad
    i=0
    flag=False
    low_sleep,high_sleep,low_awake,high_awake=limits
    for bpm,sleep_on in df[['smartphone','sleepstatus']].values:
        if i>=4:
            flag=True
            return flag
        if ( sleep_on and (bpm<40 or bpm>50) ) or ( not sleep_on and (bpm<60 or bpm>100) ):
            i+=1
        else:
            i=0
    return False


print(find_anomaly('Book1.xlsx','Anomaly-1'))




