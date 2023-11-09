N,M,K = map(int, input().split()) # height,width, count

note = [[0 for _ in range(M)] for _ in range(N)]
sticker_dict = {k:{0:[0,0], 1:[0]} for k in range(K)}
for k in range(K):
  r,c = map(int, input().split())
  s = [list(map(int, input().split())) for _ in range(r)]
  sticker_dict[k][0]=[r-1,c-1]
  sticker_dict[k][1] = s
  
def locate_sticker(sticker, size):
  global note
  r,c = size
  for start_row in range(N-r):
    for start_col in range(M-c):
      note_sticker = [[note[row][col] for col in range(start_col,start_col+c+1)] for row in range(start_row,start_row+r+1)]
      # sticker available in this location
      if fit_sticker(note_sticker, sticker, size):
        return [start_row,start_col]
  return [-1,-1]

def fit_sticker(note_sticker, sticker, size):
  # does sticker fit in this location
  r,c = size
  for i in range(r+1):
    for j in range(c+1):
      if note_sticker[i][j] and sticker[i][j]:
        return False
  return True

def rotate_sticker(sticker,size,rotate_num):
  r,c = size
  if rotate_num==0:
    return sticker, size
  elif rotate_num==1:
    return [[sticker[r-i][j] for i in range(r+1)] for j in range(c+1)], size[::-1]
  elif rotate_num==2:
    return [[sticker[r-i][c-j] for j in range(c+1)] for i in range(r+1)], size
  else:
    return [[sticker[i][c-j] for i in range(r+1)] for j in range(c+1)], size[::-1]

for k in range(K):
  size = sticker_dict[k][0]
  sticker = sticker_dict[k][1]

  # find place
  start_v = locate_sticker(sticker,size)

  if start_v[0]==-1: # rotate 90'
    sticker_,size_ = rotate_sticker(sticker, size, 1)
    start_v = locate_sticker(sticker_,size_)
    if start_v[0]>-1:
      sticker,size = sticker_[:],size_[:]

  if start_v[0]==-1: # rotate 180'
    sticker_,size_ = rotate_sticker(sticker, size, 2)
    start_v = locate_sticker(sticker_,size_)
    if start_v[0]>-1:
      sticker,size = sticker_[:],size_[:]

  if start_v[0]==-1: # rotate 270'
    sticker_,size_ = rotate_sticker(sticker, size, 3)
    start_v = locate_sticker(sticker_,size_)
    if start_v[0]>-1:
      sticker,size = sticker_[:],size_[:]
      
  # attach
  if start_v[0]>-1:
    r,c = size
    start_r,start_c = start_v
    for i in range(r+1):
      for j in range(c+1):
        if sticker[i][j]:
          note[start_r+i][start_c+j] = 1

print(sum([sum(note[row]) for row in range(N)]))