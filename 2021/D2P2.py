f = open('inputs.txt','r')
hori, depth, aim = 0,0,0
for i in f.readlines():
  command,steps = i.split(" ")
  if command=="forward":
    hori+=int(steps)
    depth+=aim*int(steps)
  elif command=="down":
    aim+=int(steps)
  elif command=="up":
    aim-=int(steps)

print(hori, depth, depth*hori)
