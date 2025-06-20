# 👤 User Detail Tracking System

This is a modular Django-based project designed to track and manage user details such as albums, posts, to-dos, and personal information. The project supports Docker for containerized deployment and is structured for scalability and maintainability.

---

## 📁 Project Structure

### 🔹 Core Files

- `manage.py`: Django's command-line utility.
- `requirements.txt`: Lists required Python packages.
- `schema.yml`: Defines API structure and data models.
- `.gitignore`: Specifies files and folders to ignore in Git.
- `Docker/`
  - `Dockerfile`: Docker image configuration.
  - `.dockerignore`: Files to exclude from Docker build context.
  - `docker-compose.yml`: Manages multi-container Docker setup.

---

## 📦 Application Modules

### 1. `albums/`  
- Handles user album operations.  
- API endpoints located in `albums/api/`.  
- Database migrations in `albums/migrations/`.

### 2. `posts/`  
- Manages user-generated posts.  
- API logic in `posts/api/`.  
- Migrations in `posts/migrations/`.

### 3. `todos/`  
- Controls user to-do items.  
- API implemented under `todos/api/`.

### 4. `users/`  
- Manages user accounts, authentication, and sessions.  
- API routes in `users/api/`.  
- Migrations in `users/migrations/`.

---

## ⚙️ Django Project Settings

Located in `user_detail_tracking/`:

- `settings.py`: Project configuration (databases, installed apps, etc.)
- `urls.py`: URL routing.

---

## 📂 Media Directory

- `media/images/`: Includes sample image files used for testing.

---

## 🚀 Getting Started

### 🔧 Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔄 Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 🧪 Run the Development Server (without Docker)

```bash
python manage.py runserver
```

Note: If you're not using Docker, update the DATABASES['default']['HOST'] setting in settings.py from 'db' to 'localhost'.

## 🐳 Run with Docker (Optional)

```bash
docker-compose up --build
```

This will spin up the web app and PostgreSQL DB in containers.

## 🔌 API Endpoints

Each module has its own set of RESTful endpoints:

Module	| Endpoint
---|---
Albums	|/api/albums/
Posts	|/api/posts/
Todos	|/api/todos/
Users	|/api/users/

See schema.yml for a full OpenAPI-style API reference.

## 🧑‍💻 Contributing

Pull requests and issues are welcome! To contribute:

1. Fork the repository

2. Create a new branch (git checkout -b feature/YourFeature)

3. Commit your changes

4. Open a Pull Request

## 📄 License

This project is licensed under the [MIT License](LICENCE).

## 🔗 Developer Info

Omer Gokdemir
📧 omer66gokdemir@gmail.com
🌐 [LinkedIn](https://www.linkedin.com/in/omer-gokdemir/)
🐙 [GitHub](https://github.com/OmerGokdemir)
📦 [Upwork](https://www.upwork.com/freelancers/~01cf80f9e22cf120e3)

****


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

3. **Sunucuyu Çalıştırın:**<br>
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
