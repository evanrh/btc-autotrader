
import .cb_auth

class CB_Trader():
    API_URL = 'https://api.coinbase.com/v2'

    def __init__(self):
        pass

    def setup(self, api_key, api_secret):
        auth = cb_auth.CoinbaseWalletAuth(api_key, api_secret)


    def get_transaction_fee(self, amt):
        # Prices in USD
        # Fee rates from Coinbase website
        if amt <= 10:
            return 0.99
        elif amt <= 25:
            return 1.49
        elif amt <= 50:
            return 1.99
        elif amt <= 200:
            return 2.99
        else:
            # Rates is based off of percentage
            return 10
