# Struktur Data
Bab ini menjelaskan beberapa hal yang telah Anda pelajari secara lebih rinci, dan menambahkan beberapa hal baru juga.

## Lebih Lanjut tentang Daftar Lists
Tipe data daftar list memiliki beberapa metode lagi.
### Code 1 
```
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

fruits.count('tangerine')

fruits.index('banana')

fruits.index('banana', 4)  # Find next banana starting a position 4

fruits.reverse()
fruits

fruits.append('grape')
fruits

fruits.sort()
fruits

fruits.pop()
```
Anda mungkin telah memperhatikan bahwa metode seperti insert, remove atau sort yang hanya mengubah daftar list tidak memiliki nilai pengembalian yang dicetak -- mereka mengembalikan standar None. 1 Ini adalah prinsip desain untuk semua struktur data yang bisa berubah mutable dalam Python.

## Menggunakan Daftar Lists sebagai Tumpukan Stacks
Metode daftar membuatnya sangat mudah untuk menggunakan daftar lust sebagai tumpukan stack, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("last-in, first-out"). Untuk menambahkan item ke atas tumpukan, gunakan append(). Untuk mengambil item dari atas tumpukan, gunakan pop() tanpa indeks eksplisit. Sebagai contoh:
### Code 2
```
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack

stack.pop()

stack

stack.pop()

stack.pop()

stack
```
## Menggunakan Daftar Lists sebagai Antrian Queues
Dimungkinkan juga untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("first-in, first-out"); namun, daftar tidak efisien untuk tujuan ini. Sementara menambahkan dan muncul dari akhir daftar cepat, melakukan memasukkan atau muncul dari awal daftar lambat (karena semua elemen lain harus digeser satu).
Untuk mengimplementasikan antrian, gunakan collections.deque yang dirancang untuk menambahkan dan muncul dengan cepat dari kedua ujungnya. Sebagai contoh:
### Code 3 
```
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

queue                           # Remaining queue in order of arrival
```
## Daftar List Comprehensions
Pemahaman daftar list comprehensions menyediakan cara singkat untuk membuat daftar. Aplikasi umum adalah membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan pada setiap anggota dari urutan lain atau iterable, atau untuk membuat urutan elemen-elemen yang memenuhi kondisi tertentu.
Misalnya, anggap kita ingin membuat daftar kotak, seperti:
### Code 4 
```
squares = []
for x in range(10):
    squares.append(x**2)

squares
```
Perhatikan bahwa ini membuat (atau menimpa) variabel bernama x yang masih ada setelah loop selesai. Kami dapat menghitung daftar kotak tanpa efek samping menggunakan:
```
squares = list(map(lambda x: x**2, range(10)))
```
atau, dengan kata lain:
```
squares = [x**2 for x in range(10)]
```
yang lebih ringkas dan mudah dibaca.
Pemahaman daftar list comprehension terdiri dari tanda kurung yang berisi ekspresi diikuti oleh klausa for, lalu nol atau lebih klausa for atau if. Hasilnya akan menjadi daftar baru yang dihasilkan dari mengevaluasi ekspresi dalam konteks dari klausa for dan if yang mengikutinya. Sebagai contoh, listcomp ini menggabungkan elemen dari dua daftar jika tidak sama:
```
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```
dan itu setara dengan:
```
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs
```
Perhatikan bagaimana urutan pernyataan for dan if adalah sama di kedua cuplikan ini.
Jika ekspresi adalah tuple (mis. (x, y) dalam contoh sebelumnya), ekspresi tersebut harus diberi kurung.
```
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]

# apply a function to all the elements
[abs(x) for x in vec]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]

# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]




# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
```
Pemahaman daftar list comprehensions dapat berisi ekspresi kompleks dan fungsi bersarang:
```
from math import pi
[str(round(pi, i)) for i in range(1, 6)]
```
## Pemahaman Daftar List Comprehensions Bersarang
Ekspresi awal dalam pemahaman daftar list comprehension dapat berupa ekspresi acak arbitrary, termasuk pemahaman daftar list comprehension lainnya.
Perhatikan contoh matriks 3x4 berikut yang diimplementasikan sebagai daftar list 3 dari daftar list panjang 4
```
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
```
Pemahaman daftar list comprehension berikut akan mengubah baris dan kolom:
```
[[row[i] for row in matrix] for i in range(4)]
```
As we saw in the previous section, the inner list comprehension is evaluated in the context of the for that follows it, so this example is equivalent to:
```
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed
```
yang, pada gilirannya, sama dengan:
```
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed
```
Di dunia nyata, Anda harus memilih fungsi bawaan untuk pernyataan aliran flow yang kompleks. Fungsi zip() akan melakukan pekerjaan yang baik untuk kasus penggunaan ini:
```
list(zip(*matrix))
```
## Pernyataan del
Ada cara untuk menghapus item dari daftar yang diberikan indeksnya, bukan nilainya: pernyataan del. Ini berbeda dari metode pop() yang mengembalikan nilai. Pernyataan del juga dapat digunakan untuk menghapus irisan dari daftar list atau menghapus seluruh daftar list (yang kami lakukan sebelumnya dengan menetapkan daftar kosong pada slice). Sebagai contoh:
### Code 5 
```
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a

del a[2:4]
a

del a[:]
a
```
del juga dapat digunakan untuk menghapus seluruh variabel:
```
del a
```
Merujuk nama a selanjutnya adalah kesalahan (setidaknya sampai nilai lain ditetapkan untuknya). Kita akan menemukan kegunaan lain untuk del nanti.

## uples and Urutan Sequences
Kita melihat bahwa daftar list dan string memiliki banyak properti yang sama, seperti operasi pengindeksan dan pemotongan. Mereka adalah dua contoh tipe data sequence (lihat Sequence Types --- list, tuple, range). Karena Python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lain: tuple.
Sebuah tuple terdiri dari sejumlah nilai yang dipisahkan oleh koma, misalnya:
### Code 6 
```
t = 12345, 54321, 'hello!'
t[0]

t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
t[0] = 88888


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
```
Masalah khusus adalah pembangunan tuple yang mengandung 0 atau 1 item: sintaksis memiliki beberapa kebiasaan quirks tambahan untuk mengakomodasi ini. Tuple kosong dibangun oleh sepasang kurung kosong; tupel dengan satu item dikonstruksi dengan mengikuti nilai dengan koma (tidak cukup untuk menyertakan nilai tunggal dalam tanda kurung). Jelek, tapi efektif. Sebagai contoh:
```
empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)

len(singleton)

singleton
```
Pernyataan t = 12345, 54321, 'hello!' Adalah contoh dari tuple packing: nilainya 12345, 54321 dan 'hello!' Dikemas bersama-sama dalam tuple. Operasi terbalik juga dimungkinkan
```
x, y, z = t
```
## Himpunan Set
Python juga menyertakan tipe data untuk sets. Himpunan atau Set adalah koleksi yang tidak terurut tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Atur objek juga mendukung operasi matematika seperti penyatuan union, persimpangan intersection, perbedaan difference, dan perbedaan simetris.
Kurung kurawal atau fungsi set() dapat digunakan untuk membuat himpunan. Catatan: untuk membuat himpunan kosong Anda harus menggunakan set(), bukan {}; yang terakhir itu membuat kamus dictionary kosong, struktur data yang kita bahas di bagian selanjutnya.

Berikut ini adalah demonstrasi singkat:
```
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

'orange' in basket                 # fast membership testing

'crabgrass' in basket


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a

a - b                              # letters in a but not in b

a | b                              # letters in a or b or both

a & b                              # letters in both a and b

a ^ b                              # letters in a or b but not both
```
Seperti halnya untuk list comprehensions, set comprehensions juga didukung:
```
a = {x for x in 'abracadabra' if x not in 'abc'}
a
```
## Kamus Dictionaries
Tipe data lain yang berguna yang dibangun ke dalam Python adalah dictionary (lihat Mapping Types --- dict). Kamus dictionary kadang-kadang ditemukan dalam bahasa lain sebagai "assosiative memories" atau "assosiative array". Tidak seperti urutan sequences, yang diindeks oleh sejumlah angka, kamus dictionary diindeks oleh keys, yang dapat berupa jenis apa pun yang tidak dapat diubah immutable type; string dan angka selalu bisa menjadi kunci key. Tuples dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tuple; jika sebuah tuple berisi objek yang bisa berubah baik secara langsung atau tidak langsung, itu tidak dapat digunakan sebagai kunci key. Anda tidak dapat menggunakan daftar list sebagai kunci, karena daftar dapat dimodifikasi di tempat menggunakan penugasan indeks, penugasan slice, atau metode seperti append() dan extend().

Melakukan list(d) pada kamus mengembalikan daftar list semua kunci yang digunakan dalam kamus, dalam urutan penyisipan (jika Anda ingin diurutkan, cukup gunakan sorted(d) sebagai gantinya). Untuk memeriksa apakah ada satu kunci dalam kamus, gunakan kaca kunci in.

Ini adalah contoh kecil menggunakan kamus dictionary:
### Code 7 
```
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'jack' not in tel
```
Pembangun constructor dict() membangun kamus langsung dari urutan pasangan kunci-nilai:
```
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
```
Selain itu, pemahaman kamus dict comprehensions dapat digunakan untuk membuat kamus dictionary dari ekspresi kunci dan nilai acak arbitrary:
```
{x: x**2 for x in (2, 4, 6)}
```
Ketika kunci adalah string sederhana, kadang-kadang lebih mudah untuk menentukan pasangan menggunakan argumen kata kunci keyword arguments:
```
dict(sape=4139, guido=4127, jack=4098)
```
## Teknik Perulangan
Saat mengulang kamus dictionaries, kunci key dan nilai value terkait dapat diambil pada saat yang sama menggunakan metode items().
### Code 8
```
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
```
Saat mengulang melalui urutan, indeks posisi dan nilai terkait dapat diambil pada saat yang sama menggunakan fungsi enumerate().
```
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
```
Untuk mengulang dua urutan atau lebih secara bersamaan, entri dapat dipasangkan dengan fungsi zip().
```
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
```
Untuk mengulang urutan secara terbalik, pertama tentukan urutan dalam arah maju dan kemudian panggil fungsi reversed().
```
for i in reversed(range(1, 10, 2)):
    print(i)
```
Untuk mengulangi sebuah urutan sequence dalam susunan yang diurutkan, gunakan fungsi sort() yang mengembalikan daftar terurut baru dengan membiarkan sumber tidak diubah.
```
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
```
Menggunakan set() pada sebuah urutan dapat menghilangkan elemen-elemen yang duplikat. Penggunaan sorted() yang dikombinasikan dengan set() terhadap sebuah urutan merupakan cara idiomatik untuk loop dari elemen-elemen unik dari urutan yang diurutkan.
```
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
```
Terkadang tergoda untuk mengubah daftar list saat Anda mengulanginya; namun, seringkali lebih mudah dan aman untuk membuat daftar list baru.
```
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data
```
## Lebih lanjut tentang Kondisi
Kondisi yang digunakan dalam pernyataan while dan if dapat berisi operator apa pun, bukan hanya perbandingan.
Perbandingan dapat digabungkan menggunakan operator Boolean and dan or, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan not. Ini memiliki prioritas lebih rendah daripada operator pembanding; di antara mereka, not memiliki prioritas tertinggi dan or terendah, sehingga A and not B or C setara dengan (A and (not B)) or C . Seperti biasa, tanda kurung dapat digunakan untuk mengekspresikan komposisi yang diinginkan.

Operator Boolean and dan or disebut operator short-circuit: argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika A dan C bernilai benar tetapi B salah, A and B and C tidak mengevaluasi ekspresi C. Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai kembalian dari operator hubung singkat short-circuit adalah argumen terakhir yang dievaluasi.
Dimungkinkan untuk menetapkan hasil perbandingan atau ekspresi Boolean lainnya ke variabel. Sebagai contoh,
### Code 9
```
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null
```
## Membandingkan Urutan Sequences dan Jenis Lainnya
Objek urutan sequence biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingan menggunakan pengurutan lexicographical: pertama dua item pertama dibandingkan, dan jika mereka berbeda ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai urutan mana pun habis. Jika dua item yang akan dibandingkan adalah urutannya sendiri dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif. Jika semua item dari dua urutan membandingkan hasilnya sama, urutannya dianggap sama. Jika satu urutan adalah sub-urutan awal dari yang lain, urutan yang lebih pendek adalah yang lebih kecil (lebih pendek). Pengurutan leksikografis untuk string menggunakan nomor titik kode Unicode untuk mengurutkan masing-masing karakter. Beberapa contoh perbandingan antara urutan dengan tipe yang sama:
### Code 10
```
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```
Perhatikan bahwa membandingkan objek dari berbagai jenis dengan < atau > adalah sah asalkan objek memiliki metode perbandingan yang sesuai. Misalnya, tipe numerik campuran dibandingkan menurut nilai numeriknya, sehingga 0 sama dengan 0.0, dll. Jika tidak, alih-alih memberikan penyusunan acak, interpreter akan memunculkan pengecualian TypeError.
