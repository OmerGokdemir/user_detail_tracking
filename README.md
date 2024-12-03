
# Kullanıcı Detay İzleme Projesi

Bu proje, Django tabanlı bir kullanıcı detay izleme ve yönetim sistemidir. Proje Docker destekli olarak geliştirilmiştir ve aşağıdaki modülleri içerir:

## Proje Yapısı

### Temel Dosyalar
- **`manage.py`**: Django yönetim komutlarını çalıştırmak için kullanılan dosya.
- **`requirements.txt`**: Projede kullanılan Python paketlerini listeler.
- **`schema.yml`**: Proje veri modeli ve ilişkilerini tanımlayan şema.
- **`.gitignore`**: Göz ardı edilmesi gereken dosyaları belirler.
- **Docker**:
  - **`dockerfile`**: Docker görüntüsünü oluşturmak için yapılandırma.
  - **`.dockerignore`**: Docker tarafından göz ardı edilecek dosyalar.
  - **`docker-compose.yml`**: Servisleri yönetmek için Docker Compose yapılandırması.

### Uygulama Modülleri
#### 1. Albums Modülü
- Kullanıcı albümlerinin yönetimi için oluşturulmuştur.
- API Endpoint'leri `albums/api` dizininde tanımlıdır.
- Migration dosyaları `albums/migrations` klasöründedir.

#### 2. Posts Modülü
- Kullanıcı gönderilerinin yönetimi için hazırlanmıştır.
- API Endpoint'leri `posts/api` dizininde yer alır.
- Migration dosyaları `posts/migrations` klasöründe bulunur.

#### 3. Todos Modülü
- Kullanıcıların yapılacaklar listesini yönetir.
- API Endpoint'leri `todos/api` dizininde tanımlıdır.

#### 4. Users Modülü
- Kullanıcı yönetimi ve oturum işlemleri için geliştirilmiştir.
- API Endpoint'leri `users/api` dizininde tanımlıdır.
- Migration dosyaları `users/migrations` klasöründe yer alır.

### Django Proje Ayarları
- `user_detail_tracking` dizini:
  - **`settings.py`**: Proje ayarları.
  - **`urls.py`**: URL yönlendirmeleri.

### Ortam Dosyaları
- **`media/images`**: Test amaçlı kullanılan resim dosyalarını içerir.

## Kurulum ve Çalıştırma

1. **Gereksinimleri Yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Veritabanı Migrasyonları:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Sunucuyu Çalıştırın:**
   **Not:** docker olmadan test için settings.py içinde database ayarında host alanını 'db' yerine 'localhost' yada sunucunuzu yazınız.
   ```bash
   python manage.py runserver
   ```

4. **Docker ile Çalıştırma (Opsiyonel):**
   ```bash
   docker-compose up --build
   ```

## API Kullanımı

Her modül için ayrı bir API seti bulunmaktadır. Örnek URL'ler aşağıdaki gibidir:
- **Albums API:** `/api/albums/`
- **Posts API:** `/api/posts/`
- **Todos API:** `/api/todos/`
- **Users API:** `/api/users/`

API dokümantasyonu için `schema.yml` dosyasına bakabilirsiniz.

## Katkıda Bulunma
Bu projeye katkıda bulunmak için lütfen bir **Pull Request** gönderin veya bir **Issue** açın.

## Lisans
Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.
