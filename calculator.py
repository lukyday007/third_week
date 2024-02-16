
# for tc in range(1, 11):
#     N = int(input())
#     string = input()
#     stack = []
#
#     for s in string:
#         # 연산자일 때
#         if not s.isdigit():
#             if len(stack) > 1:
#                 a, b = stack.pop(), stack.pop()
#                 stack.append(a+b)
#         else:
#             # 숫자면 append
#             stack.append(int(s))
#     print(f"#{tc} {sum(stack)}")

string = '7+4+8+3+4+8+5+5+3+6+7+1+2+5+6+5+5+6+1+6+7+8+6+4+7+4+3+1+6+1+2+1+6+8+6+9+2+7+4+3+2+3'
stack = []
ans = 0
for s in string:
    if not stack:
        print(stack)
        stack.append(int(s))
        ans = int(s)
    elif s != "+":
        ans = int(s) + stack[-1]
        stack.append(ans)
    print(stack)
print(ans)



