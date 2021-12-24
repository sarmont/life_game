# Вводится последовательность слов
nums = [int(el) for el in input().split()]
# print(nums)
words = [el.lower() for el in input().split()]

for i in range(len(nums)):
    if i == 0:
        print(words[nums[i] - 1].capitalize(), end=' ')
    else:
        print(words[nums[i] - 1], end=' ')
