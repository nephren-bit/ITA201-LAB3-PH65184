# Kiem tra x co phai vector rieng cua A ung voi tri rieng lambda: A * x == lambda * x
def verify_eigen(A, x, lambda_val, eps=1e-6):
    n = len(A)
    Ax = []
    for i in range(n):
        Ax.append(sum(A[i][j] * x[j] for j in range(len(x))))
    lambda_x = [lambda_val * val for val in x]
    return all(abs(Ax[i] - lambda_x[i]) < eps for i in range(n)), Ax, lambda_x


if __name__ == "__main__":
    A = [
        [4, 2],
        [1, 3]
    ]
    x = [2, 1]
    is_valid, Ax, lambda_x = verify_eigen(A, x, 5)
    print(f"Ax: {Ax} | Lambda*x: {lambda_x}")
    print(f"x la vector rieng: {is_valid}")

    # Thu voi vector khong phai vector rieng
    is_valid, Ax, lambda_x = verify_eigen(A, [1, 1], 5)
    print(f"Ax: {Ax} | Lambda*x: {lambda_x}")
    print(f"[1, 1] la vector rieng: {is_valid}")
