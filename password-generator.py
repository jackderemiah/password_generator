import random
import string
import platform
import subprocess

letters = string.ascii_letters
nums = string.digits
symbols = string.punctuation
system = platform.system()

def pswd_generator(length):
    length = int(length)
    if (length > 0):
        combo = random.sample(letters + nums + symbols, length)
        password = "".join(combo)
    return password

def copyPasswordToClipboard(password, system):
    if(system == "Windows"):
     cmd='echo '+password.strip()+'|clip' 
     return [subprocess.check_call(cmd, shell=True), password.strip()]
    else:
     cmd='echo '+password.strip()+'|pbcopy'
     return [subprocess.check_call(cmd, shell=True), password.strip()]

        
length = input("Please enter length of password. \n")

res = copyPasswordToClipboard(pswd_generator(length), system)

if(res[0] == 0):
    print( res[1] ,"was successfully copied to clipboard! ")
else:
    print("Something went wrong! Please try again. ")

