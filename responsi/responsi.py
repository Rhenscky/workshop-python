# Untuk menggunakan pandas, import pandas sebagai pd
import pandas as pd

# Untuk mendownload data CSV
url = "https://raw.githubusercontent.com/lrjoshi/webpage/master/public/post/c159s.csv"
df = pd.read_csv(url)

# Untuk Menampilkan 2 data
df.head(2)