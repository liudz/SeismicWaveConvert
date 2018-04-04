#! python3
#-*- coding: gbk -*-

# 处理 ACC 格式 => x, y, z格式
# mm/s2 =>  m/s2
# 天然波 => PKPM 地震波

import os

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
    
