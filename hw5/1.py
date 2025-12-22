import random

class FiniteField:
    """有限體 F_p"""
    def __init__(self, p):
        if p <= 1 or not self.is_prime(p):
            raise ValueError("p 必須為質數")
        self.p = p

    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def element(self, value):
        """建立有限體元素"""
        return FiniteFieldElement(value % self.p, self)

    def random_element(self):
        return self.element(random.randint(0, self.p - 1))

    def random_nonzero_element(self):
        return self.element(random.randint(1, self.p - 1))


class FiniteFieldElement:
    """有限體元素，支持 + - * / 運算"""
    def __init__(self, value, field: FiniteField):
        self.value = value % field.p
        self.field = field

    def __repr__(self):
        return f"{self.value} (mod {self.field.p})"

    # 加法
    def __add__(self, other):
        self._check_same_field(other)
        return FiniteFieldElement((self.value + other.value) % self.field.p, self.field)

    def __radd__(self, other):
        return self + other

    # 減法
    def __sub__(self, other):
        self._check_same_field(other)
        return FiniteFieldElement((self.value - other.value) % self.field.p, self.field)

    def __rsub__(self, other):
        self._check_same_field(other)
        return FiniteFieldElement((other.value - self.value) % self.field.p, self.field)

    # 乘法
    def __mul__(self, other):
        self._check_same_field(other)
        return FiniteFieldElement((self.value * other.value) % self.field.p, self.field)

    def __rmul__(self, other):
        return self * other

    # 除法
    def __truediv__(self, other):
        self._check_same_field(other)
        if other.value == 0:
            raise ZeroDivisionError("除以零元素")
        # 使用模逆元
        inv = pow(other.value, self.field.p - 2, self.field.p)
        return FiniteFieldElement((self.value * inv) % self.field.p, self.field)

    def __rtruediv__(self, other):
        self._check_same_field(other)
        if self.value == 0:
            raise ZeroDivisionError("除以零元素")
        inv = pow(self.value, self.field.p - 2, self.field.p)
        return FiniteFieldElement((other.value * inv) % self.field.p, self.field)

    # 負元素
    def __neg__(self):
        return FiniteFieldElement(-self.value % self.field.p, self.field)

    # 比較
    def __eq__(self, other):
        return isinstance(other, FiniteFieldElement) and self.value == other.value and self.field.p == other.field.p

    # 檢查是否屬於同一有限體
    def _check_same_field(self, other):
        if not isinstance(other, FiniteFieldElement):
            raise TypeError("兩個元素必須屬於同一有限體")
        if self.field.p != other.field.p:
            raise ValueError("元素不屬於同一有限體")

# --- 範例使用 ---
if __name__ == "__main__":
    p = 7
    F = FiniteField(p)

    a = F.random_element()
    b = F.random_element()
    c = F.random_nonzero_element()

    print(f"a = {a}, b = {b}, c = {c}")

    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * c = {a * c}")
    print(f"c / a = {c / a}")

    # 分配律測試
    lhs = c * (a + b)
    rhs = c * a + c * b
    print(f"{c} * ({a} + {b}) = {lhs}")
    print(f"{c}*{a} + {c}*{b} = {rhs}")
    assert lhs == rhs, "分配律測試失敗！"
    print("分配律測試成功！")
