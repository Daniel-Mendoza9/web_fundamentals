# Print intergers from 0 to 150

for i in range(0, 151):
    print(i)

# Multiples of five

print(list(range(5,1005,5)))

#Counting, the Dojo way

for i in range(1, 101):
    if i % 5 == 0:
        print("Coding")

    if i % 10 == 0:
        print("Coding Dojo")

    else:
        print(i)

# Whoa, That sucker's huge

sum = 0
for i in range(0, 500000):
    if i % 2 == 0:
        sum += i
print(sum)

# Countdown by fours

for i in range(2018,0,-4):
    if i > 0:
        print(i)

# Flexible Counter

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print(i)
        


