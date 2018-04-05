#! python3
#-*- coding: gbk -*-

# 处理 ACC 格式 => x, y, z格式
# mm/s2 =>  m/s2
# 天然波 => PKPM 地震波

import os
import matplotlib.pyplot as plt

def convert2pkpm():
    for filename in os.listdir():
        if filename.endswith('.ACC'):
            
            #获取不带后缀名的文件名
            PureFilename = filename.split(".")[0]
            
            #读取地震波文件
            with open(filename) as file_object:
                # Read file from line 2 or skip header row
                Header_line = next(file_object) 
                Points = int(Header_line.split()[0])
                Step = Header_line.split()[1]
                
                #读取地震波数据
                wavedatas = []
                for line in file_object:
                    wavedatas += line.split()
                #print(wavedatas)
            
                # 单位换算
                for i in range(Points):
                    wavedatas[i] = float(wavedatas[i]) / 1000.0
                #print(wavedatas)
            
            #绘图
            #https://matplotlib.org/users/pyplot_tutorial.html
        
            wavetimes = list(range(1, Points + 1))
            TimeStep = [wavetimes * Step for wavetimes in range(1, Points + 1)]
        
            #图像x坐标上限
            xuplimit = (int(TimeStep[-1] / 10) + 1) * 10
            ylimit = (int(max(max(WaveDates),(-1)*min(WaveDates)) * 10) + 1) / 10

            #默认是'b-'，蓝色实线
            # r--: 红色虚线；bs: 蓝色方块；g^: 绿色三角，等等
            plt.plot(TimeStep, WaveDates, 'r-', linewidth = 0.3)
        
            #设置图表标题
            plt.title("地震波时程曲线", fontsize = 20)
            plt.xlabel("时间(s)", fontsize = 15)
            plt.ylabel("加速度(m/s2)", fontsize = 15)
        
            #x, y坐标范围
            plt.axis([0, xuplimit, -ylimit, ylimit])
        
            #图像里有网格
            plt.grid(True)
        
            #设置刻度标记的大小
            plt.tick_params(axis = 'both', labelsize = 14)
        
            #plt.show()
            plt.savefig('地震波-' + PureFilename + '.png', bbox_inches = 'tight')

            #如果是y向、z向波，后缀名修改为.y或者.z
            Newfilename = PureFilename + '.x'
    
            #写入文件
            with open(Newfilename, 'w') as file_object:
                
                # 人工波就改为下面的格式，后面加一个空格和m
                #file_object.write(str(Points) + ' ' + Step + ' m' + '\n')
                file_object.write(str(Points) + ' ' + Step + '\n')
                for i in range(Points):
                    file_object.write(str(wavedatas[i]) + '\n')
                    
convert2pkpm()
    
