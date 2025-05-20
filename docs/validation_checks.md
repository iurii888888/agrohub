# Validation & Quality Checks

## Data Validation
- Schema validation using Pydantic for incoming JSON payloads.
- Range checks on sensor data (e.g., temperature  -40°C to 60°C).
- Automated data integrity tests scheduled daily.

## Model Validation
- Cross-validation (5-fold) on disease classification dataset: average accuracy 92.3%.
- Confusion matrices reviewed weekly to detect class drift.
- Drift detection: population stability index (PSI) monitored per feature.

## Code Quality & Coverage
- Static analysis via flake8 and mypy (targeting 90% code coverage).
- Unit and integration tests covering 95% of critical paths.
- Code coverage reports generated in GitHub Actions.
