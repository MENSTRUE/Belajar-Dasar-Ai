# Struktur package:
# my_package/
# ├── __init__.py
# └── math_operations.py  <-- modul

# ===========================
# File: my_package/math_operations.py
# ===========================

PI = 3.14159  # Konstanta, huruf besar semua


class PersegiPanjang:
    """Kelas untuk menghitung luas dan keliling persegi panjang."""

    def __init__(self, panjang: float, lebar: float):
        self.panjang = panjang  # variabel publik
        self.lebar = lebar  # variabel publik
        self._luas_cache = None  # variabel non-publik

    def hitung_luas(self) -> float:
        """Method publik untuk menghitung luas."""
        if self._luas_cache is None:
            self._luas_cache = self.panjang * self.lebar
        return self._luas_cache

    def _reset_cache(self):
        """Method non-publik."""
        self._luas_cache = None


# Exception khusus
class DivideByZeroError(Exception):
    def __init__(self, message="Division by zero is not allowed"):
        super().__init__(message)


def bagi_angka(a: float, b: float) -> float:
    """Fungsi publik untuk membagi dua angka."""
    if b == 0:
        raise DivideByZeroError()
    return a / b


# ===========================
# File: main.py (di luar package)
# ===========================

from my_package.math_operations import PersegiPanjang, bagi_angka, PI

# Variabel lokal
panjang_persegi = 5
lebar_persegi = 2

persegi = PersegiPanjang(panjang_persegi, lebar_persegi)
print("Luas persegi panjang:", persegi.hitung_luas())

try:
    hasil = bagi_angka(10, 0)
except DivideByZeroError as e:
    print(f"Error: {e}")

print("Konstanta PI:", PI)
