Knowella CSV Processor:

A Django-based backend system that allows users to upload CSV/Excel files, process structured data, validate entries, and store them into a database with duplicate handling.

Features:

Upload CSV or Excel files

Automatic data parsing using Pandas

Stores structured data into SQLite database

Duplicate email protection

Simple and clean Django architecture

🛠 Tech Stack

Python 3.12

Django 6

Pandas

SQLite

HTML

📂 Project Structure
data_processor/
│
├── uploader/          # File upload and processing logic
├── templates/         # HTML templates
├── db.sqlite3         # Database
└── manage.py

⚙️ How to Run Locally

Clone the repository:

git clone <repo_link>


Create virtual environment:

python -m venv venv


Activate environment:

venv\Scripts\activate


Install dependencies:

pip install django pandas openpyxl


Run migrations:

python manage.py migrate


Start server:

python manage.py runserver
