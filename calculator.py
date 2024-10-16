def sum(x,y):
      return x+y

def mul(x,y):
      return x*y

def sub(x,y):
      return x-y

def div(x,y):
    if y==0:
        return 0
    return x/y

print("This is a calculator")
ans=int(input())
oper=' '
while(oper!='='):
      oper=input()
      if oper=='=':
          print(f"Your answer:{ans}")
          break
      num=int(input())
      if oper=='+':
         ans=sum(ans,num)
      elif oper=='-':
          ans=sub(ans,num)
      elif oper=='x' or oper=='X' or oper=='*':
         ans=mul(ans,num)
      elif oper=='/':
          ans=div(ans,num)
      else:
          print("Please enter a valid operator")
