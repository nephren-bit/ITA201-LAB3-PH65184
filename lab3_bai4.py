import math


# Chieu du lieu len thanh phan chinh: z_i = <X_centered[i], pc_vector>
def project_data_1d(X_centered, pc_vector):
    return [sum(row[j] * pc_vector[j] for j in range(len(pc_vector))) for row in X_centered]


if __name__ == "__main__":
    X_centered = [
        [1.0, 1.0],
        [-1.0, -1.0],
        [2.0, 1.5],
        [-2.0, -1.5]
    ]
    pc_vector = [1 / math.sqrt(2), 1 / math.sqrt(2)]  # do dai = 1
    projected = project_data_1d(X_centered, pc_vector)
    print(f"Du lieu sau khi chieu (1D): {[round(v, 4) for v in projected]}")
