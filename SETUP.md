# Setup Guide - Vehicle Information & Diagnostics Platform

## Prerequisites

### System Requirements
- **OS**: Ubuntu 20.04+ / macOS 11+ / Windows 10+
- **CPU**: 2+ cores (4+ recommended)
- **RAM**: 4GB+ (8GB recommended)
- **Disk**: 50GB+ free space

### Required Software

1. **Docker & Docker Compose**
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install docker.io docker-compose
   
   # macOS (using Homebrew)
   brew install docker docker-compose
   
   # Verify installation
   docker --version
   docker-compose --version
   ```

2. **Python 3.11+** (for local development)
   ```bash
   python --version
   ```

3. **Flutter 3.0+** (for mobile development)
   ```bash
   flutter --version
   ```

4. **PostgreSQL Client** (optional, for direct DB access)
   ```bash
   psql --version
   ```

## Installation

### Option 1: Docker Compose (Recommended)

Most straightforward approach for development and testing.

#### Step 1: Clone Repository

```bash
git clone https://github.com/hed149405/Plakyab.git
cd Plakyab
```

#### Step 2: Environment Configuration

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your settings
nano .env
```

**Key Environment Variables**:

```env
# Backend
FASTAPI_ENV=development
FASTAPI_DEBUG=true
SECRET_KEY=your-super-secret-key-change-this
ALGORITHM=HS256

# Database
DATABASE_URL=postgresql://plakyab:plakyab_password@postgres:5432/plakyab
DATABASE_ECHO=true

# Redis
REDIS_URL=redis://redis:6379
REDIS_CACHE_TTL=3600

# API Keys (for authorized vehicle providers)
VEHICLE_API_KEY=your-api-key
VEHICLE_API_URL=https://api.official-provider.com

# JWT
JWT_EXPIRATION_HOURS=24
JWT_REFRESH_EXPIRATION_DAYS=7

# Cors
CORS_ORIGINS=http://localhost:3000,http://localhost:8080

# Logging
LOG_LEVEL=INFO
LOG_FILE=/app/logs/app.log
```

#### Step 3: Start Services

```bash
# Start all services in background
docker-compose up -d

# View logs
docker-compose logs -f

# View logs for specific service
docker-compose logs -f backend
```

#### Step 4: Initialize Database

```bash
# Run migrations
docker-compose exec backend alembic upgrade head

# Seed initial data (optional)
docker-compose exec backend python -m app.database.seeds
```

#### Step 5: Access Services

| Service | URL | Credentials |
|---------|-----|-------------|
| Frontend | http://localhost:3000 | - |
| Backend API | http://localhost:8000 | - |
| API Docs (Swagger) | http://localhost:8000/docs | - |
| API Docs (ReDoc) | http://localhost:8000/redoc | - |
| Database Admin | http://localhost:8081 | postgres/plakyab_password |

**Test Login Credentials** (after seeding):
```
Email: admin@plakyab.local
Password: admin123456
Role: Admin
```

### Option 2: Local Development

For development with hot reload and debugging.

#### Backend Setup

```bash
cd backend

# Create virtual environment
python3.11 -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Configure .env for local PostgreSQL
# DATABASE_URL=postgresql://plakyab:plakyab_password@localhost:5432/plakyab

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Backend Running**:
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

#### Frontend Setup

```bash
cd frontend

# Get dependencies
flutter pub get

# Run on connected device or emulator
flutter run

# Or run web version
flutter run -d chrome

# Build for release
flutter build apk      # Android
flutter build ios      # iOS
flutter build web      # Web
```

#### Database Setup (PostgreSQL)

If running PostgreSQL locally:

```bash
# Install PostgreSQL
# Ubuntu/Debian
sudo apt install postgresql postgresql-contrib

# macOS
brew install postgresql

# Start PostgreSQL service
sudo systemctl start postgresql  # Linux
brew services start postgresql   # macOS

# Create database and user
sudo -u postgres psql

CREATE DATABASE plakyab;
CREATE USER plakyab WITH PASSWORD 'plakyab_password';
ALTER ROLE plakyab SET client_encoding TO 'utf8';
ALTER ROLE plakyab SET default_transaction_isolation TO 'read committed';
ALTER ROLE plakyab SET default_transaction_deferrable TO on;
ALTER ROLE plakyab SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE plakyab TO plakyab;
\q
```

#### Redis Setup

```bash
# Install Redis
# Ubuntu/Debian
sudo apt install redis-server

# macOS
brew install redis

# Start Redis
sudo systemctl start redis-server  # Linux
brew services start redis          # macOS

# Verify Redis is running
redis-cli ping  # Should return PONG
```

## Configuration

### Backend Configuration

**File**: `backend/app/config.py`

```python
class Settings:
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/plakyab"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # JWT
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_HOURS: int = 24
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # API Configuration
    API_VERSION: str = "v1"
    API_TITLE: str = "Vehicle Information & Diagnostics Platform"
    API_DESCRIPTION: str = "..."
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "/app/logs/app.log"
    
    # CORS
    CORS_ORIGINS: list = ["http://localhost:3000"]
```

### Frontend Configuration

**File**: `frontend/lib/config/app_config.dart`

```dart
class AppConfig {
  static const String apiBaseUrl = 'http://localhost:8000/api/v1';
  static const String apiTimeout = Duration(seconds: 30);
  static const String appName = 'Plakyab';
  static const String appVersion = '1.0.0';
  
  // Feature flags
  static const bool enableOfflineMode = true;
  static const bool enablePushNotifications = true;
  static const bool enableAnalytics = true;
}
```

## Database Migrations

### Creating a New Migration

```bash
cd backend

# Auto-generate migration based on model changes
alembic revision --autogenerate -m "Add new_field to users table"

# Edit the migration file if needed
nano alembic/versions/xxxx_add_new_field_to_users_table.py

# Apply migration
alembic upgrade head
```

### Viewing Migration History

```bash
alembic history
alembic current
```

## Testing

### Backend Testing

```bash
cd backend

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/unit/test_vin_decoder.py

# Run specific test function
pytest tests/unit/test_vin_decoder.py::test_valid_vin_format

# Run with coverage
pytest --cov=app tests/

# Generate coverage report
pytest --cov=app --cov-report=html tests/
```

### Frontend Testing

```bash
cd frontend

# Run all tests
flutter test

# Run with coverage
flutter test --coverage

# Run specific test file
flutter test test/unit/validators_test.dart
```

## Docker Operations

### Docker Compose Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f backend

# Execute command in container
docker-compose exec backend bash

# Rebuild images
docker-compose build

# Remove all containers, networks, volumes
docker-compose down -v
```

### Container Operations

```bash
# List running containers
docker ps

# Stop container
docker stop <container_id>

# Start container
docker start <container_id>

# View container logs
docker logs -f <container_id>

# Execute command in container
docker exec -it <container_id> bash
```

## Troubleshooting

### Issue: Port Already in Use

```bash
# Find process using port
lsof -i :8000

# Kill process
kill -9 <PID>

# Or change port in .env
FASTAPI_PORT=8001
```

### Issue: Database Connection Failed

```bash
# Check PostgreSQL is running
sudo systemctl status postgresql

# Check database credentials in .env
cat .env | grep DATABASE_URL

# Test connection
psql -U plakyab -h localhost -d plakyab -c "SELECT 1"
```

### Issue: Redis Connection Failed

```bash
# Check Redis is running
redis-cli ping

# Check Redis configuration in .env
cat .env | grep REDIS_URL
```

### Issue: Docker Build Fails

```bash
# Clear Docker cache
docker system prune

# Rebuild without cache
docker-compose build --no-cache
```

### Issue: Permission Denied

```bash
# Add user to docker group (Linux)
sudo usermod -aG docker $USER
newgrp docker
```

## Development Workflow

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/vehicle-search

# Make changes
git add .
git commit -m "feat: implement vehicle search endpoint"

# Push to GitHub
git push origin feature/vehicle-search

# Create Pull Request
# (On GitHub)
```

### Code Style

#### Backend (Python)

```bash
cd backend

# Format code
black app/

# Check style
flake8 app/

# Sort imports
isort app/
```

#### Frontend (Dart)

```bash
cd frontend

# Format code
dart format lib/ test/

# Analyze code
dart analyze

# Check for issues
flutter analyze
```

## Production Deployment

### Using Production Compose File

```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Environment Variables for Production

Create `.env.production`:

```env
FASTAPI_ENV=production
FASTAPI_DEBUG=false
SECRET_KEY=<secure-random-key>
DATABASE_URL=postgresql://user:pass@prod-db-host:5432/plakyab
REDIS_URL=redis://prod-redis-host:6379
ALLOWED_HOSTS=example.com,www.example.com
```

### Health Checks

```bash
# Check backend health
curl http://localhost:8000/health

# Check database
curl http://localhost:8000/health/db

# Check redis
curl http://localhost:8000/health/cache
```

## Getting Help

- **Documentation**: See [README.md](./README.md)
- **Architecture**: See [ARCHITECTURE.md](./ARCHITECTURE.md)
- **API Docs**: http://localhost:8000/docs
- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions

---

**Last Updated**: 2026-07-25
