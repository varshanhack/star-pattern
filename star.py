#Star pattern printing
import sys,subprocess
while True:
 n=int(input("enter the size = "))
 for i in range(1,n+1):
     print("*"*i)
 inp=input("Press enter to continue")
 subprocess.run("cls",shell=True)
 
