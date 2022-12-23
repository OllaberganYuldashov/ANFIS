import Humidity
import Temp
import fuzzy

t=100
h=0


T=Temp.temp.run(t)
H=Humidity.hum.run(h)

w=[]
wn=[]
f=[]

r_file=open("rules.txt", "r")
rules=r_file.readlines()

for rule in rules:
    value=fuzzy.rules_walue(rule,T,H)
    w.append(value[0])
    coef=value[1]
    f.append(round(coef[0]*t+coef[1]*h+coef[2],2))
print(w)
print(f)
s=0
for i in w:
    s=s+i
for i in w:
    wn.append(i/s)

z=0
for i in range(len(wn)):
    z=z+wn[i]*f[i]

z=round(z,2)

print(z)

