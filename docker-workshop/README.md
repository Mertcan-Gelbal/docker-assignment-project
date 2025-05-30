# Docker Getting Started Workshop

Bu proje, Docker resmi "Get Started Workshop" uygulamasının akademik amaçlı implementasyonudur. Todo list uygulaması olarak tasarlanmış olup Docker teknolojisinin temel özelliklerini öğrenmek ve uygulamak için geliştirilmiştir.

## 🔗 Repository Links

- **GitHub:** [docker-assignment-project](https://github.com/Mertcan-Gelbal/docker-assignment-project)
- **Docker Hub:** [gelbalmertcan/docker-assignment:workshop](https://hub.docker.com/r/gelbalmertcan/docker-assignment)
- **Proje Klasörü:** `/docker-workshop/`

## Proje Özellikleri

- React tabanlı kullanıcı arayüzü
- Node.js backend servisi
- MySQL veritabanı entegrasyonu
- Docker Compose ile çoklu container mimarisi
- Volume ve bind mount yapılandırmaları
- Multi-stage Dockerfile implementasyonu

## Sistem Gereksinimleri

- Docker Desktop (v20.10 veya üzeri)
- Docker Compose (v2.0 veya üzeri)
- Git versiyon kontrol sistemi

## Kurulum ve Çalıştırma

### Geliştirme Ortamı Kurulumu

```bash
# Repository klonlama
git clone <repository-url>
cd docker-workshop

# Docker Compose ile sistem başlatma
docker compose up -d

# Uygulama erişimi
http://localhost:3000
```

### Production Ortamı Kurulumu

```bash
# Production image oluşturma
docker build -t getting-started:prod --target production .

# Production container çalıştırma
docker run -dp 3000:3000 getting-started:prod
```

## Docker Komut Referansı

### Temel Container İşlemleri

```bash
# Image oluşturma
docker build -t getting-started .

# Container çalıştırma
docker run -dp 3000:3000 getting-started

# Docker Hub'a push
docker tag getting-started gelbalmertcan/docker-assignment:workshop
docker push gelbalmertcan/docker-assignment:workshop

# Volume ile veri kalıcılığı
docker run -dp 3000:3000 --mount type=volume,src=todo-db,target=/etc/todos getting-started

# Bind mount ile geliştirme ortamı
docker run -dp 3000:3000 --mount type=bind,src="$(pwd)",target=/app node:18-alpine sh -c "cd /app && npm install && npm run dev"
```

### Docker Compose İşlemleri

```bash
# Servisleri başlatma
docker compose up -d

# Servisleri durdurma
docker compose down

# Logları görüntüleme
docker compose logs

# Servis durumu kontrolü
docker compose ps
```

## Proje Mimarisi

```
docker-workshop/
├── src/                    # Uygulama kaynak kodları
│   ├── static/            # Frontend statik dosyaları
│   │   ├── css/          # Stil dosyaları
│   │   └── js/           # JavaScript dosyaları
│   └── index.js          # Backend server dosyası
├── spec/                  # Test spesifikasyonları
├── Dockerfile             # Multi-stage container tanımı
├── compose.yaml           # Docker Compose yapılandırması
├── package.json           # Node.js bağımlılık tanımları
├── .dockerignore         # Docker build hariç tutma kuralları
├── README.md             # Proje dokümantasyonu
├── LICENSE               # Lisans bilgileri
├── CONTRIBUTING.md       # Katkı kuralları
├── CODE_OF_CONDUCT.md    # Davranış kuralları
└── NOTICE.md             # Üçüncü parti lisans bildirimleri
```

## Teknik Detaylar

### Container Mimarisi
- **Frontend**: React.js tabanlı single-page application
- **Backend**: Node.js Express server
- **Veritabanı**: MySQL 8.0 container
- **Network**: Docker bridge network ile servis iletişimi

### Volume Yönetimi
- `todo-mysql-data`: MySQL veri kalıcılığı
- `todo-db`: Uygulama veri depolama

### Port Yapılandırması
- **3000**: Web uygulaması portu
- **3306**: MySQL veritabanı portu (internal)

## Katkıda Bulunma

Proje katkılarını kabul etmektedir. Katkıda bulunmak için lütfen CONTRIBUTING.md dosyasındaki kuralları inceleyiniz.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylı bilgi için LICENSE dosyasına bakınız.

## Referanslar

- Docker Official Documentation: https://docs.docker.com/
- Node.js Documentation: https://nodejs.org/docs/
- React Documentation: https://reactjs.org/docs/
- MySQL Documentation: https://dev.mysql.com/doc/