# 🚗 Vehicle Information & Diagnostics Platform

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Flutter 3.0+](https://img.shields.io/badge/Flutter-3.0+-blue.svg)](https://flutter.dev/)
[![Docker](https://img.shields.io/badge/Docker-Latest-blue.svg)](https://www.docker.com/)

A comprehensive enterprise-grade platform for vehicle information management, diagnostics, and VIN decoding built with Flutter, FastAPI, and PostgreSQL.

## 🌟 Features

### Authentication & Security
- ✅ JWT-based authentication with refresh tokens
- ✅ Role-based access control (Admin, Technician, User)
- ✅ Multi-factor authentication support
- ✅ Secure password hashing with bcrypt
- ✅ OAuth2 provider support

### Vehicle Management
- ✅ VIN decoding with ISO 3779 validation
- ✅ Comprehensive vehicle search (VIN, Plate, Engine, Chassis)
- ✅ Vehicle details and specifications
- ✅ Service history tracking
- ✅ Maintenance schedules
- ✅ Multiple vehicle management

### Admin Dashboard
- ✅ User management
- ✅ Vehicle inventory management
- ✅ Analytics and reporting
- ✅ System health monitoring
- ✅ Role and permissions management

### Mobile Application (Flutter)
- ✅ Material Design 3 UI
- ✅ Dark mode support
- ✅ Offline caching with SQLite
- ✅ Push notifications
- ✅ Multi-language support (English, Arabic, French, Spanish)
- ✅ Responsive design for all screen sizes

### Backend API
- ✅ RESTful API with versioning (v1, v2)
- ✅ Swagger/OpenAPI documentation
- ✅ Comprehensive error handling
- ✅ Structured logging
- ✅ Rate limiting and throttling
- ✅ Caching layer with Redis

### Database
- ✅ PostgreSQL with advanced features
- ✅ Optimized indexes and queries
- ✅ Automated migrations
- ✅ Transaction support
- ✅ Audit logging

### DevOps
- ✅ Docker & Docker Compose
- ✅ GitHub Actions CI/CD pipeline
- ✅ Automated testing (Unit & Integration)
- ✅ Code coverage reporting
- ✅ Nginx reverse proxy configuration

## 📋 Project Structure

```
vehicle-diagnostics-platform/
├── backend/
├── frontend/
├── database/
├── docker-compose.yml
├── nginx/
├── .github/workflows/
└── docs/
```

## 🚀 Quick Start

### Using Docker Compose

```bash
git clone https://github.com/hed149405/Plakyab.git
cd Plakyab
cp .env.example .env
docker-compose up -d
```

Access services:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs
- Admin: http://localhost:8000/admin

## 📚 Documentation

- [ARCHITECTURE.md](./ARCHITECTURE.md) - System architecture
- [SETUP.md](./SETUP.md) - Setup guide
- [API_DOCUMENTATION.md](./API_DOCUMENTATION.md) - API reference
- [CONTRIBUTING.md](./CONTRIBUTING.md) - Contribution guidelines

## 🔐 Security

- JWT authentication
- Bcrypt password hashing
- Rate limiting
- CORS protection
- SQL injection prevention
- Audit logging

## 🧪 Testing

```bash
# Backend tests
cd backend && pytest --cov=app tests/

# Frontend tests
cd frontend && flutter test --coverage
```

## 🌐 Supported Languages

- 🇬🇧 English
- 🇸🇦 Arabic
- 🇫🇷 French
- 🇪🇸 Spanish

## 📝 License

GNU General Public License v3.0 - See [LICENSE](./LICENSE) file

## 👥 Support

For support, create a GitHub issue with detailed information.

---

**Built with ❤️ for vehicle management excellence**
