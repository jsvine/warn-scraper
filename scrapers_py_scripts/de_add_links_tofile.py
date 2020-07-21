from os import path

import csv 
from datetime import datetime
import pandas as pd

from bs4 import BeautifulSoup
import requests
import json

def add_links_de():

    output_csv = '/Users/dilcia_mercedes/Big_Local_News/prog/WARN/data/delaware_warn_raw.csv'
    max_entries = 200 # manually inserted

    start_row_list = range(1, max_entries, 50)
    start_row = 1
    links = []
    for start_row in start_row_list:
        try:
            url = 'https://joblink.delaware.gov/ada/mn_warn_dsp.cfm?securitysys=on&start_row={}&max_rows=50&orderby=employer&choice=1'.format(start_row)
            page = requests.get(url)

            print(page.status_code) # should be 200

            soup = BeautifulSoup(page.text, 'html.parser')

            table = soup.find_all('table') # output is list-type
            for a in soup.find_all('a', href=True, text=True):
                link_text = a['href']
    #             print(link_text)
                if 'callingfile' in link_text:
                    links.append(link_text)

        except IndexError:
            print(url + ' not found')

    data = pd.read_csv('/Users/dilcia_mercedes/Big_Local_News/prog/WARN/data/delaware_warn_raw.csv')
    data['url_suffix'] = links
    data['Employer Name'] = data['Employer'].str.replace('\r', '')
    data.drop(columns='Employer', inplace=True)
    data = data[['url_suffix', 'Employer Name', 'City', 'Zip', 'LWIB Area', 'Notice Date']]
    data.to_csv(output_csv)


if __name__ == '__main__':
    add_links_de()