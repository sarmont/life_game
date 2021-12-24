s = input()
nums = [int(el) for el in s.split() if int(el) % 2 != 0]
sq = [str(i ** 2) for i in nums if i ** 2 % 10 != 9]
print(' '.join(sq))
