from google_play_scraper import reviews, Sort
import pandas as pd

# 🔍 Ganti ini sesuai target kamu
app_package = 'com.gojek.app'  # Untuk Gojek
# app_package = 'com.grabtaxi.passenger'  # Untuk Grab

# Ambil review dari Play Store
result, _ = reviews(
    app_package,
    lang='id',          # Bahasa Indonesia
    country='id',       # Lokasi Indonesia
    sort=Sort.NEWEST,   # Atau bisa Sort.RATING / Sort.HELPFUL
    count=100000          # Ubah jumlah sesuai kebutuhan
)

# Simpan ke dataframe
df = pd.DataFrame(result)

# Pilih kolom penting
df_clean = df[['userName', 'score', 'content', 'at']]

# Simpan ke CSV
csv_filename = f'{app_package.split(".")[1]}_reviews.csv'
df_clean.to_csv(csv_filename, index=False, encoding='utf-8-sig')

print(f"✅ {len(df_clean)} review berhasil disimpan ke {csv_filename}")
