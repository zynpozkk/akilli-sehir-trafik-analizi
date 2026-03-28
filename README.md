# 🚗 Akıllı Şehir Canlı Yoğunluk Paneli - Ankara

Bu proje, şehirlerdeki trafik yoğunluğunu analiz eden ve görselleştiren interaktif bir **Streamlit** uygulamasıdır. Proje kapsamında, Ankara ili için oluşturulan **sentetik veri setleri** kullanılarak gerçek zamanlı trafik durumu simüle edilmiş ve analiz edilmiştir.

> **Not:** Bu proje, BTK Akademi eğitim serisi kapsamında geliştirilen bir eğitim projesidir ve şu an için sentetik verilerle çalışmaktadır.

---

## 📸 Uygulama Ekran Görüntüleri

Uygulamanın ana ekranı, canlı harita ve grafik analiz panellerinden oluşmaktadır:

[Image showing main title and central traffic map of Ankara]



---

## 🚀 Özellikler

Uygulama, şehir planlamacıları ve meraklı kullanıcılar için aşağıdaki temel özellikleri sunar:

-   **📍 İnteraktif Canlı Harita:** Ankara'nın farklı bölgelerindeki trafik yoğunluğunu renk kodlarıyla (Yeşil, Sarı, Kırmızı) anlık olarak gösterir.
-   **📈 Grafik Analizi:** Belirli bir bölge seçildiğinde, o bölgenin günlük saatlik ortalama trafik yoğunluğunu sütun grafiği ile görselleştirir.
-   **📊 Detaylı Veri Tablosu:** Seçilen bölgeye ait saatlik trafik yoğunluğu metriklerini tablo formatında sunar.
-   **🐍 İzole Çalışma Ortamı:** Proje, kütüphane çakışmalarını önlemek için `.venv` (sanal ortam) kullanılarak geliştirilmiştir.

---

## 🛠️ Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

### 1. Ön Hazırlık
Bilgisayarınızda Python yüklü olduğundan emin olun.

### 2. Projeyi İndirin
```bash
git clone [https://github.com/zynpozkk/akilli-sehir-trafik-analizi.git](https://github.com/zynpozkk/akilli-sehir-trafik-analizi.git)
cd akilli-sehir-trafik-analizi