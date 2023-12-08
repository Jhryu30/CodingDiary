N = int(input())
count = 0

for _ in range(N):
  word = list(input())
  stack = []
  for w in word:
    if stack:
      if w==stack[-1]:
        stack.pop()
      else:
        stack.append(w)
    else:
      stack.append(w)
  if not stack:
    count += 1
print(count)