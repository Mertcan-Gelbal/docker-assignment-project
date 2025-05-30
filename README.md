# Docker Assignment Project

Bu repository, Docker teknolojisini öğrenmek ve uygulamak amacıyla geliştirilmiş iki aşamalı bir projedir.

## 🔗 Repository Links

- **GitHub:** [docker-assignment-project](https://github.com/Mertcan-Gelbal/docker-assignment-project)
- **Docker Hub:** [gelbalmertcan/docker-assignment](https://hub.docker.com/r/gelbalmertcan/docker-assignment)
  - `latest` / `flask-app` → Flask Task Manager
  - `workshop` → Docker Workshop App

## Proje Yapısı

```
Docker Project/
├── docker-workshop/          # Aşama 1: Docker Workshop
├── mini-docker-project/      # Aşama 2: Mini Docker Projesi
├── DELIVERY_TEMPLATE.md      # Teslim raporu
├── Docker_Assignment.md      # Ödev açıklaması
├── README.md                 # Bu dosya
└── LICENSE                   # MIT Lisansı
```

## Aşama 1: Docker Workshop

Docker'ın resmi "Get Started Workshop" uygulamasının tamamlanması.

**Teknolojiler:** Node.js, MySQL, Docker Compose

**Özellikler:**
- Multi-stage Dockerfile
- Volume management
- Container networking
- Docker Compose orchestration

## Aşama 2: Mini Docker Projesi

Flask tabanlı görev yönetim uygulaması.

**Teknolojiler:** Python Flask, PostgreSQL, Bootstrap

**Özellikler:**
- CRUD operations
- Responsive UI
- Database persistence
- Health monitoring

## Hızlı Başlangıç

### Docker Workshop
```bash
cd docker-workshop
docker compose up -d
# http://localhost:3000
```

### Mini Proje
```bash
cd mini-docker-project
docker compose up -d
# http://localhost:5001
```

## Öğrenci Bilgileri

- **Ad:** Mertcan Gelbal
- **Numara:** 171421012
- **Tarih:** 30.05.2025

## Lisans

MIT License - Detaylar için LICENSE dosyasına bakınız. 