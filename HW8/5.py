import numpy as np

def hamming74_encode(bits):
    """7-4 Hamming 編碼"""
    G = np.array([[1,0,0,0,0,1,1],
                  [0,1,0,0,1,0,1],
                  [0,0,1,0,1,1,0],
                  [0,0,0,1,1,1,1]])
    bits = np.array(bits)
    code = bits @ G % 2
    return code

def hamming74_decode(code):
    """7-4 Hamming 解碼，返回原始4位元"""
    H = np.array([[0,1,1,1,1,0,0],
                  [1,0,1,1,0,1,0],
                  [1,1,0,1,0,0,1]])
    code = np.array(code)
    syndrome = H @ code % 2
    # 計算錯誤位置
    err_pos = sum([2**i*syndrome[2-i] for i in range(3)])
    if err_pos != 0:
        code[err_pos-1] ^= 1  # 修正錯誤
    return code[[0,1,2,3]]

# 範例
data = [1,0,1,1]
encoded = hamming74_encode(data)
print("Encoded:", encoded)

# 模擬單一錯誤
encoded[2] ^= 1
decoded = hamming74_decode(encoded)
print("Decoded:", decoded)
