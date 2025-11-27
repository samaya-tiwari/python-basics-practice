
# Exercise 3: Sum of even numbers in a list

nums = [1, 4, 7, 12, 50, 33, 2]
sum = 0
for num in nums:
    if num % 2 == 0:
        sum = sum + num
print('The sum of even numbers is',sum)

'''for i in range(0, 7):
    if nums[i] % 2 == 0:
        sum += nums[i]
print(sum)'''