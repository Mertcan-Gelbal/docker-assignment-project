# Docker Hub Push Komutları

## Önce image'ları yeniden tag'leyin:

```bash
# Mevcut tag'leri temizle
docker rmi mertcangelbal/docker-assignment:workshop
docker rmi mertcangelbal/docker-assignment:latest
docker rmi mertcangelbal/docker-assignment:flask-app

# Yeni kullanıcı adı ile tag'le
docker tag getting-started gelbalmertcan/docker-assignment:workshop
docker tag task-manager:prod gelbalmertcan/docker-assignment:latest
docker tag task-manager:prod gelbalmertcan/docker-assignment:flask-app
```

## Repository oluşturduktan sonra çalıştırılacak komutlar:

```bash
# Workshop uygulamasını push et
docker push gelbalmertcan/docker-assignment:workshop

# Flask uygulamasını push et
docker push gelbalmertcan/docker-assignment:latest
docker push gelbalmertcan/docker-assignment:flask-app
```

## Doğrulama komutları:

```bash
# Push edilen image'ları kontrol et
docker images | grep gelbalmertcan/docker-assignment

# Docker Hub'dan çek ve test et
docker pull gelbalmertcan/docker-assignment:workshop
docker pull gelbalmertcan/docker-assignment:latest
```

## Docker Hub Repository URL:
https://hub.docker.com/r/gelbalmertcan/docker-assignment 