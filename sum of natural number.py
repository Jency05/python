def recur_sum(n):
  if n<=1:
    return n
  else:
    return n+recur_sum(n-1)
num=16
if n<0:
  print("enter a +ve number")
else:
  print("the sum is",recur_sum(num))