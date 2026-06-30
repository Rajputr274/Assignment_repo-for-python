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