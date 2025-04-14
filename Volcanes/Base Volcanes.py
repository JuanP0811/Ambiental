#Base File for Volcano Emissions

#This code extracts functions and meteorological variables from a nc file 
#and creates plots per hour for one day data (22 PNG files).Then, the code generates a sequence of images
#in a mp4 video file.
#This model starts at 0 (Day 1, 10:00 UTC, 05:00 LT) and ends in 21 (Day 2, 7:00 UTC, 2:00 LT)

#MAIN FUNCTION
    #This function extracts the geographic features from nc and shapefiles, sets the main variables such as 
    #time, altitude, latitude and longitude. As input it has the name of the variable to plot, the hour of the 
    #Air Quality event and both the input and output files paths. 
def main(dir_in,dir_out):
    #Imports Libraries
    from black import Encoding
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap
    import numpy as np
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    from matplotlib.colors import LinearSegmentedColormap
    from netCDF4 import Dataset 
    import cartopy.crs as ccrs
    from cartopy.io.shapereader import Reader
    import matplotlib.patches as mpatches
    import shapefile

    #Paths: The function reads the atributes and sets them into variables
    out_path=dir_out

    #NetCDF and Shapefiles in variables: Copy the path to the file in the shapefile variables 
    nc = Dataset(dir_in)
    spf= shapefile.Reader(r'c:\Users\Usuario\OneDrive - Universidad San Francisco de Quito\Asistencia Investigacion\Volcanes\Zona Urbana\zonaurbanafinal2014.shp',encoding='latin-1')
    records=spf.shapeRecords()# Get the shapefile records (coordinates of points)
    polygons=list(range(22))
    for i in range(22):#22 polygons, 22 cities
        polygons[i]=records[i]#Store the polygons into an array

    #Longitude, Latitude and Height in  m.a.s.l.
    lons = nc.variables ['lon']
    lats = nc.variables ['lat']
    n=len(nc.variables ['time'])
    
    #Date and PM variables
    date=list(range(n));p0=list(range(n));p2=list(range(n));p3=list(range(n));p4=list(range(n))
    
    #Storing Variables from nc file (code after main)
    date=time(nc,n);p0=variables(0,nc,n);p2=variables(200,nc,n);p3=variables(300,nc,n);p4=variables(400,nc,n)

    print("Creating png figures...")
    for j in range (n):
        plt.figure(j)
        #Fixing the axes of the figure using the PlateCarree projection. 
        ax = plt.axes(projection=ccrs.PlateCarree())

        #Adding the shapefile features to the current plot
        ax.add_feature(cfeature.COASTLINE,edgecolor='dimgrey',facecolor='none'); ax.add_feature(cfeature.BORDERS,edgecolor='dimgrey',facecolor='none')
        
        #Adding cities features
        for k in range (22):
            urban(polygons[k],ax)

        #Map Axes (y:Latitude and x:Longitude)
        x = [-81,-80,-79,-78,-77,-76,-75];y = [-5,-4,-3,-2,-1,0,1];y_l=['-05','-04','-03','-02','-01','0','01']
        xlim = [-81.5,-75];ylim = [-5,1.5]

        #Setting ticks and limits
        ax.set_xticks(x);ax.set_yticks(y)
        ax.set_xticklabels(x,ha='center');ax.set_yticklabels(y_l)
        ax.set_xlim(xlim);ax.set_ylim(ylim)

        #colorlist0=["white","deepskyblue","dodgerblue","royalblue","blue","navy"]
        colorlist2=["white","lawngreen"]#P2:"white","lime","limegreen" P3:"paleturquoise","cyan","darkturquoise"
        colorlist3=["white","gold"]#P3,P2="white","orange","darkorange"
        colorlist4=["white","darkorange"]#P2:"white","red" P3:"white","gold"

        #Colormap for C_FL200
        cmp2 = LinearSegmentedColormap.from_list('testCmap2',colors=colorlist2, N=256)
        my_cmap2 = cmp2(np.arange(cmp2.N))#Get and arrange the color codes from the colormap.
        my_cmap2[:,-1] = np.linspace(0, 1, cmp2.N)#Add transparecy alpha values from 0 (fully transparent) to 1 (opaque) starting from the right.
        newcmp2 = ListedColormap(my_cmap2)#Set a new color map with transparency values.

        #Colormap for C_FL300
        cmp3 = LinearSegmentedColormap.from_list('testCmap3',colors=colorlist3, N=256)
        my_cmap3 = cmp3(np.arange(cmp3.N))
        my_cmap3[:,-1] = np.linspace(0, 1, cmp3.N)
        newcmp3 = ListedColormap(my_cmap3)

        #Colormap for C_FL400
        cmp4 = LinearSegmentedColormap.from_list('testCmap4',colors=colorlist4, N=256)
        my_cmap4 = cmp4(np.arange(cmp4.N))
        my_cmap4[:,-1] = np.linspace(0, 1, cmp4.N)
        newcmp4 = ListedColormap(my_cmap4)

        #Thickness
        plt.pcolormesh(lons,lats,p0[j]*10000,vmin=0.001,vmax=5,cmap='Greys',shading='gouraud',alpha=0.85)#0.00016492733
        clb=plt.colorbar(shrink=0.9,location='right',format='%1.0f',anchor=(0.0,0.1))
        clb.set_label('cm\n$[x10^{-4}]$',labelpad=-21,y=1.11,rotation=0,fontsize=9.5,family='sans-serif')
        
        #Concentration at flight level C_FL200
        plt.pcolormesh(lons,lats,p2[j],vmin=1e-10,vmax=1.8e-06,cmap=newcmp2,edgecolors='darkgreen',shading='gouraud',label='C_FL200')#1.8e-05
        #Concentration at flight level C_FL300
        plt.pcolormesh(lons,lats,p3[j],vmin=1e-10,vmax=1.7e-06,cmap=newcmp3,edgecolors='darkorange',shading='gouraud',label='C_FL300')#1.7e-05
        #Concentration at flight level C_FL400
        plt.pcolormesh(lons,lats,p4[j],vmin=1e-21,vmax=1.4e-18,cmap=newcmp4,edgecolors='darkred',shading='gouraud',label='C_FL400')#1.4e-18
        
        #Legend
        pop_a = mpatches.Patch(color='lawngreen',label='FL200($\simeq$6.1 km)')#P2:limegreen,P3=darkturquoise
        pop_b = mpatches.Patch(color='gold',label='FL300($\simeq$9.1 km)')#P2:darkorange,P3=darkorange
        pop_c = mpatches.Patch(color='darkorange',label='FL400($\simeq$12.2 km)')#P2:red,P3=gold

        plt.legend(handles=[pop_a,pop_b,pop_c],loc='upper right',bbox_to_anchor=(0.95,0.3),ncol=1,handlelength=1,handleheight=0.5,labelspacing=0.3,fontsize='small',title='Nube de Ceniza',title_fontsize='small')
        
        #Adding the volcano polygon and name
        volcan(ax,-78.34059,-2.00511,'Sangay')

        #Title, Axes Labels and Text Box
        plt.xlabel('Longitud',fontsize=12,family='sans-serif')
        plt.ylabel('Latitud',fontsize=12,family='sans-serif')
        plt.title(f'Sedimento de Ceniza: {date[j]}',fontsize=14,family='sans-serif')
        text(ax)

        #Saving the figure
        if j<10:
            plt.savefig(out_path+f"F_00A{j}.png",dpi=700,facecolor='w',edgecolor='w',orientation='portrait',format='png',transparent=False,pad_inches=0.1,bbox_inches="tight")
        else:
            plt.savefig(out_path+f"F_0A{j}.png",dpi=700,facecolor='w',edgecolor='w',orientation='portrait',format='png',transparent=False,pad_inches=0.1,bbox_inches="tight")
        print(f"Figure:{j} succesfully created")
        plt.close(j)
    
    print('Figures successfully created in:',out_path)

    #Plot Function Run (code after main)
    #plots(lons,lats,out_path)
    return 0 #End of main

#VARIABLES FUNCTION
    #This function extracts the desired variables from the nc file and sets them on a list named p. Notice that time array is
    #not used, since the colum variables take as reference the model time (0 to 21 hours).
    #For the Column, we consider differt flight levels.v
def variables(z,nc,n):
    p=list(range(n))
    #THICKNESS (cm)
    if z==0:
        for i in range(n):
            p[i]=nc.variables ["THICKNESS"][i,:,:]
    # C_FL100 (gr/m3)
    if z==100:
        for i in range(n):
            p[i]=nc.variables ["C_FL100"][i,:,:]
    # C_FL200 (gr/m3) 
    elif z==200:
        for i in range(n):
            p[i]=nc.variables ["C_FL200"][i,:,:]
    #C_FL300 (gr/m3) 
    elif z==300:
        for i in range(n):
            p[i]=nc.variables ["C_FL300"][i,:,:]
    #C_FL400 (gr/m3) 
    elif z==400:
        for i in range(n):
            p[i]=nc.variables ["C_FL400"][i,:,:]
    return p #End of variables
#TIME FUNCTION
#This function extracts the values of years, months, days and hours from the nc file and stores them into an array
def time(nc,n):
    local_time= utc_local(nc,n)#Get dates in local time
    #Create arrays to store time components
    date=list(range(n));year=list(range(n));month=list(range(n));day=list(range(n));hour=list(range(n))
    #Dictionary for month number to string
    dic_m={1:"Ene",2:"Feb",3:"Mar",4:"Abr",5:"May",6:"Jun",7:"Jul",8:"Ago",9:"Sep",10:"Oct",11:"Nov",12:"Dic"}
    for i in range(n):
        #Year
        year[i] = local_time[i].year
        #Month
        m = local_time[i].month
        month[i] = dic_m[m]
        #Day
        d = local_time[i].day
        if d<10: day[i]=f'0{d}'
        else: day[i]=d
        #Hour
        h = local_time[i].hour
        if h<10: hour[i]=f'0{h}'
        else: hour[i]=h
        date[i]=f'{day[i]}-{month[i]}-{year[i]} {hour[i]}:00 LT'
    return date#End of time
#UTC_TO_LOCAL FUNCTION
#This function extracts the time variables from the nc file and changes them from UTC to Local Time (America/Guayaquil)
def utc_local(nc,n):
    from netCDF4 import num2date
    from datetime import datetime
    from dateutil import tz
    #Extract time from nc file and change it from num to a date format
    time_var = nc.variables['time']
    dtime = num2date(time_var[:],time_var.units)
    #Store year, month, day and hour into arrays and concatenate it to a string array
    date=list(range(n));year=list(range(n));month=list(range(n));day=list(range(n));hour=list(range(n))
    for i in range(n):
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
    #Setting Time Zones
    from_zone= tz.gettz('UTC')
    to_zone= tz.gettz('America/Guayaquil')
    #Replace dates from UTC to Local Time and store then in date arrays
    utc=list(range(n));local=list(range(n))
    for i in range(n):
        utc[i]= datetime.strptime(date[i],'%Y-%m-%d %H:%M:%S')
        utc[i]= utc[i].replace(tzinfo=from_zone)
        local[i]= utc[i].astimezone(to_zone)
    return local#End of UTC_Local
#TEXT BOX FUNCTION
    #This function creates a textbox with the event and institutional information.
def text(ax):
    #Imports Libraries
    from matplotlib.offsetbox import AnchoredText
    #Textbox the organization information.
    text1=AnchoredText(f'Universidad San Francisco de Quito\nDepartamento de Ingeniería Ambiental',loc=4,prop={'size':6.5},frameon=True)
    #text2=AnchoredText(f'Quito',loc='lower left',bbox_to_anchor=(5,0.7),prop={'size':5},frameon=False)
    ax.add_artist(text1)
    #ax.add_artist(text2)
    return 0#End of text
#URBAN FUNCTION
    #This function takes a polygon, representing a main urban area, and sets it in the plot. Additionally, it puts a text label next to 
    #the main cities location: Quito, Guayaquil and Cuenca.
def urban(polygon,ax):
    from matplotlib.offsetbox import AnchoredText
    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    import numpy as np 
    n=len(polygon.shape.points)#Get the lenght of each polygon
    xy=list(range(n))#Array of x an y points
    for i in range(n):
        xy[i]=polygon.shape.points[i]#Store the polygon points into an array
    #print(xy[i])
    xs,ys = zip(*xy)#Create lists of x and y values
    plt.plot(xs,ys,c='dimgray',linewidth=0.6,alpha=0.85,transform=ccrs.PlateCarree()) 
    plt.fill(xs,ys,facecolor='black',transform=ccrs.PlateCarree())
    ciu=polygon.record[5]
    if ciu=='QUITO':
        text=AnchoredText('Quito',loc='lower left',prop=dict(size=5.5),frameon=False,bbox_to_anchor=(0.46,0.71),bbox_transform=ax.transAxes,alpha=0.3,zorder=1.1)
        ax.add_artist(text)
    elif ciu=='GUAYAQUIL':
        text=AnchoredText('Guayaquil',loc='lower left',prop=dict(size=5.5),frameon=False,bbox_to_anchor=(0.243,0.41),bbox_transform=ax.transAxes,alpha=0.3,zorder=1.1)#0.243,0.097
        ax.add_artist(text)
    elif ciu=='CUENCA':
        text=AnchoredText('Cuenca',loc='lower left',prop=dict(size=5.5),frameon=False,bbox_to_anchor=(0.39,0.3),bbox_transform=ax.transAxes,alpha=0.3,zorder=1.1)
        ax.add_artist(text)
    return 0
#VOLCAN FUNCTION
    #This function draws a polygon representing the volcano, sets it in the plot. Additionally, it puts a text label with the volcano name.
def volcan(ax,x,y,name):
    import matplotlib.pyplot as plt
    from matplotlib.offsetbox import AnchoredText
    r=0.07
    x1=x+r;x2=x;x3=x-r
    y1=y-(r*2);y2=y;y3=y-(r*2)
    #poly_coords=[(-77.93233,-1.78889),(-77.98233,-1.68889),(-78.03233,-1.78889)]
    poly_coords=[(x1,y1),(x2,y2),(x3,y3)]
    ax.add_patch(plt.Polygon(poly_coords,fill=True,facecolor='brown',edgecolor='lightgray',linewidth=0.65,alpha=1))#P2:facecolor=yellow, edgecolor=dimgray,P1:facecolor=brown, edgecolor=lightgray,P3:facecolor=brown, edgecolor=white
    text=AnchoredText(name,loc='lower left',prop=dict(size=6),frameon=False,bbox_to_anchor=(0.479,0.423),bbox_transform=ax.transAxes)
    ax.add_artist(text)
    return 0
#VIDEO FUNCTION
    #This function reads the png files and creates the image sequence video as an mp4 file. Takes as input the variable
    #name, the hour of the event, the direction to the png files and the direction to store the video.
def video(name,step,dir_in,dir_out):
    #Libraries Import
    import cv2
    import numpy as np
    import os
    from cv2 import destroyAllWindows
    #Set the video timestep
    t=step
    #Set the variable name as a string
    x=name
    #In and Out Paths
    path = dir_in; out_path = dir_out; out_video_name = x+'.mp4'
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
    video = cv2.VideoWriter(video_name,fourcc,t,size)
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
dir_in =r'c:\Users\Usuario\OneDrive - Universidad San Francisco de Quito\Asistencia Investigacion\Volcanes\Sangay_ejemplo.nc'
dir_out='c:/Users/Usuario/Documents/Volcanes/PNG/P1/'
dir_vid='c:/Users/Usuario/Documents/Volcanes/VID/'

#Main and Video Function Run
main(dir_in,dir_out)
video('PM_Sangay_P1',0.75,dir_out,dir_vid)