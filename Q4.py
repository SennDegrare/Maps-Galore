# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:25:18 2021

@author: user
"""

#Creating dictionary to store choices for different levels
menu = {0:[1,2], 1:[3,4], 2:[5,6], 3:[7,8],4:[9,10],5:[11],6:[12,13]}

names = ["Welcome to Festa Italiana!", "Pizza",
         "Pasta","Veg","Non-Veg","Veg","Non-Veg"
         "Peppy Paneer","Cheese Corn","Barbeque","Supreme","Latin white sauce",
         "Bolonese Chicken", "Lasagna"]


#initialize to pass over the dictionary
i = 0
print(names[0])
print()

while i in menu:
    #Checking to see whether a choice is necessary
    if len(menu[i]) == 2:
        print("Give 0 for", names[menu[i][0]], "1 for", names[menu[i][1]],": ")
        #Evaluation of string is necessary for comparison
        nxtemp = eval(input())
        i = menu[i][nxtemp]

    #No choice necessary    
    elif len(menu[i]) == 1:
        i = menu[i][0]
    else:
        continue

print("Enjoy your ", names[i], " !!!")