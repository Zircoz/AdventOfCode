f = open('inputs.txt','r')
inps = list()
for i in f.readlines():
  inps.append(i.split("\n")[0])
gamma,epsilon = '',''
for i in range(len(inps[0])):
  digits = [k[i] for k in inps]
  count1 = digits.count("1")
  count0 = digits.count("0")
  print(count1,count0)
  if count1>count0:
    gamma+='1'
    epsilon+='0'
  elif count0>count1:
    gamma+='0'
    epsilon+='1'
print(int(gamma,2)*int(epsilon,2))
