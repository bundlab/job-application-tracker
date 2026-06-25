# Job Application Tracker 🚀

Modern full-stack application to track job applications, interviews, offers and follow-ups.

Clean architecture • FastAPI backend • React frontend • PostgreSQL • Docker-ready

<p align="center">
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Frontend-React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Container-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/ORM-SQLModel-007ACC?style=for-the-badge&logoColor=white" alt="SQLModel" />
</p>

## ✨ Features

- 🔐 Authentication (JWT + refresh tokens)
- 📝 Create, update, archive job applications
- 🏷️ Status tracking (Applied → Interviewing → Offer → Rejected → Ghosted 💀)
- 📅 Interview scheduling & reminders
- 🔍 Company & job board search / autocomplete
- 📊 Simple dashboard & statistics
- 🌙 Dark / Light mode support
- 📱 Mobile responsive design
- 🐳 Docker + docker-compose for local development

## 📁 Project Structure

```text
job-application-tracker/
├── backend/                    # FastAPI application
│   ├── app/
│   │   ├── api/               # API routers
│   │   ├── core/              # settings, security, dependencies
│   │   ├── crud/              # database operations
│   │   ├── models/            # SQLModel database models
│   │   ├── schemas/           # Pydantic request/response models
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/                   # React + Vite
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── types/
│   │   └── main.tsx
│   ├── public/
│   ├── vite.config.ts
│   └── Dockerfile             # optional (for static hosting)
├── docker-compose.yml
├── .github/workflows/          # CI/CD pipelines
├── .env.example
├── README.md
└── .gitignore
```
## 📜 License
MIT License


## 👨‍💻 Author
Abdullahi Bundi


## ⭐ Support
If you like this project:
* ⭐ Star the repository
* 🍴 Fork the project
* 🛠 Contribute improvements

## 📢 Project Status
🚧 **Active Development**

More features and improvements coming soon.