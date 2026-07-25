# Contributing to Vehicle Information & Diagnostics Platform

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

We are committed to providing a welcoming and inspiring community for all. Please read our Code of Conduct before participating.

### Our Pledge

- Be respectful and inclusive
- Welcome newcomers and help them get up to speed
- Focus on constructive criticism
- Respect differing opinions and experiences

## Getting Started

### Prerequisites

1. Fork the repository
2. Clone your fork locally
3. Add upstream remote: `git remote add upstream https://github.com/hed149405/Plakyab.git`
4. Create a branch for your changes: `git checkout -b feature/your-feature-name`

### Development Setup

Follow the [SETUP.md](./SETUP.md) guide for local development environment setup.

## Types of Contributions

### Bug Reports

If you find a bug:

1. **Check existing issues** - Avoid duplicates
2. **Create detailed report** including:
   - Title: Clear and descriptive
   - Description: What you expected vs. what happened
   - Steps to reproduce: Detailed steps
   - Environment: OS, versions, etc.
   - Screenshots/logs: If applicable

### Feature Requests

For new features:

1. **Use descriptive title**
2. **Explain the use case** - Why is this needed?
3. **Provide examples** - How would it be used?
4. **Consider alternatives** - Are there other solutions?

### Code Contributions

#### Coding Standards

**Backend (Python)**

```bash
# Code formatting
black app/

# Linting
flake8 app/ --max-line-length=100

# Import sorting
isort app/

# Type checking
mypy app/

# All at once
make lint
```

Style guide:
- Follow PEP 8
- Use type hints
- Write docstrings for functions and classes
- Keep functions small and focused
- Maximum line length: 100 characters

**Frontend (Dart)**

```bash
# Code formatting
dart format lib/ test/

# Static analysis
dart analyze

# Flutter specific
flutter analyze

# All at once
make lint-flutter
```

Style guide:
- Follow Dart style guide
- Use meaningful variable names
- Add comments for complex logic
- Keep widgets focused and composable

#### Commit Message Format

Use conventional commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type**: feat, fix, docs, style, refactor, perf, test, chore

**Scope**: Feature area (auth, vehicles, admin, etc.)

**Subject**: Imperative, present tense, lowercase, no period

**Examples**:
```
feat(vehicles): add VIN decoder endpoint
fix(auth): resolve JWT token validation issue
docs: update API documentation
test(repositories): add vehicle repository tests
```

#### Pull Request Process

1. **Update your branch**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Make your changes**
   - Keep PRs focused and manageable
   - One feature/fix per PR
   - Include tests for new functionality
   - Update documentation

3. **Run tests locally**
   ```bash
   # Backend
   cd backend && pytest --cov=app tests/
   
   # Frontend
   cd frontend && flutter test
   ```

4. **Commit and push**
   ```bash
   git add .
   git commit -m "feat(scope): description"
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request**
   - Use PR template
   - Link related issues
   - Describe changes clearly
   - Include screenshots if UI changes

6. **Address feedback**
   - Respond to reviews
   - Make requested changes
   - Push updates
   - Mark conversations as resolved

### Testing Requirements

**Backend Tests**

```python
import pytest
from app.services.vin_decoder import VINDecoder

class TestVINDecoder:
    """Test VIN decoder functionality"""
    
    def test_valid_vin_format(self):
        """Test that valid VIN is accepted"""
        decoder = VINDecoder()
        vin = "WBADT43452G296706"
        assert decoder.validate(vin) is True
    
    def test_invalid_vin_format(self):
        """Test that invalid VIN is rejected"""
        decoder = VINDecoder()
        vin = "INVALID"
        assert decoder.validate(vin) is False
```

**Frontend Tests**

```dart
import 'package:flutter_test/flutter_test.dart';
import 'package:plakyab/core/utils/validators.dart';

void main() {
  group('VINValidator', () {
    test('validates correct VIN format', () {
      final vin = 'WBADT43452G296706';
      expect(VINValidator.validate(vin), true);
    });

    test('rejects invalid VIN format', () {
      final vin = 'INVALID';
      expect(VINValidator.validate(vin), false);
    });
  });
}
```

### Documentation

Update relevant documentation for:
- New API endpoints (API_DOCUMENTATION.md)
- Architecture changes (ARCHITECTURE.md)
- Setup changes (SETUP.md)
- New features (README.md)

Documentation should include:
- Clear descriptions
- Code examples
- Configuration details
- Related links

## Review Process

### What We Look For

- **Code quality**: Clear, maintainable, follows conventions
- **Test coverage**: Adequate tests for new functionality
- **Documentation**: Clear and complete
- **Performance**: No unnecessary overhead
- **Security**: No security vulnerabilities
- **Backward compatibility**: No breaking changes without justification

### Review Timeline

- Core team aims to review within 48 hours
- Multiple reviewers for significant changes
- Maintainer approves before merge

## Development Workflow

### Creating a Feature

1. Create issue and discuss approach
2. Create feature branch from updated main
3. Implement feature with tests
4. Create PR with clear description
5. Address review feedback
6. Merge when approved

### Fixing a Bug

1. Create issue with reproduction steps
2. Create bugfix branch
3. Add test that reproduces bug
4. Implement fix
5. Verify test passes
6. Create PR with link to issue

## Running Tests Locally

### Backend

```bash
cd backend

# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test
pytest tests/unit/test_vin_decoder.py::test_valid_vin

# Run integration tests
pytest tests/integration/
```

### Frontend

```bash
cd frontend

# Run all tests
flutter test

# Run with coverage
flutter test --coverage

# Run specific test file
flutter test test/unit/validators_test.dart
```

## Project Management

### Issues

- **Bug** (🐛): Something isn't working
- **Feature** (✨): New functionality
- **Documentation** (📚): Documentation improvements
- **Question** (❓): Questions about the project

### Project Board

Track progress on our GitHub Project Board:
- **Todo**: Backlog items
- **In Progress**: Currently being worked on
- **In Review**: PR submitted, under review
- **Done**: Completed items

## Useful Links

- [GitHub Issues](https://github.com/hed149405/Plakyab/issues)
- [GitHub Discussions](https://github.com/hed149405/Plakyab/discussions)
- [GitHub Projects](https://github.com/hed149405/Plakyab/projects)
- [Code of Conduct](./CODE_OF_CONDUCT.md)

## Questions?

- Check existing discussions
- Create new GitHub Discussion
- Review existing documentation
- Ask in pull request comments

## Recognition

Contributors are recognized through:
- GitHub contributors page
- CONTRIBUTORS.md file
- Release notes
- Community discussions

---

Thank you for contributing to make this project better! 🎉
