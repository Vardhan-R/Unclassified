var=True
n1=float(input("No. 1: "))
func=input("+ (OR) - (OR) * (OR) /: ")
while var:
    if func=="+" or func=="-" or func=="*" or func=="/":
        var=0
    else:
        func=input("+ (OR) - (OR) * (OR) /: ")
n2=float(input("No. 2: "))
q=str(n1)+" "+func+" "+str(n2)
if func=="+":
    ans=n1+n2
elif func=="-":
    ans=n1-n2
elif func=="*":
    ans=n1*n2
elif func=="/":
    ans=n1/n2
print(q, "=", ans)
