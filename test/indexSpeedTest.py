#! /usr/bin/python
import time

iteration = 1

string = ".:foo::bar:. .:IfInThread:: .:boo:: .:foo::bar:. :. :: lolilol :. .:END:. .:TEST AGAIN:: .:WITHIN:. :."
print('>', string)

def algo1():
    op = []
    cp = []
    i = 0
    l = len(string)
    output = string
    offset=0
    while i < l:
        i = output.find(".:", i)
        if i == -1:
            i=0
            break
        op.append(i)
        i+=2
    
    while i < l:
        i = output.find(":.", i)
        if i == -1:
            i=0
            break
        cp.append(i)
        i+=2

    l = len(op)
    while l:
        for i in range(0, l):
            try:
                cmpr = cp[i] < op[i+1]

            except Exception as e:
                if len(cp) != l:
                    raise e

                cmpr = True

            if cmpr:
                vop, vcp = op[i], cp[i]
                print(output[vop+2:vcp])
                fields = [field.strip() for field in output[vop+2:vcp].split("::") if field != '']
                new_string = "["+'---'.join(fields)+"]"
                output = output[0:vop] + new_string + output[vcp+2:]
                offset = len(new_string) - (vcp + 2 - vop)
                print(output)
                for j in range(i+1,l):
                    op[j]+=offset
                    cp[j]+=offset
                print(op)
                print(cp)
                print()
                op.pop(i)
                cp.pop(i)
                l = len(op)
                break

                
                
    return output

def algo2(string):
    op = []
    cp = []
    l = len(string)
    fields=[]
    for i in range(0, l):
        if string[i:i+2] == ".:":
            op.append(i)    
        
        elif string[i:i+2] == ":.":
            cp.append(i)
            
        if len(cp) <= len(op) and len(cp) != 0 and len(op) != 0:
            if op[-1] < cp[-1]:
                fields = [field.strip() for field in string[op[-1]+2:cp[-1]].split("::") if field != '']
                
                return algo2(string[:op[-1]]+"["+'---'.join(fields)+"]"+string[cp[-1]+2:])

    return string

t = time.time()
for i in range(0,iteration):
    c = algo1()

print(c)

print("ALGO1", time.time()-t)
t = time.time()
for j in range(0,iteration):
    s = algo2(string)
print(s)
print("ALGO2", time.time()-t)
