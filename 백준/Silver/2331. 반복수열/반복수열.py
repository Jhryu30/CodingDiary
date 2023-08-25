A, P = map(int, input().split())

def seq_d(A,P):
  return sum(map(lambda x:int(x)**P, list(str(A))))

graph = [A]

while True:
  new_A = seq_d(A,P)
  if new_A in graph:
    i = graph.index(new_A)
    print(i)
    break
  else:
    graph.append(new_A)
    A = new_A