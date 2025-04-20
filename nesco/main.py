#!/usr/bin/env python3

import click
from tabulate import tabulate as t
from nesco import NescoPrepaid
import re

@click.group()
def app():
    pass

@app.command(help="Get balance and consumption")
@click.option('--customernumber', '-c', type=click.INT, required=True, help="Account ID")
def get_balance(customernumber):
    balance = NescoPrepaid(customernumber).get_balance()
    print(balance)

@app.command(help="Get customer info")
@click.option('--customernumber', '-c', type=click.INT, required=True, help="Account ID")
def get_customer_info(customernumber):
    data, headers = NescoPrepaid(customernumber).get_customer_info()
    print(t(data, headers=headers))

@app.command(help="Get recharge history")
@click.option('--customernumber', '-c', type=click.INT, required=True, help="Account ID")
def get_recharge_history(customernumber):
    data, headers = NescoPrepaid(customernumber).get_recharge_history()
    print(t(data, headers=headers))

@app.command(help="Get monthly consumption")
@click.option('--customernumber', '-c', type=click.INT, required=True, help="Account ID")
def get_monthly_consumption(customernumber):
    data, headers = NescoPrepaid(customernumber).get_monthly_consumption()
    print(t(data, headers=headers))

if __name__ == "__main__":
    app()
