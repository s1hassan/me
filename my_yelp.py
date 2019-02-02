#Maintainer Qamber Mehdi
# Created on August 25, 2018

import requests

def search_businesses(search_term, search_location):

    api_key = "UltCcVIZngopW1H2oyQZOwN2yARWw86wRD2JdwpG5897kMLGOLciOxLWShuW8iO7LyDS42BKe8BRzdndrDG-bU5eBz2JbjhNV83ROKduaCktheyc1enBSqktRfoRWnYx"

    url = "https://api.yelp.com/v3/businesses/search"

    my_headers = {
        "Authorization": "Bearer %s" % api_key
    }

    my_params = {
        "term": search_term,
        "location": search_location,
        "limit": 3,
    }

    businesses_object = requests.get(url, headers=my_headers, params=my_params)

    businesses_dict = businesses_object.text

    print(businesses_dict)

#calling the search_businesses function
search_businesses("restaurants", "chicago")
