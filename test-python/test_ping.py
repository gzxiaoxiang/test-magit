import numpy as np
import matplotlib as mt


import subprocess    
import re
p = subprocess.Popen(["ping.exe", 'baidu.com'], 
                                         stdin = subprocess.PIPE, 
                                         stdout = subprocess.PIPE, 
                                         stderr = subprocess.PIPE, 
                                         shell = True)    

out = p.stdout.read()                                     
regex = re.compile("Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)ms", re.IGNORECASE)
print regex.findall(out)
print (out)

def test(x):
    print(x)
test(3)
