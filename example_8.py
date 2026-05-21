#write a Python program to check whether a list contains a sublist. 
lst_name=["haidar","batti","mohammad"]
lst_name2=["haidar","mohammad",["batti","hasan","ali"]]

for i in lst_name2:
    if type(i)==list:
        print("List contains a sublist")
        break
else:
        print("List does not contain a sublist")
        