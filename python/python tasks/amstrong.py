
num = int(input("Enter the Nuumber : "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num,"is an Amstrong Number.")
else:
    print(num,"is not an Amstrong Number.")