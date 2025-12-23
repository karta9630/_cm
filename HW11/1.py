import numpy as np
from collections import Counter
def solve_ode_general(coefficients,tol=1e-4):
    roots = np.roots(coefficients)
    roots = [r for r in roots if r.imag >= -tol]
    roots = sorted(roots, key=lambda z: (z.real, z.imag))
    terms = []
    cnt=[]
    tmp=0
    idx=1
    skip = False
    for i in range(len(roots)):
        r=roots[i]

        if i>0 and abs(roots[i]-roots[i-1])<tol:
            tmp+=1
        else :
            tmp=0
        
        x_term = f"x^{tmp} * " if tmp > 0 else ""
        is_complex = r.imag > tol

        if is_complex:
            alpha = r.real
            beta = r.imag
            if alpha>tol:
                term_cos = f"C_{idx} * {x_term}e^({alpha:.2f}x) * cos({beta:.2f}x)"
                terms.append(term_cos)
                idx += 1
                term_sin = f"C_{idx} * {x_term}e^({alpha:.2f}x) * sin({beta:.2f}x)"
                terms.append(term_sin)
                idx += 1
            else :
                term_cos = f"C_{idx} * {x_term}cos({beta:.2f}x)"
                terms.append(term_cos)
                idx += 1
                term_sin = f"C_{idx} * {x_term}sin({beta:.2f}x)"
                terms.append(term_sin)
                idx += 1
        else:
            if abs(r.imag)<tol :
                r= f"{r.real:.2f}"
            elif abs(r.real)<tol:
                r= f"{r.imag:.2f}i"
            else :
                r=f"{r.real:.2f} + {r.imag:.2f}i"

            if tmp==0:
                terms.append(f"C_{idx}e^({r}x)")    
            else :
                terms.append(f"C_{idx} * x^{tmp} * e^({r}x)")
            idx+=1   
        #看幾個重根

        # if i < len(roots) - 1:
        #     if abs(roots[i] - roots[i+1]) >= tol:
        #         cnt.append(tmp)
        # else:
        #     cnt.append(tmp)
    return terms 

# 1231231
# 1112233
#  2233 tmp=2
# 131

# 以下是測試主程式

# 範例測試 (1): 實數單根: y'' - 3y' + 2y = 0  特徵方程: lambda^2 - 3lambda + 2 = 0, 根: 1, 2
# 預期解: C_1e^(1x) + C_2e^(2x)
print("--- 實數單根範例 ---")
coeffs1 = [1, -3, 2]
print(f"方程係數: {coeffs1}")
print(solve_ode_general(coeffs1))

# 範例測試 (2): 實數重根: y'' - 4y' + 4y = 0  特徵方程: lambda^2 - 4lambda + 4 = 0, 根: 2, 2
# 預期解: C_1e^(2x) + C_2xe^(2x)
print("\n--- 實數重根範例 ---")
coeffs2 = [1, -4, 4]
print(f"方程係數: {coeffs2}")
print(solve_ode_general(coeffs2))

# 範例測試 (3): 複數共軛根: y'' + 4y = 0  特徵方程: lambda^2 + 4 = 0, 根: 2i, -2i (alpha=0, beta=2)
# 預期解: C_1cos(2x) + C_2sin(2x)
print("\n--- 複數共軛根範例 ---")
coeffs3 = [1, 0, 4]
print(f"方程係數: {coeffs3}")
print(solve_ode_general(coeffs3))

# 範例測試 (4): 複數重根 (二重): (D^2 + 1)^2 y = 0  特徵方程: (lambda^2 + 1)^2 = 0, 根: i, i, -i, -i (alpha=0, beta=1, m=2)
# 預期解: C_1cos(1x) + C_2sin(1x) + C_3xcos(1x) + C_4xsin(1x)
print("\n--- 複數重根範例 ---")
coeffs4 = [1, 0, 2, 0, 1]
print(f"方程係數: {coeffs4}")
print(solve_ode_general(coeffs4))

# 範例測試 (5): 高階重根: y''' - 6y'' + 12y' - 8y = 0  特徵方程: (lambda - 2)^3 = 0, 根: 2, 2, 2
# 預期解: C_1e^(2x) + C_2xe^(2x) + C_3x^2e^(2x)
print("\n--- 高階重根範例 ---")
coeffs5 = [1, -6, 12, -8]
print(f"方程係數: {coeffs5}")
print(solve_ode_general(coeffs5))