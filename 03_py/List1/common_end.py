def common_end(a, b):
  return (a[0] == b[0]) or (a[len(a) - 1] == b[len(b) - 1])


#I made an or statement inside the return statement. This will check whether the start or end of both lists equal.

#common_end([2,3,4,2],[1,2,3,1]) ------> False
#common_end([2,3,7,8],[2.1.2.6]) ------> True
#common_end([1,6,7,5,4],[3,4,3,5,4]) ------> True
