"""
NESCO Prepaid Python Client

A Python package for interacting with Northern Electric Supply Company Limited (NESCO)
prepaid electricity account endpoints.

Example:
    >>> from nesco import NescoPrepaid
    >>> client = NescoPrepaid(customer_number=12345678)
    >>> balance = client.get_balance()
    >>> print(balance)
"""

from .nesco import NescoPrepaid

# Version will be updated by GitHub Actions during release
__version__ = "1.0.0"
__author__ = "Md Minhazul Haque"
__email__ = "mdminhazulhaque@gmail.com"

__all__ = ["NescoPrepaid"]