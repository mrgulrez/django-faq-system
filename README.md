
# Django FAQ System 📖  
A Django-based FAQ management system with **WYSIWYG editor support, multilingual translations, caching, and REST APIs**.

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Start the server: `python manage.py runserver`.

## API Usage
- Fetch FAQs in English: `curl http://localhost:8000/api/faqs/`
- Fetch FAQs in Hindi: `curl http://localhost:8000/api/faqs/?lang=hi`

## Contribution Guidelines
- Fork the repository.
- Create a new branch for your feature.
- Submit a pull request.

