# Responsi Workshop Python
## URL dari file c159s.csv
https://raw.githubusercontent.com/lrjoshi/webpage/master/public/post/c159s.csv
Berisi data percobaan Sel Firus

## Menjalankan di CMD
Buka CMD dan masuk ke python
```
> python
```
Untuk menggunakan pandas, import pandas sebagai pd
```
>>> import pandas as pd
```

## Untuk mendwnload data 
>>> url = "https://raw.githubusercontent.com/lrjoshi/webpage/master/public/post/c159s.csv"
>>> df = pd.read_csv(url)

## Menampilkan data 
masukkan perintah dibawah untuk menampilkan semua data, data berjumlah 72 rows × 6 columns
```
>>> df
   Experiment  Virus   Cell   MOI  hpi  Titer
0        EXP I  C159S  OFTu   0.1    0   4.75
1        EXP I  C159S  OFTu   0.1    6   2.75
2        EXP I  C159S  OFTu   0.1   12   2.75
3        EXP I  C159S  OFTu   0.1   24   5.00
4        EXP I  C159S  OFTu   0.1   48   5.50
..         ...    ...   ...   ...  ...    ...
67     EXP III  C159S   STU  10.0    6   5.00
68     EXP III  C159S   STU  10.0   12   5.00
69     EXP III  C159S   STU  10.0   24   5.00
70     EXP III  C159S   STU  10.0   48   5.00
71     EXP III  C159S   STU  10.0   72   5.00

[72 rows x 6 columns]
```
Untuk Menampilkan 2 data
```
>>> df.head(2)
  Experiment  Virus   Cell  MOI  hpi  Titer
0       EXP I  C159S  OFTu  0.1    0   4.75
1       EXP I  C159S  OFTu  0.1    6   2.75
```
