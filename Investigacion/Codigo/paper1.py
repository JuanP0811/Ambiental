
import os
from netCDF4 import Dataset 
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

# Open the NetCDF file

nc = Dataset('c:/Cuenca_31Decdata/res/wrfout_2021-12-31_18_cuenca.nc')
urban = 'c:/cuenca/cuencaurbano.shp'
canton = 'c:/cuenca/cantoncuenca.shp'
imd = 'c:/cuenca/imdcuenca.shp'

ax = plt.axes(projection=ccrs.PlateCarree())

urban_zone =  ShapelyFeature (Reader(urban).geometries(),ccrs.PlateCarree(),edgecolor='black', facecolor='none')
canton_zone =  ShapelyFeature (Reader(canton).geometries(),ccrs.PlateCarree(),edgecolor='grey', facecolor='none')
#imd =  ShapelyFeature (Reader(imd).geometries(),ccrs.PlateCarree(),edgecolor='grey', facecolor='none')

ax.add_feature (urban_zone)
ax.add_feature (canton_zone)
ax.add_feature (imd)


time1=19 #0 to 79, 12sep2019 01h00LT
time2=20 #0 to 79, 12sep2019 07h00LT
time3=21 #0 to 79, 12sep2019 07h00LT
time4=22 #0 to 79, 12sep2019 07h00LT
time5=23 #0 to 79, 12sep2019 07h00LT
time6=24 #0 to 79, 12sep2019 07h00LT
time7=25 #0 to 79, 12sep2019 07h00LT
time8=26 #0 to 79, 12sep2019 07h00LT
time9=27 #0 to 79, 12sep2019 07h00LT
time10=28 #0 to 79, 12sep2019 07h00LT
time11=29 #0 to 79, 12sep2019 07h00LT
time12=30 #0 to 79, 12sep2019 07h00LT
time13=31 #0 to 79, 12sep2019 07h00LT
time14=32 #0 to 79, 12sep2019 07h00LT
time15=33 #0 to 79, 12sep2019 07h00LT
time16=34 #0 to 79, 12sep2019 07h00LT
time17=35 #0 to 79, 12sep2019 07h00LT
time18=36 #0 to 79, 12sep2019 07h00LT
time19=37 #0 to 79, 12sep2019 07h00LT
time20=38 #0 to 79, 12sep2019 07h00LT
time21=39 #0 to 79, 12sep2019 07h00LT
time22=40 #0 to 79, 12sep2019 07h00LT
time23=41 #0 to 79, 12sep2019 07h00LT
time24=42 #0 to 79, 12sep2019 07h00LT
# Get o3, layer

z=0

p1 = nc.variables ["T2"][time1,z,:,:]
p2 = nc.variables ["T2"][time2,z,:,:]
p3 = nc.variables ["T2"][time3,z,:,:]
p4 = nc.variables ["T2"][time4,z,:,:]
p5 = nc.variables ["T2"][time5,z,:,:]
p6 = nc.variables ["T2"][time6,z,:,:]
p7 = nc.variables ["T2"][time7,z,:,:]
p8 = nc.variables ["T2"][time8,z,:,:]
p9 = nc.variables ["T2"][time9,z,:,:]
p10 = nc.variables ["T2"][time10,z,:,:]
p11 = nc.variables ["T2"][time11,z,:,:]
p12 = nc.variables ["T2"][time12,z,:,:]
p13 = nc.variables ["T2"][time13,z,:,:]
p14 = nc.variables ["T2"][time14,z,:,:]
p15 = nc.variables ["T2"][time15,z,:,:]
p16 = nc.variables ["T2"][time16,z,:,:]
p17 = nc.variables ["T2"][time17,z,:,:]
p18 = nc.variables ["T2"][time18,z,:,:]
p19 = nc.variables ["T2"][time19,z,:,:]
p20 = nc.variables ["T2"][time20,z,:,:]
p21 = nc.variables ["T2"][time21,z,:,:]
p22 = nc.variables ["T2"][time22,z,:,:]
p23 = nc.variables ["T2"][time23,z,:,:]
p24 = nc.variables ["T2"][time24,z,:,:]

o3c = p5  #p3= 16:00 p4= 17:00 p5=18:00 p6= 19:00 p7=20:00, p8= 21:00, p9=22:00, p10 = 23:00, p11 = 00:00, p12=01:00, p13=02:00
lons = nc.variables ['XLONG'][time1,:,:]
lats = nc.variables ['XLAT'][time1,:,:]
hgt = nc.variables ['HGT'][time1,:,:]

levels = [5, 10,14,16,18,20, 25,30]
alt = [5,10, 14, 18, 20,20,25,30]

plt.contour(lons, lats, hgt, alt, colors='grey', linestyles='dashed',linewidths=1 )

cs = plt.contour(lons, lats, hgt, alt, colors='grey', linestyles='dashed',linewidths=1)

ax.clabel(cs, inline=1,fmt='%1.0f', fontsize=10)

plt.contourf(lons, lats, o3c, levels, colors=('0.1','pink','cyan','blue', 'red', 'yellow', 'gold'))

plt.colorbar()

x = [-79.4,-79.3,-79.2,-79.1,-79.0,-78.9,-78.8]
y = [-3.1,-3.0,-2.9,-2.8,-2.7,-2.6,-2.5]

#!xlim=[-79.1,-78.85]
#!ylim=[-3.0,-2.75]

ax.set_xticks(x)
ax.set_yticks(y)

#!ax.set_xlim(xlim)
#!ax.set_ylim(ylim)


plt.xlabel ('Longitude')
plt.ylabel ('Latitude') 
plt.title("Temperature (°C): 31-Dec-2021 18:00 LT")
fig = 'c:/Cuenca_31Decdata/res/t2_1h_31Dec2021_18_21_LT'
ax.set_aspect(aspect=0.8)
plt.tight_layout()
plt.savefig(fig, dpi=200, facecolor='w', edgecolor='w', orientation='portrait',  format='tiff',transparent=False, pad_inches=0.1,  tigth=True)
plt.show()
