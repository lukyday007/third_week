priority = {"*": 2, "+": 1}
op = '*+'
string = '9+5*2+1+3*3*7*6*9*1*7+1+8*6+6*1*1*5*2*4*7+4*3*8*2*6+7*8*4*5+3+7+2+6+5+1+7+6+7*3*6+2+6+6*2+4+2*2+4*9*3'
pos = ''
stack = []
for s in string:
    if s.isdigit():
        pos += s

    elif s in op:
        while stack and priority[stack[-1]] >= priority[s]:
            pos += stack.pop()
        stack.append(s)

while stack:
    pos += stack.pop()
posList = list(pos)
num_cal = []
for p in posList:
    if not p.isdigit():
        if len(num_cal) > 1 and p == "*":
            a, b = num_cal.pop(), num_cal.pop()
            num_cal.append(a * b)
        elif len(num_cal) > 1 and p == "+":
            a, b = num_cal.pop(), num_cal.pop()
            num_cal.append(a + b)
    else:
        num_cal.append(int(s))
print(sum(num_cal))



