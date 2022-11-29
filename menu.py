"""

print(" Enter 1 for porotta \n Enter 2 for appam \n Enter 3 for mandhi \n Enter 4 for biriyani")
a=int(input(" Enter your choice:"))
if a==1 :
   print("You have selected porotta")
elif a==2 :
   print("you have selected appam")
elif a==3 :
   print("you have selected mandhi")
elif a == 4 :
   print("you have selected biriyani")
else :
   print("Enter a valid choice")
   
"""


list = ['1-Porotta', '2-Biriyani', '3-Appam', '4-Mandi']
print(list)
menu = int(input("Enter the option number of respected item : "))
if menu == 1 :
    print("You have selected Porotta")
elif menu == 2 :
    print("You have selected Biriyani")
elif menu == 3 :
    print("You have selected Appam")
elif menu == 4 :
    print("You have selected Mandi")
else :
    print("Sorry,Not Available")
