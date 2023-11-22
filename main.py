import random

nums = []
new_num = ""

for i in range(10):
    x = (random.randint(1000000000, 9999999999))
    nums.append(str(x))
    y = nums[i][i]
    if y != "9":
        new_num += str(int(nums[i][i]) + 1)
    else:
        new_num += "0"


for i in range(len(nums)):
    nums[i] = float("0." + str(nums[i]))

print(nums)
print((float("0." + new_num)))
