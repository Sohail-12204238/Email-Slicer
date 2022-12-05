while(True):
    x=str(input("Enter email: "))   #user will enter the email
    i=0
    j=0
    str1=""
    str2=""
    for i in range(0,len(x)):        #loop has initiated
        if(x[i]=="@"):
            break
        str1=str1+x[i]
    print("username:",(str1))
    for j in range(x.index("@"),len(x)):     #username is printed
        if(x[j] !="@"):
            str2=str2+x[j]
    print("Domain:",(str2.upper()))        #domain is printed
