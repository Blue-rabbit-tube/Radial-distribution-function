import decimal
import math
import matplotlib.pyplot as plt
import numpy

def distance(x,y,z,x1,y1,z1):            #function计算两点之间的距离
    return(math.sqrt(pow(x-x1,2)+pow(y-y1,2)+pow(z-z1,2)))


if __name__=="__main__":
    file=open("allall.xyz","rt")         #打开一个文件流
    sp=file.readlines()                  #读取文件内容到一个数组
    
    #数据统计
    num_1=0
    num_2=0
    num_3=0
    num_4=0
    
    num_1_xyz=[[],[],[]]
    num_2_xyz=[[],[],[]]
    num_3_xyz=[[],[],[]]
    num_4_xyz=[[],[],[]]
    
    #文件预处理部分
    
    for i in sp:
        ps=i[0:-1].split(" ")                  #写入一个数组 并执行数据分割操作并删掉\n
        # print(ps)
        if ps[0]=='1':
            num_1+=1
            num_1_xyz[0].append(decimal.Decimal(ps[1]))
            num_1_xyz[1].append(decimal.Decimal(ps[2]))
            num_1_xyz[2].append(decimal.Decimal(ps[3]))
        if ps[0]=='2':
            num_2+=2
            num_2_xyz[0].append(decimal.Decimal(ps[1]))
            num_2_xyz[1].append(decimal.Decimal(ps[2]))
            num_2_xyz[2].append(decimal.Decimal(ps[3]))
        if ps[0]=='3':
            num_3+=3
            num_3_xyz[0].append(decimal.Decimal(ps[1]))
            num_3_xyz[1].append(decimal.Decimal(ps[2]))
            num_3_xyz[2].append(decimal.Decimal(ps[3]))
        if ps[0]=='4':
            num_4+=4
            num_4_xyz[0].append(decimal.Decimal(ps[1]))
            num_4_xyz[1].append(decimal.Decimal(ps[2]))
            num_4_xyz[2].append(decimal.Decimal(ps[3]))
    
    print("数据量统计:",num_1,num_2,num_3,num_4)
    #计算中心点
    center_1={'x':0,'y':0,'z':0}
    center_2={'x':0,'y':0,'z':0}
    center_3={'x':0,'y':0,'z':0}
    center_4={'x':0,'y':0,'z':0}
    
    #没几个数据 懒得封装函数了
    for s in range(0,len(num_1_xyz[0])):
        center_1['x']+=num_1_xyz[0][s]
        center_1['y']+=num_1_xyz[1][s]
        center_1['z']+=num_1_xyz[2][s]
    center_1['x']/=len(num_1_xyz[0])
    center_1['y']/=len(num_1_xyz[0])
    center_1['z']/=len(num_1_xyz[0])
    print("center_1中心点：",center_1)
    
    for s in range(0,len(num_2_xyz[0])):
        center_2['x']+=num_2_xyz[0][s]
        center_2['y']+=num_2_xyz[1][s]
        center_2['z']+=num_2_xyz[2][s]
    center_2['x']/=len(num_2_xyz[0])
    center_2['y']/=len(num_2_xyz[0])
    center_2['z']/=len(num_2_xyz[0])
    print("center_2中心点：",center_2)
    
    for s in range(0,len(num_3_xyz[0])):
        center_3['x']+=num_3_xyz[0][s]
        center_3['y']+=num_3_xyz[1][s]
        center_3['z']+=num_3_xyz[2][s]
    center_3['x']/=len(num_3_xyz[0])
    center_3['y']/=len(num_3_xyz[0])
    center_3['z']/=len(num_3_xyz[0])
    print("center_3中心点：",center_3)
    
    for s in range(0,len(num_4_xyz[0])):
        center_4['x']+=num_4_xyz[0][s]
        center_4['y']+=num_4_xyz[1][s]
        center_4['z']+=num_4_xyz[2][s]
    center_4['x']/=len(num_4_xyz[0])
    center_4['y']/=len(num_4_xyz[0])
    center_4['z']/=len(num_4_xyz[0])
    print("center_4中心点：",center_4)
    
    #开始计算最远点
    
    disance_temportary={'x':0,'y':0,'z':0,'distance':0}
    
    for s in range(0,len(num_1_xyz[0])):
        num=distance(num_1_xyz[0][s],num_1_xyz[1][s],num_1_xyz[2][s],center_1['x'],center_1['y'],center_1['z'])
        if num>disance_temportary['distance']:
            disance_temportary['x']=num_1_xyz[0][s]
            disance_temportary['y']=num_1_xyz[1][s]
            disance_temportary['z']=num_1_xyz[2][s]
            disance_temportary['distance']=num
    print("数据1最远的点是：",disance_temportary)
    r_1=disance_temportary['distance']
    
    disance_temportary={'x':0,'y':0,'z':0,'distance':0}
    
    for s in range(0,len(num_2_xyz[0])):
        num=distance(num_2_xyz[0][s],num_2_xyz[1][s],num_2_xyz[2][s],center_2['x'],center_2['y'],center_2['z'])
        if num>disance_temportary['distance']:
            disance_temportary['x']=num_2_xyz[0][s]
            disance_temportary['y']=num_2_xyz[1][s]
            disance_temportary['z']=num_2_xyz[2][s]
            disance_temportary['distance']=num
    print("数据2最远的点是：",disance_temportary)
    r_2=disance_temportary['distance']
    
    disance_temportary={'x':0,'y':0,'z':0,'distance':0}
    
    for s in range(0,len(num_3_xyz[0])):
        num=distance(num_3_xyz[0][s],num_3_xyz[1][s],num_3_xyz[2][s],center_3['x'],center_3['y'],center_3['z'])
        if num>disance_temportary['distance']:
            disance_temportary['x']=num_3_xyz[0][s]
            disance_temportary['y']=num_3_xyz[1][s]
            disance_temportary['z']=num_3_xyz[2][s]
            disance_temportary['distance']=num
    print("数据3最远的点是：",disance_temportary)
    r_3=disance_temportary['distance']
    
    disance_temportary={'x':0,'y':0,'z':0,'distance':0}
    
    for s in range(0,len(num_4_xyz[0])):
        num=distance(num_4_xyz[0][s],num_4_xyz[1][s],num_4_xyz[2][s],center_4['x'],center_4['y'],center_4['z'])
        if num>disance_temportary['distance']:
            disance_temportary['x']=num_4_xyz[0][s]
            disance_temportary['y']=num_4_xyz[1][s]
            disance_temportary['z']=num_4_xyz[2][s]
            disance_temportary['distance']=num
    print("数据4最远的点是：",disance_temportary)
    r_4=disance_temportary['distance']
    
    #开始计算各个数据的密度
    density_1=num_1/(math.pi*pow(r_1,3)*(4/3))
    density_2=num_2/(math.pi*pow(r_2,3)*(4/3))
    density_3=num_3/(math.pi*pow(r_3,3)*(4/3))
    density_4=num_4/(math.pi*pow(r_4,3)*(4/3))
    
    print("数据1平均密度",density_1)
    print("数据2平均密度",density_2)
    print("数据3平均密度",density_3)
    print("数据4平均密度",density_4)
    
    
    #开始计算径向分布函数
        #数据集合1
    step=0.1      #dr的步进值
    x=list(numpy.arange(0,r_1,step))
    # print(x)
    y=list(0 for i in range(0,len(x),1))

    
    for s in range(0,len(num_1_xyz[0])):
        num=distance(num_1_xyz[0][s],num_1_xyz[1][s],num_1_xyz[2][s],center_1['x'],center_1['y'],center_1['z'])
        y[int(num/0.1)]+=1
    # print(y)
    for ssp in range(0,len(y)):
        y[ssp]=y[ssp]*density_1
    # print(y)
    
    plt.subplot(2,2,1)
    plt.title("data_1_picture")
    plt.ylabel("g(r)")
    plt.xlabel("distance")
    plt.plot(x,y,'.-r')
    # plt.show()
    
    
    
         #数据集合2
    x=list(numpy.arange(0,r_2,step))
    # print(x)
    y=list(0 for i in range(0,len(x),1))

    
    for s in range(0,len(num_2_xyz[0])):
        num=distance(num_2_xyz[0][s],num_2_xyz[1][s],num_2_xyz[2][s],center_2['x'],center_2['y'],center_2['z'])
        y[int(num/0.1)]+=1
    # print(y)
    for ssp in range(0,len(y)):
        y[ssp]=y[ssp]*density_2
    # print(y)
    
    plt.subplot(2,2,2)
    plt.title("data_2_picture")
    plt.ylabel("g(r)")
    plt.xlabel("distance")
    plt.plot(x,y,'.-r')
    # plt.show()
    
    
    
         #数据集合3
    x=list(numpy.arange(0,r_3,step))
    # print(x)
    y=list(0 for i in range(0,len(x),1))

    
    for s in range(0,len(num_3_xyz[0])):
        num=distance(num_3_xyz[0][s],num_3_xyz[1][s],num_3_xyz[2][s],center_3['x'],center_3['y'],center_3['z'])
        y[int(num/0.1)]+=1
    # print(y)
    for ssp in range(0,len(y)):
        y[ssp]=y[ssp]*density_3
    # print(y)
    
    plt.subplot(2,2,3)
    plt.title("data_3_picture")
    plt.ylabel("g(r)")
    plt.xlabel("distance")
    plt.plot(x,y,'.-r')
    # plt.show()
    
    
         #数据集合4
    x=list(numpy.arange(0,r_4,step))
    # print(x)
    y=list(0 for i in range(0,len(x),1))

    
    for s in range(0,len(num_4_xyz[0])):
        num=distance(num_4_xyz[0][s],num_4_xyz[1][s],num_4_xyz[2][s],center_4['x'],center_4['y'],center_4['z'])
        y[int(num/0.1)]+=1
    # print(y)
    for ssp in range(0,len(y)):
        y[ssp]=y[ssp]*density_4
    # print(y)
    
    plt.subplot(2,2,4)
    plt.title("data_4_picture")
    plt.ylabel("g(r)")
    plt.xlabel("distance")
    plt.plot(x,y,'.-r')
    plt.show()
    
    
    
    file.close()                                           #关闭文件流