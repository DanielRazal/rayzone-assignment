# Rayzone Home Assignment - ParaBank QA Automation

Python/pytest/Selenium test suite covering client registration (UI) and a fund
transfer with validation (mixed API/UI) against the ParaBank demo banking app.

## Setup

1. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env`:
   ```
   copy .env.example .env
   ```
   The default values already work as-is, no editing needed.

## Running the tests

```
pytest -v
```

Or run a single test:
```
pytest tests/test_registration.py -v
pytest tests/test_transfer.py -v
```
