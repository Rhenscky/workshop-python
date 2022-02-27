# Struktur Data
Struktur Data adalah struktur yang dapat menyimpan dan mengorganisasikan kumpulan data. Berikut struktur data yang ada dalam Python.

Struktur data berbicara mengenai suatu cara untuk menyimpan, menyusun, mengelompokkan dan merepresentasikan suatu data. Struktur data merupakan hal yang sangat penting dan wajib dikuasai oleh seorang programmer. Di forum-forum pemrograman, saya sering menjumpai pertanyaan-pertanyaan yang menurut saya bisa diselesaikan jika orang tersebut paham mengenai konsep struktur data. Dalam Python terdapat empat struktur data built-in yaitu List, Tuple, Dictionary, dan Set. Sebenarnya masih ada lagi, tapi menurut saya 4 struktur data tersebut yang paling penting dan sering digunakan.

## 1. List
List merupakan struktur data terurut (sequence). Setiap item dalam List memiliki sebuah index yang dimulai dari 0. List direpresentasikan dengan karakter square brackets []. Mungkin terlihat mirip dengan Array pada bahasa pemrograman lain seperti Java, tapi List dalam Python bisa menampung berbagai tipe data.

## 2. Tuple
Tuple sebenarnya sama dengan List, perbedaannya adalah Tuple memiliki sifat immutable yang artinya tidak bisa dirubah bahkan dihapus. Sebuah Tuple direpresentasikan dengan karakter parentheses ().

## 3. Dictionary
Dictionary merupakan struktur data yang berupa pasangan key-value. Setiap informasi yang disimpan pada Dictionary di petakan dengan satu key untuk mengakses informasi tersebut. Bahkan sebuah Dictionary bisa berisi Dictionary lain.

## 4. Set
Set merupakan struktur data yang memiliki kelebihan yaitu bersifat unique, jadi ketika kita memasukkan data yang sama pada Set, maka salah satu data itu akan di replace. Namun yang perlu diperhatikan bahwa struktur data Set juga bersifat unordered atau tidak berurut. Selain itu Set juga bersifat unindexed atau tidak memiliki index, sehingga kita tidak bisa mengakses salah satu data dari Set berdasarkan index tertentu.

### Daftar Structur Data

Berikut adalah semua metode objek yang digunakan pada daftar Python :
```
list.append( x )
Tambahkan item ke akhir daftar. Setara dengan .a[len(a):] = [x]
```
```
list.extend( dapat diubah )
Perluas daftar dengan menambahkan semua item dari iterable. Setara dengan .a[len(a):] = iterable
```
```
list.insert( saya , x )
Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen yang akan disisipkan sebelumnya, jadi disisipkan di bagian depan daftar, dan sama dengan .a.insert(0, x)a.insert(len(a), x)a.append(x)
```
```
list.remove( x )
Hapus item pertama dari daftar yang nilainya sama dengan x . Ini menimbulkan ValueErrorjika tidak ada item seperti itu.
```
```
list.pop( [ saya ] )
Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop()hapus dan kembalikan item terakhir dalam daftar. 
(Kurung siku di sekitar i dalam tanda tangan metode menunjukkan bahwa parameternya opsional, bukan berarti Anda harus mengetikkan tanda kurung siku pada posisi itu. Anda akan sering melihat notasi ini di Referensi Pustaka Python.)
```
```
list.clear( )
Hapus semua item dari daftar. Setara dengan .del a[:]
```
list.index( x [ , mulai [ , akhir ] ] )
Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x . Menaikkan a ValueErrorjika tidak ada item seperti itu.
Argumen opsional mulai dan akhir ditafsirkan seperti dalam notasi irisan dan digunakan untuk membatasi pencarian ke urutan daftar tertentu. Indeks yang dikembalikan dihitung relatif terhadap awal urutan penuh daripada argumen awal.
```
list.count( x )
Kembalikan berapa kali x muncul dalam daftar.
```
```
list.sort( * , kunci = Tidak ada , terbalik = Salah )
Urutkan item dari daftar di tempat (argumen dapat digunakan untuk penyesuaian pengurutan, lihat sorted()penjelasannya).
```
```
list.reverse( )
Balikkan elemen daftar di tempatnya.
```
```
list.copy( )
Kembalikan salinan daftar yang dangkal. Setara dengan a[:].
```

Contoh yang menggunakan sebagian besar metode daftar :

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
