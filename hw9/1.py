import numpy as np
from scipy.linalg import lu, qr, svd, eig

np.set_printoptions(precision=4, suppress=True)

# 1. 遞迴方式計算行列式 (Recursive Determinant)
def recursive_det(matrix):
    n = len(matrix)
    # Base case: 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    # Laplace expansion along the first row
    for c in range(n):
        sub_matrix = np.delete(np.delete(matrix, 0, axis=0), c, axis=1)
        det += ((-1) ** c) * matrix[0][c] * recursive_det(sub_matrix)
    return det

# 測試矩陣
A = np.array([[6, 1, 1], 
              [4, -2, 5], 
              [2, 8, 7]], dtype=float)

print(f"## 1. 遞迴計算行列式: {recursive_det(A)}")
print(f"   (Numpy 驗證): {np.linalg.det(A)}")
print("-" * 30)

# 2. LU 分解計算行列式
# A = P * L * U (P is permutation matrix)
# det(A) = det(P) * det(L) * det(U)
# det(L) is 1 (diagonal is 1s), det(U) is product of diagonal
P, L, U = lu(A)
det_P = np.linalg.det(P) # Usually 1 or -1
det_U = np.prod(np.diag(U))
det_via_lu = det_P * 1 * det_U

print(f"## 2. LU 分解後計算行列式: {det_via_lu}")
print("-" * 30)

# 3. 驗證分解與還原 (LU, Eigen, SVD)
print("## 3. 驗證分解還原")

# LU
A_recon_lu = P @ L @ U
print(f"   LU 還原成功? {np.allclose(A, A_recon_lu)}")

# Eigen decomposition (A = V * diag(w) * V^-1)
w, V = np.linalg.eig(A)
D = np.diag(w)
A_recon_eig = V @ D @ np.linalg.inv(V)
print(f"   Eigen 還原成功? {np.allclose(A, A_recon_eig)}")

# SVD (A = U * S * Vt)
U_svd, s, Vt = np.linalg.svd(A)
S_mat = np.diag(s) # convert vector s to diagonal matrix
A_recon_svd = U_svd @ S_mat @ Vt
print(f"   SVD 還原成功? {np.allclose(A, A_recon_svd)}")
print("-" * 30)

# 4. 用特徵值分解實作 SVD (Conceptual Implementation)
# 原理: 
# V 是 A.T @ A 的特徵向量
# Singular values (sigma) 是 A.T @ A 特徵值的平方根
# U 可以由 A @ v / sigma 得到
print("## 4. 手刻 SVD (透過 Eigen)")

ATA = A.T @ A
eig_vals, V_calc = np.linalg.eigh(ATA) # eigh for symmetric matrix

# Sort eigenvalues and vectors in descending order (SVD convention)
idx = eig_vals.argsort()[::-1]
eig_vals = eig_vals[idx]
V_calc = V_calc[:, idx]

# Calculate Singular values
sigmas = np.sqrt(np.abs(eig_vals))

# Calculate U: u_i = A * v_i / sigma_i
U_calc = np.zeros_like(A)
for i in range(len(sigmas)):
    U_calc[:, i] = np.dot(A, V_calc[:, i]) / sigmas[i]

print(f"   計算出的奇異值: {sigmas}")
print(f"   Numpy SVD 奇異值: {s}")
print(f"   數值接近? {np.allclose(sigmas, s)}")
print("-" * 30)

# 5. PCA 主成分分析實作
print("## 5. PCA 實作")
# 假設數據集 X (5 samples, 3 features)
X = np.array([[2.5, 2.4, 0.5],
              [0.5, 0.7, 0.3],
              [2.2, 2.9, 0.4],
              [1.9, 2.2, 0.2],
              [3.1, 3.0, 0.6]])

# Step 1: Center the data (減去平均)
X_mean = np.mean(X, axis=0)
X_centered = X - X_mean

# Step 2: Covariance Matrix
cov_matrix = np.cov(X_centered, rowvar=False)

# Step 3: Eigen decomposition of Covariance
eigen_values, eigen_vectors = np.linalg.eigh(cov_matrix)

# Sort (descending)
sorted_index = np.argsort(eigen_values)[::-1]
sorted_eigenvectors = eigen_vectors[:, sorted_index]

# Step 4: Project data (e.g., reduce to 2D)
n_components = 2
eigenvector_subset = sorted_eigenvectors[:, 0:n_components]
X_reduced = np.dot(X_centered, eigenvector_subset)

print(f"   原始維度: {X.shape}")
print(f"   降維後維度: {X_reduced.shape}")
print(f"   主成分方向 (Top 2):\n{eigenvector_subset}")