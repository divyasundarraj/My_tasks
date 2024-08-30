

str = input("Enter The String : ") 
revstr = ""
for i in str:
    revstr = i + revstr
if(str == revstr):
    print("The String is Palindrme.")
else:
    print("The String is Not a Palindrme.")




