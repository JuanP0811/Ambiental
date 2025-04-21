#Base File for Air Quality and Meteorological Variables

#This code extracts functions and meteorological variables from a nc file 
#and creates plots per hour for one day data (24 PNG files).Then, the code generates a sequence of images
#in a mp4 video file.
#This model starts at 0 (Day 1, 14:00 LT) and ends in 24 (Day 2, 13:00 LT)

#MAIN FUNCTION
    #This function extracts the geographic features from nc and shapefiles, sets the main variables such as 
    #time, altitude, latitude and longitude. As input it has the name of the variable to plot, the hour of the 
    #Air Quality event and both the input and output files paths. 
def main(nombre,hora,dir_in,dir_out):
    #Imports Libraries
    import os
    from netCDF4 import Dataset 
    import cartopy.crs as ccrs
    from cartopy.io.shapereader import Reader
    from cartopy.feature import ShapelyFeature

    #Paths: The function reads the atributes and sets them into variables
    out_path=dir_out
    name=nombre;hour=hora

    #NetCDF and Shapefiles in variables: Copy the path to the file in the shapefile variables 
    nc = Dataset(dir_in)
    urban = r'c:\Users\USER\Devi\Cuenca\cuencaurbano.shp'
    canton = r'c:\Users\USER\Devi\Cuenca\cantoncuenca.shp'
    imd = r'c:\Users\USER\Devi\Cuenca\imdcuenca.shp'#imd is image metadata format.

    #Read and store the collection of shapely geometries and visual characteristics in variables
    urban_zone = ShapelyFeature (Reader(urban).geometries(),ccrs.PlateCarree(),edgecolor='black',facecolor='none',alpha=0.6)#0.8,0.6
    canton_zone = ShapelyFeature (Reader(canton).geometries(),ccrs.PlateCarree(),edgecolor='darkgray',facecolor='none',alpha=0.4)#0.6,0.4
    imd = ShapelyFeature (Reader(imd).geometries(),ccrs.PlateCarree(),edgecolor='darkgrey', facecolor='none',alpha=0.2)#0.35,0.2
    
    #Variable extraction
    #Set the global variables time, var, U and V in form of arrays 
    #U and V call for zonal and meridional wind components and var is where we store the hourly variable data
    global time;global U;global V
    time=list(range(0,24));U=list(range(0,24));V=list(range(0,24));var=list(range(0,24))
    
    #Time, Wind and Variables Functions Run (code after main)
    tiempo();wind(nc);var=variables(name,nc)

    #Longitude, Latitude and Height in  m.a.s.l.
    lons = nc.variables ['XLONG'][time[0],:,:]
    lats = nc.variables ['XLAT'][time[0],:,:]
    hgt = nc.variables ['HGT'][time[0],:,:]

    #Labels: Set the labels for the main variables.
    #Temperature (levels_T:0 to 27 ºC) and Altitude (alt:2500 to 3900 m.a.s.l.)
    levels_T = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    alt = [2500,2700,2900,3100,3300,3500,3700,3900]
    #Plot Function Run (code after main)
    plots(name,hour,var,lons,lats,hgt,alt,levels_T,imd,canton_zone,urban_zone,out_path)
    return 0 #End of main

#PLOTS FUNCTION
    #This function takes the variable, hour of event, longitude, latitude, altitude, levels and geographic features
    #to make the hourly plots. 
def plots(name,hour,var,lons,lats,hgt,alt,levels,imd,canton_zone,urban_zone,out_path):
    #Imports Libraries
    import matplotlib.pyplot as plt
    from matplotlib import cm
    from matplotlib.colors import ListedColormap, LinearSegmentedColormap
    from turtle import width
    import cartopy.crs as ccrs
    print("Creating png figures...")
    for j in range (0,24):
        plt.figure(j)
        #Fixing the axes of the figure using the PlateCarree projection. 
        ax = plt.axes(projection=ccrs.PlateCarree())

        #Map Axes (y:Latitude and x:Longitude)
        x = [-79.4,-79.3,-79.2,-79.1,-79.0,-78.9,-78.8];y = [-3.1,-3.0,-2.9,-2.8,-2.7,-2.6,-2.5]
        xlim=[-79.1,-78.85];ylim=[-3.0,-2.75]

        #Setting ticks and limits
        ax.set_xticks(x);ax.set_yticks(y)
        ax.set_xlim(xlim);ax.set_ylim(ylim)

        #Altitude Contour and Label 
        #a calls for transparency values depending on the input variable (from 0 to 1)
        a=0
        if name=="T"or"W":a=0.4
        elif name=="PM":a=0.25
        cs=ax.contour(lons,lats,hgt,alt,colors='dimgray',linestyles='dashed',linewidths=0.7,alpha=a)
        ax.clabel(cs,inline=True,fmt='%1.0f'+'m',fontsize=8)

        #Adding the shapefile features to the current plot
        ax.add_feature(imd); ax.add_feature(canton_zone); ax.add_feature(urban_zone)

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
            plt.pcolormesh(lons,lats,var[j],vmin=0.1,vmax=250,cmap=newcmp1,shading='gouraud',alpha=1,zorder=1.4)

        elif name=="W":#Colormesh Plot and Black Arrows
            N = "Viento"
            plt.pcolormesh(lons,lats,var[j],vmin=0,vmax=8,cmap='Blues',shading='gouraud',alpha=0.65)
            clb=plt.colorbar(shrink=0.81)
            clb.set_label('m/s',labelpad=-20,y=1.05,rotation=0,fontsize=11)
            plt.quiver(lons,lats,U[j],V[j],transform=ccrs.PlateCarree(),scale=200,width=0.003,minshaft=1.5,color='black')

        #Title and Axes Labels
        plt.xlabel('Longitud',fontsize=12,family='sans-serif')
        plt.ylabel('Latitud',fontsize=12,family='sans-serif')
        
        if j<10:
            plt.title(f"{N}: 31-Dic-2021 {j+14}:00 HL",fontsize=14,family='sans-serif')
        elif j<20:
            plt.title(f"{N}: 01-Ene-2022 0{j-10}:00 HL",fontsize=14,family='sans-serif')
        else:
            plt.title(f"{N}: 01-Ene-2022 {j-10}:00 HL",fontsize=14,family='sans-serif')
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
    print('Figures successfully created in:',out_path)
    return 0#End of plots

#VARIABLES FUNCTION
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
    if hour==00:x='00:00 HL'
    elif hour==18:x='18:00 HL'
    elif hour==21:x='21:00 HL'
    
    #Textbox the organization information.
    text1=AnchoredText('Universidad San Francisco de Quito\nDepartamento de Ingeniería Ambiental',loc=3,prop={'size':6.5},frameon=True)
    ax.add_artist(text1)

    #Textbox with the hour of the event.
    if hour==00:
        text2=AnchoredText('Emisiones de Combustión y Fuegos\nPirotécnicos: 01-Ene-2022 '+x,loc=4,prop={'size':6.5},frameon=True)
    else:
        text2=AnchoredText('Emisiones de Combustión y Fuegos\nPirotécnicos: 31-Dic-2021 '+x,loc=4,prop={'size':6.5},frameon=True)
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

#TIEMPO FUNCTION
    #This function creates an array of hours starting from 19 to 43 (the time interval previously set by the model)
def tiempo():
    for i in time:
        time[i]=i+19
    return 0#End of tiempo

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
    return 0

#Set Input and Output Paths
dir_in=r'c:\Users\USER\Devi\Cuenca\wrfout_2021-12-31_cuenca.nc'
dir_out='c:/Users/USER/Devi/Investigacion/Avances/Cuenca/PNG/PM25/00_LT/'
dir_vid='c:/Users/USER/Devi/Investigacion/Avances/Cuenca/VID/'

#Main and Video Function Run
main('PM',00,dir_in,dir_out)
video('PM',00,dir_out,dir_vid)