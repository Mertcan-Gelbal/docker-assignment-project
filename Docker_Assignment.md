# Açık Kaynak Uygulamalı Docker Ödevi

## 🎓 Ders: Açık Kaynak Kodlu Yazılımlar
**Teslim Tarihi**: 31 Mayıs 2025  
**Teslim Yeri**: Google Classroom (Yalnızca DELIVERY.md dosyası)

---

## 🎯 Ödevin Amacı

Bu ödevin amacı, Docker teknolojisini adım adım öğrenmek ve açık kaynak proje yapısını deneyimlemektir. Öğrenciler hem Docker resmi workshop'unu uygulayacak hem de kendi seçtikleri bir mini projeyi containerize ederek kendi çözümlerini üreteceklerdir.

---

## 📌 Ödev İki Aşamadan Oluşur

### 🧩 Aşama 1 – Docker Workshop Uygulaması

Docker Docs üzerindeki ["Get Started Workshop"](https://docs.docker.com/get-started/workshop/) serisini takip ederek 8 aşamalı çalışmayı birebir uygulayınız:

| Bölüm | Konu Başlığı                       |
| ----- | ---------------------------------- |
| 1     | Containerize the application       |
| 2     | Update the application             |
| 3     | Share the image on Docker Hub      |
| 4     | Persist the database using volumes |
| 5     | Bind mounts for live development   |
| 6     | Multi-container setup with MySQL   |
| 7     | Use Docker Compose                 |
| 8     | Image building best practices      |

#### 🔧 Gereklilikler:
- Workshop içeriği için ayrı bir GitHub reposu açılmalı
- Oluşturulan image Docker Hub hesabına push edilmeli
- Açık kaynak proje yapısına uygun dosyalar (README, LICENSE, CONTRIBUTING vb.) repo içinde yer almalı

---

### 🧪 Aşama 2 – Kendi Mini Docker Projen

Workshop tamamlandıktan sonra kendi basit web uygulamanızı containerize ederek çoklu servisli bir yapı kurunuz.

#### 🔨 Kurallar:
- En az 1 web uygulaması + 1 veritabanı servisi
- Dockerfile ve compose.yaml dosyaları yazılmalı
- Volume ve network kullanılmalı
- Ortam değişkenleriyle yapılandırma sağlanmalı
- `docker-compose up` komutuyla sistem ayağa kalkmalı
- Bu proje için de ayrı bir GitHub reposu ve ayrı bir Docker Hub image oluşturulmalı

---

## 🗂️ GitHub Reposunda Bulunması Gereken Dosyalar

Her iki proje (workshop + mini proje) için aşağıdaki yapının uygulanması beklenmektedir:

```
/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── NOTICE.md
├── CODE_OF_CONDUCT.md
├── Dockerfile
├── compose.yaml
├── .dockerignore
└── src/
```

---

## 📝 Teslimat Formatı

Her öğrenci yalnızca **`DELIVERY.md`** adlı markdown dosyasını doldurarak Google Classroom'a yükleyecektir.

### DELIVERY.md içeriği:
- Workshop projesi için GitHub ve Docker Hub linkleri
- Mini proje için GitHub ve Docker Hub linkleri
- Her iki proje için açıklamalar
- Açık kaynak proje dosyalarının listesi

Hazır şablon dosyasını Google Classroom’da bulabilirsiniz.

---

## 🧮 Değerlendirme Kriterleri

| Kriter                            | Puan    |
| --------------------------------- | ------- |
| Workshop adımlarının tamamlanması | 30      |
| GitHub açık kaynak yapı uyumu     | 20      |
| Docker Hub image çalışırlığı      | 10      |
| Kendi projenizin çalışması        | 30      |
| Kod kalitesi ve açıklamalar       | 10      |
| **Toplam**                        | **100** |

---

Başarılar!
