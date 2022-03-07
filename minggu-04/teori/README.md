# Pertemuan 4
## Moduls
Module pada Python adalah sebuah file yang berisikan sekumpulan kode fungsi, class dan variabel yang disimpan dalam satu file berekstensi .py dan dapat dieksekusi oleh interpreter Python. Nama dari module .py merupakan nama nama dari file itu sendiri. Misalkan kita memiliki file bernama "dqlab.py", maka kita telah membuat sebuah module bernama "dqlab. Dan module sendiri bisa memiliki berbagai macam isi, baik itu fungsi, class, maupun variabel.

Saat program Anda semakin panjang, Anda mungkin ingin membaginya menjadi beberapa file untuk perawatan yang lebih mudah. Anda mungkin juga ingin menggunakan fungsi praktis yang telah Anda tulis di beberapa program tanpa menyalin definisinya ke dalam setiap program. Untuk mendukung ini, Python memiliki cara untuk menempatkan definisi dalam file dan menggunakannya dalam skrip atau dalam instance interpreter yang interaktif. 

File seperti itu disebut modul; definisi dari sebuah modul dapat diimpor ke modul lain atau ke modul utama (kumpulan variabel yang dapat Anda akses dalam skrip yang dijalankan di tingkat atas dan dalam mode kalkulator). Modul adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran ```.py``` ditambahkan. Di dalam sebuah modul, nama modul (sebagai string) tersedia sebagai nilai dari variabel global ```__name__```. 

### Membuat file yang dipanggil ```fibo.py``` di direktori dengan konten pada kode dibawah :
#### ```Kode 1```
```
#Fibonacci numbers module
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

Sekarang masukkan interpreter Python dan impor modul ini dengan perintah berikut:

#### ```Kode 1.0```
```
>>> import fibo
```

Ini tidak memasukkan nama fungsi yang didefinisikan fibo secara langsung di tabel simbol saat ini; itu hanya memasukkan nama modul di fibosana. Menggunakan nama modul Anda dapat mengakses fungsi :
#### ```Kode 1.1```
```
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

Jika Anda ingin sering menggunakan suatu fungsi, Anda dapat menetapkannya ke nama lokal:
#### ```Kode 1.2```
```
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

## More on Modules
Setiap modul memiliki tabel simbol pribadinya sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. Dengan demikian, pembuat modul dapat menggunakan variabel global dalam modul tanpa mengkhawatirkan bentrokan yang tidak disengaja dengan variabel global pengguna. Di sisi lain, jika Anda tahu apa yang Anda lakukan, Anda dapat menyentuh variabel global modul dengan notasi yang sama yang digunakan untuk merujuk ke fungsinya, ```modname.itemname```.

Modul dapat mengimpor modul lain. Merupakan kebiasaan tetapi tidak diharuskan untuk menempatkan semua importpernyataan di awal modul (atau skrip, dalam hal ini). Nama modul yang diimpor ditempatkan di tabel simbol global modul pengimpor.

### Mengimpor nama dari modul langsung ke tabel simbol modul pengimpor :
#### ```Kode 2```
```
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Bahkan ada varian untuk mengimpor semua nama yang didefinisikan oleh modul:
#### ```Kode 2.0```
```
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Ini mengimpor semua nama kecuali yang dimulai dengan garis bawah ```(_)```. Dalam kebanyakan kasus, pemrogram Python tidak menggunakan fasilitas ini karena fasilitas ini memperkenalkan serangkaian nama yang tidak diketahui ke dalam juru bahasa, mungkin menyembunyikan beberapa hal yang telah Anda tetapkan.
Perhatikan bahwa secara umum praktik mengimpor ```*``` dari modul atau paket tidak disukai, karena sering menyebabkan kode yang tidak dapat dibaca dengan baik. Namun, tidak apa-apa menggunakannya untuk menyimpan pengetikan dalam sesi interaktif.

Jika nama modul diikuti oleh as, maka nama berikut asterikat langsung ke modul yang diimpor.
#### ```Kode 2.1```
```
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Ini secara efektif mengimpor modul dengan cara yang sama seperti yang akan dilakukan, dengan satu-satunya perbedaan tersedia sebagai ```.import fibofib```.

Ini juga dapat digunakan saat menggunakan fromdengan efek serupa :
#### ```Kode 2.2```
```
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```


## Menjalankan modul sebagai
Saat Anda menjalankan modul Python dengan
#### ```Kode 3```
```
python fibo.py <arguments>
```
kode dalam modul akan dieksekusi, sama seperti jika Anda mengimpornya, tetapi dengan ```__name__ ```set ke ```"__main__"```. Itu berarti dengan menambahkan kode ini di akhir modul Anda:
#### ```Kode 3.0```
```
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
Anda dapat membuat file dapat digunakan sebagai skrip serta modul yang dapat diimpor, karena kode yang mem-parsing baris perintah hanya berjalan jika modul dijalankan sebagai file "utama":
#### ```Kode 3.1```
```
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```
Jika modul diimpor, kode tidak dijalankan:
#### ```Kode 3.2```
```
>>> import fibo
>>>
```
Ini sering digunakan baik untuk menyediakan antarmuka pengguna yang nyaman ke modul, atau untuk tujuan pengujian (menjalankan modul saat skrip mengeksekusi rangkaian pengujian).

## Jalur Pencarian
Ketika sebuah modul bernama spamdiimpor, interpreter pertama mencari modul built-in dengan nama itu. Jika tidak ditemukan, maka akan mencari file bernama ```spam.py``` dalam daftar direktori yang diberikan oleh variabel sys.path. sys.path diinisialisasi dari lokasi ini :

* Direktori yang berisi skrip input (atau direktori saat ini ketika tidak ada file yang ditentukan).
* PYTHONPATH(daftar nama direktori, dengan sintaks yang sama dengan variabel shellPATH).
* Default yang bergantung pada instalasi (berdasarkan konvensi termasuk ```site-packages``` direktori, ditangani oleh sitemodul).

## File Python "Dikompilasi 
Untuk mempercepat pemuatan modul, Python menyimpan versi kompilasi dari setiap modul dalam ```__pycache__``` direktori dengan nama , di mana versi tersebut mengkodekan format file yang dikompilasi; biasanya berisi nomor versi Python. Misalnya, di CPython rilis 3.3 versi kompilasi dari spam.py akan di-cache sebagai . Konvensi penamaan ini memungkinkan modul yang dikompilasi dari rilis yang berbeda dan versi Python yang berbeda untuk hidup berdampingan```.module.version.pyc__pycache__/spam.cpython-33.pyc```
Python memeriksa tanggal modifikasi sumber terhadap versi yang dikompilasi untuk melihat apakah itu kedaluwarsa dan perlu dikompilasi ulang. Ini adalah proses yang sepenuhnya otomatis. Juga, modul yang dikompilasi adalah platform-independen, sehingga perpustakaan yang sama dapat dibagi di antara sistem dengan arsitektur yang berbeda.

#### Beberapa tips untuk para ahli :
Anda dapat menggunakan -O atau -OO mengaktifkan perintah Python untuk mengurangi ukuran modul yang dikompilasi. Sakelar ```-O``` menghapus pernyataan tegas, ```-OO``` sakelar menghapus pernyataan tegas dan string ```__doc__```. Karena beberapa program mungkin bergantung pada ketersediaannya, Anda hanya boleh menggunakan opsi ini jika Anda tahu apa yang Anda lakukan. Modul "Dioptimalkan" memiliki ```opt-``` tag dan biasanya lebih kecil. Rilis mendatang dapat mengubah efek pengoptimalan.

* Sebuah program tidak berjalan lebih cepat saat dibaca dari ```.pyc``` file daripada saat dibaca dari .pyfile; satu-satunya hal yang lebih cepat tentang ```.pyc``` file adalah kecepatan pemuatannya.
* Modul compilealldapat membuat file .pyc untuk semua modul dalam direktori.
* Ada lebih detail tentang proses ini, termasuk diagram alir keputusan, diPP 3147 .

## Standard Modules
Python hadir dengan pustaka modul standar, yang dijelaskan dalam dokumen terpisah, Referensi Pustaka Python (“Referensi Pustaka” selanjutnya). Beberapa modul dibangun ke dalam juru bahasa; ini menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti panggilan sistem. Kumpulan modul tersebut adalah opsi konfigurasi yang juga bergantung pada platform yang mendasarinya. Misalnya, winregmodul hanya disediakan pada sistem Windows. Satu modul tertentu patut mendapat perhatian: sys, yang dibangun ke dalam setiap juru bahasa Python. Variabel ```sys.ps1``` dan ```sys.ps2``` 

### Menentukan string yang digunakan sebagai prompt primer dan sekunder :
#### ```Kode 4```
```
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```
Kedua variabel ini hanya ditentukan jika interpreter dalam mode interaktif.
Variabel ```sys.path``` adalah daftar string yang menentukan jalur pencarian interpreter untuk modul. Ini diinisialisasi ke jalur default yang diambil dari variabel lingkunganPYTHONPATH, atau dari default bawaan jika PYTHONPATHtidak diatur. 
Anda dapat memodifikasinya menggunakan operasi daftar standar:
#### ```Kode 4.0```
```
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

## The dir() Function
The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings:
#### ```Kode 5```
```
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
 ```
Without arguments, dir() lists the names you have defined currently:
#### ```Kode 5.0```
```
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

Note that it lists all types of names: variables, modules, functions, etc.
dir() does not list the names of built-in functions and variables. If you want a list of those, they are defined in the standard module builtins:
#### ```Kode 5.1```
```
>>> import builtins
>>> dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
 ```
