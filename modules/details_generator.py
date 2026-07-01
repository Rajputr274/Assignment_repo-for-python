import random
import os
import string
id="".join([random.choice(string.digits +string.ascii_uppercase) for i in range(9)])
Meeting_id="".join([random.choice(string.digits +string.ascii_uppercase) for i in range(17)])

def create_details(files):
    for i in files:
        if ".txt" in i:
            print(f"files : {i}")
    select=input("select your file without ext : ")
    with open(f"{select}.txt","w") as file:
        file.write(f"Name: {select}"+"\n")
        file.write(f"EmpID: {id}"+"\n")
        file.write(f"MeetingID : {Meeting_id}"+"\n")
        file.write(f"EmailID : {input("enter your mail id : ")}"+"\n")

    print(f"{select} file updated")
path=r"C:\Users\Dell\Desktop\batch_118\python\modules\emp_name"

files=os.chdir(path)
files = os.listdir() 
create_details(files)