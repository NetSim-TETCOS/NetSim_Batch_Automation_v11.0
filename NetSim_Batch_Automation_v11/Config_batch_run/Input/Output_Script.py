import os
import commands
import sys
import subprocess
import random
import os.path
import filecmp
import shutil

result=[]
result.append("File Location ---------------------------------> File Status \n")
a=sys.argv[1]
b=sys.argv[2]
DIR=a
OUTPUT_PATH='C:\Users\TETCOS\Desktop\NetSim_Batch_Automation_v11\'
NETSIM_PATH='"'+ b + '"'
TEMP_PATH='C:\Users\TETCOS\AppData\Local\Temp\NETSIM'
os.chdir(DIR)

def filecheck(line):
        name=line+"_Results"
        DIR_C=OUTPUT_PATH + "\\Output\\" + name
        if os.path.exists(DIR_C):
           shutil.rmtree(DIR_C)
        if not os.path.exists(DIR_C):
            os.makedirs(DIR_C)
        os.chdir(TEMP_PATH)
        files=os.listdir(TEMP_PATH)
        for f in files:
            os.unlink(f)
        os.chdir(DIR)
        shutil.copy2(line,TEMP_PATH)
        shutil.copy2('NetSim_Params.bat',TEMP_PATH)
        os.chdir(TEMP_PATH)
        original=line
        overwrite="Configuration.netsim"
        os.rename(original,overwrite)
        command = 'NetSim_Params.bat ' + NETSIM_PATH + ' ' + '"' + TEMP_PATH + '"'
        os.system(command)
        open("Tetcostesting.txt","w+")
        subprocess.check_call(["attrib","+H","Tetcostesting.txt"])
        files=os.listdir(TEMP_PATH)
        for f in files:
                shutil.move(f,DIR_C)
        os.chdir(DIR)
        
with open("filetext.txt") as files:
    content = files.read().splitlines()
    for line in content:
        filecheck(line)
       

