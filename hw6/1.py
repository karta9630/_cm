import math

EPS = 1e-9

# =====================
# 基本幾何物件
# =====================

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def scale(self, k):
        return Point(k * self.x, k * self.y)

    def rotate(self, theta):
        c, s = math.cos(theta), math.sin(theta)
        return Point(
            c * self.x - s * self.y,
            s * self.x + c * self.y
        )

    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Point({self.x:.3f}, {self.y:.3f})"


class Line:
    # ax + by + c = 0
    def __init__(self, a, b, c):
        self.a, self.b, self.c = float(a), float(b), float(c)


class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = float(r)


class Triangle:
    def __init__(self, A, B, C):
        self.A, self.B, self.C = A, B, C

    def translate(self, v):
        self.A += v
        self.B += v
        self.C += v

    def scale(self, k):
        self.A = self.A.scale(k)
        self.B = self.B.scale(k)
        self.C = self.C.scale(k)

    def rotate(self, theta):
        self.A = self.A.rotate(theta)
        self.B = self.B.rotate(theta)
        self.C = self.C.rotate(theta)

# =====================
# 幾何計算
# =====================

def intersect_line_line(L1, L2):
    D = L1.a * L2.b - L2.a * L1.b
    if abs(D) < EPS:
        return None
    x = (L1.b * L2.c - L2.b * L1.c) / D
    y = (L2.a * L1.c - L1.a * L2.c) / D
    return Point(x, y)


def intersect_line_circle(line, circle):
    a, b, c = line.a, line.b, line.c
    h, k = circle.center.x, circle.center.y
    r = circle.r

    # 將直線化為 y = mx + d
    if abs(b) > abs(a):
        m = -a / b
        d = -c / b

        A = 1 + m*m
        B = 2 * (m * (d - k) - h)
        C = h*h + (d - k)**2 - r*r
    else:
        # x = my + d
        m = -b / a
        d = -c / a

        A = 1 + m*m
        B = 2 * (m * (d - h) - k)
        C = k*k + (d - h)**2 - r*r

    Δ = B*B - 4*A*C
    if Δ < 0:
        return []

    sqrtΔ = math.sqrt(Δ)
    t1 = (-B + sqrtΔ) / (2*A)
    t2 = (-B - sqrtΔ) / (2*A)

    if abs(b) > abs(a):
        return [Point(t1, m*t1 + d), Point(t2, m*t2 + d)]
    else:
        return [Point(m*t1 + d, t1), Point(m*t2 + d, t2)]


def intersect_circle_circle(C1, C2):
    d = C1.center.dist(C2.center)
    if d > C1.r + C2.r or d < abs(C1.r - C2.r):
        return []

    a = (C1.r**2 - C2.r**2 + d*d) / (2*d)
    h = math.sqrt(C1.r**2 - a*a)

    x0, y0 = C1.center.x, C1.center.y
    x1, y1 = C2.center.x, C2.center.y

    xm = x0 + a * (x1 - x0) / d
    ym = y0 + a * (y1 - y0) / d

    rx = -(y1 - y0) * (h / d)
    ry = (x1 - x0) * (h / d)

    return [Point(xm + rx, ym + ry), Point(xm - rx, ym - ry)]


def foot_of_perpendicular(P, line):
    a, b, c = line.a, line.b, line.c
    t = (a*P.x + b*P.y + c) / (a*a + b*b)
    return Point(P.x - a*t, P.y - b*t)

# =====================
# 畢氏定理驗證
# =====================

def verify_pythagoras(A, P, line):
    H = foot_of_perpendicular(P, line)

    PA = P.dist(A)
    PH = P.dist(H)
    HA = H.dist(A)

    return abs(PA**2 - (PH**2 + HA**2)) < EPS

# =====================
# 範例測試
# =====================

if __name__ == "__main__":
    line = Line(1, 0, 0)        # x = 0
    A = Point(0, 0)            # 直線上一點
    P = Point(3, 4)            # 線外一點

    print("垂足：", foot_of_perpendicular(P, line))
    print("畢氏定理成立：", verify_pythagoras(A, P, line))
