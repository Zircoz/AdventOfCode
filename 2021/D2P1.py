f = open('inputs.txt','r')
hori, depth = 0,0
for i in f.readlines():
  command,steps = i.split(" ")
  if command=="forward":
    hori+=int(steps)
  elif command=="down":
    depth+=int(steps)
  elif command=="up":
    depth-=int(steps)

print(hori, depth, depth*hori)
