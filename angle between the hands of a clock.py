h=-1
m=0
ha=0
ma=0

for i in range (12):
    m=0
    h=h+1
    ma=0
    
    for j in range (60):
        
        if ((len(str(h)))==1):
            x=("0" + str(h))
            
            if ((len(str(m)))==1):
                y=("0" + str(m))

                print(x, ":", y, "  angle:", abs(ha-ma), " ", 360-abs(ha-ma));

            else:
                print(x, ":", m, "  angle:", abs(ha-ma), " ", 360-abs(ha-ma));
            
        else:
            if((len(str(m)))==1):
                y=("0" + str(m))
                
                print(h, ":", y, "  angle:", abs(ha-ma), " ", 360-abs(ha-ma));

            else:
                print(h, ":", m, "  angle:", abs(ha-ma), " ", 360-abs(ha-ma));
            
        m=m+1
        ha=ha+0.5
        ma=ma+(6)
