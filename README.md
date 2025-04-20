# Nesco Prepaid CLI

A command-line interface (CLI) tool to collect information about Nesco Prepaid Accounts.

## Installation

Install the package using pip:

```bash
pip install nesco
```

## Usage

### Get Balance

Retrieve the current balance for a specific account:

```bash
nesco-cli get-balance -c <customer_number>
```

Example:

```bash
$ nesco-cli get-balance -c 12345678
987.43
```

### Get Recharge History

View the recharge history for a specific account:

```bash
nesco-cli get-recharge-history -c <customer_number>
```

Example:

```bash
$ nesco-cli get-recharge-history -c 12345678
  ID  Token                     Power    Amount    Via     Date                  Status
----  ------------------------  -------  --------  ------  --------------------  --------
   1  0183-4597-1724-6908-6354   957.12   1000     ROCKET  01-JAN-2025 11:00 AM   Success
   2  4815-9365-5179-7943-3266   258.65    400     BKASH   01-FEB-2025 11:00 PM   Success
   3  2265-9417-3127-5691-9994   134.45    400     BKASH   01-MAR-2025 11:00 PM   Success
   ...
```

### Get Monthly Consumption

Retrieve monthly consumption details for a specific account:

```bash
nesco-cli get-monthly-consumption -c <customer_number>
```

Example:

```bash
$ nesco-cli get-monthly-consumption -c 12345678
  Year  Month        Recharge    Discount    Usage
------  ---------  ----------  ----------  -------
  2025  March            2000       -20    1875.22
  2025  February          500        -5     433.15
  2025  January          1000       -10     812.08
  ...
```

Replace `<customer_number>` with your actual account number to use the commands.

### Get Customer Info

```
$ nesco-cli get-customer-info -c 12345678
Name                Address   Electricity Office  Feeder Name      Meter Number    Approved Load (kW)
------------------  --------  ------------------  -------------  --------------  --------------------
MD. MINHAZUL HAQUE  RAJSHAHI  Rajshahi S&D4       GREATER ROAD      12345678901                     2
```