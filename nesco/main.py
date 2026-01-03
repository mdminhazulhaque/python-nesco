#!/usr/bin/env python3
"""
NESCO Prepaid CLI

A command-line interface for interacting with NESCO prepaid electricity accounts.
Provides commands to check balance, get customer info, view consumption history,
and track recharge records.
"""

import click
import sys
from tabulate import tabulate
from .nesco import NescoPrepaid
from . import __version__


def handle_api_error(func):
    """Decorator to handle API errors gracefully."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            click.echo(f"❌ Error: {str(e)}", err=True)
            sys.exit(1)
    return wrapper


@click.group()
@click.version_option(version=__version__, prog_name="nesco-cli")
def app():
    """
    🔌 NESCO Prepaid CLI

    A command-line tool for managing NESCO prepaid electricity accounts.
    Get real-time balance, consumption data, customer information, and recharge history.
    """
    pass

@app.command(name="get-balance")
@click.option(
    '--customernumber', '-c',
    type=click.INT,
    required=True,
    help="NESCO prepaid account number"
)
@handle_api_error
def get_balance(customernumber):
    """Get current account balance and consumption information."""
    click.echo("💰 Fetching account balance...")
    balance = NescoPrepaid(customernumber).get_balance()
    if balance:
        click.echo(f"\n📊 Account Balance: {balance}")
    else:
        click.echo("⚠️  No balance data found for this account.")

@app.command(name="get-customer-info")
@click.option(
    '--customernumber', '-c',
    type=click.INT,
    required=True,
    help="NESCO prepaid account number"
)
@handle_api_error
def get_customer_info(customernumber):
    """Get detailed customer and meter information."""
    click.echo("👤 Fetching customer information...")
    data, headers = NescoPrepaid(customernumber).get_customer_info()
    if data:
        click.echo("\n📋 Customer Information:")
        click.echo(tabulate(data, headers=headers, tablefmt="simple"))
    else:
        click.echo("⚠️  No customer data found for this account.")

@app.command(name="get-recharge-history")
@click.option(
    '--customernumber', '-c',
    type=click.INT,
    required=True,
    help="NESCO prepaid account number"
)
@handle_api_error
def get_recharge_history(customernumber):
    """Get recharge and payment history for the account."""
    click.echo("🔄 Fetching recharge history...")
    data, headers = NescoPrepaid(customernumber).get_recharge_history()
    if data:
        click.echo("\n💳 Recharge History:")
        click.echo(tabulate(data, headers=headers, tablefmt="simple"))
    else:
        click.echo("⚠️  No recharge history found for this account.")

@app.command(name="get-monthly-consumption")
@click.option(
    '--customernumber', '-c',
    type=click.INT,
    required=True,
    help="NESCO prepaid account number"
)
@handle_api_error
def get_monthly_consumption(customernumber):
    """Get monthly consumption history for the account."""
    click.echo("📊 Fetching monthly consumption data...")
    data, headers = NescoPrepaid(customernumber).get_monthly_consumption()
    if data:
        click.echo("\n⚡ Monthly Consumption History:")
        click.echo(tabulate(data, headers=headers, tablefmt="simple"))
    else:
        click.echo("⚠️  No consumption data found for this account.")

if __name__ == "__main__":
    app()
