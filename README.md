# 🔌 NESCO Prepaid CLI

[![PyPI version](https://badge.fury.io/py/nesco.svg)](https://badge.fury.io/py/nesco)
[![Python Versions](https://img.shields.io/pypi/pyversions/nesco.svg)](https://pypi.org/project/nesco/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/nesco)](https://pepy.tech/project/nesco)

A Python CLI tool to collect information about **Northern Electric Supply Company Limited (NESCO)** prepaid electricity accounts. Get real-time balance, consumption data, customer information, and recharge history directly from your terminal.

## ✨ Features

- 💰 **Balance Check**: Get current account balance instantly
- 👤 **Customer Info**: Retrieve detailed customer and meter information
- 📊 **Monthly Consumption**: View historical monthly usage data
- 🔄 **Recharge History**: Track your payment and recharge records with token details
- 🚀 **Fast & Lightweight**: Built with Python and designed for speed
- 🔒 **Secure**: Direct API integration with NESCO's official endpoints

## 📦 Installation

### From PyPI (Recommended)
```bash
pip install nesco
```

### From Source
```bash
git clone https://github.com/mdminhazulhaque/python-nesco.git
cd python-nesco
pip install -e .
```

## 🚀 Quick Start

After installation, use the `nesco-cli` command:

```bash
# Get help
nesco-cli --help

# Check balance
nesco-cli get-balance -c YOUR_CUSTOMER_NUMBER

# Get customer information
nesco-cli get-customer-info -c YOUR_CUSTOMER_NUMBER
```

## 📖 Usage

```
Usage: nesco-cli [OPTIONS] COMMAND [ARGS]...

  A CLI tool for NESCO Prepaid electricity account management.

Options:
  --help  Show this message and exit.

Commands:
  get-balance              Get current account balance
  get-customer-info        Get detailed customer and meter information
  get-monthly-consumption  Get monthly consumption history
  get-recharge-history     Get recharge and payment history
```

## 💡 Examples

### 💰 Check Balance

Get your current account balance:

```bash
$ nesco-cli get-balance -c 12345678
```

**Sample Output:**
```
987.43
```

### 👤 Get Customer Information

Retrieve comprehensive customer and meter details:

```bash
$ nesco-cli get-customer-info -c 12345678
```

**Sample Output:**
```
Name                Address   Electricity Office  Feeder Name      Meter Number    Approved Load (kW)
------------------  --------  ------------------  -------------  --------------  --------------------
MD. MINHAZUL HAQUE  RAJSHAHI  Rajshahi S&D4       GREATER ROAD      12345678901                     2
```

### 🔄 Get Recharge History

View your recent payment and recharge transactions with token details:

```bash
$ nesco-cli get-recharge-history -c 12345678
```

**Sample Output:**
```
  ID  Token                     Power    Amount    Via     Date                  Status
----  ------------------------  -------  --------  ------  --------------------  --------
   1  0183-4597-1724-6908-6354   957.12   1000     ROCKET  01-JAN-2025 11:00 AM   Success
   2  4815-9365-5179-7943-3266   258.65    400     BKASH   01-FEB-2025 11:00 PM   Success
   3  2265-9417-3127-5691-9994   134.45    400     BKASH   01-MAR-2025 11:00 PM   Success
```

### 📊 Get Monthly Consumption

Analyze your monthly electricity usage patterns:

```bash
$ nesco-cli get-monthly-consumption -c 12345678
```

**Sample Output:**
```
  Year  Month        Recharge    Discount    Usage
------  ---------  ----------  ----------  -------
  2025  March            2000       -20    1875.22
  2025  February          500        -5     433.15
  2025  January          1000       -10     812.08
```

## 🛠️ Development

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Setting up for Development

1. Clone the repository:
```bash
git clone https://github.com/mdminhazulhaque/python-nesco.git
cd python-nesco
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install in development mode:
```bash
pip install -e .
```

### Dependencies

- `requests` - HTTP library for API calls
- `click` - Command line interface framework
- `tabulate` - Pretty-print tabular data

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This is an unofficial tool. Use at your own discretion. The authors are not responsible for any issues that may arise from using this tool.