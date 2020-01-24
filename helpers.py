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