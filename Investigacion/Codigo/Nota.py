#print(nc.variables['PM2_5_DRY'])
#for d in nc.dimensions.items():
    #print(d)
#print(nc.variables.keys())
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
Time
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

Paramemter
p1 = nc.variables ["T2"][time1,:,:]
p2 = nc.variables ["T2"][time2,:,:]
p3 = nc.variables ["T2"][time3,:,:]
p4 = nc.variables ["T2"][time4,:,:]
p5 = nc.variables ["T2"][time5,:,:]
p6 = nc.variables ["T2"][time6,:,:]
p7 = nc.variables ["T2"][time7,:,:]
p8 = nc.variables ["T2"][time8,:,:]
p9 = nc.variables ["T2"][time9,:,:]
p10 = nc.variables ["T2"][time10,:,:]
p11 = nc.variables ["T2"][time11,:,:]
p12 = nc.variables ["T2"][time12,:,:]
p13 = nc.variables ["T2"][time13,:,:]
p14 = nc.variables ["T2"][time14,:,:]
p15 = nc.variables ["T2"][time15,:,:]
p16 = nc.variables ["T2"][time16,:,:]
p17 = nc.variables ["T2"][time17,:,:]
p18 = nc.variables ["T2"][time18,:,:]
p19 = nc.variables ["T2"][time19,:,:]
p20 = nc.variables ["T2"][time20,:,:]
p21 = nc.variables ["T2"][time21,:,:]
p22 = nc.variables ["T2"][time22,:,:]
p23 = nc.variables ["T2"][time23,:,:]
p24 = nc.variables ["T2"][time24,:,:]"""

#Wind 10 m (m/s)
#U=list(range(0,24))
#V=list(range(0,24))
#W=list(range(0,24))
#for i in T:
 #   U[i]=nc.variables ["U10"][time[i],:,:]
 #   V[i]=nc.variables ["V10"][time[i],:,:]
 #   W[i]=(U[i]**2 + V[i]**2)** 0.5
 #for i in U_norm:
    #U_NORM = U[i]/W[i]
#for i in V_norm:
    #v_norm = V[i]/W[i]
"""img_array1=['PM_31Dec2021_14.png','PM_31Dec2021_15.png', 'PM_31Dec2021_16.png','PM_31Dec2021_17.png', 'PM_31Dec2021_18.png', 'PM_31Dec2021_19.png',
            'PM_31Dec2021_20.png', 'PM_31Dec2021_21.png', 'PM_31Dec2021_22.png','PM_31Dec2021_23.png', 'PM_1Jan2022_0.png', 'PM_1Jan2022_1.png', 
            'PM_1Jan2022_2.png', 'PM_1Jan2022_3.png', 'PM_1Jan2022_4.png','PM_1Jan2022_5.png', 'PM_1Jan2022_6.png', 'PM_1Jan2022_7.png',
            'PM_1Jan2022_8.png', 'PM_1Jan2022_9.png', 'PM_1Jan2022_10.png','PM_1Jan2022_11.png', 'PM_1Jan2022_12.png', 'PM_1Jan2022_13.png','PM_1Jan2022_14.png']"""
"""for i in range(0,24):
    img_array.append(cv2.imread('PM_'+str(i)+'.png'))

height,width,layers= img_array[23].shape
size=(width,height)

fourcc= cv2.VideoWriter_fourcc(*'mp4v')
video=cv2.VideoWriter('PM.mp4',fourcc,15,size)

#resized = cv2.resize(img_array,(1280,720),fx=0,fy=0)
for j in range(len(img_array)):
    img=cv2.imread('PM_'+str(j)+'.png')
    video.write(img)
#cv2.destroyAllWindows()
video.release()"""
#M2:"ghostwhite","cornflowerblue","blue","blueviolet","darkviolet","darkmagenta","mediumvioletred","deeppink","crimson"
#M3:"mintcream","aquamarine","springgreen","lime","cyan","deepskyblue","dodgerblue","royalblue","blue","navy"
#M4:"ghostwhite","palegreen","lightgreen","lawngreen","greenyellow","yellow","gold","orange","darkorange","chocolate","brown","maroon"
#M6:"seashell", "bisque", "orange", "darkorange","chocolate","sienna","saddlebrown","maroon"