# Kelas-Kelas Pada Python
Kelas atau class pada python bisa kita katakan sebagai sebuah blueprint (cetakan) dari objek (atau instance) yang ingin kita buat.
Kelas adalah cetakannya atau definisinya, sedangkan objek (atau instance) adalah objek nyatanya.

## Contoh Lingkup Scopes dan Ruang Nama Namespaces
contoh yang menunjukkan cara mereferensikan lingkup scopes dan ruang nama namespaces yang berbeda. Bagaimana global dan nonlocal memengaruhi pengikatan variabel :
#### ```Kode 1```
```
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```
Keluaran dari contoh kode adalah:
```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

## Sintaks Definisi Kelas
Definisi kelas paling sederhana
#### ```Kode 2```
```
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```
Ini pada dasarnya adalah pembungkus di sekitar isi namespace yang dibuat oleh definisi kelas; kita akan belajar lebih banyak tentang objek kelas di bagian selanjutnya. Lingkup scope lokal asli (yang berlaku tepat sebelum definisi kelas dimasukkan) diaktifkan kembali, dan objek kelas terikat di sini dengan nama kelas yang diberikan dalam header definisi kelas (ClassName dalam contoh).

## Objek Kelas Class Objects
Kelas pendukung operasi referensi atribut dan inisialisasi.
Nama atribut yang valid adalah semua nama yang ada di namespace kelas saat objek kelas dibuat.
#### ```Kode 3```
```
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```
Instantiation kelas menggunakan notasi fungsi.
#### ```Kode 4```
```
x = MyClass()
```
Membuat instance baru dari kelas dan menetapkan objek ini ke variabel lokal x.
#### ```Kode 5```
```
def __init__(self):
    self.data = []
```
Mendefinisikan metode __init__(), instantiasi kelas secara otomatis memanggil __init__()
#### ```Kode 6```
```
x = MyClass()
```
Argumen yang diberikan kepada operator instantiasi kelas diteruskan ke __init__()
#### ```Kode 7```
```
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i
```
## Objek Instance
Operasi yang dipahami oleh objek instan adalah referensi atribut. atribut memiliki dua jenis yaitu atribut data dan metode.
Kode berikut akan mencetak nilai 16, tanpa meninggalkan jejak.
#### ```Kode 8```
```
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```
## Metode Objek
metode dipanggil tepat setelah terikat.
#### ```Kode 9```
```
x.f()
```
x.f adalah metode objek, dan dapat disimpan dan dipanggil di lain waktu.
#### ```Kode 10```
```
xf = x.f
while True:
    print(xf())
```
## Variabel Kelas dan Instance
Variabel instance adalah untuk data unik untuk setiap instance dan variabel kelas adalah untuk atribut dan metode yang dibagikan oleh semua instance kelas.
#### ```Kode 11```
```
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```
Daftar tricks dalam kode berikut tidak boleh digunakan sebagai variabel kelas karena hanya satu daftar yang akan dibagikan oleh semua Dog instance
#### ```Kode 12```
```
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```
Desain kelas yang benar harus menggunakan variabel instance sebagai gantinya
#### ```Kode 13```
```
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```
## Keterangan Acak
Ketika nama atribut yang sama muncul di kedua instance dan di kelas, maka pencarian atribut memprioritaskan instance.
#### ```Kode 14```
```
class Warehouse:
w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)
```
Kelas tidak dapat digunakan untuk mengimplementasikan tipe data abstrak murni.
Menetapkan objek fungsi ke variabel lokal di kelas sebagai berikut.
#### ```Kode 15```
```
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)
class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g
```
Sekarang f, g dan h adalah semua atribut class C yang merujuk ke objek-objek fungsi, dan akibatnya semuanya adalah metode instance dari C --- h sama persis dengan g.

Metod memanggil metod lain dengan menggunakan atribut metode dari argumen self
#### ```Kode 16```
```
class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

## Pewarisan
Fitur bahasa tidak akan layak untuk nama "class" tanpa mendukung pewarisan, berikut
sintaks untuk definisi kelas turunan.
#### ```Kode 17```
```
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
Nama BaseClassName harus didefinisikan dalam lingkup yang berisi definisi kelas turunan.

#### ```Kode 18```
```
class DerivedClassName(modname.BaseClassName):
```
Python memiliki dua fungsi bawaan yang bekerja dengan warisan:

* Gunakan isinstance() untuk memeriksa jenis instance: isinstance(obj, int) akan menjadi True hanya jika obj.__class__ adalah int atau beberapa kelas yang diturunkan dari int.

* Gunakan issubclass() untuk memeriksa warisan kelas: issubclass(bool, int)``adalah ``True karena bool adalah subkelas dari int. Namun, issubclass(float, int) adalah False karena float bukan subkelas dari int.

## Pewarisan Berganda
Bentuk pewarisan berganda dengan beberapa kelas dasar.
#### ```Kode 19```
```
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```
## Variabel Privat
Variabel "Private" yang tidak dapat diakses kecuali dari dalam suatu objek tidak ada dalam Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: nama diawali dengan garis bawah (mis. _spam) harus diperlakukan sebagai bagian non-publik dari API (apakah itu fungsi, metode atau anggota data).
Name mangling sangat membantu untuk membiarkan subclass menimpa metode tanpa memutus panggilan metode intraclass.
#### ```Kode 20```
```
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```
Contoh di atas akan berfungsi bahkan jika MappingSubclass akan memperkenalkan sebuah pengidentifikasi update karena diganti dengan Mapping update di kelas Mapping dan MappingSubclass update di kelas MappingSubclass masing-masing.

## Barang Sisa Odds and Ends
Tipe data yang mirip dengan "record" Pascal atau "struct" C, menyatukan beberapa item data bernama.
#### ```Kode 21```
```
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```
Objek metode instance memiliki atribut, juga: m.__self__ adalah objek instan dengan metode m(), dan m.__func__ adalah objek fungsi yang sesuai dengan metode tersebut.
## Iterators
Sebagian besar objek penampung container dapat dibuat perulangan menggunakan pernyataan for
#### ```Kode 22```
```
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```
Pernyataan for memanggil iter() pada objek penampung container. Fungsi mengembalikan objek iterator yang mendefinisikan metode __next__() yang mengakses elemen dalam penampung container satu per satu. Ketika tidak ada lagi elemen, __next__() memunculkan pengecualian StopIteration yang memberi tahu perulangan for untuk mengakhiri. 
Memanggil metode __next__() menggunakan next() fungsi bawaan :
#### ```Kode 23```
```
s = 'abc'
it = iter(s)
it
next(it)
next(it)
next(it)
next(it)
```
Definisikan metode __iter__() yang mengembalikan objek dengan metode __next__(). Jika kelas mendefinisikan __next__(), maka __iter__() bisa langsung mengembalikan self
#### ```Kode 24```
```
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```
#### ```Kode 25```
```
rev = Reverse('spam')
iter(rev)

for char in rev:
    print(char)
```
## Pembangkit Generator
Generators adalah sebuah tool yang sederhana dan simpel untuk membuat sebuah iterasi. Itu ditulis seperti fungsi biasa tapi menggunakan pernyataan yield setiap kali ingin mengembalikan sebuah data. 
#### ```Kode 26```
```
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```
#### ```Kode 27```
```
for char in reverse('golf'):
    print(char)
```
Apa pun yang dapat dilakukan dengan pembangkit generator juga dapat dilakukan dengan iterator berbasis kelas seperti yang dijelaskan pada bagian sebelumnya. Apa yang membuat pembangkit generator sangat kompak adalah bahwa metode __iter__() dan __next__() dibuat secara otomatis.
Fitur utama lainnya adalah variabel lokal dan status eksekusi secara otomatis disimpan di antara pemanggilan.

## Ekspresi Pembangkit Generator
embangkit generators sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaksis yang mirip dengan pemahaman daftar list comprehensions tetapi dengan tanda kurung bukan dengan tanda kurung siku. Ungkapan-ungkapan ini dirancang untuk situasi di mana generator digunakan segera oleh fungsi penutup. Ekspresi generator lebih kompak tetapi kurang fleksibel daripada definisi generator penuh dan cenderung lebih ramah memori daripada pemahaman daftar list comprehensions setara, Contohnya :
#### ```Kode 27```
```
sum(i*i for i in range(10))                 # sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product

unique_words = set(word for line in page  for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
```
## Kesimpulan
Mekanisme kelas Python yang menambah kelas dengan minimum sintaksis dan semantik baru, adalah campuran dari mekanisme kelas yang ditemukan dalam C++. Kelas Python menyediakan semua fitur standar Pemrograman Berorientasi Objek, mekanisme pewarisan kelas memungkinkan beberapa kelas dasar, kelas turunan dapat menimpa metode apa pun dari kelas dasar atau kelasnya, dan metode dapat memanggil metode kelas dasar dengan nama yang sama. Objek dapat berisi jumlah dan jenis data yang berubah-ubah. Seperti halnya untuk modul, kelas mengambil bagian dari sifat dinamis Python, mereka dibuat pada saat runtime, dan dapat dimodifikasi lebih lanjut setelah pembuatan.
