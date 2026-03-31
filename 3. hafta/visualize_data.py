import csv
import numpy as np
import matplotlib.pyplot as plt

# Normal dağılım (çan eğrisi) yoğunluk fonksiyonu
def norm_pdf(x, mu, sigma):
    return (1.0 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Verileri oku
uyku_suresi = []
kahve_tuketimi = []

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        uyku_suresi.append(float(row['Uyku_Suresi_Saat']))
        kahve_tuketimi.append(float(row['Kahve_Tuketimi_ml']))

uyku_suresi = np.array(uyku_suresi)
kahve_tuketimi = np.array(kahve_tuketimi)

# Görselleştirme için figür ayarları
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# --- Uyku Süresi Görselleştirmesi ---
mu1, std1 = np.mean(uyku_suresi), np.std(uyku_suresi)
# Histogram
axes[0].hist(uyku_suresi, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black', label="Veri (Histogram)")
xmin1, xmax1 = axes[0].get_xlim()
x1 = np.linspace(xmin1, xmax1, 100)
p1 = norm_pdf(x1, mu1, std1)
# Çan eğrisi (Bell curve)
axes[0].plot(x1, p1, 'r-', linewidth=2, label=fr'Normal Eğri ($\mu={mu1:.2f}, \sigma={std1:.2f}$)')
axes[0].set_title('Uyku Süresi: Histogram ve Normal Eğri')
axes[0].set_xlabel('Uyku Süresi (Saat)')
axes[0].set_ylabel('Yoğunluk (Density)')
axes[0].legend()

# --- Kahve Tüketimi Görselleştirmesi ---
mu2, std2 = np.mean(kahve_tuketimi), np.std(kahve_tuketimi)
# Histogram
axes[1].hist(kahve_tuketimi, bins=30, density=True, alpha=0.6, color='sandybrown', edgecolor='black', label="Veri (Histogram)")
xmin2, xmax2 = axes[1].get_xlim()
x2 = np.linspace(xmin2, xmax2, 100)
p2 = norm_pdf(x2, mu2, std2)
# Çan eğrisi (Bell curve)
axes[1].plot(x2, p2, 'r-', linewidth=2, label=fr'Normal Eğri ($\mu={mu2:.2f}, \sigma={std2:.2f}$)')
axes[1].set_title('Kahve Tüketimi: Histogram ve Normal Eğri')
axes[1].set_xlabel('Kahve Tüketimi (ml)')
axes[1].set_ylabel('Yoğunluk (Density)')
axes[1].legend()

# Düzenleme ve Kaydetme
plt.tight_layout()
plt.savefig('veri_gorsellestirme.png', dpi=300)
print("Histogramlar ve normal dağılım eğrileri 'veri_gorsellestirme.png' dosyasına başarıyla kaydedildi.")
