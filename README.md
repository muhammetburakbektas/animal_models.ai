# 🧠 Yapay Zeka Destekli Görüntü Sınıflandırıcı

# 📦 Kütüphane Kurulumu Hakkında Bilgilendirme
Projeyi çalıştırmadan önce, ortamınıza gerekli Python kütüphanelerinin yüklenmiş olması gerekmektedir. Bu kütüphaneler, requirements.txt dosyasında listelenmiştir. Aşağıdaki komutu terminalde çalıştırarak tüm bağımlılıkları kolayca yükleyebilirsiniz:

pip install -r requirements.txt

Bu adımı tamamladıktan sonra proje sorunsuz şekilde başlatılabilir.

## 📌 Proje Açıklaması
Bu proje, kullanıcıların yüklediği bir görselin içeriğini tanımlayarak hangi hayvan sınıfına ait olduğunu tahmin eden bir yapay zeka uygulamasıdır. TensorFlow kullanılarak eğitilen görüntü sınıflandırma modeli, Gradio arayüzü ile kullanıcıya sade ve etkileşimli bir şekilde sunulmaktadır.

## 🎯 Hedef
Makine öğrenmesi teknikleri kullanılarak bir görüntü sınıflandırma modeli oluşturmak ve bu modeli kullanıcı dostu bir arayüz ile entegre ederek herkesin kolayca kullanabileceği bir yapay zeka uygulaması geliştirmek.

## 📂 Proje Yapısı
Proje, aşağıdaki temel bileşenlerden oluşur:
- `data/` → Eğitimde kullanılan veri kümesi
- `main.py` → Model eğitimi ve Gradio arayüzünü içeren ana Python dosyası
- `animal_classifier_model.h5` → Eğitilmiş model dosyası
- `requirements.txt` → Gerekli kütüphanelerin listesi
- `README.md` → Proje dökümantasyonu

## ⚙️ Kurulum ve Kullanımgit remote add origin https://github.com/muhammetburakbektas/animal_models.ai.git
git branch -M main
git push -u origin main

### 1. Depoyu Klonlayın
```bash
git clone <repo-link>
cd cloud_project
```

### 2. Sanal Ortam Oluşturun ve Etkinleştirin
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Gerekli Kütüphaneleri Yükleyin
```bash
pip install -r requirements.txt
```

### 4. Uygulamayı Başlatın
```bash
python main.py
```

## 🧪 Kullanılan Teknolojiler
- Python
- TensorFlow
- Gradio
- NumPy
- Pillow


## 📊 Model Başarımı
Model eğitimi sırasında elde edilen temel başarı metrikleri:

- Accuracy: 0.9900
- Loss: 0.0386
- Val_accuracy: 0.6097
- Val_loss: 2.4182

## 🔍 Veri Seti
Proje, [Animals-10 Dataset](https://www.kaggle.com/datasets/alessiocorrado99/animals10) kullanılarak geliştirilmiştir. Veri kümesi dengeli ve etiketli 10 farklı hayvan sınıfından oluşmaktadır.

## 📁 Dosya Yapısı
```
cloud_project/
├── data/
├── venv/
├── main.py
├── animal_classifier_model.h5
├── requirements.txt
└── README.md
```


## 🧑‍💻 Geliştirici
- Muhammet Burak Bektaş 
# animal_models.ai
