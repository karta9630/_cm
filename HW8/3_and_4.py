import numpy as np

def entropy(p):
    """計算熵 H(p)"""
    p = np.array(p)
    p = p[p > 0]  # 避免 log(0)
    return -np.sum(p * np.log2(p))

def cross_entropy(p, q):
    """計算交叉熵 H(p,q)"""
    p = np.array(p)
    q = np.array(q)
    q = np.clip(q, 1e-12, 1)  # 避免 log(0)
    return -np.sum(p * np.log2(q))

def kl_divergence(p, q):
    """計算 KL 散度 D_KL(p||q)"""
    p = np.array(p)
    q = np.array(q)
    mask = p > 0
    return np.sum(p[mask] * np.log2(p[mask] / q[mask]))

def mutual_information(p_xy, p_x, p_y):
    """
    計算互資訊 I(X;Y)
    p_xy: 二維聯合分布矩陣 p(x,y)
    p_x: X 的邊際分布
    p_y: Y 的邊際分布
    """
    I = 0.0
    for i in range(p_xy.shape[0]):
        for j in range(p_xy.shape[1]):
            if p_xy[i,j] > 0:
                I += p_xy[i,j] * np.log2(p_xy[i,j] / (p_x[i]*p_y[j]))
    return I

# 範例
p = [0.5, 0.5]
q = [0.7, 0.3]

print("H(p) =", entropy(p))
print("H(p,q) =", cross_entropy(p,q))
print("D_KL(p||q) =", kl_divergence(p,q))

# 驗證 H(p) < H(p,q) 當 p != q
print("H(p) =", cross_entropy(p,p))
print("H(p,q) =", cross_entropy(p,q))
