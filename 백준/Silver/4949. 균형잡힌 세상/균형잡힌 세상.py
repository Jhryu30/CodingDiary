def check_result(check):
  checklist = [] #'()':1 '[]':2
  for c in check:
    if c=='(':
      checklist.append(1)
    elif c=='[':
      checklist.append(2)
      
    elif c==')':
      try:
        if checklist.pop()>1:
          return False
      except:
        return False
    
    elif c==']':
      try:
        if checklist.pop()<2:
          return False
      except:
        return False

  if len(checklist):
    return False
  else:
    return True
    
flag = 1
while flag:
  check = input()
  
  if check=='.':
    flag=0
  
  if flag:
    if check_result(check):
      print('yes')
    else:
      print('no')