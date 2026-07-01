#----------- File handling----------------------------------------
#1. File handling in python means reading from and writing to files/folder stored on
# disk using python.

#2. Your python code can open a file , pull out data of it , put data into it and 
# also close it properly.

#---------- What is file-------------------------
# files are store of data and information on the specific path of device.

# Types of file
# 1.Text file (.txt,.csv,.json)
# 2.Binary file (images,vedios,audio)

# Types of file path.
# 1.Absolute path : The complete path from the root of the filesystem.
# 2.Relative path : The path relative to where your current folder (current working dir)

# file mode
# 1. a : append , a+ : append and read
# 2. w : write , w+ : write and read
# 3. r : read  ,  r+ : read and write
# 4. x : strictly create file

# python file handling methods.
# 1.open(file_name,mode) : opens file 
# 2.close() : close file.
# 3.flush() : memory cleanup.

# 4.read() : file read.
# 5.readlines(): file read line by line.
# 6.write() : writes data in file only take string.
# 7.write data in file of any data types.

# 8.tail(): cursor move
# 9.seek(): specific position set of cursor


# 1.create a file in strict mode.
# try:
#     file=open("strict.txt","x")
#     print("File created...")
# except Exception as e:
#     print("Error : File nhi bn sakti pehle se hai...")

# file=open("write.txt","w")
# file.write("This is python file handling...")
# file.write("This is New line of python file handling...")

# print("File Created...")

# file=open("write.txt","w")
# file.write("This is completely python file handling...")
# file.flush()
# file.close()
# print("File Created...")

# context manager
# with open("manager.txt","w+") as file:
#     file.write("This is completely python file handling...")
#     file.seek(0)
#     r=file.read(4)
#     print("File created and written...")
#     print(f"File Content : {r}" )


# with open("product.json","r") as f:
#     r=f.read()
#     print(r)


emp_list=["aman","shivam","shubham","anshu","kamal"]










# try:

#     file =open("strict.txt","x")
#     print("file created...... ")
# except Exception as e:
#     print("error: File is already exist")

# file =open("strict.txt","w")
# print("file created...... ")
# file.write("this is python file ")
# file.write("this is new  python file ")


# context manager
# with.open(filename,mode) as file 

# with open ("manager.txt","w+") as file:
#     file .write("this is completely python file handling ......")
#     file.seek(0)  # it read file from starting 
#     r=file.read()
#     print("file is creted.... ")
#     print(f"file content,{r}")


# with open("demo.txt","w+") as file:
#     file.write("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
#             Lorem Ipsum has been the industry's standard dummy text ever since 1966, 
#             when designers at Letraset and James Mosley, 
#             the librarian at St Bride Printing Library in London, 
#             took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. 
#             It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. 
#             It was popularised thanks to these sheets and more recently with desktop publishing software like Aldus PageMaker and Microsoft Word including versions of Lorem Ipsum.""")
#     file.seek(0)
#     r=file.read()
#     with open("newdemo.txt", "w+") as newfile:
#         for i in r:
#             if i in "0123456789":
#                 newfile.write("@")
#             else:
#                 newfile.write(i)

emp_list=['aman','shivam','anshu','kamal']
for i in emp_list:
    with open(i+".txt","w+") as file:

        file.read()
print("file Created")

emp_list=['aman','shivam','anshu','kamal']
res=[str(i)+"txt" for in] 