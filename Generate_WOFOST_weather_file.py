import os
import datetime
import xarray as xr
import pandas as pd

# weather data
data_dir = "D:/hh/weather"
site_names=['Zhengzhou','Yucheng']
site_coors=[[113.65,34.72],[116.57176600,36.83038800]]
lon,lat=site_coors[1]
site=site_names[1]

ds = xr.open_mfdataset("D:/hh/weather/elev_ITPCAS-CMFD_V0106_B-01_010deg.nc")
pnt = ds.sel(lon=lon, lat=lat, method="nearest")
alt=int(pnt.elev)

c1=-0.18
c2=-0.55
station_number=1
year_begin,year_end = 2019,2020

ds = xr.open_mfdataset(os.path.join(data_dir,"AgERA5_NC_10_10_grid/%03d_%03d.nc"%(int(lon),int(lat+1))))
pnt = ds.sel(lon=lon, lat=lat, method="nearest")
df=pnt.to_dataframe()
df['Date']=df.index.date
df=df.set_index('Date',drop=True)
  
'''
ranges = {"LAT": (-90., 90.),
          "LON": (-180., 180.),
          "ELEV": (-300, 6000),
          "IRRAD": (0., 40e6),
          "TMIN": (-50., 60.),
          "TMAX": (-50., 60.),
          "VAP": (0.06, 199.3),  # hPa, computed as sat. vapour pressure at -50, 60 Celsius
          "RAIN": (0, 25),
          "E0": (0., 2.5),
          "ES0": (0., 2.5),
          "ET0": (0., 2.5),
          "WIND": (0., 100.),
          "SNOWDEPTH": (0., 250.),
          "TEMP": (-50., 60.),
          "TMINRA": (-50., 60.)}
'''
year = year_begin
while year <= year_end:
    t = datetime.date(year,1,1)
    
    f=open(os.path.join(data_dir,"%s-2.%s"%(site,str(year)[-3:])),"w+")
    print (year,"begins for site",site)
    f.write("*------------------------------------------------------------*"+"\n"
                +'*'+"%12s"%("Country: ")+"China"+"\n"
                +'*'+"%12s"%("Station: ")+site+"\n"
                +'*'+"%12s"%("Year: ")+"%d"%(year)+"\n"
                +'*'+"%12s"%("Origin: ")+"AgERA5 dataset"+"\n"
                +'*'+"%12s"%("Author: ")+"Huang Hai, CAU"+"\n"
                +'*'+"%12s"%("Longitude: ")+"%.2f"%(lon)+" E"+"\n"
                +'*'+"%12s"%("Latitude: ")+"%.2f"%(lat)+" N"+"\n"
                +'*'+"%12s"%("Elevation: ")+"%.2f"%(alt)+" m"+"\n"
                +'*'+"%12s"%("Columns: ")+"\n"
                +'*'+"%12s"%("======== ")+"\n"
                +'*'+"  station number"+"\n"
                +'*'+"  year"+"\n"
                +'*'+"  day"+"\n"
                +'*'+"  irradiation (kJ·m-2·d-1)"+"\n"
                +'*'+"  minimum temperature (degrees Celsius)"+"\n"
                +'*'+"  maximum temperature (degrees Celsius)"+"\n"
                +'*'+"  vapour pressure (kPa)"+"\n" 
                +'*'+"  mean wind speed (m·s-1)"+"\n" 
                +'*'+"  precipitation (mm·d-1)"+"\n" 
                +'**'+" WCCDESCRIPTION="+site+", China"+"\n" 
                +'**'+" WCCFORMAT=2"+"\n" 
                +'**'+" WCCYEARNR="+"%d"%(year)+"\n" 
                +"*------------------------------------------------------------*"+"\n"
                +"%.2f  %.2f  %.2f  %.2f  %.2f\n"%(lon, lat, alt, c1, c2)
                )
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        numdays = 366
    else:
        numdays = 365
    
    for d in range(0,numdays):
        date=t+datetime.timedelta(d)
        
        if df["prec"][date]<0:
           df["prec"][date]=0 
        if df["prec"][date]>250:#模型中降水不超过250mm
           df["prec"][date] =200
        if df["hum"][date]<0.06:#模型中VAP不超过0.06-199.3
           df["hum"][date] =0.1
        if df["tmin"][date]<-50:#模型中tmin不超过-50
           dfr["tmin"][date] =-49
        if df["tmax"][date]>60:#模型中tmax不超过60
           df["tmax"][date] =59
        if df["wind"][date]>100:#模型中wind不超过100
           df["wind"][date] =99    
        try:
            f.write("%d"%(station_number)+"\t"+"%d"%(year)+"\t"+"%3d"%(d+1)+"\t"
                        +"%5d"%(round(df["rad"][date]))+"\t"
                        +"%5.1f"%(round(df["tmin"][date]*10)/10)+"\t"
                        +"%5.1f"%(round(df["tmax"][date]*10)/10)+"\t"
                        +"%5.3f"%(round(df["hum"][date]*1000)/1000)+"\t"
                        +"%4.1f"%(round(df["wind"][date]*10)/10)+"\t"
                        +"%4.1f"%(round(df["prec"][date]*10)/10)+"\n")
        except:#masked value
            print ('Wrong')        
    f.close()
    year += 1
    
