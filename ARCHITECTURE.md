# Architecture Documentation

## System Overview

The Vehicle Information & Diagnostics Platform follows **Clean Architecture** principles with clear separation of concerns across multiple layers.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Presentation Layer                        │
│  ┌──────────────────┐        ┌──────────────────────────┐  │
│  │  Flutter Mobile  │        │   Admin Web Dashboard    │  │
│  └──────────────────┘        └──────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  Application Layer (API)                     │
│  FastAPI Endpoints (v1, v2) with Versioning               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  /api/v1/auth  │ /api/v1/vehicles │ /api/v1/admin  │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    Middleware Layer                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │ JWT Auth     │  │Error Handler │  │   Logging    │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   Service Layer                              │
│  ┌─────────────────┐  ┌─────────────────┐                 │
│  │ VehicleProvider │  │  VINDecoder     │                 │
│  │ (Authorized API │  │  (ISO 3779)     │                 │
│  │  Integration)   │  │  (Validation)   │                 │
│  └─────────────────┘  └─────────────────┘                 │
│  ┌─────────────────┐  ┌─────────────────┐                 │
│  │ AuthService     │  │ CacheService    │                 │
│  └─────────────────┘  └─────────────────┘                 │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                 Repository Pattern Layer                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   Vehicle    │  │     User     │  │    Audit     │    │
│  │  Repository  │  │  Repository  │  │  Repository  │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    Data Access Layer                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         SQLAlchemy ORM Models & Schemas             │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    Persistence Layer                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │  PostgreSQL  │  │    Redis     │  │    SQLite    │    │
│  │   Database   │  │    Cache     │  │ (Offline)    │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Architectural Patterns

### 1. Clean Architecture Principles

```
┌─────────────────────────────┐
│   ENTITIES (Core Rules)     │
│   ┌─────────────────────┐   │
│   │  Vehicle Entity     │   │
│   │  User Entity        │   │
│   │  Role Entity        │   │
│   └─────────────────────┘   │
└─────────────────────────────┘
          ↑
┌─────────────────────────────┐
│  USE CASES (Business Logic) │
│  ┌─────────────────────┐   │
│  │  Search Vehicle     │   │
│  │  Decode VIN         │   │
│  │  Authenticate User  │   │
│   └─────────────────────┘   │
└─────────────────────────────┘
          ↑
┌─────────────────────────────┐
│  INTERFACE ADAPTERS         │
│  ┌─────────────────────┐   │
│  │  Controllers        │   │
│  │  Gateways           │   │
│  │  Presenters         │   │
│  └─────────────────────┘   │
└─────────────────────────────┘
          ↑
┌─────────────────────────────┐
│  FRAMEWORKS & DRIVERS       │
│  ┌─────────────────────┐   │
│  │  Web (FastAPI)      │   │
│  │  DB (PostgreSQL)    │   │
│  │  Cache (Redis)      │   │
│  └─────────────────────┘   │
└─────────────────────────────┘
```

### 2. Repository Pattern

The repository pattern abstracts data access logic:

```python
# Interface
class IVehicleRepository(ABC):
    @abstractmethod
    async def get_by_vin(self, vin: str) -> Optional[Vehicle]:
        pass

# Implementation
class VehicleRepository(IVehicleRepository):
    def __init__(self, db: Session):
        self.db = db
    
    async def get_by_vin(self, vin: str) -> Optional[Vehicle]:
        return self.db.query(VehicleModel).filter(
            VehicleModel.vin == vin
        ).first()
```

### 3. Dependency Injection

Dependencies are injected at the endpoint level:

```python
@router.get("/vehicles/search")
async def search_vehicles(
    query: str,
    vehicle_repo: IVehicleRepository = Depends(get_vehicle_repo),
    cache_service: CacheService = Depends(get_cache_service)
):
    # Endpoint logic
    pass
```

## Backend Layer Details

### API Layer (Presentation)

**File**: `backend/app/api/v1/vehicles.py`

Responsibilities:
- Handle HTTP requests/responses
- Request validation
- Response serialization
- Error handling

### Service Layer (Business Logic)

**File**: `backend/app/services/vehicle_provider.py`

Responsibilities:
- Business logic implementation
- External API integration (authorized sources only)
- Data transformation
- Validation rules

### Repository Layer (Data Access)

**File**: `backend/app/repositories/vehicle_repository.py`

Responsibilities:
- Database queries
- Data persistence
- Transaction management
- Query optimization

### Model Layer (Data Structure)

**File**: `backend/app/models/vehicle.py`

Responsibilities:
- Database table definition
- Field constraints
- Relationships
- Indexes

## Frontend Architecture (Flutter)

### Layered Architecture

```
┌───────────────────────────┐
│   Presentation Layer      │
│ (Screens & Widgets)       │
└───────────────┬───────────┘
                ↓
┌───────────────────────────┐
│   State Management        │
│ (Riverpod Providers)      │
└───────────────┬───────────┘
                ↓
┌───────────────────────────┐
│   Domain Layer            │
│ (Entities & Use Cases)    │
└───────────────┬───────────┘
                ↓
┌───────────────────────────┐
│   Data Layer              │
│ (Repositories, Models)    │
└───────────────┬───────────┘
                ↓
┌───────────────────────────┐
│   Core Layer              │
│ (Network, Storage, Utils) │
└───────────────────────────┘
```

### State Management (Riverpod)

- **Providers** for dependency injection
- **FutureProviders** for async operations
- **StateNotifiers** for complex state
- **Async value** handling with loading/error states

## Database Architecture

### Schema Design

```sql
-- Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role_id INTEGER REFERENCES roles(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Vehicles Table
CREATE TABLE vehicles (
    id SERIAL PRIMARY KEY,
    vin VARCHAR(17) UNIQUE NOT NULL,
    plate_number VARCHAR(20),
    engine_number VARCHAR(50),
    chassis_number VARCHAR(50),
    manufacturer VARCHAR(100),
    model VARCHAR(100),
    model_year INTEGER,
    color VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Audit Logs
CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    entity_type VARCHAR(50),
    entity_id INTEGER,
    action VARCHAR(20),
    changes JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Indexing Strategy

- **VIN index**: For fast VIN lookups (unique, B-tree)
- **Plate number index**: For plate-based searches
- **Engine/Chassis indexes**: For comprehensive searches
- **User email index**: For authentication queries
- **Audit timestamp index**: For log queries

## VehicleProvider Service Layer

### Design Principles

The `VehicleProvider` is designed with these core principles:

1. **API Abstraction**: Hides external API complexity
2. **Authorization Only**: Only connects to authorized, official APIs
3. **Interface-Based**: Easy to swap implementations
4. **Error Resilience**: Graceful fallbacks and error handling
5. **Caching**: Reduces API calls and improves performance

### Implementation Structure

```python
class VehicleProvider(ABC):
    """Abstract base for authorized vehicle data providers"""
    
    @abstractmethod
    async def get_vehicle_info(
        self, identifier: str, search_type: SearchType
    ) -> VehicleInfo:
        """Get vehicle info from authorized API"""
        pass

class OfficialAPIProvider(VehicleProvider):
    """Implementation for authorized official APIs"""
    
    def __init__(self, api_key: str, cache: CacheService):
        self.api_key = api_key
        self.cache = cache
    
    async def get_vehicle_info(
        self, identifier: str, search_type: SearchType
    ) -> VehicleInfo:
        # Check cache first
        cached = await self.cache.get(f"vehicle:{identifier}")
        if cached:
            return cached
        
        # Call authorized API
        response = await self._call_authorized_api(identifier, search_type)
        
        # Cache result
        await self.cache.set(f"vehicle:{identifier}", response)
        
        return response
```

## Security Architecture

### Authentication Flow

```
┌──────────────────────────────────────┐
│  1. User submits credentials         │
└────────────────┬─────────────────────┘
                 ↓
┌──────────────────────────────────────┐
│  2. Password validation (bcrypt)     │
└────────────────┬─────────────────────┘
                 ↓
┌──────────────────────────────────────┐
│  3. JWT token generation             │
│     - Access Token (15min)           │
│     - Refresh Token (7days)          │
└────────────────┬─────────────────────┘
                 ↓
┌──────────────────────────────────────┐
│  4. Token returned to client         │
└──────────────────────────────────────┘
```

### Authorization Levels

1. **Admin**: Full system access
2. **Technician**: Vehicle search, diagnostics, records
3. **User**: Own vehicles only, limited searches
4. **Public**: Anonymous searches (limited)

## Error Handling Strategy

### Error Categories

```python
class APIError(Exception):
    """Base API error"""
    pass

class ValidationError(APIError):
    """Request validation failed"""
    status_code = 422

class AuthenticationError(APIError):
    """Authentication failed"""
    status_code = 401

class AuthorizationError(APIError):
    """Authorization failed"""
    status_code = 403

class ResourceNotFoundError(APIError):
    """Resource not found"""
    status_code = 404

class InternalServerError(APIError):
    """Internal server error"""
    status_code = 500
```

## Caching Strategy

### Cache Layers

1. **Application Cache** (Redis)
   - TTL: 1 hour for vehicle data
   - TTL: 24 hours for reference data
   - Key pattern: `vehicle:{vin}:{timestamp}`

2. **Database Query Cache** (SQLAlchemy)
   - Automatically managed by ORM
   - Cache invalidation on writes

3. **Client Cache** (SQLite on mobile)
   - Offline support
   - Sync on connection restore

## Deployment Architecture

### Docker Compose Stack

```yaml
services:
  nginx:           # Reverse proxy
  backend:         # FastAPI application
  frontend:        # Flutter web build
  postgres:        # Main database
  redis:           # Cache layer
  adminer:         # Database admin (dev only)
```

### Environment Separation

- **Development**: docker-compose.yml (with hot reload)
- **Production**: docker-compose.prod.yml (optimized)

## Scaling Considerations

### Horizontal Scaling

- Stateless API servers (multiple instances behind Nginx)
- Shared PostgreSQL database
- Centralized Redis cache
- Message queue for async tasks (future)

### Performance Optimization

- Database query optimization (explain analyze)
- Caching strategy for frequent queries
- API rate limiting
- Connection pooling
- Async/await for I/O operations

## Testing Strategy

### Test Pyramid

```
        △
       /|
      / │ Integration Tests (API)
     /  │
    /───┼───────────────────
   /    │ Unit Tests
  /     │ (Services, Utils)
 /______│___________________
```

### Coverage Targets

- Unit tests: >80% coverage
- Integration tests: Critical paths
- E2E tests: User workflows

---

**Last Updated**: 2026-07-25
