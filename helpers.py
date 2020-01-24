# support functions that are used in multiple files

import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials
import sys,traceback
import codecs

sys.path.append('../')


def write_to_file(filename, data):
        
        f= codecs.open(filename,'w', 'utf-8') 
        f.write(data)
        f.close()

def read_file(filename):
        
        f= codecs.open(filename,'r', 'utf-8') 
        list = []

        for items in f:
                list.append(items)

        f.close()
        
        return items

def connect_to_sheet(sheetName):
        json_key = json.load(open('/Nemovitosti_Scraping/creds.json')) # json credentials
        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
        credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds
        file = gspread.authorize(credentials) # authenticate with Google
        spreadsheet = file.open(sheetName) # open spreadsheet
        return spreadsheet

def sort_list_by_nested_element(sub_li,nestedIndexElement):
        # according to https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
        l = len(sub_li)
        for i in range(0, l):
                for j in range(0, l-i-1):
                        if (sub_li[j][nestedIndexElement] > sub_li[j + 1][nestedIndexElement]):
                                tempo = sub_li[j]
                                sub_li[j]= sub_li[j + 1]
                                sub_li[j + 1]= tempo
        return sub_li

def colnum_string(n): # convert index to google sheet col name
        string = ""
        while n > 0:
                n, remainder = divmod(n - 1, 26)
                string = chr(65 + remainder) + string
        return string