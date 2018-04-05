#! python3
#-*- coding: gbk -*-

# 处理 ACC 格式 => THD 格式
# mm/s2 =>  m/s2
# 天然波 => MIDAS GEN 地震波

import os
import math
import string

def conver2midasgen():
    for filename in os.listdir():
        if filename.endswith('.ACC'):
            
            #获取不带后缀名的文件名
            PureFilename = filename.split(".")[0]
            print(PureFilename)
            
            #读取地震波文件
            with open(filename) as file_object:
                
                # Read file from line 2 or skip header row
                Header_line = next(file_object) 
                Points = int(Header_line.split()[0])
                Step = float(Header_line.split()[1])

                #读取地震波数据
                wavedatas = []
                for line in file_object:
                    wavedatas += line.split()
            
                # 单位换算
                for i in range(Points):
                    wavedatas[i] = float(wavedatas[i]) / 1000.0
            
            # MIDAS GEN 地震波后缀名必须是大写的，小写的导不进去
            Newfilename = PureFilename + '.THD'
    
            #写入文件
            with open(Newfilename, 'w') as file_object:
                file_object.write("**Comments- Coded by liudongze\n")
                file_object.write("*UNIT,M,KN\n") 
                file_object.write("*TYPE,ACCEL\n")
                file_object.write("*DATA\n")
                
                # https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
                for i in range(Points):
                    file_object.write(("%.4f" % (i * Step)) + ', ' + ("%.4f" % wavedatas[i]) + '\n')
                    
if __name__ == "__main__":
    conver2midasgen()
