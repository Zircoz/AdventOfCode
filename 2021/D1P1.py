f = open('inputs.txt','r')
prev, count = int(f.readline()), 0
for i in range(1999):
  next = int(f.readline())
  if next>prev:
    count+=1
  prev = next
print(count)
