import requests

from web_search.main import SearchEngines


class WebRequest:
    def __init__(self):
        pass

    # TODO : validation here, search engine
    def response(self, query: str, search_engine: str = SearchEngines.GOOGLE):
        url = search_engine + self._better_query(query)
        r = requests.get(url=url)

        if self._response_check(r):
            return r.text
        return None

    @staticmethod
    def _response_check(request) -> bool:
        if request.status_code != 200:
            print(f'Status code: {request.status_code}\nMessage: {request.text}')
            return False
        return True

    @staticmethod
    def _better_query(user_input) -> str:
        return 'q=price of ' + user_input
