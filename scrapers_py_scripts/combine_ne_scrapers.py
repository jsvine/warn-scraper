from os import path
import os

import csv 
from datetime import datetime

from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

def combine():

    ne_one = pd.read_csv('/Users/dilcia_mercedes/Big_Local_News/prog/WARN/data/nebraska_warn_raw1.csv')
    ne_two = pd.read_csv('/Users/dilcia_mercedes/Big_Local_News/prog/WARN/data/nebraska_warn_raw2.csv')
    ne_all_data = pd.concat([ne_one, ne_two])
    ne_all_data.to_csv('/Users/dilcia_mercedes/Big_Local_News/prog/WARN/data/nebraska_warn_raw.csv')
    os.remove('/Users/dilcia_mercedes/Big_Local_News/prog/WARN/data/nebraska_warn_raw1.csv')
    os.remove('/Users/dilcia_mercedes/Big_Local_News/prog/WARN/data/nebraska_warn_raw2.csv')


if __name__ == '__main__':
    combine()