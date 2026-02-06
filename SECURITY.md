# Security Design for Secure Todo App

## Overview
This app demonstrates real-world security in web apps, focusing on proactive threat hardening.

## Core Features
- **Authentication & Authorization**: Flask-Login for sessions, role-based access (RBAC). Users can't access admin routes without 'admin' role.
- **Hashing & Password Policies**: Bcrypt for salting/hashing. Passwords require 8+ chars, mixed case, numbers, specials.
- **Input Validation & Sanitization**: WTForms validators prevent invalid data. Bleach strips malicious HTML (XSS prevention).
- **Session Handling & Access Control**: Signed cookies, rate limiting (Flask-Limiter) for brute-force protection. Secure headers against XSS/clickjacking.

## Mitigated Threats
- XSS: Sanitization with Bleach.
- SQL Injection: SQLAlchemy parameterized queries.
- CSRF: WTForms built-in protection.
- Brute-Force: Login rate-limited to 5/min.
- Weak Auth: Strong password policies.

In production: Use HTTPS, monitor logs, scan with OWASP ZAP.