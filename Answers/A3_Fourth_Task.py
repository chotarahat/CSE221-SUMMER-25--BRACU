
MOD = 1000000007

def multi(A, B):
  result = [[0, 0], [0, 0]]
  for i in range(2):
    for j in range(2):
      for k in range(2):
        result[i][j] += A[i][k] * B[k][j]
      result[i][j] %= MOD
  return result
def mat_pow(matrix, power):
    if power == 1:
        return [[matrix[0][0] % MOD, matrix[0][1] % MOD],
                [matrix[1][0] % MOD, matrix[1][1] % MOD]]

    half = mat_pow(matrix, power // 2)
    result = multi(half, half)
    if power % 2 == 1:
        result = multi(result, matrix)
    return result


t = int(input())

for i in range(t):
    mat_list = list(map(int, input().split()))
    a_mat = [[mat_list[0], mat_list[1]], [mat_list[2], mat_list[3]]]
    X = int(input())

    powered = mat_pow(a_mat, X)

    print(f"{powered[0][0]} {powered[0][1]}")
    print(f"{powered[1][0]} {powered[1][1]}")