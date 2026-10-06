import math

from lab3_bai3 import mean_centering, compute_covariance_matrix


def mat_vec_mul(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


# Tim tri rieng lon nhat va vector rieng tuong ung bang phuong phap lap luy thua (Power Iteration)
def power_iteration(A, num_iter=1000, eps=1e-12):
    n = len(A)
    v = [1.0] * n
    for _ in range(num_iter):
        w = mat_vec_mul(A, v)
        norm = math.sqrt(dot(w, w))
        if norm < eps:
            break
        w = [val / norm for val in w]
        if max(abs(w[i] - v[i]) for i in range(n)) < eps:
            v = w
            break
        v = w
    eigenvalue = dot(v, mat_vec_mul(A, v))
    return eigenvalue, v


# Tim k tri rieng / vector rieng lon nhat cua ma tran doi xung bang Deflation:
# A <- A - lambda * v * v^T sau moi lan tim duoc 1 cap (lambda, v)
def top_k_eigen(A, k):
    n = len(A)
    B = [row[:] for row in A]
    eigenvalues, eigenvectors = [], []
    for _ in range(k):
        lam, v = power_iteration(B)
        eigenvalues.append(lam)
        eigenvectors.append(v)
        B = [[B[i][j] - lam * v[i] * v[j] for j in range(n)] for i in range(n)]
    return eigenvalues, eigenvectors


# PCA thu gon: tru trung binh -> hiep phuong sai 4x4 -> chieu len PC1, PC2
def pca_reduce_2d(data):
    X_centered = mean_centering(data)
    Cov = compute_covariance_matrix(X_centered)
    eigenvalues, (pc1, pc2) = top_k_eigen(Cov, 2)
    reduced = [[dot(row, pc1), dot(row, pc2)] for row in X_centered]
    return reduced, eigenvalues, [pc1, pc2], Cov


def explained_variance_ratio(lambdas, k=2):
    return sum(lambdas[:k]) / sum(lambdas)


if __name__ == "__main__":
    # Cot: Huyet ap, Duong huyet, Cholesterol, BMI
    medical_data = [
        [120, 95, 210, 24.5],
        [140, 130, 250, 29.0],
        [110, 85, 180, 21.5],
        [155, 160, 280, 32.0],
        [130, 105, 220, 26.0]
    ]

    reduced, eigenvalues, pcs, Cov = pca_reduce_2d(medical_data)
    print("Ma tran hiep phuong sai 4x4:")
    for row in Cov:
        print([round(val, 2) for val in row])
    print(f"Tri rieng lon nhat (PC1, PC2): {[round(v, 4) for v in eigenvalues]}")
    print(f"PC1: {[round(v, 4) for v in pcs[0]]}")
    print(f"PC2: {[round(v, 4) for v in pcs[1]]}")
    print("Du lieu sau khi giam chieu (4D -> 2D):")
    for i, row in enumerate(reduced):
        print(f"  Benh nhan {i + 1}: {[round(v, 4) for v in row]}")

    lambdas = [145.2, 32.8, 4.5, 1.2]
    ratio = explained_variance_ratio(lambdas)
    print(f"Ty le phuong sai giai thich duoc: {ratio:.4f} ({ratio * 100:.2f}%)")

# Phan tich y nghia hoc may:
# - Ratio = (145.2 + 32.8) / 183.7 ~ 96.9% > 90%: hai truc PC1, PC2 da giu lai gan nhu toan
#   bo phuong sai (thong tin) cua du lieu. Hai chieu cuoi chi chiem ~3.1%, chu yeu la nhieu
#   hoac bien dong nho, nen loai bo chung KHONG lam mat ban chat du lieu. Nguoc lai con giup
#   giam nhieu, giam tuong quan giua cac thuoc tinh (huyet ap, duong huyet, cholesterol, BMI
#   tang giam cung nhau) va giam chi phi tinh toan cho mo hinh phia sau.
# - Loi ich khi truc quan hoa 2D cho chuyen gia y te: co the ve moi benh nhan thanh 1 diem
#   tren mat phang, de dang nhin thay cac nhom benh nhan co nguy co tuong tu (cum), phat hien
#   benh nhan bat thuong (outlier) va xu huong rui ro tim mach / chuyen hoa ma khong can doc
#   bang so lieu 4 chieu. PC1 o day gan nhu la "chi so nguy co tong hop" vi tat ca cac thong
#   so deu dong gop cung chieu.
