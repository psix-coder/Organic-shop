# 🛒 Organic Shop - E-commerce Platform

![Django](https://img.shields.io/badge/django-4.2-green.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![SQLite](https://img.shields.io/badge/sqlite-3-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

> Django asosida yaratilgan organik mahsulotlar uchun to'liq funksional e-commerce platformasi

## 📖 Loyiha haqida

Organic Shop - bu organik va tabiiy mahsulotlar sotish uchun mo'ljallangan zamonaviy online do'kon platformasi. Loyiha Django framework yordamida yaratilgan va to'liq e-commerce funksiyalari bilan jihozlangan.

## ✨ Asosiy xususiyatlar

### 🏪 Mahsulot Boshqaruvi
- ✅ **Multi-level Categories** - Departments → All Categories → Categories
- ✅ **Product Management** - To'liq CRUD operatsiyalari
- ✅ **Image Gallery** - Har bir mahsulot uchun ko'p rasmlar
- ✅ **Price & Discount** - Narx va chegirmalar tizimi
- ✅ **Stock Management** - Mahsulot miqdorini boshqarish
- ✅ **Weight & Measurements** - KG, G, L, ML o'lchov birliklari

### 🎨 Kategoriya Tizimi
- ✅ **Departments** - Asosiy bo'limlar (rasmlar bilan)
- ✅ **All Categories** - Umumiy kategoriyalar
- ✅ **Sub Categories** - Pastki kategoriyalar
- ✅ **Slug System** - SEO-friendly URL'lar
- ✅ **Hierarchical Structure** - Ierarxik tuzilma

### 🖼️ Media Management
- ✅ **Product Images** - Mahsulot rasmlari yuklash
- ✅ **Department Images** - Bo'lim rasmlari
- ✅ **Image Preview** - Admin panelda rasm ko'rish
- ✅ **Media Storage** - Media fayllar boshqaruvi

### ⚙️ Admin Panel
- ✅ **Rich Admin Interface** - Django admin panel
- ✅ **Inline Editing** - Ichki tahrirlash
- ✅ **Bulk Actions** - Ommaviy operatsiyalar
- ✅ **Search & Filters** - Qidiruv va filtrlar
- ✅ **Image Thumbnails** - Rasm preview'lari

## 🛠️ Texnologiyalar

<div align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
</div>

**Backend:**
- Python 3.8+
- Django 4.2
- SQLite3
- Pillow (Image processing)

**Frontend:**
- HTML5
- CSS3
- Django Template Engine

## 🚀 O'rnatish va ishga tushirish

### Talablar

```
Python 3.8+
pip
virtualenv (tavsiya etiladi)
```

### Qadamlar

1. **Repository'ni clone qiling:**
```bash
git clone https://github.com/psix-coder/organic-shop.git
cd organic-shop/commerce
```

2. **Virtual environment yarating:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Kerakli paketlarni o'rnating:**
```bash
pip install django
pip install Pillow  # Rasmlar bilan ishlash uchun
```

4. **Migratsiyalarni bajaring:**
```bash
python manage.py migrate
```

5. **Media papkasini yarating:**
```bash
mkdir media
```

6. **Superuser yarating:**
```bash
python manage.py createsuperuser
```

7. **Serverni ishga tushiring:**
```bash
python manage.py runserver
```

8. **Brauzerda oching:**
```
http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/
```

## 📁 Loyiha strukturasi

```
organic-shop/
├── commerce/
│   ├── commerce/              # Loyiha sozlamalari
│   │   ├── settings.py       # Asosiy sozlamalar
│   │   ├── urls.py           # Root URL config
│   │   └── wsgi.py           # WSGI config
│   ├── shop/                 # Shop application
│   │   ├── models.py         # Ma'lumotlar modellari
│   │   ├── admin.py          # Admin konfiguratsiya
│   │   ├── views.py          # View funksiyalari
│   │   ├── urls.py           # URL routing
│   │   └── migrations/       # Database migrations
│   ├── media/                # Yuklangan fayllar
│   │   ├── menu/images/      # Department rasmlari
│   │   └── products/images/  # Mahsulot rasmlari
│   ├── templates/            # HTML shablonlar
│   ├── db.sqlite3           # Ma'lumotlar bazasi
│   └── manage.py            # Django management
└── README.md
```

## 🗄️ Ma'lumotlar bazasi modellari

### Departments
```python
- id (AutoField)
- name (CharField, max_length=150, unique)
- slug (SlugField, unique)
- image (ImageField, upload_to='menu/images/')
```

### AllCategories
```python
- id (AutoField)
- name (CharField, max_length=150, unique)
- slug (SlugField, unique)
- departments (ForeignKey → Departments)
```

### Category
```python
- id (AutoField)
- name (CharField, max_length=150, unique)
- slug (SlugField, unique)
- departments (ForeignKey → Departments)
- allcategories (ForeignKey → AllCategories, nullable)
```

### Product
```python
- id (AutoField)
- name (CharField, max_length=150, unique)
- descriptions (TextField)
- price (DecimalField, max_digits=10, decimal_places=3)
- quantity (IntegerField, default=15)
- discount (IntegerField, default=0)
- weight (DecimalField, max_digits=5, decimal_places=2)
- type_product (CharField, choices: kg/g/l/ml)
- slug (SlugField, unique)
- category (ForeignKey → Category)
```

### ProductImage
```python
- id (AutoField)
- image (ImageField, upload_to='products/images/')
- product (ForeignKey → Product)
```

## 🎯 Admin Panel Xususiyatlari

### Departments Admin
- Inline category editing
- Auto slug generation
- Image upload
- List display with custom fields

### Product Admin
- Multiple image upload (Inline)
- Image preview in list view
- Price, discount, quantity management
- Auto slug generation
- Category filtering

## 💡 Foydalanish

### Admin Panel orqali mahsulot qo'shish

1. Admin panelga kiring: `/admin/`
2. **Departments** yarating (bo'limlar)
3. **Categories** qo'shing
4. **Products** yarating:
   - Nomi, tavsif, narx kiriting
   - Kategoriyani tanlang
   - Og'irlik va o'lchov birligini belgilang
   - Rasmlarni yuklang (ProductImage inline)
5. Saqlang

### Kategoriya ierarxiyasi

```
Departments (Meva-sabzavot)
  ├── AllCategories (Organik mahsulotlar)
  │     ├── Category (Yangi mevalar)
  │     │     ├── Product (Organik olma)
  │     │     └── Product (Organik banan)
  │     └── Category (Sabzavotlar)
  │           ├── Product (Organik pomidor)
  │           └── Product (Organik bodring)
```

## 📈 Kelajakdagi yangilanishlar

- [ ] Frontend UI (React/Vue)
- [ ] Shopping Cart tizimi
- [ ] User authentication va registration
- [ ] Checkout va payment integration
- [ ] Order management tizimi
- [ ] Wishlist funksiyasi
- [ ] Product reviews va ratings
- [ ] Search va filtering
- [ ] Email notifications
- [ ] PostgreSQL'ga o'tish
- [ ] Redis caching
- [ ] RESTful API (DRF)
- [ ] Mobile app support
- [ ] Multi-language support
- [ ] Analytics dashboard
- [ ] Inventory management

## 🎨 Screenshot

```
Bu yerga loyihangizning screenshot'larini qo'shing:
- Admin panel
- Product list
- Category management
- Product detail
```

## 🤝 Hissa qo'shish

1. Fork qiling
2. Feature branch yarating (`git checkout -b feature/NewFeature`)
3. Commit qiling (`git commit -m 'Add new feature'`)
4. Push qiling (`git push origin feature/NewFeature`)
5. Pull Request oching

## 🐛 Muammolar

Xato topsangiz: [GitHub Issues](https://github.com/psix-coder/organic-shop/issues)

## 📝 Litsenziya

MIT License

## 👤 Muallif

**Psix Coder**
- GitHub: [@psix-coder](https://github.com/psix-coder)

## 🙏 Minnatdorchilik

- Django jamoasiga
- Pillow library
- Open-source jamiyatiga

---

<div align="center">

**⭐ Foydali bo'lsa, star qo'yishni unutmang! ⭐**

Made with ❤️ and Django by [Psix Coder](https://github.com/psix-coder)

🌿 **Organic Shop - Tabiiy mahsulotlar uchun zamonaviy platforma**

</div>
