import requests
from send_email import send_email

topic= "techcrunch"
api_key = "76964584e15e4952bb481b8f78d20c2e"
url = "https://newsapi.org/v2/top-headlines?" \
      f"sources={topic}&" \
      "apiKey=76964584e15e4952bb481b8f78d20c2e&" \
      "language=en"

request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"][:10]:
    body = "Subject: Today's News" \
            + "\n" + body + article["title"] \
            + "\n" + article["description"] + "\n" \
            + article["url"] + 2*"\n"

body = body.encode("utf-8")
 
send_email(message=body)