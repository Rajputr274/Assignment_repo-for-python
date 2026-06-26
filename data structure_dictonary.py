# Dictionary in Python
# • What is a Dictionary
# • Create Dictionary
# • Access Dictionary Values
# • Dictionary Methods
# • Dictionary – Add, Modify & Remove Items
# • Dictionary Iteration
# • Nested Dictionary
# • Dictionary Comprehensions

# ---------------Defination and property of dic.-------------
# 1. it store data in key : value pair
# 2. ordered , mutable 
# 3. index by key , not position
# 4. key must be unique 
# 5. value can be any type
# 6.used in fast lookup

# ------- Create Dictionary----------

# stu_pro={"aman":"noida","rohan":"dellhi"}
# print(type(stu_pro))
# print(stu_pro)


# -----alternate method -------------

# stu_pro=dict([('aman',300),('shivam',80)])

# print(stu_pro)

# stu_pro={"aman":"noida","rohan":"dellhi"}
# stu_pro["aman"]="london"
# print(stu_pro)


# inbuilt -methods-------------------
# stu_marks={'aman':300,"shivam":80,'rohan':40}
# v=stu_marks.values()
# k=stu_marks.keys()
# i=stu_marks.items()
# print(stu_marks.get("rahul","not found"))
# print(v)
# print(k)
# print(i)

# update()---------------------------

# stu_marks={'aman':300,"shivam":80,'rohan':40}
# stu_marks_new={"kamal":87,"rahul":98}
# stu_marks.update(stu_marks_new)
# print(stu_marks)


# --------nested dict-------------------

# profile={'aman': {'address':["noida","gwl", "Mra"],
#                   'hobbies':["reading","cooking"],
#                   "password": {'insta':"123456",'fb':"1432"}
#                   },
#         'rahul':{'address':["noida","gwl", "Mra"],
#                   'hobbies':["reading","cooking"],
#                   "password": {'insta':"0000",'fb':"143214"}
#                   }
#          }

# res1=profile["aman"]["password"]["insta"]
# res2=profile["rahul"]["password"]["fb"]
# print(res1)
# print(res2)

# st_marks=[76,54,98]
# st_name=["rahul","aman","surendra"]
# res=zip(st_name,st_marks)
# print(dict(res))


# stu_marks={'aman':300,"shivam":80,'rohan':40}
# v=stu_marks.values()

# print(sum(v))


  


