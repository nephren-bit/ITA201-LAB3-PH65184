# Tru trung binh tung cot: X_centered[i][j] = X[i][j] - mean_j
def mean_centering(X):
    M = len(X)
    N = len(X[0])
    means = [sum(X[i][j] for i in range(M)) / M for j in range(N)]
    X_centered = [[X[i][j] - means[j] for j in range(N)] for i in range(M)]
    return X_centered


# Ma tran hiep phuong sai N x N: Cov[i][j] = sum(Xc[k][i] * Xc[k][j]) / (M - 1)
def compute_covariance_matrix(X_centered):
    M = len(X_centered)
    N = len(X_centered[0])
    Cov = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            Cov[i][j] = sum(X_centered[k][i] * X_centered[k][j] for k in range(M)) / (M - 1)
    return Cov


if __name__ == "__main__":
    X = [
        [2.5, 2.4],
        [0.5, 0.7],
        [2.2, 2.9],
        [1.9, 2.2],
        [3.1, 3.0]
    ]
    X_centered = mean_centering(X)
    print("X_centered:")
    for row in X_centered:
        print([round(val, 4) for val in row])
    print("Ma tran hiep phuong sai:")
    for row in compute_covariance_matrix(X_centered):
        print([round(val, 4) for val in row])
