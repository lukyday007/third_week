# # powerset 1
# def f(i, k):
#     if i == k:
#         for j in range(k):
#             if bit[j]:
#                 print(arr[j], end=" ")
#         print()
#     else:
#         bit[i] = 0
#         f(i + 1, k)
#         bit[i] = 1
#         f(i + 1, k)
#
# N = 4
# arr = [1,2,3,4]
# # bit[i] : arr[i]가 부분집합에 포함되었는지를 나타내었는지 배열
# bit = [0] * N
# # bit[i] 에 1 또는 0을 채우고, N개의 원소가 결정되면 부분집합을 출력
# f(0, N)



# # powerset 2
# def backtrack(a, k, input):
#     global maxCandi
#     c = [0] * maxCandi
#
#     if k == input:
#         onProcess(a, k) # 답이면 처리 수행
#     else:
#         k += 1
#         nCandi = buildCandi(a, k, input, c)
#         for i in range(nCandi):
#             a[k] = c[i]
#             backtrack(a, k, input)
#
# def buildCandi(a, k, input, c):
#     c[0] = True
#     c[1] = False
#     return 2
#
# maxCandi = 2
# nMax = 4
# a = [0] * nMax
# backtrack(a, 0, 4)

# powerset 2
# def backtrack(a, k, input):
#     global maxCandi
#     c = [0] * maxCandi
#
#     if k == input:
#         # onProcess(a, k)  # Process/print the solution
#         return
#     else:
#         nCandi = buildCandi(a, k, input, c)
#         print()
#         print(f"nCandi : {nCandi}")
#         for i in range(nCandi):
#             a[k] = c[i]
#             print(f"a : {a}")
#             print(f"k + 1 : {k + 1}, input : {input}")
#             backtrack(a, k + 1, input)  # k should be k + 1 to move to the next level
#
# def buildCandi(a, k, input, c):
#     # Example candidate logic (true/false)
#     c[0] = True
#     c[1] = False
#     return 2  # Number of candidates
#
# def onProcess(a, k):
#     # Simple process to print the solution
#     print(a[:k])  # Adjusted to print relevant part of the solution
#
# maxCandi = 2
# nMax = 4
# a = [0] * (nMax)  # Adjusted to account for 1-based indexing in onProcess
# backtrack(a, 0, nMax)

N = 3
bits = [0] * N

# def backTrack1(k, cnt):
#     if k == N:
#         print("\t"*cnt, k, '-', cnt)
#         print("\t"*cnt,bits, cnt)
#         return
#     print("\t"*cnt, k, '-', cnt)
#     bits[k] = k + 10
#     print("\t"*cnt, bits, cnt)
#     backTrack1(k+1, cnt + 1)
#     bits[k] = 0
#     print("\t"*cnt, bits, cnt)
#
# backTrack1(0,0)
# print()
#
# def backTrack2(k):
#     if k == N:
#         return
#     # arr[k]를 포함
#     bits[k] = 1
#     backTrack2(k + 1)
#     print(f"포함 : {bits}")
#     # 포함 X
#     bits[k] = 0
#     backTrack2(k + 1)
#     print(f"미포함 : {bits}")
#
# backTrack2(0)
# print()

# arr = 'ABC'
# subset = [] # 빈 리스트에 추가
# def backTrack3(k):
#     if k == N:
#         for i in range(N):
#             if bits[i]:
#                 print(arr[i], end=" ")
#         print()
#         return
#     # arr[k]를 포함
#     bits[k] = 1
#     backTrack3(k+1)
#     # arr[k] 미포함
#     bits[k] = 0
#     backTrack3(k+1)
#
# backTrack3(0)


# ver 1
arr = ['A', 'B', 'C']
N = len(arr)

for i in range(0, N):
    arr[0], arr[i] = arr[i], arr[0]
    for j in range(1, N):
        arr[1], arr[j] = arr[j], arr[1]
        for k in range(2, N):
            arr[2], arr[k] = arr[k], arr[2]
            print(arr)
            arr[2], arr[k] = arr[k], arr[2]
        arr[1], arr[j] = arr[j], arr[1]
    # 출력하고 난 후 원위치
    arr[0], arr[i] = arr[i], arr[0]


# ver 2
arr = ['A', 'B', 'C']
N = len(arr)

def perm(k):
    if k == N:
        print(*arr)
        return
    for i in range(k, N):
        arr[k], arr[i] = arr[i], arr[k]
        # 재귀 호출
        perm(k+1)
        arr[k], arr[i] = arr[i], arr[k]
perm(0)


















