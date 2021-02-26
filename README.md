# TwitterImageDownloader

"TwitterImageDownloader" is an image collection tool that uses the Twitter API.

# Features


# Requirement

* OAuth1Session

# Installation
 
```bash
pip install OAuth1Session
```

# Usage

1. You need to configure the "config.ini".
    - Env Field
        - api_key
        - api_secret
        - access_token
        - access_secret
    - Params Field
        - screen_name
           - Screen name of the user for whom you want to retrieve the image
        - count
           - Number of timelines to retrieve at a time
        - exclude_replies
           - Whether or not to include replies
        - include_rts
           - Whether or not to include retweets
        - max_id

2. run "main.py".
```bash
python3 main.py
```

# Note

> GET endpoints
The standard API rate limits described in this table refer to GET (read) endpoints. Note that endpoints not listed in the chart default to 15 requests per allotted user. All request windows are 15 minutes in length.  These rate limits apply to the standard API endpoints only, does not apply to premium APIs.

[Document](https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits).

# License

[MIT license](https://en.wikipedia.org/wiki/MIT_License).
