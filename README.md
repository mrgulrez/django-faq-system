# Django FAQ System 📖  
A Django-based FAQ management system with **WYSIWYG editor support, multilingual translations, caching, and REST APIs**.

## 🚀 Features  
✔️ Rich-text FAQ support using CKEditor  
✔️ Automatic **multilingual translations** (Hindi, Bengali, etc.)  
✔️ **Fast API** with **caching** using Redis  
✔️ **Admin panel** for easy management  
✔️ **Unit tests** for reliability  
✔️ **Docker support** (Bonus)
```

---

### **📌 Installation Instructions**  
```markdown
## 🔧 Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/mrgulrez/django-faq-system.git  
```

### 2️⃣ Create a Virtual Environment  
```bash
python -m venv env  
source env/bin/activate  # For macOS/Linux  
env\Scripts\activate     # For Windows  
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt  
```

### 4️⃣ Set Up Database  
```bash
python manage.py migrate  
```

### 5️⃣ Run the Server  
```bash
python manage.py runserver  
```

🚀 Your FAQ system is now running at `http://127.0.0.1:8000/` 🎉  
```

---

### **📌 API Usage**  
```markdown
## 🌐 API Endpoints  

### 🔍 Fetch All FAQs (Default: English)  
```bash
curl http://localhost:8000/api/faqs/
```

### 🌍 Fetch FAQs in Hindi  
```bash
curl http://localhost:8000/api/faqs/?lang=hi
```

### 🌍 Fetch FAQs in Bengali  
```bash
curl http://localhost:8000/api/faqs/?lang=bn
```
```

---

### **📌 Running Tests**  
```markdown
## 🧪 Running Tests  
```bash
pytest  
```
✔️ Ensures translation, caching, and API functionality  
✔️ Confirms **high code quality**  
```



---

### **📌 Git Commit Message Convention**  
```markdown
## 📌 Git Best Practices  
- `feat:` Adds a new feature  
- `fix:` Fixes a bug  
- `docs:` Updates documentation  
- `test:` Adds or improves tests  
- `refactor:` Improves code without changing functionality  
