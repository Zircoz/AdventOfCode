f = open('inputs.txt','r')
inps = list()
for i in f.readlines():
  inps.append(i.split("\n")[0])

def findOGR(li):
  i=0
  while(len(li)>1):
    print("before",len(li))
    digits = [k[i] for k in li]
    count1 = digits.count("1")
    count0 = digits.count("0")
    print(i,count1, count0)
    check=''
    if count1>count0:
      check='1'
    elif count0>count1:
      check='0'
    else:
      check='1'
    print(check)
    li = list(filter(lambda x: x[i]==check, li))
    print("after",len(li))
    i+=1
  return int(li[0],2)

def findCOSR(li):
  i=0
  while(len(li)>1):
    digits = [k[i] for k in li]
    count1 = digits.count("1")
    count0 = digits.count("0")
    check=''
    if count1>count0:
      check='0'
    elif count0>count1:
      check='1'
    else:
      check='0'
    li = list(filter(lambda x: x[i]==check, li))
    i+=1
  return int(li[0],2)
#print(findOGR(inps))
#print(findCOSR(inps))
print(findOGR(inps)*findCOSR(inps))
