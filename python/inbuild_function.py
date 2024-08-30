
str1 = "Python is prOgramming language"
str2 = "Python"
str3 = "457"
str4 = "Python"

capital = str1.capitalize()
print("capitalize:",capital) #first letter is capital

ends_with = str1.endswith("language")#end of the word
print("endswith",ends_with)

starts_with = str1.startswith("python")
print("startswith",starts_with) #start of the word

index_demo = str1.index("y")
print("Index:",index_demo) #particular index value

length = len(str2)
print("Length:",length) #entire string length

strip_demo = str1.strip() #remove the spaces
print("Strip:",strip_demo)

lstrip_demo = str1.lstrip()
print("lstrip:",lstrip_demo) #remove the left spaces

rstrip_demo = str1.rstrip()
print("rstrip:",rstrip_demo)#remove right spaces

title_demo = str1.title() #first letter of the word is capital
print("Title:",title_demo)

is_title_demo = str2.istitle() #check the capital letters
print("is_title_demo:",is_title_demo)

lst = ["Python","java","Cpp"]
join_demo = "#".join(lst)
print("Join:",join_demo) #join the symbol

swap_demo = str1.swapcase()
print("swap:",swap_demo) #small to capital,capital to small

is_digit_demo = str3.isdigit() #only digit
print("is_digit_demo:",is_digit_demo)

is_alpha_demo = str4.isalpha() #only alphabatical letter
print("is_alpha_demo:",is_alpha_demo)


is_alnum_demo = str4.isalnum() #check atleast one character are alpha
print("is_alnum_demo:",is_alnum_demo)


count_demo = str1.count("g") #count the number of letters
print("count_demo:",count_demo)

contains_demo = str1.__contains__("is") #word is include or not 
print("contains_demo:",contains_demo)

upper_demo = str1.upper()
print("upper_demo:",upper_demo)  #all the string in capital

lower_demo = str1.lower()
print("lower_demo:",lower_demo) #all the string in  lower

enumerate_demo = enumerate(str1)
print("enumerate_demo:",list(enumerate_demo)) #create list inside tuple and give the key and value

ord_demo = ord("C") #
print(ord_demo)

find_demo = str1.find("o")
print(find_demo)

index_demo = str1.index("is")
print("Index:",index_demo)
