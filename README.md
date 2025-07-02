### 🔒 Fayllarni Butunlay O‘chirish Algoritmlari (Professional Tavsif, Algoritm va Kodlar bilan)

Quyida eng mashhur va xavfsiz fayl o‘chirish algoritmlari to‘liq tushuntirilgan: ishlash prinsipi, bosqichma-bosqich algoritmi, professional Python kodi va har bir qadamning vazifasi bilan birga.

---

## 1. DoD 5220.22-M (AQSh Mudofaa Departamenti Standarti, 3-Pass)

### 🎯 Maqsad:

Faylni ustiga 3 marta yozib, uni qayta tiklab bo‘lmas darajaga yetkazish.

### ✅ Algoritm:

1. Faylni tekshir: mavjudligini aniqlash
2. Fayl hajmini top
3. Faylni 3 marta yoz:

   * Pass 1: 0x00 (hammasi 0)
   * Pass 2: 0xFF (hammasi 1)
   * Pass 3: tasodifiy baytlar
4. Faylni o‘chir

### 📝 Kod:

```python
import os

def dod_5220_22m(filepath):
    if not os.path.isfile(filepath):
        return "Fayl topilmadi"

    size = os.path.getsize(filepath)
    with open(filepath, 'r+b') as f:
        f.seek(0)
        f.write(b'\x00' * size)  # Pass 1: 0x00

        f.seek(0)
        f.write(b'\xFF' * size)  # Pass 2: 0xFF

        f.seek(0)
        f.write(os.urandom(size))  # Pass 3: random

    os.remove(filepath)
    return "DoD 5220.22-M: Fayl o‘chirildi"
```

### 🔹 Har bir qadam vazifasi:

* `seek(0)`: fayl boshiga qaytadi
* `write(...)`: ustiga yozadi
* `os.urandom(size)`: tasodifiy bitlar

---

## 2. DoD ECE (Extended, 7-Pass)

### 🎯 Maqsad:

DoD 5220 asosida, lekin ko‘proq pass bilan yuqori xavfsizlikni ta‘minlaydi.

### ✅ Algoritm:

1. Faylni 7 marta yoz:

   * 0x00
   * 0xFF
   * random
   * 0x00
   * 0xFF
   * random
   * random
2. Faylni o‘chir

### 📝 Kod:

```python
def dod_ece(filepath):
    if not os.path.isfile(filepath):
        return "Fayl topilmadi"

    size = os.path.getsize(filepath)
    pattern = [b'\x00', b'\xFF', 'random', b'\x00', b'\xFF', 'random', 'random']

    with open(filepath, 'r+b') as f:
        for p in pattern:
            f.seek(0)
            if p == 'random':
                f.write(os.urandom(size))
            else:
                f.write(p * size)

    os.remove(filepath)
    return "DoD ECE: Fayl o‘chirildi"
```

---

## 3. Gutmann (35-Pass)

### 🎯 Maqsad:

Turli texnologiyalardagi disklarni hisobga olib, maksimum xavfsizlikka erishish.

### ✅ Algoritm:

1. 27 marta tasodifiy yozish
2. 8 marta maxsus HEX patternlar yozish:

   * 0x55, 0xAA, 0x92, 0x6D, 0x24, 0xDB, 0x49, 0xB6

### 📝 Kod:

```python
def gutmann(filepath):
    if not os.path.isfile(filepath):
        return "Fayl topilmadi"

    size = os.path.getsize(filepath)
    patterns = ['random'] * 27 + [0x55, 0xAA, 0x92, 0x6D, 0x24, 0xDB, 0x49, 0xB6]

    with open(filepath, 'r+b') as f:
        for p in patterns:
            f.seek(0)
            if p == 'random':
                f.write(os.urandom(size))
            else:
                f.write(bytes([p]) * size)

    os.remove(filepath)
    return "Gutmann: Fayl o‘chirildi"
```

---

## 4. RCMP TSSIT OPS-II (Kanada Politsiyasi Standarti)

### 🎯 Maqsad:

Kanada xavfsizlik standarti bo‘lib, 8-pass orqali ma‘lumotni butunlay o‘chiradi.

### ✅ Algoritm:

1. 0x00
2. 0xFF
3. 0x00
4. 0xFF
5. random
6. random
7. random
8. random

### 📝 Kod:

```python
def rcmp_ops_ii(filepath):
    if not os.path.isfile(filepath):
        return "Fayl topilmadi"

    size = os.path.getsize(filepath)
    pattern = [b'\x00', b'\xFF', b'\x00', b'\xFF', 'random', 'random', 'random', 'random']

    with open(filepath, 'r+b') as f:
        for p in pattern:
            f.seek(0)
            if p == 'random':
                f.write(os.urandom(size))
            else:
                f.write(p * size)

    os.remove(filepath)
    return "RCMP OPS-II: Fayl o‘chirildi"
```

---

## 5. NIST 800-88 (Zamonaviy Standart, 1-Pass)

### 🎯 Maqsad:

SSD va zamonaviy disklar uchun: tez va yetarlicha xavfsiz o‘chirish.

### ✅ Algoritm:

1. Faqat 1 marta random bitlar yoziladi
2. Fayl o‘chiriladi

### 📝 Kod:

```python
def nist_800_88(filepath):
    if not os.path.isfile(filepath):
        return "Fayl topilmadi"

    size = os.path.getsize(filepath)
    with open(filepath, 'r+b') as f:
        f.seek(0)
        f.write(os.urandom(size))

    os.remove(filepath)
    return "NIST 800-88: Fayl o‘chirildi"
```

---

## ✅ Yakuniy Tavsiyalar:

| Algoritm      | Pass soni | Foydalanish joyi              |
| ------------- | --------- | ----------------------------- |
| DoD 5220.22-M | 3         | Odatdagi HDD foydalanuvchi    |
| DoD ECE       | 7         | Harbiy & maxfiy tizimlar      |
| Gutmann       | 35        | Maksimal xavfsizlik           |
| RCMP OPS-II   | 8         | Kanada politsiya standartlari |
| NIST 800-88   | 1         | SSD va tez ishlash uchun      |

Agar sizga GUI/Flet/FastAPI asosida ishlaydigan versiyasi ham kerak bo‘lsa, alohida yozib beraman.
