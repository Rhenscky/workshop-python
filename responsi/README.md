# Responsi Workshop Python
## URL dari file c159s.csv
https://raw.githubusercontent.com/lrjoshi/webpage/master/public/post/c159s.csv
berisi data percobaan sel firus

# Menjalankan di CMD
Buka CMD dan masuk ke python
```
> python
```
Untuk menggunakan pandas, import pandas sebagai pd
```
>>> import pandas as pd
```

Buka CMD lalu masukkan perintah 
## Untuk mendwnload data 
>>> url = "https://raw.githubusercontent.com/lrjoshi/webpage/master/public/post/c159s.csv"
>>> df = pd.read_csv(url)

## Menampilkan data 
masukkan perintah dibawah untuk menampilkan semua data, data berjumlah 72 rows × 6 columns
```
>>> df
```
Untuk Menampilkan 2 data
```
>>> df.head(2)
```
