import random

# # emp_names = ["Aman", "Raman", "Ramesh", "Suresh", "Rakesh", "Rohit", "Rahul"]
# # res=random.choice(emp_names)
# # print(res)

# # emp_names = ["Aman", "Raman", "Ramesh", "Suresh"]
# # weight=[2,3,4,0]
# # res=random.choices(emp_names, weights=weight, k=10)
# # print(res)


# # res=random.random()*1000000  # jitne zeros utna bada no. ye 6 digit k liye use kiya hai 
# # print(int(res))

# res1=random.randint(1,10) #include 10 

# res2=random.randrange(1,10) # not include 10 

# print(res1)
# print(res2)


# # wap to user max attemp=6
# # each attemp random number Generate
# # random nu. sum
# # fix_value= 150
# # too far
# # too close



# import random

# def guess_game():
#     FIX_VALUE = 150
#     MAX_ATTEMPTS = 6
#     running_sum = 0
    
#     print("--- Welcome to the Random Sum Game! ---")
#     print(f"Goal: Reach exactly {FIX_VALUE} by generating random numbers.")
#     print(f"You have a maximum of {MAX_ATTEMPTS} attempts.\n")
    
#     for attempt in range(1, MAX_ATTEMPTS + 1):
#         input(f"Press Enter to roll for Attempt {attempt}/{MAX_ATTEMPTS}...")
        
        
#         num = random.randint(1, 50)
#         running_sum += num
        
#         print(f"-> Generated: {num}")
#         print(f"-> Current Total Sum: {running_sum}")
        
       
#         if running_sum == FIX_VALUE:
#             print("\n🎉 Amazing! You hit exactly 150! You Win!")
#             return
#         elif running_sum > FIX_VALUE:
#             print(f"\n💥 Busted! Your sum ({running_sum}) exceeded 150. Game Over!")
#             return
            
#         difference = FIX_VALUE - running_sum
#         if difference > 100:
#             print("Status: Too far from 150! Keep going.\n")
#         else:
#             print("Status: Too close! Watch out.\n")
            

#     print(f"\nGame Over! You ran out of attempts. Your final sum was {running_sum}.")


# guess_game()

#SAMPLE---------------------------------

# emp_names = ["Aman", "Raman", "Ramesh", "Suresh"]
# res=random.sample(emp_names, k=2)
# print(res)


# # Shuffle()-----------------------------

# emp_names = ["Aman", "Raman", "Ramesh", "Suresh"]
# random.shuffle(emp_names)
# print(emp_names)

#cupon code--------------------
#CXYZ4353

# def gen_cupon():

#     str1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     num="1234567890"
#     char=[random.choice(str1).upper() for i in range(1,5)]
#     digit=[random.choice(num) for i in range(1,5)]

#     print("".join(char+digit))
# for i in range(1,10):
#     gen_cupon()



# def gen_cupon():

#     str1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     num="1234567890"
#     char="".join(random.choices(str1,k=4))
#     digit=random.random()*10000
    
#     res=char.upper()+str(int(digit))
#     print(res)

   


# for i in range(1,10):
#     gen_cupon()

def gen_cupon():
    import string
    print(
    "".join(random.choices(string.ascii_uppercase,k=4))
    + "".join(random.choices(string.digits,k=4)))

    

for i in range(1,10):
    gen_cupon()
