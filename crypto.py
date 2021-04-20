# Created and Modified by Malik B. Parker 2021

from requests import Request, Session, post
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time

##### Globals

# Coin Market Cap API KEY
coinmarketcap_key = open("coinmarketcap.key").readline()
# Gathers data from all the coins on the website
coin_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# IFTTT API Key
ifttt_key = open("ifttt.key").readline()
# Sends a webhook to IFTTT with Price information
ifttt_webhook_url = f"https://maker.ifttt.com/trigger/new_DOGE_data/with/key/{ifttt_key}"

# Dictionary containing information on all coins from Coin Market Cap
coins = {}

##### Functions

# Gets the latest DOGE Price as well as populate the coins dictionary
def get_latest_doge():
  global coins
  try:
    if(DEBUG): # Uses the sample data so that you don't waste an API Call
      response = open('sample_data.json')
      data = json.load(response)
    else:
      response = session.get(coin_url, params=parameters)
      data = json.loads(response.text)
      data = data["data"]

    for coin in data:
      coins[coin["symbol"]] = coin

    # Pretty print the results for DOGE to the console
    # print(json.dumps(coins["DOGE"], indent=2))
    
    price = coins["DOGE"]["quote"]["USD"]["price"]
    return price
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


# Send the price value to IFTTT via the Webhook
def post_ifttt_webhook(price):
  try:
    data = {'value1': price}
    post(ifttt_webhook_url, json=data)
  except:
    print("ERROR")


##### Session Start-Up Parameters
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
  }
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': coinmarketcap_key,
}

session = Session()
session.headers.update(headers)

WAIT_TO_SEND_TIME = 300 # Seconds
DEBUG = False   # Set to true if you want to use the sample data
if __name__ == "__main__":
  # while(True):
  #   post_ifttt_webhook(get_latest_doge())
  #   time.sleep(WAIT_TO_SEND_TIME)
  post_ifttt_webhook(get_latest_doge())