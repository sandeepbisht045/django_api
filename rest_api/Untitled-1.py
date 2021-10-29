# """0001-9999"""
import os

pan_no=name=""
while name =="" :
        name=input("Enter Full Name of PAN Number ").upper()
        if name=="":
            os.system('cls||clear')
    
while len(pan_no)!=10:
        pan_no=input("Enter PAN Number ").upper().replace(" ","")
        if  len(pan_no)!=10:
            os.system('cls||clear')
            
        
    

    

# surname_index=int((name.index(" ")))+1
lst=name.split()
length=len(lst)
surname_index=lst[length-1][0]
pan_length=len(pan_no.replace(" ",""))
import re
status=re.findall("[PFCHAT]",pan_no[3])

# if pan_length!=10:
    # print("PAN must be 10 characters long")
    
if not pan_no[0].isupper() or not pan_no[1].isupper() or not pan_no[2].isupper():
    print("either first three characters are not upper alphabets")

elif not pan_no[5].isdigit() or not pan_no[6].isdigit() or not pan_no[7].isdigit() or not pan_no[8].isdigit():
    print("either 6th to 9th character is not a digit")
    
elif not pan_no[9].isupper():
    print("last character is not alphabetic")
    
elif  pan_no[4]!=surname_index:
    print("5th character is not the first alphabet of user Surname")
    

elif len(status)==0:
    print("4th char is not a valid status")

else:
    print("Valid PAN")

    

   

