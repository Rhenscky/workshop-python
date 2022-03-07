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
```
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Bahkan ada varian untuk mengimpor semua nama yang didefinisikan oleh modul:

```
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Ini mengimpor semua nama kecuali yang dimulai dengan garis bawah ```(_)```. Dalam kebanyakan kasus, pemrogram Python tidak menggunakan fasilitas ini karena fasilitas ini memperkenalkan serangkaian nama yang tidak diketahui ke dalam juru bahasa, mungkin menyembunyikan beberapa hal yang telah Anda tetapkan.
Perhatikan bahwa secara umum praktik mengimpor ```*``` dari modul atau paket tidak disukai, karena sering menyebabkan kode yang tidak dapat dibaca dengan baik. Namun, tidak apa-apa menggunakannya untuk menyimpan pengetikan dalam sesi interaktif.

Jika nama modul diikuti oleh as, maka nama berikut asterikat langsung ke modul yang diimpor.
```
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
Ini secara efektif mengimpor modul dengan cara yang sama seperti yang akan dilakukan, dengan satu-satunya perbedaan tersedia sebagai ```.import fibofib```.

Ini juga dapat digunakan saat menggunakan fromdengan efek serupa:
```
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
