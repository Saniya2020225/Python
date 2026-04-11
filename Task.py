# Task - Find all numbers divisible by 3 from 1to 100 ,also print count of such number.abs

count = 0
for number in range(1,101):
    if number %3 == 0:
        count = count + 1
        print(number)

print(f"We have {count} numbers divisible by 3 from 1 to 100")        