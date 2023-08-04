#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from sec_api import QueryApi

# your API key
api_key = "4d4137fd4dba200cc2668ea001120c1eb98fd42998dd5f55c85be207bbf30b12"

# create QueryApi object
queryApi = QueryApi(api_key=api_key)

query = {
  "query": { "query_string": {
      "query": "ticker:AAPL AND filedAt:{2001-01-01 TO 2023-12-31} AND formType:\"10-Q\""
    } },
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

filings = queryApi.get_filings(query)

print(filings)



# %%% 

from sec_api import QueryApi

# your API key
api_key = "4d4137fd4dba200cc2668ea001120c1eb98fd42998dd5f55c85be207bbf30b12"

# create QueryApi object
queryApi = QueryApi(api_key=api_key)

# initial query parameters
start_from = 0
size = 1000  # adjust this based on the API's maximum limit

all_filings = []

while True:
    # define the query
    query = {
        "query": { 
            "query_string": {
                "query": "ticker:AAPL AND filedAt:{2001-01-01 TO 2023-12-31} AND formType:\"10-Q\""
            } 
        },
        "from": str(start_from),
        "size": str(size),
        "sort": [{ "filedAt": { "order": "desc" } }]
    }

    # fetch the filings
    filings = queryApi.get_filings(query)

    # break if no more filings
    if not filings['filings']:
        break

    # add filings to the all_filings list
    all_filings.extend(filings['filings'])

    # increment the start_from
    start_from += size

# print the id of each filing
for filing in all_filings:
    print(filing.get('id'))

# print the total number of filings
print(f"Total filings returned: {len(all_filings)}")





# %%% 
from sec_api import ExtractorApi

extractorApi = ExtractorApi(api_key)

filing_url_10q = "https://www.sec.gov/Archives/edgar/data/320193/000032019323000064/0000320193-23-000064.txt"

extracted_section_10q = extractorApi.get_section(filing_url_10q, "part1item2", "text")

from bs4 import BeautifulSoup

html_text = extracted_section_10q
# Create a BeautifulSoup object
soup = BeautifulSoup(html_text, 'html.parser')

# Extract the text content without HTML tags
text = soup.get_text()

print(text)
