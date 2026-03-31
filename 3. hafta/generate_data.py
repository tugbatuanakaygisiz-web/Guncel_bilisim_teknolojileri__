import csv
import random

def generate_dataset(filename, num_rows=500):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Uyku_Suresi_Saat', 'Kahve_Tuketimi_ml'])
        
        for _ in range(num_rows):
            # Normal dağılım (Ortalama: 7.5 saat, Standart Sapma: 1.5 saat)
            uyku = random.gauss(7.5, 1.5)
            uyku = max(0.0, min(uyku, 24.0)) # 0'dan küçük veya 24'ten büyük olmaması için
            
            # Normal dağılım (Ortalama: 250 ml, Standart Sapma: 100 ml)
            kahve = random.gauss(250, 100)
            kahve = max(0.0, kahve) # 0'dan küçük olmaması için
            
            writer.writerow([round(uyku, 2), round(kahve, 2)])

if __name__ == "__main__":
    generate_dataset('data.csv', 500)
    print("500 satırlık normal dağılımlı sentetik veri seti oluşturuldu: data.csv")
