# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 23:51:09 2021

@author: HH
"""

import cdsapi

c = cdsapi.Client()

for year in range(2012,2015):
    start_month=1
    end_month=12
    outpath='F:/agrometeorological data/'
    
    
    #Tmax
    for month in range(start_month,end_month+1):
        c.retrieve(
            'sis-agrometeorological-indicators',
            {
                'variable': '2m_temperature',
                'statistic': '24_hour_maximum',
                'year': '%d'%year,
                'month': [
                    '%02d'%month,
                ],
                'day': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',
                ],
                'format': 'zip',
            },
            outpath+'tmax_%d_%02d.zip'%(year,month))
        
    #Tmin
    for month in range(start_month,end_month+1):
        c.retrieve(
            'sis-agrometeorological-indicators',
            {
                'variable': '2m_temperature',
                'statistic': '24_hour_minimum',
                'year': '%d'%year,
                'month': [
                    '%02d'%month,
                ],
                'day': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',
                ],
                'format': 'zip',
            },
            outpath+'tmin_%d_%02d.zip'%(year,month))
    
    #rad
    for month in range(start_month,end_month+1):
        c.retrieve(
            'sis-agrometeorological-indicators',
            {
                'variable': 'solar_radiation_flux',
                'year': '%d'%year,
                'month': '%02d'%month,
                'day': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',
                ],
                'format': 'zip',
            },
            outpath+'rad_%d_%02d.zip'%(year,month))
        
    #hum
    for month in range(start_month,end_month+1):
        c.retrieve(
            'sis-agrometeorological-indicators',
            {
                'variable': 'vapour_pressure',
                'statistic': '24_hour_mean',
                'year': '%d'%year,
                'month': '%02d'%month,
                'day': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',
                ],
                'format': 'zip',
            },
            outpath+'hum_%d_%02d.zip'%(year,month))
        
    #wind
    for month in range(start_month,end_month+1):   
        c.retrieve(
            'sis-agrometeorological-indicators',
            {
                'variable': '10m_wind_speed',
                'statistic': '24_hour_mean',
                'year': '%d'%year,
                'month': '%02d'%month,
                'day': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',
                ],
                'format': 'zip',
            },
            outpath+'wind_%d_%02d.zip'%(year,month))   
        
    #prec
    for month in range(start_month,end_month+1):     
        c.retrieve(
            'sis-agrometeorological-indicators',
            {
                'variable': 'precipitation_flux',
                'year': '%d'%year,
                'month': '%02d'%month,
                'day': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',
                ],
                'format': 'zip',
            },
            outpath+'prec_%d_%02d.zip'%(year,month)) 
            
        