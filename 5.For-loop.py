#1
import random
list1=[]
count_two_consecutive_sixes=0
for i in range(20) :
    j=random.randint(1,6)
    list1.append(j)
print(list1)    
print("No : of times you rolled 6 :",list1.count(6))
print("No : of times you rolled 1 : ",list1.count(1))
for i in range(len(list1)-1):
    if list1[i]==6 and list1[i+1]==6 :
        count_two_consecutive_sixes+=1
print("No:of two consecutive sixes :",count_two_consecutive_sixes)


#2
for i in range(10, 101, 10):  
    if i == 100:
        print("Congratulations! You completed the workout")
        break
    print(f"You have completed {i} jumping jacks.")
    resp = input("Are you tired? (yes/y or no/n): ").strip().lower()
    if resp in ['y', 'yes']:
        print(f"You completed a total of {i} jumping jacks.")
        break
    elif resp in ['n', 'no']:
        print(f"{100 - i} jumping jacks are remaining.")