# Katkıda Bulunma Rehberi

Docker Workshop projesine katkıda bulunduğunuz için teşekkür ederiz. Bu dokümantasyon, projeye katkı sağlamak isteyen geliştiriciler için gerekli kuralları ve süreçleri açıklamaktadır.

## Katkı Türleri

### Issue Bildirimi
- Yazılım hatalarını detaylı bir şekilde raporlayınız
- Yeni özellik önerilerinizi gerekçeleriyle birlikte sununuz
- Dokümantasyon iyileştirme önerilerinizi belirtiniz

### Pull Request Süreci

1. **Repository Fork İşlemi**: Projeyi kendi GitHub hesabınıza fork ediniz
2. **Branch Oluşturma**: 
   ```bash
   git checkout -b feature/feature-name
   ```
3. **Geliştirme**: Kodunuzu yazınız ve test ediniz
4. **Commit İşlemi**: 
   ```bash
   git commit -m 'feat: add new feature description'
   ```
5. **Push İşlemi**: 
   ```bash
   git push origin feature/feature-name
   ```
6. **Pull Request**: GitHub üzerinden pull request oluşturunuz

## Kod Standartları

### Commit Mesaj Formatı
Conventional Commits standardını kullanınız:
- `feat:` - Yeni özellik ekleme
- `fix:` - Hata düzeltmesi
- `docs:` - Dokümantasyon değişikliği
- `style:` - Kod formatı düzenlemesi
- `refactor:` - Kod yeniden yapılandırması
- `test:` - Test ekleme veya düzeltme
- `chore:` - Yapılandırma değişiklikleri

### Docker En İyi Uygulamaları
- Multi-stage build yapısını kullanınız
- Layer caching optimizasyonu uygulayınız
- Güvenlik en iyi uygulamalarını takip ediniz
- .dockerignore dosyasını güncel tutunuz

### Kod Kalitesi Gereksinimleri
- ESLint kurallarına uygunluk sağlayınız
- Anlamlı değişken ve fonksiyon isimleri kullanınız
- Gerekli durumlarda kod yorumları ekleyiniz
- Mümkün olduğunca test yazınız

## Test Prosedürleri

### Geliştirme Ortamı Testi
```bash
# Geliştirme ortamında test
docker compose up -d
curl http://localhost:3000
```

### Production Ortamı Testi
```bash
# Production build testi
docker build -t getting-started:prod --target production .
docker run -dp 3001:3000 getting-started:prod
curl http://localhost:3001
```

## Pull Request Kontrol Listesi

Pull request göndermeden önce aşağıdaki maddeleri kontrol ediniz:

- [ ] Kod çalışır durumda ve test edilmiştir
- [ ] Commit mesajları conventional format standardındadır
- [ ] README dosyası güncellenmiştir (gerekli durumlarda)
- [ ] Breaking change durumları dokümante edilmiştir
- [ ] Docker image'ları başarıyla build edilmektedir
- [ ] Kod standartlarına uygunluk sağlanmıştır

## Davranış Kuralları

Proje katılımcılarından beklenen davranış standartları:

- Saygılı ve yapıcı iletişim kurma
- Farklı görüşlere açık olma
- Yardımlaşma ve işbirliği destekleme
- Sürekli öğrenme odaklı yaklaşım

## İletişim Kanalları

- **Issues**: GitHub Issues sistemi
- **Discussions**: GitHub Discussions platformu
- **Email**: proje-email@example.com

## Katkı Değerlendirme Süreci

Tüm katkılar aşağıdaki süreçlerden geçmektedir:

### Code Review Süreci
- Kod kalitesi değerlendirmesi
- Güvenlik analizi
- Performance değerlendirmesi
- Dokümantasyon kontrolü

### Test Süreci
- Otomatik test çalıştırma
- Manuel test prosedürleri
- Integration test kontrolü
- Regression test analizi

## Kabul Edilen Katkı Türleri

Projeye aşağıdaki türde katkılar kabul edilmektedir:

- Kod geliştirmeleri ve yeni özellikler
- Hata düzeltmeleri ve güvenlik yamaları
- Dokümantasyon iyileştirmeleri
- Test coverage artırımı
- Performance optimizasyonları
- Code review katılımı

Katkılarınız için teşekkür ederiz. 