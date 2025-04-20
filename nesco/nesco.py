#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup

class NescoPrepaid():
    SUBMIT_TYPE_RECHARGE_HISTORY = 'রিচার্জ হিস্ট্রি'
    SUBMIT_TYPE_MONTHLY_CONSUMPTION = 'মাসিক ব্যবহার'
    
    def __init__(self, customer_number):
        self.customer_number = customer_number
        
    def _make_request(self, submit_type):
        url = 'https://customer.nesco.gov.bd/pre/panel'
        session = requests.Session()
        response = session.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token_meta = soup.find('meta', attrs={'name': 'csrf-token'})
        csrf_token = csrf_token_meta['content'] if csrf_token_meta else None

        data = {
            '_token': csrf_token,
            'cust_no': self.customer_number,
            'submit': submit_type
        }

        response = session.post(url, data=data)

        return response.text

    def _extract_balance(self, response):
        soup = BeautifulSoup(response, 'html.parser')
        labels = soup.find_all('label')
        inputs = soup.find_all('input')
        data = {}
        for label in labels:
            label_text = label.text.strip()
            label_text = re.sub(r'\s+', ' ', label_text)
            input_field = label.find_next('input')
            if input_field:
                value = input_field['value'].strip()
                data[label_text] = value
        return data
    
    def _extract_monthly_consumption(self, response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table', class_='bfont_post')
        if not table:
            return []

        headers = [th.text.strip() for th in table.find('thead').find_all('th')]

        rows = []
        for tr in table.find('tbody').find_all('tr'):
            row = [td.text.strip() for td in tr.find_all('td')]
            rows.append(row)

        return headers, rows

    def _extract_customer_info(self, response):
        soup = BeautifulSoup(response, 'html.parser')
        labels = soup.find_all('label')
        data = {}
        for label in labels:
            label_text = label.text.strip()
            label_text = re.sub(r'\s+', ' ', label_text)
            input_field = label.find_next('input')
            if input_field:
                value = input_field.get('value', '').strip()
                data[label_text] = value
        return data

    def get_balance(self):
        response = self._make_request(self.SUBMIT_TYPE_MONTHLY_CONSUMPTION)
        data = self._extract_balance(response)
        return list(data.values())[-1]

    def get_customer_info(self):
        response = self._make_request(self.SUBMIT_TYPE_RECHARGE_HISTORY)
        info = self._extract_customer_info(response)
        data = list(info.values())
        data = [data[1], data[3], data[5], data[6], data[8], data[9]]
        headers = ['Name', 'Address', 'Electricity Office', 'Feeder Name', 'Meter Number', 'Approved Load (kW)']
        return [data], headers
        
    def get_recharge_history(self):
        response = self._make_request(self.SUBMIT_TYPE_RECHARGE_HISTORY)
        _, data = self._extract_monthly_consumption(response)
        data = [
            [row[0], row[1], row[8], row[9], row[11], row[12], row[13]]
            for row in data
        ]
        headers = ['ID', 'Token', 'Power', 'Amount', 'Via', 'Date', 'Status']
        return data, headers

    def get_monthly_consumption(self):
        response = self._make_request(self.SUBMIT_TYPE_MONTHLY_CONSUMPTION)
        headers, data = self._extract_monthly_consumption(response)
        headers = ["Year", "Month", "Recharge", "Discount", "Usage"]
        data = [row[:5] for row in data]
        return data, headers