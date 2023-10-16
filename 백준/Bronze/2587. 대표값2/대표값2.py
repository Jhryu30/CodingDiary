lst = []
for _ in range(5):
  n = int(input(''))
  lst.append(n)
lst = sorted(lst)
print(int(sum(lst)/5))
print(lst[2])