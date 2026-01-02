import cmath
import math

def dft(x):
    """
    離散傅立葉轉換 (Discrete Fourier Transform)
    輸入: x (時間域/空間域的數列)
    輸出: X (頻率域的複數數列)
    """
    N = len(x)
    X = []
    for k in range(N):
        sum_val = 0
        for n in range(N):
            # Euler's formula: e^(-ix) = cos(x) - i*sin(x)
            # Python 的 cmath.exp 可以直接處理複數指數
            theta = -2 * math.pi * k * n / N
            sum_val += x[n] * cmath.exp(1j * theta)
        X.append(sum_val)
    return X

def idft(X):
    """
    逆離散傅立葉轉換 (Inverse Discrete Fourier Transform)
    輸入: X (頻率域的複數數列)
    輸出: x_recon (重建的時間域/空間域數列)
    """
    N = len(X)
    x_recon = []
    for n in range(N):
        sum_val = 0
        for k in range(N):
            # 逆轉換指數為正，且最後需除以 N
            theta = 2 * math.pi * k * n / N
            sum_val += X[k] * cmath.exp(1j * theta)
        x_recon.append(sum_val / N)
    return x_recon

# --- 驗證區 ---

# 1. 定義一個原始函數 f (這裡用一個簡單的數列代表離散後的 f(x))
# 例如：f(x) = [1, 2, 3, 4]
f_original = [1.0, 2.0, 3.0, 4.0]

print(f"原始信號 f(x): {f_original}")

# 2. 執行正轉換 (DFT)
F_omega = dft(f_original)
print("\n正轉換後的 F(ω) (複數形式):")
for i, val in enumerate(F_omega):
    print(f"  F[{i}]: {val:.2f}")

# 3. 執行逆轉換 (IDFT)
f_reconstructed = idft(F_omega)

print("\n逆轉換回來的 f(x) (取實部):")
# 因為計算會有極小的浮點數誤差，虛部應趨近於 0，我們取實部來驗證
f_final = [val.real for val in f_reconstructed]
print(f"{f_final}")

# 4. 驗證是否相等
is_close = all(abs(a - b) < 1e-9 for a, b in zip(f_original, f_final))
print(f"\n驗證結果 (是否還原): {'成功' if is_close else '失敗'}")