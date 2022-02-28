# Struktur Data
Struktur Data adalah struktur yang dapat menyimpan dan mengorganisasikan kumpulan data. Berikut struktur data yang ada dalam Python.

Struktur data berbicara mengenai suatu cara untuk menyimpan, menyusun, mengelompokkan dan merepresentasikan suatu data. Struktur data merupakan hal yang sangat penting dan wajib dikuasai oleh seorang programmer. Di forum-forum pemrograman, saya sering menjumpai pertanyaan-pertanyaan yang menurut saya bisa diselesaikan jika orang tersebut paham mengenai konsep struktur data. Dalam Python terdapat empat struktur data built-in yaitu List, Tuple, Dictionary, dan Set. Sebenarnya masih ada lagi, tapi menurut saya 4 struktur data tersebut yang paling penting dan sering digunakan.

#### 1. List
List merupakan struktur data terurut (sequence). Setiap item dalam List memiliki sebuah index yang dimulai dari 0. List direpresentasikan dengan karakter square brackets []. Mungkin terlihat mirip dengan Array pada bahasa pemrograman lain seperti Java, tapi List dalam Python bisa menampung berbagai tipe data.

#### 2. Tuple
Tuple sebenarnya sama dengan List, perbedaannya adalah Tuple memiliki sifat immutable yang artinya tidak bisa dirubah bahkan dihapus. Sebuah Tuple direpresentasikan dengan karakter parentheses ().

#### 3. Dictionary
Dictionary merupakan struktur data yang berupa pasangan key-value. Setiap informasi yang disimpan pada Dictionary di petakan dengan satu key untuk mengakses informasi tersebut. Bahkan sebuah Dictionary bisa berisi Dictionary lain.

#### 4. Set
Set merupakan struktur data yang memiliki kelebihan yaitu bersifat unique, jadi ketika kita memasukkan data yang sama pada Set, maka salah satu data itu akan di replace. Namun yang perlu diperhatikan bahwa struktur data Set juga bersifat unordered atau tidak berurut. Selain itu Set juga bersifat unindexed atau tidak memiliki index, sehingga kita tidak bisa mengakses salah satu data dari Set berdasarkan index tertentu.

## Daftar Structur Data pada Python

Berikut adalah semua metode objek yang digunakan pada daftar Python :

1. List.append( x )

   Tambahkan item ke akhir daftar. Setara dengan .a[len(a):] = [x]
   
2. List.extend( dapat diubah )
   
   Perluas daftar dengan menambahkan semua item dari iterable. Setara dengan .a[len(a):] = iterable

3. List.insert( saya , x )
   
   Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen yang akan disisipkan        sebelumnya, jadi disisipkan di bagian depan daftar, dan sama dengan .a.insert(0, x)a.insert
   (len(a), x)a.append(x)

4. List.remove( x )
   
   Hapus item pertama dari daftar yang nilainya sama dengan x . Ini menimbulkan ValueErrorjika tidak    ada item seperti itu.

5. List.pop( [ saya ] )
   
   Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang        ditentukan, a.pop()hapus dan kembalikan item terakhir dalam daftar. 
   (Kurung siku di sekitar i dalam tanda tangan metode menunjukkan bahwa parameternya opsional, bukan    berarti Anda harus mengetikkan tanda kurung siku pada posisi itu. Anda akan sering melihat notasi    ini di Referensi Pustaka Python.)

6. List.clear( )
   
   Hapus semua item dari daftar. Setara dengan .del a[:]

7. List.index( x [ , mulai [ , akhir ] ] )

   Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x . Menaikkan a    ValueErrorjika tidak ada item seperti itu. Argumen opsional mulai dan akhir ditafsirkan seperti      dalam notasi irisan dan digunakan untuk membatasi pencarian ke urutan daftar tertentu. Indeks yang    dikembalikan dihitung relatif terhadap awal urutan penuh daripada argumen awal.

8. List.count( x )

   Kembalikan berapa kali x muncul dalam daftar.

9. List.sort( * , kunci = Tidak ada , terbalik = Salah )

   Urutkan item dari daftar di tempat (argumen dapat digunakan untuk penyesuaian pengurutan, lihat      sorted()penjelasannya).

10.List.reverse( )

   Balikkan elemen daftar di tempatnya.

11.List.copy( )
   
   Kembalikan salinan daftar yang dangkal. Setara dengan a[:].


#### Contoh yang menggunakan sebagian besar metode daftar :

```
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```
Anda mungkin telah memperhatikan bahwa metode seperti insert, removeatau sortyang hanya mengubah daftar tidak memiliki nilai kembalian yang dicetak – metode tersebut mengembalikan default None. 1 Ini adalah prinsip desain untuk semua struktur data yang dapat diubah dengan Python.

### 1.1 Menggunakan Daftar sebagai 
Metode daftar membuatnya sangat mudah untuk menggunakan daftar sebagai tumpukan, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("masuk terakhir, keluar pertama"). Untuk menambahkan item ke bagian atas tumpukan, gunakan append(). Untuk mengambil item dari atas tumpukan, gunakan pop()tanpa indeks eksplisit. Sebagai contoh:

```
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

### 1.2 Menggunakan Daftar sebagai 
Dimungkinkan juga untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("masuk pertama, keluar pertama"); namun, daftar tidak efisien untuk tujuan ini. Sementara menambahkan dan muncul dari akhir daftar cepat, melakukan penyisipan atau muncul dari awal daftar lambat (karena semua elemen lain harus digeser satu).

Untuk mengimplementasikan antrian, gunakan collections.dequeyang dirancang untuk menambahkan dan muncul dengan cepat dari kedua ujungnya. Sebagai contoh:

```
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

### 1.3 Pemahaman
Pemahaman daftar menyediakan cara ringkas untuk membuat daftar. Aplikasi umum adalah untuk membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota dari urutan lain atau iterable, atau untuk membuat suburutan dari elemen-elemen yang memenuhi kondisi tertentu.

Misalnya, anggap kita ingin membuat daftar kotak, seperti:

```
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Perhatikan bahwa ini membuat (atau menimpa) variabel bernama xyang masih ada setelah loop selesai. Kami dapat menghitung daftar kotak tanpa efek samping menggunakan:

```
squares = list(map(lambda x: x**2, range(10)))
```
atau, ekuivalen:
```
squares = [x**2 for x in range(10)]
```
yang lebih ringkas dan mudah dibaca.

Pemahaman daftar terdiri dari tanda kurung yang berisi ekspresi diikuti oleh forklausa, lalu nol atau lebih foratau if klausa. Hasilnya adalah daftar baru yang dihasilkan dari evaluasi ekspresi dalam konteks fordan ifklausa yang mengikutinya. Misalnya, listcomp ini menggabungkan elemen dari dua daftar jika tidak sama :

```
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
dan itu setara dengan:
```
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
Perhatikan bagaimana urutan pernyataan forand ifsama di kedua cuplikan ini.
Jika ekspresi adalah tuple (misalnya dalam contoh sebelumnya), itu harus dikurung.(x, y)
```
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Pemahaman daftar dapat berisi ekspresi kompleks dan fungsi bersarang:
```
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```
### 1.4 Pemahaman Daftar 
Ekspresi awal dalam pemahaman daftar dapat berupa ekspresi arbitrer, termasuk pemahaman daftar lainnya.
Perhatikan contoh berikut dari matriks 3x4 yang diimplementasikan sebagai daftar 3 daftar panjang 4:
```
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```
Pemahaman daftar berikut akan mengubah baris dan kolom:
```
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
Seperti yang kita lihat di bagian sebelumnya, listcomp bersarang dievaluasi dalam konteks foryang mengikutinya, jadi contoh ini setara dengan:
```
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
yang, pada gilirannya, sama dengan:
```
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
Di dunia nyata, Anda harus lebih memilih fungsi bawaan daripada pernyataan aliran yang kompleks. Fungsi zip()ini akan melakukan pekerjaan yang baik untuk kasus penggunaan ini:
```
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```
Lihat Membongkar Daftar Argumen untuk detail tentang tanda bintang di baris ini.

### 2. Pernyataan del_ 
Ada cara untuk menghapus item dari daftar yang diberikan indeksnya alih-alih nilainya: delpernyataan. Ini berbeda dari pop()metode yang mengembalikan nilai. Pernyataan deljuga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar (yang kita lakukan sebelumnya dengan menetapkan daftar kosong ke irisan). Sebagai contoh:
```
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```
deljuga dapat digunakan untuk menghapus seluruh variabel:
```
>>> del a
```
Merujuk nama aselanjutnya adalah kesalahan (setidaknya sampai nilai lain diberikan padanya). Kami akan menemukan kegunaan lain untuk delnanti.

### 3. Dan Urutan
Kami melihat bahwa daftar dan string memiliki banyak properti umum, seperti operasi pengindeksan dan pengirisan. Mereka adalah dua contoh tipe data urutan (lihat Jenis Urutan — daftar, tupel, rentang ). Karena Python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lainnya: tuple .
Tuple terdiri dari sejumlah nilai yang dipisahkan dengan koma, misalnya:
```
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```
Seperti yang Anda lihat, pada tupel keluaran selalu diapit tanda kurung, sehingga tupel bersarang diinterpretasikan dengan benar; mereka mungkin dimasukkan dengan atau tanpa tanda kurung di sekitarnya, meskipun seringkali tanda kurung diperlukan (jika tupel adalah bagian dari ekspresi yang lebih besar). Hal ini tidak mungkin untuk menetapkan ke item individu dari tupel, namun dimungkinkan untuk membuat tupel yang berisi objek yang bisa berubah, seperti daftar.

Masalah khusus adalah konstruksi tupel yang berisi 0 atau 1 item: sintaks memiliki beberapa kebiasaan tambahan untuk mengakomodasi ini. Tupel kosong dibangun oleh sepasang tanda kurung kosong; tuple dengan satu item dibangun dengan mengikuti nilai dengan koma (tidak cukup untuk menyertakan satu nilai dalam tanda kurung). Jelek, tapi efektif. Sebagai contoh:
```
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```
Pernyataan tersebut adalah contoh pengepakan tuple : nilai , dan dikemas bersama dalam sebuah tupel. Operasi sebaliknya juga dimungkinkan:t = 12345, 54321, 'hello!'1234554321'hello!'
```
>>> x, y, z = t
```
Ini disebut, cukup tepat, pembongkaran urutan dan berfungsi untuk urutan apa pun di sisi kanan. Pembukaan urutan mensyaratkan bahwa ada banyak variabel di sisi kiri tanda sama dengan jumlah elemen dalam urutan. Perhatikan bahwa beberapa penugasan sebenarnya hanyalah kombinasi dari pengemasan Tuple dan pembongkaran urutan.

### 4. Set 
Python juga menyertakan tipe data untuk set . Himpunan adalah kumpulan yang tidak berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Set objek juga mendukung operasi matematika seperti serikat pekerja, persimpangan, perbedaan, dan perbedaan simetris.

Kurung kurawal atau set()fungsi dapat digunakan untuk membuat himpunan. Catatan: untuk membuat set kosong Anda harus menggunakan set(), bukan {}; yang terakhir membuat kamus kosong, struktur data yang akan kita bahas di bagian selanjutnya.
Berikut adalah demonstrasi singkat:
```
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```
Sama halnya dengan daftar pemahaman , pemahaman set juga didukung:
```
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```
### 5. Kamus 
Tipe data lain yang berguna yang dibangun ke dalam Python adalah kamus (lihat Jenis Pemetaan — dict ). Kamus kadang-kadang ditemukan dalam bahasa lain sebagai "ingatan asosiatif" atau "array asosiatif". Tidak seperti urutan, yang diindeks oleh rentang angka, kamus diindeks oleh kunci , yang dapat berupa tipe apa pun yang tidak dapat diubah; string dan angka selalu bisa menjadi kunci. Tuple dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tupel; jika sebuah tuple berisi objek yang bisa berubah baik secara langsung maupun tidak langsung, itu tidak dapat digunakan sebagai kunci. Anda tidak dapat menggunakan daftar sebagai kunci, karena daftar dapat dimodifikasi di tempat menggunakan penetapan indeks, penetapan irisan, atau metode seperti append()dan extend().

Melakukan list(d)di kamus mengembalikan daftar semua kunci yang digunakan dalam kamus, dalam urutan penyisipan (jika Anda ingin diurutkan, gunakan sorted(d)saja). Untuk memeriksa apakah satu kunci ada dalam kamus, gunakan inkata kunci.
Berikut adalah contoh kecil menggunakan kamus:
```
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```
Konstruktor dict()membangun kamus langsung dari urutan pasangan nilai kunci:
```
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```
Selain itu, pemahaman dict dapat digunakan untuk membuat kamus dari kunci arbitrer dan ekspresi nilai:
```
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```
Jika kuncinya adalah string sederhana, terkadang lebih mudah untuk menentukan pasangan menggunakan argumen kata kunci:
```
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```
### 6. Teknik 
Saat mengulang melalui kamus, kunci dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan items()metode ini.
```
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```
Saat mengulang melalui urutan, indeks posisi dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan enumerate()fungsi.
```
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```
Untuk mengulang dua atau lebih urutan pada saat yang sama, entri dapat dipasangkan dengan zip()fungsi.
```
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```
Untuk mengulang urutan secara terbalik, pertama tentukan urutan dalam arah maju dan kemudian panggil reversed()fungsinya.
```
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```
Untuk mengulang urutan dalam urutan terurut, gunakan sorted()fungsi yang mengembalikan daftar terurut baru sambil membiarkan sumbernya tidak berubah.
```
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```
Menggunakan set()pada urutan menghilangkan elemen duplikat. Penggunaan sorted()kombinasi dengan set()lebih dari urutan adalah cara idiomatik untuk mengulang elemen unik dari urutan dalam urutan yang diurutkan.
```
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```
Terkadang tergoda untuk mengubah daftar saat Anda mengulangnya; namun, seringkali lebih sederhana dan lebih aman untuk membuat daftar baru.
```
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```
### 7. Ketentuan
Kondisi yang digunakan dalam whiledan ifpernyataan dapat berisi operator apa pun, bukan hanya perbandingan. Operator perbandingan indan merupakan tes keanggotaan yang menentukan apakah suatu nilai ada di (atau tidak) dalam wadah. Operator dan membandingkan apakah dua objek benar-benar objek yang sama. Semua operator pembanding memiliki prioritas yang sama, yaitu lebih rendah dari semua operator numerik.not inisis not 
Perbandingan dapat dirantai. Misalnya, menguji apakah kurang dari dan apalagi sama dengan .a < b == cabbc

Perbandingan dapat digabungkan menggunakan operator Boolean anddan or, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan not. Ini memiliki prioritas lebih rendah daripada operator pembanding; antara mereka, notmemiliki prioritas tertinggi dan orterendah, sehingga setara dengan . Seperti biasa, tanda kurung dapat digunakan untuk menyatakan komposisi yang diinginkan.A and not B or C(A and (not B)) or C
Operator Boolean and dan or yang disebut operator hubung singkat : argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika Adan Cbenar tetapi Bsalah, tidak mengevaluasi ekspresi . Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai kembalian dari operator hubung singkat adalah argumen terakhir yang dievaluasi.A and B and CC
Dimungkinkan untuk menetapkan hasil perbandingan atau ekspresi Boolean lainnya ke variabel. Sebagai contoh,
```
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```
Perhatikan bahwa dalam Python, tidak seperti C, penugasan di dalam ekspresi harus dilakukan secara eksplisit dengan operator walrus := . Ini menghindari kelas umum dari masalah yang dihadapi dalam program C: mengetik = ekspresi ketika ==dimaksudkan.

### 8. Membandingkan Urutan dan Jenis 
Objek urutan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingannya menggunakan leksikografispemesanan: pertama dua item pertama dibandingkan, dan jika berbeda, ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu urutan habis. Jika dua item yang akan dibandingkan itu sendiri merupakan urutan dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif. Jika semua item dari dua urutan membandingkan sama, urutan dianggap sama. Jika satu barisan merupakan sub-urutan awal dari yang lain, barisan yang lebih pendek adalah yang lebih kecil (lebih kecil). Urutan leksikografis untuk string menggunakan nomor titik kode Unicode untuk mengurutkan karakter individual. Beberapa contoh perbandingan antara urutan dari jenis yang sama:
```
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```
Perhatikan bahwa membandingkan objek dari jenis yang berbeda dengan <atau >legal asalkan objek tersebut memiliki metode perbandingan yang sesuai. Misalnya, tipe numerik campuran dibandingkan menurut nilai numeriknya, jadi 0 sama dengan 0,0, dll. Jika tidak, alih-alih memberikan pengurutan arbitrer, penerjemah akan memunculkan TypeErrorpengecualian.
