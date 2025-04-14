#Prueba y lectura de variables archivos nc Volcanes
from netCDF4 import Dataset
from netCDF4 import num2date
from datetime import datetime, timezone
#from zoneinfo import ZoneInfo 
from dateutil import tz
import numpy as np 
import shapefile
from shapely.geometry import MultiPolygon,Polygon

nc = Dataset(r'C:\Users\Usuario\OneDrive - Universidad San Francisco de Quito\Asistencia Investigacion\Volcanes\Sangay_ejemplo.res.nc')
spf= shapefile.Reader(r'c:\Users\Usuario\OneDrive - Universidad San Francisco de Quito\Asistencia Investigacion\Volcanes\SHP\nxcantones.shp')
shapes=spf.shapes()#Get the ashape names
print(shapes)
fields=spf.fields
print(fields)
#records=spf.records[2][0:3]
#records=spf.shapeRecords(1)
#print(records)
#imd = r'c:\Users\Usuario\Documents\Cuenca\imdcuenca.shp'#imd is image metadata format.
    #cant=shapefile.Reader(r'c:\Users\Usuario\Documents\Volcanes\Poblados\poblados.shp')
    #Read and store the collection of shapely geometries and visual characteristics in variables
    #cantones_zone = ShapelyFeature(Reader(cantones).geometries(),ccrs.PlateCarree(),edgecolor='k',facecolor='none',linewidth=1)#0.6,0.4
    #shape = shapefile.Reader(r'c:\Users\Usuario\Documents\Ciudades\ciudades.shp')
    #print(shape.shapeTypeName)
    #cantones_zone = ShapelyFeature (Reader(cantones).geometries(),ccrs.PlateCarree(),edgecolor='darkgray',facecolor='none',alpha=1)#0.6,0.4
    #md = ShapelyFeature (Reader(imd).geometries(),ccrs.PlateCarree(),edgecolor='darkgrey',facecolor='none',alpha=0.2)#0.35,0.2
    #points = list(cartopy.io.shapereader.Reader(r'c:\Users\Usuario\OneDrive - Universidad San Francisco de Quito\Asistencia Investigacion\Volcanes\SHP\nxcantones.shp').geometries())
    #ax.scatter([point.x for point in points],
           #[point.y for point in points],
           #transform=ccrs.PlateCarree())
        #Variable extraction

#records=spf.shapeRecords()
#records=spf.records[0][1:3]
#print(records)
#print(fields)
#print(shapes)
#print(dir(shapes[0]))
#first = geomet[0]
#first.shape.points
#shapes=MultiPolygon(load_shapes(spf))
#print(spf)
#Time: From 10 am 13/06/2022 to 7 am 14/13/2022
#22 elements in Time, starting from hour 10 Day 1 to hour 31 Day 2 

#print(nc)
#TITLE: Fall3d 7.1 results
# float32 C_PM10_GRND(time, lat, lon), float32 C_PM20_GRND(time, lat, lon), float32 COL_MASS(time, lat, lon), 
# float32 COL_MASS_SO2(time, lat, lon), float32 COL_MASSPM05(time, lat, lon), float32 COL_MASSPM10(time, lat, lon), 
# float32 COL_MASSPM20(time, lat, lon), float32 C_FL050(time, lat, lon), float32 C_FL100(time, lat, lon), 
# float32 C_FL150(time, lat, lon), float32 C_FL200(time, lat, lon), float32 C_FL250(time, lat, lon), 
# float32 C_FL300(time, lat, lon), float32 C_FL350(time, lat, lon), float32 C_FL400(time, lat, lon), 
# float32 AOD(time, lat, lon)

# Keys

#print(nc.variables.keys())
#dict_keys=(['lon', 'lat', 'alt', 'time', 'times', 'diameter', 'density', 'sphericity', 'TOPOGRAPHY', 
#           'LOAD', 'WET', 'THICKNESS', 'C_GRND', 'C_PM05_GRND', 'C_PM10_GRND', 'C_PM20_GRND', 'COL_MASS', 
#           'COL_MASS_SO2', 'COL_MASSPM05', 'COL_MASSPM10', 'COL_MASSPM20', 'C_FL050', 'C_FL100', 'C_FL150', 
#           'C_FL200', 'C_FL250', 'C_FL300', 'C_FL350', 'C_FL400', 'AOD'])
#float32 time(time)
# units: hours since 2022-06-13 00:00:0.0
# description: time after 0000UTC
# unlimited dimensions: time
# current shape = (22,)

#Descriptions
"""p1=nc.variables['C_FL100']
print(p1)
#print(p1[12])
#p2=nc.variables ['times']
print(p2)
def time(nc):
    t=list(range(0,22))
    for i in range(0,22):
        t[i]=nc.variables ["time"][i]
    return t 
t1=time(nc)
#for i in t1:
    #print(i)
print(nc.variables["times"][0])
def date(nc):
    d=[]
    for i in range(0,22):
        d.append(nc.variables["times"][i])
        return d
fecha=date(nc)
for j in fecha:
    print(j)"""
#SHAPEFILES TEST

#UTC TO LOCAL FUNCTION
"""time_var = nc.variables['time']
lats = nc.variables ['lat']
print(len(lats))
print(time_var[0])
dtime = num2date(time_var[:],time_var.units)
year = list(range(0,22));month = list(range(0,22));day = list(range(0,22));hour = list(range(0,22))
date=list(range(0,22))
for i in range(0,22):
    year[i] = dtime[i].year
    m=dtime[i].month
    if m<10: month[i]=f'0{m}'
    else: month[i]=m
    d=dtime[i].day
    if d<10: day[i]=f'0{d}'
    else: day[i]=d
    h = dtime[i].hour
    if h<10: hour[i]=f'0{h}'
    else: hour[i]=h
    date[i]=f'{year[i]}-{month[i]}-{day[i]} {hour[i]}:00:00'
print (date)
#Time Zones
from_zone= tz.gettz('UTC')
to_zone= tz.gettz('America/Guayaquil')
#UTC to Local
utc=list(range(0,22));local=list(range(0,22))
for i in range(0,22):
    utc[i] = datetime.strptime(date[i],'%Y-%m-%d %H:%M:%S')
    utc[i]=utc[i].replace(tzinfo=from_zone)
    local[i] = utc[i].astimezone(to_zone)

#Store date in arrays in Time Function
date_n=list(range(0,22));year_n = list(range(0,22));month_n = list(range(0,22));day_n = list(range(0,22));hour_n = list(range(0,22))
for i in range(0,22):
    year_n[i]= local[i].year
    month_n[i]= local[i].month
    day_n[i]= local[i].day
    hour_n[i]= local[i].hour
    date_n[i]=f'{year_n[i]}-{month_n[i]}-{day_n[i]} {hour_n[i]}:00'
    print(date_n[i])"""

#print(utc)
#print(local)
#print(local.hour)
#print(utc.hour)
#print (dtime)
#print(dtime[21].month)
#print(dtime[21].day)
#print(dtime[21].hour)
#print(p2.mean())
#for i in p1:
    #print(p1)
#time=nc.variables['time']
#t=time[:]
#print (t[21],t[1],t[2])
#print(len(time))
#current shape = (22, 199, 199), unlimited dimensions: time
#THICKNESS: Ground deposit thickness, units: cm, max = 0.61309135, mean= 0.00016492733
#C_PM10_GRND: PM10 concentration at ground (1st layer), units: gr/m3
#C_PM20_GRND: PM20 concentration at ground (1st layer), units: gr/m3
#COL_MASS: Particle column mass, units: gr/m2
#COL_MASS_SO2: Column mass for SO2, units: kg/m2
#COL_MASSPM05: PM05 column mass, gr/m2
#C_FL100: Concentration at flight level C_FL100, gr/m3, max= 0.30683082 mean= 5.434234e-05
#C_FL200: Concentration at flight level C_FL200, gr/m3, max= 0.6509737, mean= 1.773318e-05
#C_FL300: Concentration at flight level C_FL200, gr/m3, max= 1.1840523, mean= 1.6823476e-05
#C_FL400: Concentration at flight level C_FL200, gr/m3, max= 1.0242233e-13, mean= 1.3533379e-18
#AOD: Particle Aerosol Optical Depth at 0.5 micron, units: -
#lon: Longitude, units: degrees_east (east positive)
#lat: Latitude, units: degrees_north (north positive)
#alt: Altitude, units: m (above sea lavel)

#for d in nc.dimensions.items():
    #print(d)
#time=nc.variables["Time"]
#t=time[:]
#z1=nc.variables["z"]
#z2=z1[:]
#print(time.dimensions)
#print(time.shape)
#print(t)
#print(t[0])
#print(z1.dimensions)
#print(z1.shape)
#print(z2)
#print(z2[0])
#print(nc.variables['T2'])
#print(nc.variables['HGT'])

"""
#PLOTS FUNCTION
    #This function takes the variable, hour of event, longitude, latitude, altitude, levels and geographic features
    #to make the hourly plots. 
def plots(cantones_zone,out_path):
    #Imports Libraries
    import matplotlib.pyplot as plt
    from matplotlib import cm
    from matplotlib.colors import ListedColormap, LinearSegmentedColormap
    from turtle import width
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature

    #print("Creating png figures...")
    #for j in range (0,22):
        #plt.figure(j)
    cant_z=cantones_zone
    plt.figure()
        #Fixing the axes of the figure using the PlateCarree projection. 
    ax = plt.axes(projection=ccrs.PlateCarree())

        #Adding the shapefile features to the current plot
    ax.add_feature(cfeature.COASTLINE,edgecolor='dimgrey',facecolor='none'); ax.add_feature(cfeature.BORDERS,edgecolor='dimgrey',facecolor='none')
    ax.add_feature(cant_z)
        #Map Axes (y:Latitude and x:Longitude)
    x = [-81,-80,-79,-78,-77,-76,-75];y = [-5,-4,-3,-2,-1,0,1]
    xlim=[-81.5,-75];ylim=[-5,1.5]

        #Setting ticks and limits
    ax.set_xticks(x);ax.set_yticks(y)
    ax.set_xlim(xlim);ax.set_ylim(ylim)

    #Plot Style and Colorbar
        N=str()#Plot Name
        if name=="T":#Contour Filled Plot
            N="Temperatura"
            plt.contourf(lons,lats,var[j],levels,cmap='coolwarm',alpha=0.9)
            clb=plt.colorbar(shrink=0.81)
            clb.set_label('ºC',labelpad=-28,y=1.05,rotation=0,fontsize=11,family='sans-serif')
        elif name=="PM":#Colormesh Plot
            N="PM$_{2.5}$"
            colorlist=["ghostwhite","palegreen","lightgreen","lawngreen","greenyellow","yellow","gold","orange","darkorange","chocolate","brown","maroon"]
            newcmp = LinearSegmentedColormap.from_list('testCmap',colors=colorlist,N=256)
            plt.pcolormesh(lons,lats,var[j],vmin=0.1,vmax=250,cmap=newcmp,shading='gouraud',alpha=1,zorder=1.4)
            clb=plt.colorbar(shrink=0.81)
            clb.set_label('$µg/m^3$',labelpad=-29,y=1.06,rotation=0,fontsize=11,family='sans-serif')
            
            newcmp1 = LinearSegmentedColormap.from_list('testCmap',colors=colorlist, N=256)
            plt.pcolormesh(lons,lats,var[j],vmin=0.1,vmax=250,cmap=newcmp,shading='gouraud',alpha=1,zorder=1.4)

    #Title and Axes Labels
        plt.xlabel('Longitud',fontsize=12,family='sans-serif')
        plt.ylabel('Latitud',fontsize=12,family='sans-serif')
        
        if j<10:
            plt.title(f"31-Dic-2021 {j+14}:00 LT",fontsize=14,family='sans-serif')
        else:
            plt.title(f"1-Ene-2022 {j-10}:00 LT",fontsize=14,family='sans-serif')
        #Text Box Function Run
        text(ax,hour)
        #Storing the figure in a desired folder
        ax.set_aspect(aspect=0.8)
        plt.tight_layout()
        if j<10:
            plt.savefig(out_path+name+f"_00A{j}.png",dpi=700,facecolor='w',edgecolor='w',orientation='portrait',format='png',transparent=False,pad_inches=0.1,bbox_inches="tight")
            print(out_path+name+f"_00A{j}.png")
        else:
            plt.savefig(out_path+name+f"_0A{j}.png",dpi=700,facecolor='w',edgecolor='w',orientation='portrait',format='png',transparent=False,pad_inches=0.1,bbox_inches="tight")
            print(out_path+name+f"_0A{j}.png")
        plt.close(j)
    plt.savefig(out_path+f"_00A1.png",dpi=700,facecolor='w',edgecolor='w',orientation='portrait',format='png',transparent=False,pad_inches=0.1,bbox_inches="tight")
    plt.close()
    #print('Figures successfully created in:',out_path)
        return 0#End of plots"""

"""VARIABLES FUNCTION
    #This function extracts the desired variables from the nc file and sets them on a list named p.
    def variables(name,nc):
    p=list(range(0,24))
    z=0#For the PM, we consider only the values at surface level.
    
    #Temperature (ºC)
    if name=="T":
        for i in p:
            p[i]=nc.variables ["T2"][time[i],:,:]-273.15 
    #PM 2.5 (UG/M3) 
    elif name=="PM":
        for i in p:
            p[i]=nc.variables ["PM2_5_DRY"][time[i],z,:,:]
    #Wind (m/s)
    elif name=="W":
        for i in p:
            p[i]=((U[i]**2) + (V[i]**2))**0.5
    return p #Returns the array

#TEXT FUNCTION
    #This function creates a textbox with the event and institutional information.
def text(ax,hora):
    #Imports Libraries
    from matplotlib.offsetbox import AnchoredText
    import cartopy.crs as ccrs

    #Setting the Hour of the Air Quality Event for the textbox 2
    hour=hora
    x=0
    if hour==00:x='00:00 LT'
    elif hour==18:x='18:00 LT'
    elif hour==21:x='21:00 LT'

    #Textbox the organization information.
    text1=AnchoredText('Universidad San Francisco de Quito\nDepartamento de Ingeniería Ambiental',loc=3,prop={'size':6.5},frameon=True)
    ax.add_artist(text1)

    #Textbox with the hour of the event.
    text2=AnchoredText('Quema de Monigotes: '+x,loc=4,prop={'size':6.5},frameon=True)
    ax.add_artist(text2)
    return 0#End of text

#WIND FUNCTION
    #This function reads the wind components and saves them into global arrays.
def wind(nc):
    for i in U:
        U[i]=nc.variables['U10'][time[i],:,:]
    for i in V:
        V[i]=nc.variables['V10'][time[i],:,:]
    return 0#End of text

#VIDEO FUNCTION
    #This function reads the png files and creates the image sequence video as an mp4 file. Takes as input the variable
    #name, the hour of the event, the direction to the png files and the direction to store the video.
def video(nombre,hora,dir_in,dir_out):
    #Libraries Import
    import cv2
    import numpy as np
    import os
    from cv2 import destroyAllWindows
    #The function reads the variable name and hour atributes and sets them into variables
    name=nombre
    hour=hora
    #Set the variable name as a string
    x=''
    if name=='T':x='TEMP'
    elif name=='PM':x='PM'
    elif name=='W':x='WIND'
    #Set the time of the event name as a string
    y=0
    if hour==00:y='_00_LT'
    elif hour==18:y='_18_LT'
    elif hour==21:y='_21_LT'
    #In and Out Paths
    path = dir_in;out_path = dir_out;out_video_name = x+y+'.mp4'
    video_name = out_path + out_video_name
    #Read and add the images to a pre image array
    pre_img_array = os.listdir(path)
    #Create a void array to store the images 
    img = []
    #Add the path to the name of each file in img array
    for i in pre_img_array:
        i=path+i
        img.append(i)
    #Create the video variables for CODEC and size from the first image
    fourcc= cv2.VideoWriter_fourcc(*'mp4v')
    frame= cv2.imread(img[0])
    #Create an array of three elements (height, width, layers)
    size=list(frame.shape)
    #Delete the layer element
    del size[2]
    #Reverse the order of the remaining elements (width, height)
    size.reverse()
    #Use the method VideoWriter to set the path+name, CODEC, fps (frames per second) and size
    video = cv2.VideoWriter(video_name,fourcc,0.7,size)
    #Loop to set each image to the video in a sequence, 24 images in total
    for j in range(len(img)):
        video.write(cv2.imread(img[j]))
    #Show video output location
    print('Video successfully created as:',video_name)
    #Closes the Video Writer
    video.release()
    #Close any open window, end of the program
    cv2.destroyAllWindows()
    return 0"""