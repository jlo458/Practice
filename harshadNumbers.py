# This program takes an integer input (n) and outputs the nth Harshad number 
# A Harshad number is a number divisible by sum of its digits e.g 216 - 2+1+6=9 & 216/9 = 24

n = int(input("Enter number: "))
count = 0
num = 1

while count != n: 
  numTot = 0
  #print(count)
  for i in str(num): 
    numTot += int(i)

  if (num%numTot) == 0: 
    count += 1

  if count == n: 
    print(num)

  num+=1
