# --------------------------------Tupple------------------
# Defination and property of tupple
# creation of tupple
# indexing and slicing
# transversing
# In-built methods
# Assignement and class activity
# tupple comprihension

# # Defination and property of tupple---------------------------------------

# 1. it is data structure in pyhton used to store multiple data 
# 2. immutable



# t1=(50,40)
# print(type(t1))



#transversing of tupple
# waf to extract all numbers greater than 55 from tupple (10,20,30,40,50,60,70,80,90)

# def tuple_fun(m):
#     new_val=[] 
#     for i in m:
#         if i>=55:
#             new_val.append(i)
#     return new_val
# marks=(10,20,30,40,50,60,70,80,90)
# res=tuple_fun(marks)
# print(res)



# waf to sum of indices of  tupple (10,20,30,40,50,60,70,80,90)
# # 
# marks=(10,20,30,40,50,60,70,80,90)
# sum=0
# for i in range(len(marks)):
#     sum+=i
# print(sum)

marks=(10,20,30,40,50,60,70,80,90)
res= sum([i for i in range(len(marks))])
print(res)




