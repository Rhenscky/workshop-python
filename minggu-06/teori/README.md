# KESALAHAN DAN PENGECUALIAN
Kesalahan yang terjadi ketika Python tidak dapat memahami apa yang Anda perintahkan
2 Jenis kesalahan pada penulisan kode python yaitu kesalahan sintaksis atau kesalahan sintaks yang terjadi ketika Python tidak dapat memahami apa yang Anda perintahkan. Sedangkan masalah atau pengecualian (kesalahan saat beroperasi) terjadi ketika Python mengerti apa yang Anda perintahkan tetapi mendapatkan saat mengikuti yang Anda perintahkan (terjadi saat aplikasi sudah mulai beroperasi).
## Kesalahan Sintaksis
Contoh kesalahan pada sintaksis : setelah kondisi dari perintah sementara diharuskan ada tanda titik dua (:)
Pada kesalahan sintaksis, baris di mana kesalahan terdeteksi dimunculkan kembali, kemudian terdapat tanda panah yang menunjukkan titik paling awal dari kesalahan.
Kedua contoh di atas memiliki kelompok (tipe) kesalahan yang berbeda, yang pertama adalah IndentationError dan yang kedua adalah SyntaxError. Kemudian setelah penyebutannya, ada pesan detail kesalahan (keterangan), misalnya indentasi yang tidak diharapkan (unexpected).
#### ```Kode 1```
```
while True print('Hello world')
  File "<stdin>", line 1
                 ^ 
SyntaxError: sintaks tidak valid
```

## Pengecualian
Kesalahan yang terjadi saat proses sedang berlangsung disebut kesalahan (exceptions) dan akan berakibat fatal jika tidak ditangani. sukses di Python tidak ditangani oleh aplikasi, sehingga aplikasi terhenti kemudian muncul pesan kesalahan seperti contoh berikut.
#### ```Kode 2```
```
10 * (1/0)
4 + spam*3
'2' + 2
```

## Menangani Pengecualian
Pada aplikasi Python yang Anda buat bisa menangani penanganan terhadap penilaian (exceptions handling) dari kelompok (tipe) kesalahan yang Anda tentukan. Proses penanganan menggunakan pernyataan yang berpasangan dengan kecuali .
#### ```Kode 3```
```
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```
#### ```Kode 4```
```
except (RuntimeError, TypeError, NameError):
pass
```
#### ```Kode 5```
```
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```
#### ```Kode 6```
```
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```
#### ```Kode 7```
```
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```
#### ```Kode 8```
```
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))   # contoh pengecualian
    print(inst.args)    # argumen disimpan di .args
    print(inst)         # __str__ memungkinkan args untuk dicetak secara langsung,
                        # tetapi dapat diganti dalam subkelas pengecualian
    x, y = inst.args    # unpack args
    print('x =', x)
    print('y =', y)
```
#### ```Kode 9```
```
def this_fails():
    x = 1/0
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
```

## Memunculkan Pengecualian
Dalam membuat aplikasi, ada kemungkinan Anda butuh untuk mengembangkan (meningkatkan pengecualian), salah satu caranya dengan menggunakan ide yang ada, hanya menambahkan informasi detailnya saja.
#### ```Kode 10```
```
raise NameError('HiThere')
raise ValueError
```
#### ```Kode 11```
```
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
```

## Rantai Pengecualian
Program dapat memberi nama pengecualian mereka sendiri dengan membuat kelas pengecualian baru (lihat tut-class untuk informasi lebih lanjut tentang kelas Python). Pengecualian biasanya berasal dari kelas Exception, baik secara langsung atau tidak langsung.
#### ```Kode 12```
```
# exc harus berupa instance pengecualian atau Tidak Ada.
raise RuntimeError from exc
```
#### ```Kode 13```
```
def func():
    raise ConnectionError
try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
```
#### ```Kode 14```
```
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
```

## Mendefinisikan Tindakan Pembersihan
Pernyataan try memiliki klausa opsional lain yang dimaksudkan untuk menentukan tindakan pembersihan yang harus dijalankan dalam semua keadaan.
#### ```Kode 15```
```
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
KeyboardInterrupt
```
#### ```Kode 16```
```
def bool_return():
    try:
        return True
    finally:
        return False
bool_return()
```
#### ```Kode 17```
```
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(2, 1)
divide(2, 0)
divide("2", "1")
```

## Tindakan Pembersihan yang Sudah Ditentukan
Beberapa objek mendefinisikan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal.
#### ```Kode 18```
```
for line in open("myfile.txt"):
    print(line, end="")
```
#### ```Kode 19```
```
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

## Kesimpulan
Kesalahan sintaksis adalah kesalahan dalam sintaksis urutan karakter atau token yang ditangkap oleh penyusun. Kesalahan sintaksis harus diperbaiki agar program berhasil dikompilasi. 
Kesalahan pengecualian akan terjadi jika kode tersebut benar secara sintaks tetapi ada kesalahan dalam kode itu sendiri.

