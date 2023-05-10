from web_search.generic_scrubber import GenericScrubber


class GoogleScrubber(GenericScrubber):
    def __init__(self, web_data: str):
        super().__init__(web_data)

    def get_result_data(self):
        res = self.soup.findAll('Search Result')
        print(res)
