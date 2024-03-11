# sea_level_predictor.py

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Veri setini içe aktar
df = pd.read_csv("epa-sea-level.csv")

# Dağılım grafiğini oluştur
plt.figure(figsize=(10, 6))
plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Gözlemler", color="blue")

# En uygun çizgiyi hesapla
slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
plt.plot(df["Year"], slope * df["Year"] + intercept, label="En Uygun Çizgi", color="red")

# 2050 yılına kadar tahmin yapmak için çizgiyi uzat
future_years = range(1880, 2051)
plt.plot(future_years, slope * future_years + intercept, linestyle="--", color="green")

# 2000 yılından sonraki verilere göre yeni bir çizgi çizin
recent_data = df[df["Year"] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data["Year"], recent_data["CSIRO Adjusted Sea Level"])
plt.plot(future_years, slope_recent * future_years + intercept_recent, linestyle="--", color="orange")

# Etiketler ve başlık ekle
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")

# Görseli kaydet ve göster
plt.legend()
plt.savefig("sea_level_plot.png")
plt.show()