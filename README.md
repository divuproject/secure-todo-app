# Secure Web Application & Threat Hardening

![Secure Todo App - Home Page](screenshots/home-light.png)  
*(Light & Dark mode + Todo list)*

## Project Overview

This project demonstrates how to build a **secure web application** from scratch — focusing on **real security implementation** instead of just scanning for vulnerabilities.

**Main Goal**  
Cybersecurity is **not only about finding bugs** — it is about **proactively designing and coding** applications to resist common attacks.

**Built during**  
Cryptonic Area Virtual Internship Program

## Core Security Features Implemented

| # | Security Aspect                        | How it is implemented                                      | Threat Mitigated                          | File(s)                     |
|---|----------------------------------------|------------------------------------------------------------|-------------------------------------------|-----------------------------|
| 1 | Authentication & Authorization Flow    | Flask-Login + Role-Based Access Control (user / admin)     | Unauthorized access, privilege escalation | routes.py, models.py        |
| 2 | Hashing & Password Policies            | Bcrypt hashing + complexity regex (upper, lower, digit, special) | Credential stuffing, rainbow tables       | models.py, forms.py         |
| 3 | Input Validation & Sanitization        | WTForms validators + Bleach HTML sanitization              | XSS, SQL injection, form tampering        | forms.py, utils.py, routes.py |
| 4 | Session Handling & Access Control      | Signed cookies, rate limiting (Flask-Limiter), secure headers | Session hijacking, brute-force, CSRF      | app.py, routes.py           |
## Tech Stack

- **Backend** → Python + Flask  
- **Database** → SQLite (Flask-SQLAlchemy)  
- **Security libraries** → Flask-Login, Flask-Bcrypt, Flask-WTF, Flask-Limiter, Bleach  
- **Frontend** → Bootstrap 5 + Font Awesome + custom dark/light theme toggle

## Folder Structure
secure_todo_app/
├── app.py                    # Main application entry
├── config.py                 # Configuration & secrets
├── models.py                 # User & Todo database models
├── forms.py                  # Registration, Login, Todo forms
├── routes.py                 # All URL routes & logic
├── utils.py                  # Input sanitization helper
├── templates/                # HTML templates
│   ├── base.html             # Main layout + navbar
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   ├── admin.html
├── static/
│   ├── css/
│   │   ├── bootstrap.min.css
│   │   └── custom.css
│   └── js/
│       ├── bootstrap.bundle.min.js
│       └── custom.js
├── requirements.txt
├── .gitignore
├── .env.example              # Template for .env file
└── screenshots/              # Project images
text## How to Run Locally

1. Clone the repository

```bash
git clone https://github.com/«your-github-username»/secure-todo-app.git
cd secure-todo-app

Create & activate virtual environment

Bash# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

Install dependencies

Bashpip install -r requirements.txt

Create .env file (copy from .env.example if present)

textSECRET_KEY=«paste-a-very-long-random-string-here»
(You can generate one with: python -c "import secrets; print(secrets.token_hex(32))")

Run the application

Bashpython app.py

Open in browser → http://127.0.0.1:5000

Screenshots
Register PageLogin PageHome - Light ModeHome - Dark ModeAdmin Panel
(Add these images in a folder called screenshots/ before pushing)
What I Learned
During the Cryptonic Area Virtual Internship, I gained hands-on experience in:

Implementing secure authentication & session management using Flask-Login
Using Bcrypt for proper password storage and enforcing strong password rules
Preventing XSS attacks with input validation (WTForms) + sanitization (Bleach)
Adding rate limiting and security headers to make the application more resilient
Applying least privilege principle with role-based access control
Writing clean, professional GitHub documentation for real-world projects

This internship helped me understand secure-by-design thinking — not just finding vulnerabilities, but preventing them from the beginning.
Author

Name: Divya Hirpara
Location: Ahmedabad, Gujarat, India
GitHub: https://github.com/«divuproject»


Built with dedication during Cryptonic Area Virtual Internship Program
Date: February 2026
Test
