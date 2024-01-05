def print_triangle(edge):
  edge = sorted(edge)
  if edge[2]>=edge[0]+edge[1]:
    return 'Invalid'
  if edge[0]==edge[1] or edge[1]==edge[2] or edge[0]==edge[2]:
    if edge[0]==edge[1] and edge[1]==edge[2]:
      return 'Equilateral'
    else:
      return 'Isosceles'
  else:
    return 'Scalene'

edge = [1,1,1]
while edge[0]>0:
  edge = list(map(int, input('').split()))
  if edge[0]==0:
    break
  print(print_triangle(edge))