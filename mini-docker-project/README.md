# Görev Yöneticisi - Docker Mini Projesi

Bu proje, Flask ve PostgreSQL kullanılarak geliştirilmiş bir görev yönetim uygulamasıdır. Docker ve Docker Compose ile containerize edilmiş olup, modern web uygulaması geliştirme pratiklerini demonstre etmektedir.

## 🔗 Repository Links

- **GitHub:** [docker-assignment-project](https://github.com/Mertcan-Gelbal/docker-assignment-project)
- **Docker Hub:** [gelbalmertcan/docker-assignment:latest](https://hub.docker.com/r/gelbalmertcan/docker-assignment)
- **Proje Klasörü:** `/mini-docker-project/`

## Proje Özellikleri

- Flask tabanlı web uygulaması
- PostgreSQL veritabanı entegrasyonu
- Bootstrap ile responsive tasarım
- Docker multi-stage build yapısı
- Docker Compose ile orkestrasyon
- Volume tabanlı veri kalıcılığı
- Health check implementasyonu

## Sistem Gereksinimleri

- Docker Desktop (v20.10 veya üzeri)
- Docker Compose (v2.0 veya üzeri)
- Git versiyon kontrol sistemi

## Kurulum ve Çalıştırma

### Hızlı Başlangıç

```bash
# Repository klonlama
git clone <repository-url>
cd mini-docker-project

# Docker Compose ile sistem başlatma
docker compose up -d

# Uygulama erişimi
http://localhost:5000
```

### Manuel Kurulum

```bash
# PostgreSQL container çalıştırma
docker run -d --name postgres-db \
  -e POSTGRES_DB=taskdb \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=password \
  -p 5432:5432 \
  postgres:15-alpine

# Uygulama image'ı build etme
docker build -t task-manager .

# Uygulama container çalıştırma
docker run -d --name task-app \
  -p 5000:5000 \
  -e DB_HOST=host.docker.internal \
  -e DB_NAME=taskdb \
  -e DB_USER=postgres \
  -e DB_PASSWORD=password \
  task-manager
```

## Uygulama Özellikleri

### Fonksiyonel Özellikler
- Görev ekleme ve listeleme
- Görev tamamlama işaretleme
- Görev silme
- İstatistik görüntüleme
- Responsive web arayüzü

### Teknik Özellikler
- RESTful API yapısı
- Template tabanlı rendering
- Form validasyonu
- Error handling
- Health check endpoint

## Docker Komut Referansı

### Temel İşlemler

```bash
# Servisleri başlatma
docker compose up -d

# Servisleri durdurma
docker compose down

# Logları görüntüleme
docker compose logs -f

# Servis durumu kontrolü
docker compose ps
```

### Development İşlemleri

```bash
# Development image build
docker build --target development -t task-manager:dev .

# Production image build
docker build --target production -t task-manager:prod .

# Docker Hub'a push
docker tag task-manager:prod gelbalmertcan/docker-assignment:latest
docker tag task-manager:prod gelbalmertcan/docker-assignment:flask-app
docker push gelbalmertcan/docker-assignment:latest
docker push gelbalmertcan/docker-assignment:flask-app

# Container içinde shell açma
docker compose exec web bash

# Veritabanı backup
docker compose exec db pg_dump -U postgres taskdb > backup.sql
```

## Proje Mimarisi

```
mini-docker-project/
├── app.py                  # Ana Flask uygulaması
├── requirements.txt        # Python bağımlılıkları
├── Dockerfile             # Multi-stage container tanımı
├── compose.yaml           # Docker Compose yapılandırması
├── .dockerignore          # Docker build hariç tutma kuralları
├── templates/             # HTML template dosyaları
│   ├── base.html         # Ana template
│   ├── index.html        # Ana sayfa
│   └── add_task.html     # Görev ekleme sayfası
├── README.md             # Proje dokümantasyonu
├── LICENSE               # Lisans bilgileri
├── CONTRIBUTING.md       # Katkı kuralları
├── CODE_OF_CONDUCT.md    # Davranış kuralları
└── NOTICE.md             # Üçüncü parti lisans bildirimleri
```

## API Endpoints

| Method | Endpoint | Açıklama |
|--------|----------|----------|
| GET | `/` | Ana sayfa - görev listesi |
| GET | `/add` | Görev ekleme formu |
| POST | `/add` | Yeni görev ekleme |
| GET | `/complete/<id>` | Görevi tamamla |
| GET | `/delete/<id>` | Görev silme |
| GET | `/health` | Health check |

## Environment Variables

| Variable | Default | Açıklama |
|----------|---------|----------|
| `DB_HOST` | localhost | PostgreSQL host |
| `DB_NAME` | taskdb | Veritabanı adı |
| `DB_USER` | postgres | Veritabanı kullanıcısı |
| `DB_PASSWORD` | password | Veritabanı şifresi |
| `DB_PORT` | 5432 | Veritabanı portu |
| `SECRET_KEY` | dev-secret-key | Flask secret key |

## Güvenlik Özellikleri

- Non-root user ile container çalıştırma
- SQL injection koruması (parameterized queries)
- CSRF token koruması
- Environment variable tabanlı konfigürasyon
- Health check monitoring

## Performance Optimizasyonları

- Multi-stage Docker build
- Layer caching optimizasyonu
- Database connection pooling
- Static file caching
- Minimal base image kullanımı

## Monitoring ve Logging

```bash
# Container logları
docker compose logs web
docker compose logs db

# Resource kullanımı
docker stats

# Health check durumu
curl http://localhost:5000/health
```

## Troubleshooting

### Yaygın Sorunlar

1. **Database connection error**
   ```bash
   # PostgreSQL container durumunu kontrol edin
   docker compose ps db
   docker compose logs db
   ```

2. **Port already in use**
   ```bash
   # Kullanılan portları kontrol edin
   lsof -i :5000
   lsof -i :5432
   ```

3. **Volume permission issues**
   ```bash
   # Volume'ları temizleyin
   docker compose down -v
   docker volume prune
   ```

## Katkıda Bulunma

Proje katkılarını kabul etmektedir. Katkıda bulunmak için lütfen CONTRIBUTING.md dosyasındaki kuralları inceleyiniz.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylı bilgi için LICENSE dosyasına bakınız.

## Referanslar

- Flask Documentation: https://flask.palletsprojects.com/
- PostgreSQL Documentation: https://www.postgresql.org/docs/
- Docker Documentation: https://docs.docker.com/
- Bootstrap Documentation: https://getbootstrap.com/docs/ 