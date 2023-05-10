from request_handler.main import WebRequest
from web_search.google_scrubber import GoogleScrubber


def print_hi():
    wr = WebRequest()
    query = 'iphone 12'
    resp = wr.response(query=query)
    if resp:
        gs = GoogleScrubber(resp)
    else:
        print('error')


if __name__ == '__main__':
    print_hi()
