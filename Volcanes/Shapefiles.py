#Prueba y lectura de shapefiles
def main():
    from black import Encoding
    import matplotlib.pyplot as plt
    from matplotlib.offsetbox import AnchoredText
    import numpy as np 
    import shapefile
    import cartopy.feature as cfeature
    from matplotlib.patches import Polygon
    import cartopy.crs as ccrs
    import matplotlib.patches as mpatches
    
    spf= shapefile.Reader(r'c:\Users\Usuario\OneDrive - Universidad San Francisco de Quito\Asistencia Investigacion\Volcanes\Zona Urbana\zonaurbanafinal2014.shp',encoding='latin-1')
    #shapes=spf.shapes()Get the shape names
    fields=spf.fields#Get the shape fields
    print(fields)
    records=spf.shapeRecords()# Get the shape records (coordinates of points)
    polygons=list(range(22))
    #ciu=polygons[1].__getattribute__('CIUDAD')
    #print(ciu)
    for i in range(22):#22 cabezeras cantonales
        polygons[i]=records[i]#Store the polygons into an array
        #print(polygons[i].record)
    plt.figure()
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE,edgecolor='dimgrey',facecolor='none'); ax.add_feature(cfeature.BORDERS,edgecolor='dimgrey',facecolor='none')
    for j in range (22):
        poly(polygons[j],ax)
    #Map Axes (y:Latitude and x:Longitude)
    x = [-81,-80,-79,-78,-77,-76,-75];y = [-5,-4,-3,-2,-1,0,1];y_l=['-05','-04','-03','-02','-01','0','01']
    xlim = [-81.5,-75];ylim = [-5,1.5]
    volcan(ax,-77.98233,-1.78889,'Sangay')
    #Setting ticks and limits
    ax.set_xticks(x);ax.set_yticks(y)
    ax.set_xticklabels(x,ha='center');ax.set_yticklabels(y_l)
    ax.set_xlim(xlim);ax.set_ylim(ylim)
    plt.show()
    return 0

def poly(polygon,ax):#polygon[i]
    from matplotlib.offsetbox import AnchoredText
    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    import shapefile
    import numpy as np 
    n=len(polygon.shape.points)#Get the lenght of each polygon
    xy=list(range(n))#Array of x an y points
    for i in range(n):
        xy[i]=polygon.shape.points[i]#Store the polygon points into an array
    #print(xy[i])
    xs,ys = zip(*xy)#Create lists of x and y values
    plt.plot(xs,ys,c='dimgray',linewidth=0.7,fillstyle='full',alpha=0.7,transform=ccrs.PlateCarree()) 
    plt.fill(xs, ys,c="silver")
    ciu=polygon.record[5]
    if ciu=='QUITO':
        text=AnchoredText('Quito',loc='lower left',prop=dict(size=6),frameon=False,bbox_to_anchor=(0.46,0.71),bbox_transform=ax.transAxes)
        ax.add_artist(text)
    elif ciu=='GUAYAQUIL':
        text=AnchoredText('Guayaquil',loc='lower left',prop=dict(size=6),frameon=False,bbox_to_anchor=(0.243,0.41),bbox_transform=ax.transAxes)
        ax.add_artist(text)
    elif ciu=='CUENCA':
        text=AnchoredText('Cuenca',loc='lower left',prop=dict(size=6),frameon=False,bbox_to_anchor=(0.39,0.3),bbox_transform=ax.transAxes)
        ax.add_artist(text)
    return 0
def volcan(ax,x,y,name):
    import matplotlib.pyplot as plt
    from matplotlib.offsetbox import AnchoredText
    r=0.05
    x1=x+r;x2=x;x3=x-r
    y1=y;y2=y+(r*2);y3=y
    #poly_coords=[(-77.93233,-1.78889),(-77.98233,-1.68889),(-78.03233,-1.78889)]
    poly_coords=[(x1,y1),(x2,y2),(x3,y3)]
    ax.add_patch(plt.Polygon(poly_coords,color='brown',alpha=0.5))
    text=AnchoredText(name,loc='lower left',prop=dict(size=6.5),frameon=False,bbox_to_anchor=(0.54,0.475),bbox_transform=ax.transAxes)
    ax.add_artist(text)
    #import matplotlib.patches as mpatches
    #triangle = mpatches.RegularPolygon((0,0),3,0.5)
    #ax.add_patch(triangle)
    #import tkinter as tk
    #rom tkinter import Canvas
    #from pyglet import shapes
    #col=(165,42,42)
    # creating a batch object
    #vol=canvas.create_(-79,-3,-78.5,-2.5,-78,-3,color=col)
    #ax.add_artist(vol)
    # accessing anchor position of rectangle
    #batch.draw()
    #pyglet.app.run()
    #value_tri = vol.anchor_position
    #print(value_tri)
    return 0

main()

#To see each polygon record and names:print(polygons[i].record);print(polygons[i].shape.points)
#first=records[3]
#print(first.record)
#print(first.shape.points)
#canton_zone = ShapelyFeature (first.shape.points,ccrs.PlateCarree(),edgecolor='grey',facecolor='none',alpha=1)
#ax = plt.axes(projection=ccrs.PlateCarree())
#plt.figure()
#ax.add_feature(cfeature.COASTLINE,edgecolor='dimgrey',facecolor='none'); ax.add_feature(cfeature.BORDERS,edgecolor='dimgrey',facecolor='none')
#ax.add_feature(canton_zone)
#plt.show()
#feature= spf.shapeRecords()[1]
#first = feature.shape.__geo_interface__ 
#print(first)
#plt.plot(first) 
#print(spf)
#print(shapes)
#print(fields)
#print(records)