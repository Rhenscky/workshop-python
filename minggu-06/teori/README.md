# KESALAHAN DAN PENGECUALIAN


## Kesalahan Sintaksis
#### ```Kode 1```
```
while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

## Pengecualian
#### ```Kode 2```
```
10 * (1/0)
4 + spam*3
'2' + 2
```

## Menangani Pengecualian
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
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
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
#### ```Kode 10```
```
raise NameError('HiThere')
```
#### ```Kode 11```
```
raise ValueError  # shorthand for 'raise ValueError()'
```
#### ```Kode 12```
```
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
```

## Rantai Pengecualian
#### ```Kode 13```
```
# exc must be exception instance or None.
raise RuntimeError from exc
```
#### ```Kode 14```
```
def func():
    raise ConnectionError
try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
```
#### ```Kode 15```
```
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
```

## Mendefinisikan Tindakan Pembersihan
#### ```Kode 16```
```
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
KeyboardInterrupt
```
#### ```Kode 17```
```
def bool_return():
    try:
        return True
    finally:
        return False
bool_return()
```
#### ```Kode 18```
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
#### ```Kode 19```
```
for line in open("myfile.txt"):
    print(line, end="")
```
#### ```Kode 20```
```
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

## Kesimpulan
Fungsi input() untuk memberi jeda atau menghentikan sementara program sampai kita memasukkan data ke dalamnya, ketika data sudah dimasukkan, selanjutnya program akan berjalan kembali dan kemudian memproses data inputan.
Setelah data dimasukkan lalu diproses  menggunakan fungsi print(). fungsi print() juga dapat menginformasikan pada kita versi python yang digunakan suatu program. Jadi jika kalian menemukan program dengan deklarasi print() di dalamnya maka dapat dipastikan program tersebut sudah menggunakan versi python 3 ke atas. Sedangkan jika di dalam program tersebut ditemukan deklarasi print tanpa tanda kurung, maka dapat dipastikan program tersebut menggunakan python versi lama. Python 2.7 ke bawah.


