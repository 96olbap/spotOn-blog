from app.models import Quote
import requests


quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    quotes_response = requests.get(quote_url)

    return quotes_response.json()

def process_quote():
    quote_data = get_quotes()
    return Quote(quote_data['author'], quote_data['quote'])
