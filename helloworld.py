from random import randint

# REQ 1: Print your name
print("Robert A. Dekovich")

# REQ 2: Print 2 random numbers in the range from 0 to 100
nums = [randint(0,100) for i in range(0,2)]

print(nums[0])
print(nums[1])

# REQ 3: Print the sum and mean of the two random numbers
sum = 0

for i in nums:
	sum += i

mean = sum / len(nums)

print(sum)
print(mean)

exit(0)
