# Code Quality & CI/CD

## Linting & Formatting
- flake8 for style enforcement.
- black for code formatting.
- mypy for static type checking.

## CI/CD Pipelines
- GitHub Actions workflows:
  - **ci.yaml:** runs tests, lint, coverage.
  - **cd.yaml:** builds Docker image and deploys to demo environment on push to main.

## Coverage
- Target: 90%+ code coverage.
- Reports available via Codecov integration.
