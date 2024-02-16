# # def calculator(cal, stack):
# #     global result
# #     for i in list(map(str, cal.split())):
# #         if i.isdigit():
# #             stack.append(i)
# #         if i in '+-/*':
# #             if not len(stack) > 1:
# #                 return 'error'
# #             else:
# #                 b = int(stack.pop())
# #                 a = int(stack.pop())
# #                 if i == '+':
# #                     stack.append(a + b)
# #                 elif i == '-':
# #                     stack.append(a - b)
# #                 elif i == '/':
# #                     stack.append(a / b)
# #                 else:
# #                     stack.append(a * b)
# #
# #     if len(stack) != 1:
# #         return 'error'
# #
# #     return stack[0]
# #
# # for tc in range(1, int(input())+1):
# #     cal = input()
# #     print(f"#{tc} {calculator(cal, [])}")
#
#
# # ver 2
# def calculator(cal, stack):
#     for i in list(map(str, cal.split())):
#         if i == '.':
#             if len(stack) != 1:
#                 return 'error'
#             return stack.pop()
#
#         elif i.isnumeric():
#             stack.append(int(i))
#
#         elif i in '+-/*':
#             if len(stack) < 2:
#                 return 'error'
#             else:
#                 b = stack.pop()
#                 a = stack.pop()
#                 if i == '+':
#                     stack.append(a + b)
#                 elif i == '-':
#                     stack.append(a - b)
#                 elif i == '/':
#                     stack.append(a / b)
#                 elif i == '*':
#                     stack.append(a * b)
#         else:
#             return 'error'
#     return 'error'
#
#
#
# cal = '6 5 2 8 - * 2 / + .'
# cal2= '1 5 8 10 3 4 + + 3 + * 2 + + + .'
# cal3 = '5 3 * + .'
# cal4 = '10 2 + 3 4 + * .'
# cal5 = '- 5 3 * + .'
# cal6 = '5 3 * + 9 8.'
# print(calculator(cal, []))
# print(calculator(cal2, []))
# print(calculator(cal3, []))
# print(calculator(cal4, []))
# print(calculator(cal5, []))
# print(calculator(cal6, []))




def calculator(cal, stack):
    for i in list(map(str, cal.split())):
        if i == '.':
            if len(stack) != 1:
                return 'error'
            return stack.pop()

        elif i.isnumeric():
            stack.append(int(i))

        elif i in '+-/*':
            if len(stack) < 2:
                return 'error'
            else:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '/':
                    stack.append(a // b)  # / 로 하면 계속 실수로 나옴, 틀린 이유 
                elif i == '*':
                    stack.append(a * b)
        else:
            return 'error'
    return 'error'

for tc in range(1, int(input())+1):
    cal = input()
    print(f"#{tc} {calculator(cal, [])}")




