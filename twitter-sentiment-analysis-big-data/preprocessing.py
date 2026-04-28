import json 

 

# Original file: "data" in JSON: [ ... ] 

with open("israel_iran_tweets_sample.json", "r") as f: 

    data = json.load(f)["data"] 

 

# Write each tweet on a separate line 

with open("tweets_ldjson.json", "w") as f: 

    for tweet in data: 

        json.dump(tweet, f) 

        f.write("\n") 