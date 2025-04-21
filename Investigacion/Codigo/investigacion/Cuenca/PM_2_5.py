#PM2.5 Analysis
#Cuenca from DIC 31, 2018 14h00 LT to JAN 1, 2019 14h00 LT
# Libraries Import
import os
from tkinter import font
from matplotlib import units
from netCDF4 import Dataset 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

out_path = "c:/Users/USER/Devi/Investigacion/Avances/Cuenca/PNG/PM25/00_LT/"
# Open the NetCDF file and Store the Shapefiles in variables
nc = Dataset(r'c:\Users\USER\Devi\Cuenca\wrfout_2021-12-31_cuenca.nc')
#c:\Users\Usuario\OneDrive - Universidad San Francisco de Quito\Asistencia Investigacion\NP Files\wrfout_2021-12-31_21_cuenca.nc
#c:\Users\Usuario\OneDrive - Universidad San Francisco de Quito\Asistencia Investigacion\NP Files\wrfout_2021-12-31_cuenca.nc
#c:\Users\Usuario\OneDrive - Universidad San Francisco de Quito\Asistencia Investigacion\NP Files\wrfout_2021-12-31_18_cuenca.nc
urban = r'c:\Users\USER\Devi\Cuenca\cuencaurbano.shp'
canton = r'c:\Users\USER\Devi\Cuenca\cantoncuenca.shp'
imd = r'c:\Users\USER\Devi\Cuenca\imdcuenca.shp'#imd is image metadata format.

# Reading and storing the collection of shapely geometries and visual characteristics in variables
urban_zone = ShapelyFeature (Reader(urban).geometries(),ccrs.PlateCarree(),edgecolor='black',facecolor='none',alpha=0.6)
canton_zone = ShapelyFeature (Reader(canton).geometries(),ccrs.PlateCarree(),edgecolor='darkgray',facecolor='none',alpha=0.4)
imd = ShapelyFeature (Reader(imd).geometries(),ccrs.PlateCarree(),edgecolor='darkgrey', facecolor='none',alpha=0.2)

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
PM=list(range(0,24))
for i in PM:
    PM[i]=nc.variables ["PM2_5_DRY"][time[i],z,:,:]

#LONGIITUDE, LATITUDE AND HEIGHT IN M.A.S.L.
lons = nc.variables ['XLONG'][time[0],:,:]
lats = nc.variables ['XLAT'][time[0],:,:]
hgt = nc.variables ['HGT'][time[0],:,:]

#Labels: PM2.5 and Altitude (PM2.5:4 to 28ºC, alt:2500 to 3900 ºC)
levels = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
alt = [2500,2700,2900,3100,3300,3500,3700,3900]

#PM2.5 Plots
for j in range (0,24):
    plt.figure(j)
#Fixing the axes of the figure using the PlateCarree projection. 
    ax = plt.axes(projection=ccrs.PlateCarree())

#Map Axes (y:Latitude and x:Longitude), Setting ticks and limits
    x = [-79.4,-79.3,-79.2,-79.1,-79.0,-78.9,-78.8]
    y = [-3.1,-3.0,-2.9,-2.8,-2.7,-2.6,-2.5]
    xlim=[-79.1,-78.85];ylim=[-3.0,-2.75]
    ax.set_xticks(x);ax.set_yticks(y)
    ax.set_xlim(xlim);ax.set_ylim(ylim)

#Altitude Contour and Label
    cs = ax.contour(lons,lats,hgt,alt,colors='dimgray',linestyles='dashed',linewidths=0.7,alpha=0.25)
    ax.clabel(cs,inline=True,fmt='%1.0f'+'m',fontsize=8)
#Adding the features to the current plot
    ax.add_feature(imd); ax.add_feature(canton_zone); ax.add_feature(urban_zone)
#PM2.5 Colormesh and Colorbar
    colorlist=["ghostwhite","palegreen","lightgreen","lawngreen","greenyellow","yellow","gold","orange","darkorange","chocolate","brown","maroon"]
    #M2:"ghostwhite","cornflowerblue","blue","blueviolet","darkviolet","darkmagenta","mediumvioletred","deeppink","crimson"
    #M3:"mintcream","aquamarine","springgreen","lime","cyan","deepskyblue","dodgerblue","royalblue","blue","navy"
    #M4:"ghostwhite","palegreen","lightgreen","lawngreen","greenyellow","yellow","gold","orange","darkorange","chocolate","brown","maroon"
    #M6:"seashell", "bisque", "orange", "darkorange","chocolate","sienna","saddlebrown","maroon"
    newcmp = LinearSegmentedColormap.from_list('testCmap',colors=colorlist, N=256)
    plt.pcolormesh(lons,lats,PM[j],vmin=0.1,vmax=250,cmap=newcmp,shading='gouraud',alpha=1,zorder=1.4)
    clb=plt.colorbar(shrink=0.81)
    clb.set_label('$µg/m^3$',labelpad=-29,y=1.06,rotation=0,fontsize=11,family='sans-serif')

    newcmp1 = LinearSegmentedColormap.from_list('testCmap',colors=colorlist, N=256)
    plt.pcolormesh(lons,lats,PM[j],vmin=0.1,vmax=250,cmap=newcmp,shading='gouraud',alpha=1,zorder=1.4)

# Title and Axes Labels
    plt.xlabel ('Longitud',fontsize=12,family='sans-serif')
    plt.ylabel ('Latitud',fontsize=12,family='sans-serif')
    P="PM$_{2.5}$"
    if j<10:
        plt.title(f"{P}: 31-Dic-2021 {j+14}:00 LT",fontsize=14,family='sans-serif')
    else:
        plt.title(f"{P}: 1-Ene-2022 {j-10}:00 LT",fontsize=14,family='sans-serif')

# Text annotation for the organization information.
    text = AnchoredText('Universidad San Francisco de Quito\nDepartamento de Ingeniería Ambiental',loc=3,prop={'size':6.5},frameon=True)
    #Emisiones de Material Particulado\nQuema de monigotes a media noche\n
    ax.add_artist(text)
    text = AnchoredText('Quema de Monigotes: 00:00 LT',loc=4,prop={'size':6.5},frameon=True)
    #Emisiones de Material Particulado\nQuema de monigotes a media noche\n
    ax.add_artist(text)

#Storing the figure in the User folder
    ax.set_aspect(aspect=0.8)
    plt.tight_layout()
    if j<10:
        plt.savefig(out_path+f"PM_00A{j}.png",dpi=700,facecolor='w',edgecolor='w',orientation='portrait',format='png',transparent=False,pad_inches=0.1,bbox_inches="tight")
        #plt.savefig(f"PM_31Dec2021_{j+14}.png",dpi=700,facecolor='w',edgecolor='w',orientation='portrait',format='png',transparent=False,pad_inches=0.1,bbox_inches="tight")
    else:
        plt.savefig(out_path+f"PM_0A{j}.png",dpi=700,facecolor='w',edgecolor='w',orientation='portrait',format='png',transparent=False,pad_inches=0.1,bbox_inches="tight")
        #plt.savefig(f"PM_1Jan2022_{j-10}.png",dpi=700,facecolor='w',edgecolor='w',orientation='portrait',format='png',transparent=False,pad_inches=0.1,bbox_inches="tight")
#plt.show()