# from faker import Faker

# fake=Faker()
# print(fake.name())
# print(fake.email())
# print(fake.phone_number())

# file=open("rahul.txt","a+")
# file.write("\n soumya chutiya hai !")

# res=file.read()
# file.flush()
# file.close()
# print(res)


# with open("rahul.txt","w+") as file:
#     file.write("this is demo file...")
#     file.seek(5)
#     res=file.readline()
# print(res)

# file=open("write.txt","w")
# file.write("This is completely python file handling...")
# file.flush()
# file.close()
# print("File Created...")

# file=open("write.txt","a")
# file.write("\nThis is 3rd completely python file handling...")
# file.flush()
# file.close()
# print("File Updated...")

# file=open("write.txt","r")
# # file.write("\nThis is 3rd completely python file handling...")
# res=file.read()
# file.flush()
# file.close()
# print(res)

# file=open("write.txt","r")
# # file.write("\nThis is 3rd completely python file handling...")
# res=file.readline()
# file.flush()
# file.close()
# print(res)

# file=open("write.txt","r")
# # file.write("\nThis is 3rd completely python file handling...")
# res=file.readlines()
# file.flush()
# file.close()
# print(res)

# with open("rahul.txt","w+") as file:
#     file.write("this is a new file")
# print("file created ")


# with open("rahul.txt","w+") as file:
#     file.write("this is a new file")
#     file.seek(0)
#     res=file.read()

# print(res)

with open("rahul.txt","a+") as file:
    # file.write("\nthis is a new file 2\nthis is a new file 3\nthis is a new file 4")
    file.seek(0)
    res=file.read()

print(res)