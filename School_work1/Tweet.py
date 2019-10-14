#%%
import json


def load(In):
    with open(In, "r") as fp:
        return json.loads(fp.read())


def save(Out, jsonData):
    with open(Out, "w") as fp:
        fp.write(json.dumps(jsonData, indent=4))


def add(username, tweet):
    tweets["tweets"].append({
        "text": tweet,
        "username": username,
    })
    save("/Tweet.json", tweets)


tweets = load("Tweet.json")
choice = ["1", "2", "3"]
while True:
    print("1. Print tweet\n2. Add tweet\n3. Quit")
    choice = input(" ")

    if (choice == "1"):
        for tweet in tweets["tweets"]:
            print(f"{tweet['username']}:", tweet["text"].replace("\n", " "))
    elif (choice == "2"):
        username = input("Your username? ")
        text = input("Your text\n> ")
        add(username, text)
    elif (choice == "3"):
        break
    else:
        continue