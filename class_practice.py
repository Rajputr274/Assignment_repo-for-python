# # WAF to remove last word from string 


# str1="this is python code in vs "
# lis=str1.split()
# lis.pop()
# str1=" ".join(lis)

# print(str1)

#waf to remove vowels from the string

# WAF to remove last word from string 


# str1="this is python code in vs "
# new_str=[]

# for i in str1:
#     if i not in "aeiou":
#         new_str+=i
# res=" ".join(new_str)
# print(res)


#Waf to count white spaces in string 

# str1="this is python code in vs"
# count=0
# for i in str1:
#     if i==" ":
#         count+=1
#     else:
#         i+=i
# print(count)

# str1="this is python code in vs version-35 address noida-11096"
# new_str=""
# for i in str1:
#     if i in "0123456789":
#         new_str+=i
# print(new_str)

# str1="this is python code in vs version-35 address noida-11096"
# new_str=""
# new=str1.replace(" ","")
# print(new)


# 6 .waf to print all special char.

# str1="this is python code@123 in vs version-35 address noida-11096"
# for i in str1:
#     if  not i.isalnum() and i!=" ":
#         print(i,end=" ")




# 7.Waf to reversed the all words.

# str1="this is python code@123 in vs version-35 address noida-11096"

def reverse_words(str1):
    words = str1.split()

    for word in words:
        print(word[::-1], end=" ")

# str1 = "this is python code@123 in vs version-35 address noida-11096"
# reverse_words(str1)