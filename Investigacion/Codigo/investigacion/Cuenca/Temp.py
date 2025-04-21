#Temperature Analysis
#Cuenca from DIC 31, 2018 14h00 LT to JAN 1, 2019 14h00 LT
# Libraries Import
import os
from matplotlib import units
from netCDF4 import Dataset 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

# Open the NetCDF file and Store the Shapefiles in variables
nc = Dataset(r'c:\Users\USER\Devi\Cuenca\wrfout_2018-12-31_18_cuenca.nc')
urban = r'c:\Users\USER\Devi\Cuenca\cuencaurbano.shp'
canton = r'c:\Users\USER\Devi\Cuenca\cantoncuenca.shp'
imd = r'c:\Users\USER\Devi\Cuenca\imdcuenca.shp'#imd is image metadata format.
out_path = "c:/Users/USER/Devi/Investigacion/Avances/Cuenca/PNG/TEMP/"

# Reading and storing the collection of shapely geometries and visual characteristics in variables
urban_zone =  ShapelyFeature (Reader(urban).geometries(),ccrs.PlateCarree(),edgecolor='black',facecolor='none',alpha=0.8)
canton_zone =  ShapelyFeature (Reader(canton).geometries(),ccrs.PlateCarree(),edgecolor='darkgray',facecolor='none',alpha=0.6)
imd =  ShapelyFeature (Reader(imd).geometries(),ccrs.PlateCarree(),edgecolor='darkgrey', facecolor='none',alpha=0.35)

#TIME IN HOURS
time=list(range(0,24))
for i in time:
    time[i]=i+19

#TEMPERATURE IN K
p=list(range(0,24))
for i in p:
    p[i]=nc.variables ["T2"][time[i],:,:]

#TEMPERATURE IN ºC
T=list(range(0,24))
for i in T:
    T[i]= p[i]-273.15 
#p[2]=16:00 p[3]=17:00 p[4]=18:00 p[5]=19:00 p[6]=20:00, 
#p[7]=21:00, p[8]=22:00, p[9]=23:00, p[10]=00:00, p[11]=01:00, p[12]=02:00

z=0
#PM 2.5 IN UG/M3 
PM=list(range(0,5))
for i in PM:
    PM[i]=nc.variables ["PM2_5_DRY"][time[i],z,:,:]

#LONGIITURE, LATITUDE AND HEIGHT IN M.A.S.L.
lons = nc.variables ['XLONG'][time[0],:,:]
lats = nc.variables ['XLAT'][time[0],:,:]
hgt = nc.variables ['HGT'][time[0],:,:]

#Labels: Temperature and Altitude (T:4 to 28ºC, alt:2500 to 3900 ºC)
levels = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
alt = [2500,2700,2900,3100,3300,3500,3700,3900]

#Temperature Plots
for j in range (0,24):
    plt.figure(j)
#Fixing the axes of the figure using the PlateCarree projection. 
    ax = plt.axes(projection=ccrs.PlateCarree())

#Adding the features to the current plot
    ax.add_feature(canton_zone); ax.add_feature (imd); ax.add_feature(urban_zone)

#Altitude Contour and Label
    cs = plt.contour(lons,lats,hgt,alt,colors='dimgray',linestyles='dashed',linewidths=0.7,alpha=0.4)
    ax.clabel(cs,inline=True,fmt='%1.0f'+'m',fontsize=8)

#Map Axes (y:Latitude and x:Longitude), Setting ticks and limits
    x = [-79.4,-79.3,-79.2,-79.1,-79.0,-78.9,-78.8]
    y = [-3.1,-3.0,-2.9,-2.8,-2.7,-2.6,-2.5]
    xlim=[-79.1,-78.85];ylim=[-3.0,-2.75]
    ax.set_xticks(x);ax.set_yticks(y)
    ax.set_xlim(xlim);ax.set_ylim(ylim)

#Temperature Contour Filled and Colorbar
    plt.contourf(lons,lats,T[j],levels,cmap='coolwarm',alpha=0.9)
    clb=plt.colorbar(shrink=0.81)
    clb.set_label('ºC',labelpad=-28,y=1.05,rotation=0,fontsize=11,family='sans-serif')

# Title and Axes Labels
    plt.xlabel ('Longitud',fontsize=12,family='sans-serif')
    plt.ylabel ('Latitud',fontsize=12,family='sans-serif') 
    if j<10:
        plt.title(f"Temperatura: 31-Dic-2021 {j+14}:00 LT",fontsize=14,family='sans-serif')
    else:
        plt.title(f"Temperatura: 1-Ene-2022 {j-10}:00 LT",fontsize=14,family='sans-serif')
# Text annotation for the organization information.
    text = AnchoredText('Universidad San Francisco de Quito\nDepartamento de Ingeniería Ambiental',loc=3, prop={'size':6.5}, frameon=True)
    ax.add_artist(text)
#Storing the figure in the User folder
    #fig = r'c:\Users\Usuario\Documents\Cuenca_DIC\TIFF\TEMP\T_31Dec2021_tiff'
    ax.set_aspect(aspect=0.8)
    plt.tight_layout()
    if j<10:
        plt.savefig(out_path+f"T_00{j}.png",dpi=700,facecolor='w',edgecolor='w',orientation='portrait',format='png',transparent=False,pad_inches=0.1,bbox_inches="tight")
        #plt.savefig(f"T_31Dec2021_{j+14}.tiff",dpi=500,facecolor='w',edgecolor='w',orientation='portrait',format='tiff',transparent=False,pad_inches=0.1,bbox_inches="tight")
    else:
        plt.savefig(out_path+f"T_0{j}.png",dpi=700,facecolor='w',edgecolor='w',orientation='portrait',format='png',transparent=False,pad_inches=0.1,bbox_inches="tight")
        #plt.savefig(f"T_1Jan2022_{j-10}.tiff",dpi=500,facecolor='w',edgecolor='w',orientation='portrait',format='tiff',transparent=False,pad_inches=0.1,bbox_inches="tight")
    #plt.show()
    #If j is equal to 10 or greater, we should start again from 0, which means, j-10