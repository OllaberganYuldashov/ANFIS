import Humidity
import Temp
import regression


class membership_function:
    def __tch(x1,y1,x2,y2):
        k=(y1-y2)/(x1-x2)
        l=y1-k*x1
        return k,l

    def RTr(value, l_value, a, b):
        if(value<=a):
            return 1
        elif(value>=b):
            return 0
        k,l=membership_function.__tch(a,1,b,0)
        y=k*value+l
        return round(y,2)

    def LTr(value, l_value, a,b):
        if(value<=a):
            return 0
        elif(value>=b):
            return 1
        k,l =membership_function.__tch(a,0,b,1)
        y=k*value+l
        return round(y,2)

    def T(value, l_value, a,b,c):
        k=0
        l=0
        if((value<=a) or (value>=c)):
            k=0
            l=0
        elif(value>a and value<b):
            k,l=membership_function.__tch(a,0,b,1)
        else:
            k,l=membership_function.__tch(b,1,c,0)
        y=k*value+l
        return round(y,2)
    def Tr(value, l_value,a,b,c,d):
        if((value<a) or (value>d)):
            k=0
            l=0
        elif(value>a and value<b):
            k,l=membership_function.__tch(a,0,b,1)
        elif(value>b and value<c):
            return 1
        else:
            k,l=membership_function.__tch(c,1,d,0)
        y=k*value+l
        return round(y,2)


def rules_walue(rule,T,H):

    if("\n" in rule):
        rule=rule[:-1]
    raw=rule.split(" ")
    w_t=0
    w_h=0
    print(raw)

    t_index=0
    h_index=0
    oper="null"

    t_start=0
    t_finish=0
    h_start=0
    h_finish=0

    for i in range(len(raw)):
        if(raw[i].lower()=="temp"):
            t_index=i
        if (raw[i].lower() == "hum"):
            h_index = i
        if(raw[i].lower() in "and or"):
            oper=raw[i].lower()

    if(t_index>0):
        for k in T:
            if(k[0]==raw[t_index+2]):
                w_t=(k[1])
        t_start,t_finish=Temp.temp.interval(raw[t_index+2].lower())
    else:
        t_start=-40
        t_finish=100

    if (h_index>0):
        for z in H:
            if (z[0] == raw[h_index+2]):
                w_h = (z[1])
        h_start,h_finish=Humidity.hum.interval(raw[h_index+2].lower())
    else:
        h_start=0
        h_finish=100
    if(oper=="and"):
        w=min(w_t, w_h)
    elif(oper=="or"):
        w=max(w_t, w_h)
    else:
        w=w_t + w_h

    f=regression.Liner_Regression(t_start,t_finish,h_start,h_finish,oper)

    return w,f

