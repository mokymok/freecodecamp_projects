def arithmetic_arranger(problems,c=False):
  if 5<len(problems):
    return "Error: Too many problems."
  Op1=Op2=Ds=sR="";space="    "
  for i in range(len(problems)):
    z=problems[i].split()
    if(not(z[1]=="+"or z[1]=="-")):
      return "Error: Operator must be '+' or '-'."
    if(not z[0].isnumeric() or not z[2].isnumeric()):
      return "Error: Numbers must only contain digits."
    if(4<len(z[0] )or 4<len(z[2])):
      return "Error: Numbers cannot be more than four digits."    
    width=max(len(z[0]),len(z[2]))
    Op1+=z[0].rjust(width+2)
    Op2+=z[1]+" "+z[2].rjust(width) 
    Ds+="-"*(width+2)
    if c:
      if z[1]=="+":
        sR+=str(int(z[0])+int(z[2])).rjust(width+2)    
      else:
        sR+=str(int(z[0])-int(z[2])).rjust(width+2)        
    if i<len(problems)-1:
      Op1+=space;Op2+=space;Ds+=space;sR+=space 
  arranged_problems=Op1+"\n"+Op2+"\n"+Ds 
  if c:
    arranged_problems+="\n"+sR
  return arranged_problems
