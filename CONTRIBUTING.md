Markdown
# Contributing to FastAPI Job Application Tracker 🚀

First off, thank you for taking the time to contribute! Contributions from the community make this tool better for everyone trying to land their next tech role.

## 🛠️ Local Development Setup

This project uses a backend powered by **FastAPI + SQLModel**, a frontend built with **Vite + React + TypeScript**, and infra handled via **Docker Compose** for PostgreSQL.

### Prerequisites
- Docker & Docker Compose
- Python 3.11+
- Node.js (v18+)

### Step-by-Step Installation

1. **Fork and Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/job-application-tracker.git](https://github.com/YOUR_USERNAME/job-application-tracker.git)
   cd job-application-tracker
2. Spin Up Infrastructure (Database):

   ```Bash
   docker-compose up -d
3. Set Up the Backend:
   ```Bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
4. Set Up the Frontend:
   ```Bash
   cd ../frontend
   npm install
   npm run dev
### Development Guidelines

- *Backend:* Follow PEP 8 style guidelines. Use type hints and ensure all new code is properly tested.
- *Frontend:* Maintain consistent TypeScript usage and follow the existing component structure.
- *Database:* All changes should be made via SQLModel models and Alembic migrations where appropriate.
- *Testing:* Add or update tests for any new features or bug fixes.

### Making Changes

1. Create a new branch for your feature or bugfix:
   ```Bash
   git checkout -b feature/your-feature-name
2. Make your changes and commit them using clear, descriptive commit messages.
3. Push your branch and open a *Pull Request* on GitHub.


### Reporting Issues

- Use the GitHub Issues tab to report bugs or suggest new features.
- Provide as much detail as possible, including steps to reproduce, screenshots, and environment information.


### Code of Conduct

By participating in this project, you agree to uphold our Code of Conduct — we expect respectful and inclusive communication at all times.

**Once again, thank you for contributing!** Together we're building a better tool to help people land their dream jobs.

Happy coding! 💼✨