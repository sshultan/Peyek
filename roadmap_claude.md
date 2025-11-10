# 🐍 Roadmap Python 2 Minggu (Fundamental) + Persiapan Spesialisasi

## 📅 MINGGU 1: Python Basics

### **Hari 1-2: Setup & Dasar-dasar**
**Target: Bisa menulis dan menjalankan program Python pertama**

**Materi:**
- Install Python (versi 3.10+) & VS Code
- Setup virtual environment
- Print, input, komentar
- Variabel & tipe data (int, float, string, boolean)
- Operasi matematika dasar
- String manipulation (concatenation, formatting)

**Praktek:**
```python
# Project: Kalkulator Sederhana
# Buat program yang bisa +, -, *, /
```

**Resource:**
- Tutorial: Python.org Getting Started
- Video: Tutorial Python Bahasa Indonesia di YouTube

---

### **Hari 3-4: Control Flow**
**Target: Bisa membuat program dengan logika keputusan**

**Materi:**
- If, elif, else
- Comparison operators (==, !=, >, <, >=, <=)
- Logical operators (and, or, not)
- Loops: for loop
- Loops: while loop
- Break & continue

**Praktek:**
```python
# Project 1: Game Tebak Angka
# Program random angka 1-100, user tebak, kasih hint

# Project 2: Validasi Password
# Cek password minimal 8 karakter, ada angka & huruf besar
```

**Resource:**
- W3Schools Python Conditions
- Real Python: Control Flow

---

### **Hari 5-6: Data Structures**
**Target: Menguasai struktur data Python**

**Materi:**
- Lists (create, index, slice, methods)
- Tuples (immutable sequences)
- Dictionaries (key-value pairs)
- Sets (unique collections)
- List comprehensions
- Nested data structures

**Praktek:**
```python
# Project: Contact Book
# Simpan nama, nomor HP, email
# Fitur: tambah, hapus, cari, tampilkan semua kontak
```

**Resource:**
- Python Data Structures Documentation
- Corey Schafer: Python Lists, Tuples, Sets

---

### **Hari 7: Functions**
**Target: Membuat kode yang reusable**

**Materi:**
- Defining functions (def)
- Parameters & arguments
- Return values
- Default parameters
- *args & **kwargs
- Lambda functions
- Scope (local vs global)

**Praktek:**
```python
# Project: Program Konversi Suhu
# Functions untuk konversi: Celsius, Fahrenheit, Kelvin
# Menu pilihan konversi

# Bonus: Buat function untuk validasi input
```

---

## 📅 MINGGU 2: Intermediate Python

### **Hari 8-9: File Handling & Error Handling**
**Target: Bekerja dengan files dan handle errors**

**Materi:**
- Reading files (open, read, readline, readlines)
- Writing files (write, append)
- Context managers (with statement)
- Try, except, finally
- Raising exceptions
- Working with CSV files
- Working with JSON files

**Praktek:**
```python
# Project: To-Do List App dengan File Storage
# Fitur:
# - Tambah task (simpan ke file)
# - Lihat semua tasks
# - Tandai task selesai
# - Hapus task
# - Data persisten di file txt/json
```

**Resource:**
- Real Python: File Handling
- Python JSON module documentation

---

### **Hari 10-11: Object-Oriented Programming (OOP)**
**Target: Memahami konsep OOP**

**Materi:**
- Classes & Objects
- Attributes & Methods
- __init__ constructor
- Inheritance
- Encapsulation
- Polymorphism
- Magic methods (__str__, __repr__)

**Praktek:**
```python
# Project: Bank Account System
# Class: BankAccount
# Attributes: account_number, balance, owner
# Methods: deposit, withdraw, check_balance
# Bonus: Buat class SavingsAccount (inheritance) dengan bunga
```

**Resource:**
- Corey Schafer: OOP Tutorial
- Real Python: OOP in Python

---

### **Hari 12: Modules & Packages**
**Target: Organize code dan gunakan library**

**Materi:**
- Import statements
- Creating modules
- Python standard library (os, sys, datetime, random, math)
- Installing packages (pip)
- Popular packages introduction

**Praktek:**
```python
# Project: Expense Tracker
# Module terpisah untuk:
# - data_handler.py (baca/tulis file)
# - calculator.py (hitung total, rata-rata)
# - main.py (menu utama)

# Gunakan datetime untuk timestamp
```

---

### **Hari 13-14: Mini Project & Review**
**Target: Consolidate learning dengan project lengkap**

**Pilih salah satu project:**

**Option 1: Student Management System**
- CRUD students (Create, Read, Update, Delete)
- Simpan data ke file JSON
- Fitur: tambah siswa, edit, hapus, cari, lihat semua
- Hitung rata-rata nilai

**Option 2: Simple CLI Game (Snake atau Hangman)**
- Gunakan library seperti `random`
- Scoreboard dengan file storage
- Clean code dengan functions

**Option 3: Web Scraper Sederhana**
- Install `requests` & `beautifulsoup4`
- Scrape data dari website sederhana
- Simpan hasil ke CSV

---

## 🎯 EVALUASI AKHIR MINGGU 2

### **Checklist Skill yang Harus Dikuasai:**
- ✅ Bisa menulis program dengan sintaks yang benar
- ✅ Paham control flow (if/else, loops)
- ✅ Comfortable dengan data structures (list, dict)
- ✅ Bisa membuat dan menggunakan functions
- ✅ Paham basic OOP
- ✅ Bisa baca/tulis file
- ✅ Handle errors dengan try/except
- ✅ Organize code dengan modules

### **Test Diri Sendiri:**
Bikin program sederhana tanpa lihat tutorial:
- Input/output
- Validation
- Data storage (file)
- Functions
- Error handling

---

## 🚀 PERSIAPAN SPESIALISASI (Setelah 2 Minggu)

Setelah fundamental kuat, pilih jalur spesialisasi:

### **1️⃣ Web Development (Backend)**
**Timeline: 2-3 bulan**

**Roadmap:**
- **Minggu 1-2:** Flask/FastAPI basics
  - Routing, templates, forms
  - REST API basics
- **Minggu 3-4:** Database integration
  - SQLAlchemy ORM
  - PostgreSQL/MySQL
- **Minggu 5-6:** Authentication & Authorization
  - JWT tokens
  - User sessions
- **Minggu 7-8:** Deployment
  - Docker basics
  - Deploy ke Heroku/Railway
- **Minggu 9-12:** Django framework (optional)
  - Admin panel
  - Django ORM
  - Full web app

**Project Ideas:**
- Blog platform
- REST API untuk mobile app
- E-commerce backend

**Key Libraries:**
- Flask / FastAPI / Django
- SQLAlchemy
- Requests
- pytest

---

### **2️⃣ Data Science & Machine Learning**
**Timeline: 3-4 bulan**

**Roadmap:**
- **Minggu 1-3:** Data Analysis
  - NumPy (array operations)
  - Pandas (data manipulation)
  - Matplotlib & Seaborn (visualisasi)
- **Minggu 4-6:** Statistics & Math
  - Probability
  - Statistical analysis
  - Linear algebra basics
- **Minggu 7-10:** Machine Learning
  - Scikit-learn
  - Supervised learning (regression, classification)
  - Unsupervised learning (clustering)
- **Minggu 11-12:** Deep Learning intro
  - TensorFlow/PyTorch basics
  - Neural networks
- **Minggu 13-16:** Projects & Portfolio

**Project Ideas:**
- Exploratory Data Analysis (EDA)
- Predictive model (house prices)
- Image classification
- Sentiment analysis

**Key Libraries:**
- NumPy, Pandas, Matplotlib
- Scikit-learn
- TensorFlow / PyTorch
- Jupyter Notebook

---

### **3️⃣ Automation & Scripting**
**Timeline: 1-2 bulan**

**Roadmap:**
- **Minggu 1-2:** File & System Automation
  - os, shutil, pathlib
  - Automated file organization
  - Schedule tasks (schedule library)
- **Minggu 3-4:** Web Automation
  - Selenium (browser automation)
  - Web scraping (BeautifulSoup, Scrapy)
- **Minggu 5-6:** API Integration
  - Working with REST APIs
  - Automate workflows (Notion, Google Sheets)
- **Minggu 7-8:** Advanced Projects
  - Bot automation
  - Data pipelines

**Project Ideas:**
- Auto-organize downloads folder
- Instagram bot (dengan etika!)
- Daily report generator
- Price monitoring tool

**Key Libraries:**
- Selenium
- BeautifulSoup / Scrapy
- Requests
- schedule / APScheduler

---

### **4️⃣ DevOps & Cloud**
**Timeline: 2-3 bulan**

**Roadmap:**
- **Minggu 1-2:** Linux & Shell
  - Basic Linux commands
  - Bash scripting
- **Minggu 3-4:** Version Control Advanced
  - Git workflows
  - GitHub Actions basics
- **Minggu 5-6:** Containerization
  - Docker
  - Docker Compose
- **Minggu 7-8:** CI/CD
  - GitHub Actions
  - Testing automation
- **Minggu 9-12:** Cloud Platforms
  - AWS/GCP basics
  - Infrastructure as Code (Terraform basics)

**Project Ideas:**
- Automated deployment pipeline
- Containerized web app
- Monitoring dashboard

**Key Tools:**
- Docker
- Git & GitHub Actions
- AWS/GCP/Azure
- Terraform

---

### **5️⃣ Software Testing / QA Automation**
**Timeline: 1-2 bulan**

**Roadmap:**
- **Minggu 1-2:** Unit Testing
  - pytest framework
  - Test coverage
  - Mocking
- **Minggu 3-4:** Integration & E2E Testing
  - Selenium WebDriver
  - API testing (Requests + pytest)
- **Minggu 5-6:** Test Automation Framework
  - Page Object Model
  - Test reporting
- **Minggu 7-8:** Performance Testing
  - Load testing basics (Locust)

**Key Libraries:**
- pytest
- unittest
- Selenium
- Requests

---

## 📚 Resources Recommended

### **Platform Belajar:**
- **Free:**
  - FreeCodeCamp (YouTube)
  - Real Python (articles)
  - W3Schools
  - Python.org documentation
  
- **Berbayar (worth it):**
  - Udemy courses (tunggu diskon $10-15)
  - DataCamp (untuk Data Science)
  - Codecademy Pro

### **Praktek Coding:**
- LeetCode (algoritma)
- HackerRank (Python track)
- Codewars (game-like)
- Project Euler (math + programming)

### **Komunitas:**
- r/learnpython (Reddit)
- Python Indonesia (Telegram/Discord)
- Stack Overflow

---

## 💡 Tips Sukses

1. **Konsisten > Intensitas** - Lebih baik 1 jam setiap hari daripada 10 jam weekend doang
2. **Type, don't copy-paste** - Muscle memory penting!
3. **Debug sendiri dulu** - Jangan langsung tanya, coba solve 15 menit dulu
4. **Build projects** - Portfolio > Sertifikat
5. **Read other's code** - Belajar dari GitHub repos
6. **Join komunitas** - Networking & support system
7. **Document your learning** - Blog atau GitHub README

---

## 🎓 Setelah Spesialisasi

1. **Build Portfolio** (3-5 projects)
2. **Contribute to Open Source**
3. **Write Technical Blog**
4. **Apply for Jobs/Freelance**
5. **Never Stop Learning**

---

**Good luck! Konsistensi adalah kunci. You got this! 💪🐍**