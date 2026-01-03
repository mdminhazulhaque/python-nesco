# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python CLI tool for interacting with Northern Electric Supply Company Limited (NESCO) prepaid electricity accounts. Unlike the sibling projects (bpdb, desco), this tool uses **web scraping** instead of a REST API, parsing HTML forms and tables from the NESCO customer portal.

## Architecture

### Core Components

**nesco/nesco.py** - Web Scraping Client Layer
- `NescoPrepaid` class handles web scraping of NESCO customer portal
- Base URL: `https://customer.nesco.gov.bd/pre/panel`
- **CSRF token-based authentication** - extracted from HTML meta tags
- Uses `requests.Session()` for cookie persistence
- Uses `BeautifulSoup` for HTML parsing
- Submit types are **Bengali language strings** (constants)

**nesco/main.py** - CLI Layer
- Click-based CLI using decorator pattern (`@app.command(name="...")`)
- Commands use `--customernumber` / `-c` option (INT type, unlike desco's STRING)
- Error handling through `handle_api_error` decorator wrapper
- Entry point: `app()` function mapped to `nesco-cli` in pyproject.toml
- Uses tabulate for formatted output display

**nesco/__init__.py** - Package Entry Point
- Exports `NescoPrepaid` class for programmatic use
- Version controlled by GitHub Actions during release (format: `1.{run_number}.0`)

### Web Scraping Flow

1. **GET** request to portal page to retrieve CSRF token
2. Parse HTML with BeautifulSoup to find `<meta name="csrf-token">`
3. **POST** form data with `_token`, `cust_no`, and `submit` (Bengali text)
4. Parse HTML response based on submit type
5. Extract data from tables, labels, and input fields

### Submit Type Constants (Bengali)

```python
SUBMIT_TYPE_RECHARGE_HISTORY = 'রিচার্জ হিস্ট্রি'
SUBMIT_TYPE_MONTHLY_CONSUMPTION = 'মাসিক ব্যবহার'
```

These are used as form submit values to determine which data the portal returns.

### HTML Parsing Strategies

**Balance Extraction** (`_extract_balance`):
- Finds all `<label>` and `<input>` elements
- Maps label text to next input's value attribute
- Normalizes whitespace with regex `r'\s+' → ' '`
- Returns last value in dict (balance field)

**Customer Info Extraction** (`_extract_customer_info`):
- Similar label→input mapping
- Returns specific indices: `[1, 3, 5, 6, 8, 9]` from values list
- Hard-coded header mapping to Bengali field names

**Table Extraction** (`_extract_monthly_consumption`):
- Finds table with class `bfont_post`
- Extracts headers from `<thead>` → `<th>` elements
- Extracts rows from `<tbody>` → `<tr>` → `<td>` elements
- Returns tuple of `(headers, rows)`

**Recharge History**:
- Uses table extraction but with custom column selection
- Extracts specific columns: `[0, 1, 8, 9, 11, 12, 13]`
- Maps to: ID, Token, Power, Amount, Via, Date, Status

## Development Commands

### Setup
```bash
# Install in development mode
pip install -e .

# Or create virtual environment first
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e .
```

### Testing the CLI
```bash
# Test balance check
nesco-cli get-balance -c 12345678

# Test customer info
nesco-cli get-customer-info -c 12345678

# Test recharge history
nesco-cli get-recharge-history -c 12345678

# Test monthly consumption
nesco-cli get-monthly-consumption -c 12345678
```

### Building
```bash
# Build distribution packages
python -m pip install build
python -m build

# Output: dist/*.whl and dist/*.tar.gz
```

## Version Management

- Version is defined in `nesco/__init__.py` as `__version__ = "1.0.0"`
- GitHub Actions workflow (`.github/workflows/pypi.yml`) auto-updates version on push to main
- Version format: `1.{github.run_number}.0`
- Workflow uses sed to replace version string: `sed -i "s/__version__ = \".*\"/__version__ = \"$VERSION\"/" nesco/__init__.py`

## Publishing

Automated via GitHub Actions on push to main:
1. Version number updated automatically
2. Build artifacts created with `python -m build`
3. Published to PyPI using trusted publisher with OIDC token

Manual workflow dispatch also available via GitHub Actions UI.

## Data Extraction Details

### Balance
- Makes request with `SUBMIT_TYPE_RECHARGE_HISTORY`
- Extracts last value from label→input mapping
- Returns single string value

### Customer Info
- Makes request with `SUBMIT_TYPE_RECHARGE_HISTORY` (same as balance)
- Extracts indices `[1, 3, 5, 6, 8, 9]` from values
- Returns: Name, Address, Electricity Office, Feeder Name, Meter Number, Approved Load
- Returns tuple: `([data], headers)`

### Recharge History
- Makes request with `SUBMIT_TYPE_RECHARGE_HISTORY`
- Uses `_extract_monthly_consumption` (table parser)
- Selects columns: `[0, 1, 8, 9, 11, 12, 13]` from each row
- Returns: ID, Token, Power, Amount, Via, Date, Status

### Monthly Consumption
- Makes request with `SUBMIT_TYPE_MONTHLY_CONSUMPTION`
- Uses `_extract_monthly_consumption` (table parser)
- Takes first 5 columns: `row[:5]`
- Returns: Year, Month, Recharge, Discount, Usage

## CLI Design Pattern

Commands using `@app.command(name="...")` decorator pattern:
1. Click decorator defines command with `--customernumber` option (INT type)
2. `@handle_api_error` decorator catches exceptions and exits with error code 1
3. Print status message with emoji
4. Instantiate `NescoPrepaid(customernumber)`
5. Call scraping method
6. Format output (simple echo for balance, tabulate for others)

## Important Notes

- This is part of a multi-repository project with sibling repositories: `python-bpdb` and `python-desco` (similar utility tools for other Bangladesh power companies)
- **Unique architecture**: Only project using web scraping instead of REST API
- **Fragile by nature**: HTML structure changes will break parsing
- Bengali language constants for form submission
- CSRF token required for each request
- Session cookies maintained across GET and POST
- No SSL verification issues (unlike desco)
- Dependencies include `beautifulsoup4` (unique to this project)
- Customer number treated as INT in CLI (unlike desco's STRING)
- Hard-coded column indices make code brittle - changes to portal HTML will require updates
