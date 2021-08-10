def add_time(start, duration, starting_day=""):
  days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  timer=duration.split(":")
  st=start.replace(":"," ").split()    
  fh=0
  fm=int(timer[1])+int(st[1])
  if(fm>60):
    fh+=int(fm/60)
    fm=fm % 60
  fh+=int(timer[0])+int(st[0])
  if st[2]=="PM":
    fh+=12    
  n=int(fh/24) 
  fh=fh%24
  if fh<12:
    pm=" AM"
  else:
    pm=" PM"
  fh=fh%12
  if fh==0:
    fh=12    
  new=str(fh)+":"+str(fm).rjust(2,'0')+pm;    
  if starting_day:
    for i in range(len(days)):
      if(str.upper(starting_day)==str.upper(days[i])):
        new+=(", "+days[ (i+n) % len(days)])
        break
  if 1 <=n:
    if n==1:
      new+=" (next day)"
    else:
      new+=" ("+str(n)+" days later)"
  return new
