sum=0
print("Numbers from 1 to 20 which are not divisible by 2,3,or 5")
for i in range(1,20):
    if i%2==0 or i%3==0 or i%5==0:
        print("")
    else:
        print(i)
        sum=sum+i
print("sum of even numbers from 1 to 10 is = ",sum)