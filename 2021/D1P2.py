f = open('inputs.txt','r')
l = list()
for i in f.readlines():
  l.append(int(i))
prev, count = 0, 0
for i in range(len(l)-3):
  next = sum(l[i:i+3])
  if next>prev:
    count+=1
  prev=next
print(count)
