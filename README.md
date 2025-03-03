# Python ile Türkçe Duygu Analizi Projesi

## Proje Hakkında
Bu proje, metin tabanlı veri kümeleri üzerinde Türkçe duygu analizi gerçekleştirmek için geliştirilmiştir. Proje kapsamında, cümlelerin genel duygu durumunu belirlemek amacıyla kelime tabanlı duygu analizi yöntemi kullanılmıştır. Kullanılan model, kelimelerin pozitif, negatif veya nötr duygu değerlerini analiz ederek sonuç üretmektedir.

## Özellikler
- **Metin Ön İşleme**: Kelimelere ayırma (tokenization), stopwords filtreleme, kök bulma (stemming).
- **Duygu Analizi**: Duygu sözlüğü, yoğunlaştırıcı ve zayıflatıcı kelimeler, olumsuzlama ifadeleri kullanarak analiz.
- **Performans Ölçümü**: Doğruluk, kesinlik, duyarlılık ve F1-skoru hesaplamaları.
- **Çıktı Üretimi**: Analiz sonuçlarının Excel dosyasına kaydedilmesi.

## Kullanılan Teknolojiler

<p align="left">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
    <img src="https://img.shields.io/badge/NLTK-32CD32?style=for-the-badge&logo=python&logoColor=white" alt="NLTK">
    <img src="https://img.shields.io/badge/Zemberek-FF4500?style=for-the-badge&logo=java&logoColor=white" alt="Zemberek">
    <img src="https://img.shields.io/badge/JPype-9933CC?style=for-the-badge&logo=python&logoColor=white" alt="JPype">
    <img src="https://img.shields.io/badge/XML-8A2BE2?style=for-the-badge&logo=xml&logoColor=white" alt="XML">
</p>

## Proje Dosyaları
- **Lexicon.py**: Duygu sözlüğünü işler ve kelime duygu skorlarını hesaplar.
- **Preprocessing.py**: Metinleri analiz için hazır hale getirir.
- **Sentiment_analysis.py**: Duygu analizini gerçekleştirir.
- **Metrics.py**: Modelin doğruluk, kesinlik ve F1-skorunu hesaplar.
- **Main.py**: Tüm işlemleri yöneten ana dosya.

### Veri Dosyaları
- **Lexicon.xml**: Kelimelerin pozitif, negatif ve nötr değerlerini içeren duygu sözlüğü.
- **Boosters.txt / Diminishers.txt**: Duygu yoğunluğunu artıran veya azaltan kelimeler.
- **Negation_words.txt**: Olumsuzlama ifadelerini içeren dosya.
- **Ornek_duygu-analiz-verisi-pozitif_negatif.xlsx**: Analiz edilecek örnek cümleler.
- **Analyzed_sentences.xlsx**: Analiz sonuçlarının kaydedildiği dosya.

## Çalıştırma Adımları
1. **Gereksinimleri yükleyin**:
   ```sh
   pip install pandas nltk jpype1
   ```
2. **Zemberek kurulumu**:
   - Zemberek JAR dosyasını indirin ve proje dizinine ekleyin.
3. **Ana dosyayı çalıştırın**:
   ```sh
   python Main.py
   ```

## Örnek Çıktı
```
Cümle: "Ben elma yemeyi seviyorum."
Kelimelerine Ayrılmış Hali: ['ben', 'elma', 'yemeyi', 'sev']
Gerçek Sınıf: Pozitif
Tahmin: Pozitif
Duygu Puanı: 0.6
```

## Sonuçlar
Proje, duygu analizi sisteminin performansını doğruluk, kesinlik, duyarlılık ve F1-skoru ile değerlendirmiştir. Elde edilen doğruluk oranı **%68** olup, sistemin geliştirilmesine yönelik iyileştirme alanları bulunmaktadır. Gelecekte daha geniş veri kümeleri ve gelişmiş metin işleme teknikleri ile doğruluk oranının artırılması hedeflenmektedir.

---

Bu proje, Python ve çeşitli doğal dil işleme araçları kullanılarak geliştirilmiş, Türkçe duygu analizine yönelik bir çözümdür.

