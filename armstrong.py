def checkArmstrong(num):
    sum=0
    temp=num
    digit=0
    digits=len(str(num))
    while temp>0:
        digit=temp%10
        sum=sum+digit**digits   
        temp=temp//10
    if sum==num:
        return True
    else:
        return False
    
a=int(input("enter the number:")) 
result=checkArmstrong(a)
if result==True:
    print(a,"is an Armstrong number")       
else:
    print(a,"is not an Armstrong number")