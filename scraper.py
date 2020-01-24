from lxml import html
from datetime import datetime
import time
import requests
import re
import traceback
from lxml.cssselect import CSSSelector
import string

import notifier as Notif
import helpers as Helpers

try:
  # https://eshop.georgebee.com/keltska/ 
  medovinyEndpoint = 'https://eshop.georgebee.com/keltska/'
  unavailableMsg = 'Momentálně nedostupné'
  availabilityFile = 'availability_status'
  availabilityFromFile = Helpers.read_file(availabilityFile)

  currentDatetime = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

  responseStatus = 0
  requestNumber = 0
  response = ''
  while (responseStatus != 200 and requestNumber < 10):
    time.sleep(3) # make a request every 3 secs
    requestNumber += 1
    try:
      response = requests.get(medovinyEndpoint)
      responseStatus = response.status_code
    except:
      pass

  if requestNumber < 10:
    scrapedHtml = str(response.content.decode('utf-8'))
    
    if unavailableMsg in scrapedHtml:
      Helpers.write_to_file(availabilityFile, f'{currentDatetime}: {unavailableMsg}')
    
    elif unavailableMsg in availabilityFromFile:
      # send notif email
      Helpers.write_to_file(availabilityFile, f'{currentDatetime}: Dostupné!')
      urlButton = f'<a href="{medovinyEndpoint}"><button style="margin-left:0; box-shadow: rgb(41, 108, 146) 0px 4px 9px -2px; background: linear-gradient(rgb(41, 108, 146) 5%, rgb(41, 108, 146) 100%) rgb(41, 108, 146); border-radius: 4px; border: 1px solid rgb(41, 108, 146); display: inline-block; color: rgb(255, 255, 255); font-family: Helvetica; font-size: 15px; font-weight: bold; padding: 5px 14px; cursor: grab !important; text-decoration: none; text-shadow: rgb(41, 73, 123) 0px 1px 0px;">Přejít na odkaz</button></a>'

      notifMessage = f"""\
      <html>
        <body>
          <p> Keltská medovina je naskladněná! <br>
          <br>
          {urlButton}
          </p>
        </body>
      </html>
      """
      Notif.email_notif('pospisil.vaclav@gmail.com','','Medovina Scraper - Medovina na skladě!', notifMessage)

except:
  traceback.print_exc()
  exception = '\n'.join(traceback.format_exc())
  errorMessage = f"""\
    <html>
      <body>
        <p> A new error has just been produced: {exception} </p>
      </body>
    </html>
    """
  Notif.email_notif('pospisil.vaclav@gmail.com','','Medovina Scraper - New Error', errorMessage)