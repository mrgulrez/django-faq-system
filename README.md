# FAQ Project

This is a Django-based backend application for managing FAQs with multilingual support. It includes a REST API for fetching FAQs in different languages, a WYSIWYG editor for formatting answers, and automatic translation using Google Translate.

---

## **Features**
- **Multilingual FAQs**: Store and retrieve FAQs in multiple languages (e.g., English, Hindi, Bengali).
- **WYSIWYG Editor**: Use CKEditor for rich text formatting of answers.
- **REST API**: Fetch FAQs with language support via query parameters.
- **Automatic Translation**: Automatically translate FAQs into other languages during creation.
- **Caching**: Use Redis to cache translations for improved performance.
- **Admin Panel**: Manage FAQs through a user-friendly Django admin interface.


## **Installation**

### **Prerequisites**
- Python 3.9 or higher
- Redis (for caching)
- Docker (optional)

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/faq_project.git
   cd faq_project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser for the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

## **Running the Project**
1. Start Redis (required for caching):
   ```bash
   redis-server
   ```

2. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

3. Access the application at `http://127.0.0.1:8000/`.

---

## **API Usage**

### **Endpoints**
- **Fetch FAQs**: `GET /api/faqs/`
  - Query Parameters:
    - `lang`: Language code (e.g., `en`, `hi`, `bn`). Defaults to English (`en`).

### **Examples**
1. Fetch FAQs in English (default):
   ```bash
   curl http://127.0.0.1:8000/api/faqs/
   ```

2. Fetch FAQs in Hindi:
   ```bash
   curl http://127.0.0.1:8000/api/faqs/?lang=hi
   ```

3. Fetch FAQs in Bengali:
   ```bash
   curl http://127.0.0.1:8000/api/faqs/?lang=bn
   ```

### **Sample Response**
```json
[
    {
        "id": 1,
        "question": "What is Django?",
        "answer": "Django is a web framework.",
        "question_hi": "डजांगो क्या है?",
        "answer_hi": "डजांगो एक वेब फ्रेमवर्क है।",
        "question_bn": "ডjango কি?",
        "answer_bn": "ডjango একটি ওয়েব ফ্রেমওয়ার্ক।"
    }
]
```

---

## **Testing**

### **Running Unit Tests**
1. Install testing dependencies:
   ```bash
   pip install pytest pytest-django
   ```

2. Run tests:
   ```bash
   pytest
   ```

### **Testing API Endpoints**
1. Use `curl` or Postman to test the API endpoints.
2. Verify responses for different languages.

---

## **Admin Panel**
1. Access the admin panel at `http://127.0.0.1:8000/admin/`.
2. Log in with your superuser credentials.
3. Add, edit, or delete FAQs through the user-friendly interface.

---

## **Caching**
- Redis is used to cache translations for improved performance.
- Ensure Redis is running:
  ```bash
  redis-server
  ```

- Verify caching by accessing the API multiple times and checking response times.

---

## **Translation**
- Translations are automatically generated using the `googletrans` library.
- Supported languages: English (`en`), Hindi (`hi`), Bengali (`bn`).
- Fallback to English if translation fails.

---

## **Docker Support**

### **Run with Docker**
1. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

2. Access the application at `http://localhost:8000/`.

### **Docker Compose File**
```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - redis
  redis:
    image: redis:latest
```

---

## **Contributing**
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "feat: Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.



## **Acknowledgements**
- Django: https://www.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- CKEditor: https://ckeditor.com/
- Redis: https://redis.io/
- Google Translate API: https://pypi.org/project/googletrans/
