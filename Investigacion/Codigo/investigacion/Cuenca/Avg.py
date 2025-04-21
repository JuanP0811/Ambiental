#PM2.5 Daily Averages
#Cuenca from DIC 31, 2018 14h00 LT to JAN 1, 2019 14h00 LT
# Libraries Import
#MANOO
def main(hour,dir_in,dir_out):
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

    out_path=dir_out
    # Open the NetCDF file and Store the Shapefiles in variables
    nc = Dataset(dir_in)
    urban = r'c:\Users\USER\Devi\Cuenca\cuencaurbano.shp'
    canton = r'c:\Users\USER\Devi\Cuenca\cantoncuenca.shp'
    imd = r'c:\Users\USER\Devi\Cuenca\imdcuenca.shp'#imd is image metadata format.

    # Reading and storing the collection of shapely geometries and visual characteristics in variables
    urban_zone = ShapelyFeature (Reader(urban).geometries(),ccrs.PlateCarree(),edgecolor='black',facecolor='none',alpha=0.6)
    canton_zone = ShapelyFeature (Reader(canton).geometries(),ccrs.PlateCarree(),edgecolor='darkgray',facecolor='none',alpha=0.4)
    imd = ShapelyFeature (Reader(imd).geometries(),ccrs.PlateCarree(),edgecolor='darkgrey', facecolor='none',alpha=0.2)

    #TIME IN HOURS
    time=list(range(0,24))
    if hour==00:
        for i in time:
            time[i]=i+17 #(starts at 12:00 21 Dic 2021, ends at 12:00 01 Ene 2022)
    elif hour==18:
        for i in time:
            time[i]=i+11 #(starts at 06:00 21 Dic 2021, ends at 06:00 01 Ene 2022)
    elif hour==21:
        for i in time:
            time[i]=i+14 #(starts at 09:00 21 Dic 2021, ends at 09:00 01 Ene 2022)

    z=0
    sum=0
    average=0
    #PM 2.5 IN UG/M3 
    PM=list(range(0,24))
    for i in PM:
        PM[i]=nc.variables ["PM2_5_DRY"][time[i],z,:,:]
        sum+=PM[i]
    average=sum/24

    #Labels: Altitude (2500 to 3900 ºC)
    alt = [2500,2700,2900,3100,3300,3500,3700,3900]

    #LONGIITUDE, LATITUDE AND HEIGHT IN M.A.S.L.
    lons = nc.variables ['XLONG'][time[0],:,:]
    lats = nc.variables ['XLAT'][time[0],:,:]
    hgt = nc.variables ['HGT'][time[0],:,:]

    #PM2.5 Average Plots
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
    colorlist=["ghostwhite","palegreen","lightgreen","lawngreen","greenyellow","yellow","orange","darkorange","chocolate","brown","maroon"]
    newcmp = LinearSegmentedColormap.from_list('testCmap',colors=colorlist,N=256)
    plt.pcolormesh(lons,lats,average,vmin=0,vmax=60,cmap=newcmp,shading='gouraud',alpha=1,zorder=1.4)
    clb=plt.colorbar(shrink=0.81)
    clb.set_ticks([0,5,10,15,20,25,30,35,40,45,50,55,60])
    clb.set_ticklabels(['0','5','10','15 (OMS)','20','25','30','35','40','45','50 (NECA)','55','60'])
    clb.set_label('$µg/m^3$',labelpad=-55,y=1.08,rotation=0,fontsize=11,family='sans-serif')
    #Title and Axes Labels
    plt.xlabel('Longitud',fontsize=12,family='sans-serif')
    plt.ylabel('Latitud',fontsize=12,family='sans-serif')
    N="PM$_{2.5}$"

    if hour==00:
        plt.title(f"{N}:Promedio 24 horas\n31-Dic-2021 12:00 HL a 01-Ene-2022 12:00 HL",fontsize=12,family='sans-serif')
    elif hour==18:
        plt.title(f"{N}:Promedio 24 horas\n31-Dic-2021 06:00 HL a 01-Ene-2022 06:00 HL",fontsize=12,family='sans-serif')
    elif hour==21:
        plt.title(f"{N}:Promedio 24 horas\n31-Dic-2021 09:00 HL a 01-Ene-2022 09:00 HL",fontsize=12,family='sans-serif')

        #Textbox the organization information.
    text1=AnchoredText('Universidad San Francisco de Quito\nDepartamento de Ingeniería Ambiental',loc=3,prop={'size':6.5},frameon=True)
    ax.add_artist(text1)

    #Text Box
    x=0
    if hour==00:x='00:00 HL'
    elif hour==18:x='18:00 HL'
    elif hour==21:x='21:00 HL'
    if hour==00:
        text2=AnchoredText('Emisiones de Combustión y Fuegos\nPirotécnicos: 01-Ene-2022 '+x,loc=4,prop={'size':6.5},frameon=True)
    else:
        text2=AnchoredText('Emisiones de Combustión y Fuegos\nPirotécnicos: 31-Dic-2021 '+x,loc=4,prop={'size':6.5},frameon=True)
    ax.add_artist(text2)

    ax.set_aspect(aspect=0.8)
    plt.tight_layout()
    plt.savefig(out_path+f"/{hour}.png",dpi=700,facecolor='w',edgecolor='w',orientation='portrait',format='png',transparent=False,pad_inches=0.1,bbox_inches="tight")
    print(out_path+f"/{hour}.png")
    plt.close()
    print('Figure successfully created in:',out_path)
    return 0#End of main

#Set Input and Output Paths
dir_in=r'c:\Users\USER\Devi\Cuenca\wrfout_2021-12-31_cuenca.nc'
dir_out=r'c:\Users\USER\Devi\Investigacion\Avances\Cuenca\AVG'

#Main and Video Function Run
main(00,dir_in,dir_out)

#Set Input and Output Paths
dir_in1=r'c:\Users\USER\Devi\Cuenca\wrfout_2021-12-31_18_cuenca.nc'
dir_out1=r'c:\Users\USER\Devi\Investigacion\Avances\Cuenca\AVG'

#Main and Video Function Run
main(18,dir_in1,dir_out1)

#Set Input and Output Paths
dir_in2=r'c:\Users\USER\Devi\Cuenca\wrfout_2021-12-31_21_cuenca.nc'
dir_out2=r'c:\Users\USER\Devi\Investigacion\Avances\Cuenca\AVG'

#Main and Video Function Run
main(21,dir_in2,dir_out2)