# top = -1
# stack = [0] * 10
# # 스택 밖에서의 우선순위
# icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
# # 스택 안에서의 우선순위
# isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
#
# fx = '(6+5*(2-8)/2)'
# postfix = ''
# for tk in fx:
#     # 여는 괄호 push, 연산자이고 top 원소보다 우선순위가 높으면 push
#     if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):
#         top += 1    # push
#         stack[top] = tk
#         print(f"high - \t\tstack[{top}]: {tk} , stack : {stack}")
#
#     # 연산자이고 top 원소보다 우선순위가 낮으면
#     elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:
#         # top 원소의 우선순위가 낮을 때까지 pop
#         while isp[stack[top]] >= icp[tk]:
#             top -= 1
#             postfix += stack[top + 1]
#             print(f"low - \t\tstack[{top}]: {tk} , stack : {stack}")
#             print(f"postfix: {postfix}")
#
#         # push
#         top += 1
#         stack[top] = tk
#         print(f"low push - \tstack[{top}]: {tk} , stack : {stack}")
#         print()
#
#     # 닫는 괄호면 여는 괄호를 만날 때까지 pop
#     elif tk == ')':
#         print()
#         while stack[top] != '(':
#             top -= 1
#             postfix += stack[top + 1]
#             print(f"close - \tstack[{top}]: {tk}, stack[{top+1}] : {stack[top+1]} , stack : {stack}")
#             print(f"postfix: {postfix}")
#         # 여는 괄호 pop해서 버림
#         top -= 1
#         print(f"close pop - stack[{top}]: {tk}, stack : {stack}")
#         print()
#
#     # 피연산자인 경우
#     else:
#         postfix += tk
# print(f'postfix : {postfix}')



# 재귀 함수
# 알고리즘에서 재귀함수의 사용
# - 동적 계획법 ( 점화식을 구현 )
# - 그래프 탐색 ( DFS 재귀로 구현 ), 트리 순회
# - 백트래킹
# - 분할 정복 ( 이진 탐색 )
# i = 0
# while i < 3:
#     print('hello')
#     i += 1

# # increase recursion limit
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)
# print(sys.setrecursionlimit())

# 재귀함수에서 반복의 종료는 return 그리고 더 이상 재귀호출을 하지 않고 종료
# 어떻게 판단? -> 매개변수
def print_hello(sta, end, m):
    if sta == end:
        return
    else:   # i < 3
        print(sta, end)
        print_hello(sta + 1, end, m + '-')
        print()
        print_hello(sta + 1, end, m + '-')
        print(sta, end)
print_hello(0, 3, "-")










