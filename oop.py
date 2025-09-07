class Kendaraan:
    # class attribute (sama untuk semua objek)
    jumlah_kendaraan = 0

    def __init__(self, merek, warna):
        # instance attributes (unik untuk tiap objek)
        self.merek = merek
        self.warna = warna
        self.__kecepatan = 0  # atribut private (encapsulation)
        Kendaraan.jumlah_kendaraan += 1

    # instance method
    def info(self):
        return f"{self.merek} berwarna {self.warna}, kecepatan {self.__kecepatan} km/jam"

    def tambah_kecepatan(self, nilai):
        self.__kecepatan += nilai

    # class method
    @classmethod
    def total_kendaraan(cls):
        return f"Total kendaraan: {cls.jumlah_kendaraan}"

    # static method
    @staticmethod
    def aturan_lalu_lintas():
        return "Semua kendaraan wajib berhenti di lampu merah!"


# Inheritance
class Mobil(Kendaraan):
    def __init__(self, merek, warna, pintu):
        super().__init__(merek, warna)
        self.pintu = pintu

    # overriding method (polymorphism)
    def info(self):
        return f"Mobil {self.merek} ({self.pintu} pintu), warna {self.warna}"


class Motor(Kendaraan):
    def __init__(self, merek, warna, tipe):
        super().__init__(merek, warna)
        self.tipe = tipe

    # overriding method
    def info(self):
        return f"Motor {self.merek} tipe {self.tipe}, warna {self.warna}"


# ---- Pemakaian OOP ----
mobil1 = Mobil("Toyota", "Merah", 4)
motor1 = Motor("Yamaha", "Hitam", "Sport")

mobil1.tambah_kecepatan(60)
print(mobil1.info())  # Overriding method di Mobil
print(motor1.info())  # Overriding method di Motor

print(Kendaraan.total_kendaraan())  # Class method
print(Kendaraan.aturan_lalu_lintas())  # Static method
