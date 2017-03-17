string='string'
integer=10
floating=10.2
list1=[]
while True:
    x=int(input("Help For:-\n\t1)Integer\n\t2)Float\n\t3)String\nEnter your choice: "))
    count=1
    z=(input("Would you like to 'print' or save on a 'notepad'.:"))
    if z=='print':
        if(x==1):
            list1=dir(integer)
            for i in list1:
                print(count,') ',i)
                count+=1
            print(count,') All')
            y=int(input("Enter Your Choice: "))
            if y<count:
                result= getattr(integer,list1[y-1])
                print(list1[y-1],end=':--  ')
                print(help(result),end='\n'*5)
                print('_'*80,end='\n'*2)
            elif(y==count):
                for i in list1:
                    result= getattr(integer,i)
                    print(i,end=':--  ')
                    print(help(result),end='\n'*5)
                    print('_'*80,end='\n'*2)
            else:
                break
        elif(x==2):
            list1=dir(floating)
            for i in list1:
                print(count,') ',i)
                count+=1
            print(count,') All')
            y=int(input("Enter Your Choice: "))
            if y<count:
                result= getattr(floating,list1[y-1])
                print(list1[y-1],end=':--  ')
                print(help(result),end='\n'*5)
                print('_'*80,end='\n'*2)
            elif(y==count):
                for i in list1:
                    result= getattr(floating,i)
                    print(i,end=':--  ')
                    print(help(result),end='\n'*5)
                    print('_'*80,end='\n'*2)
            else:
                break
        elif(x==3):
            list1=dir(string)
            for i in list1:
                print(count,') ',i)
                count+=1
            print(count,') All')
            y=int(input("Enter Your Choice: "))
            if y<count:
                result= getattr(string,list1[y-1])
                print(list1[y-1],end=':--  ')
                print(help(result),end='\n'*5)
                print('_'*80,end='\n'*2)
            elif(y==count):
                for i in list1:
                    result= getattr(string,i)
                    print(i,end=':--  ')
                    print(help(result),end='\n'*5)
                    print('_'*80,end='\n'*2)
            else:
                break
        else:
            break
    elif z=='notepad':
        print('Code Under Progress')
