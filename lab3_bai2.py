# Tinh nhanh A^k bang cheo hoa: A = P * D * P^(-1)  =>  A^k = P * D^k * P^(-1)
def mat_mul_2x2(X, Y):
    return [[X[i][0] * Y[0][j] + X[i][1] * Y[1][j] for j in range(2)] for i in range(2)]


def matrix_power_fast(P, D_diag, P_inv, k):
    D_k = [[D_diag[0] ** k, 0.0], [0.0, D_diag[1] ** k]]
    # Nhan 3 ma tran: P * D_k * P_inv
    return mat_mul_2x2(mat_mul_2x2(P, D_k), P_inv)


# Cach tinh thong thuong: nhan A voi chinh no k lan (de doi chieu ket qua)
def matrix_power_naive(A, k):
    result = [[1.0, 0.0], [0.0, 1.0]]
    for _ in range(k):
        result = mat_mul_2x2(result, A)
    return result


if __name__ == "__main__":
    # A = [[4, 2], [1, 3]] co tri rieng 5, 2
    # Vector rieng: lambda = 5 -> [2, 1], lambda = 2 -> [1, -1]
    A = [[4, 2], [1, 3]]
    P = [[2, 1],
         [1, -1]]
    D_diag = [5, 2]
    P_inv = [[1 / 3, 1 / 3],
             [1 / 3, -2 / 3]]
    k = 10

    fast = matrix_power_fast(P, D_diag, P_inv, k)
    naive = matrix_power_naive(A, k)
    print(f"A^{k} (cheo hoa):  {[[round(v, 4) for v in row] for row in fast]}")
    print(f"A^{k} (nhan lap):  {naive}")
