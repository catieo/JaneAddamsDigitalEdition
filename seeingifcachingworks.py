import json
import requests

#setting up a caching file
CACHE_FNAME = 'cache_texts.json'

#setting up caching pattern
try:
    cache_file = open(CACHE_FNAME, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION = {}

def get_items(page_number):
    baseurl = "https://digital.janeaddams.ramapo.edu/api/items"
    url_params = {"key" : "ec24a147347176b9f82793ac2d9ace2a9f415bcb", "item_type" : 1, "page" : page_number}
    page_number_full = "page_{}".format(str(page_number)) #this will be the key for each page of results in the cache diction
    if page_number_full in CACHE_DICTION:
        print("Data was in the cache")
        return CACHE_DICTION[page_number_full]
    else:
        print("making a request for new data")
        response = requests.get(baseurl, url_params)
        CACHE_DICTION[page_number_full] = response.json()  #try response.json???
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close()
    return CACHE_DICTION[page_number_full]

for i in range(1,311):
    try:
        get_items(i)
    except:
        print("Not working for whatever reason lol")
