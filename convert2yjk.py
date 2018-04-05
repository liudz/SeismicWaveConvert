#! python3
#-*- coding: gbk -*-

# 处理 ACC 格式 => txt 格式
# mm/s2 =>  cm/s2
# 天然波 => YJK 地震波

import os
import math
import string

def conver2yjk():
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
            
                # 单位换算
                for i in range(Points):
                    wavedatas[i] = float(wavedatas[i]) / 10.0
            
            Newfilename = PureFilename + '.txt'
    
            #写入文件
            with open(Newfilename, 'w') as file_object:
                file_object.write('$: coded by liudongze\n')
                file_object.write("C:NW\n") # YJK 人工波是 "C:AW"
                file_object.write('D: ' + Step + '\n')
                file_object.write("PW:\n")
                
                for i in range(Points):
                    file_object.write(('{0:17.6e}'.format(MyNumber(wavedatas[i]))) + '\n')
                    
# https://stackoverflow.com/questions/39184719/exponent-digits-in-scientific-notation-in-python              
class MyNumber:
    def __init__(self, val):
        self.val = val

    def __format__(self,format_spec):
        ss = ('{0:'+format_spec+'}').format(self.val)
        if ( 'e' in ss):
            mantissa, exp = ss.split('e')            
            return mantissa + 'e'+ exp[0] + '0' + exp[1:]
        return ss

if __name__ == "__main__":
    conver2yjk()
