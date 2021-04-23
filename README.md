# Crypto Alert

This is an app to auto monitor your coin and automate purchases using [coinmarketcap](https://pro.coinmarketcap.com/account)

## 1. Fork the Repo

Fork this repo and create your own repo to work with.
[Forking a Repo](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo)

## 2. Install dependencies w/ Pipenv

We'll be using [pipenv](https://realpython.com/pipenv-guide/#:~:text=Pipenv%20is%20a%20packaging%20tool,a%20single%20command%20line%20tool.) to handle this, you can install it:

```shell
pip3 install pipenv
```

Once you have pipenv, run the following:

```shell
pipenv install --dev
```

## 3. Obtain API Keys

I'm using the 2 following apps for API's:

1. [Coinmarketcap API](https://coinmarketcap.com/api/)
2. [IFTTT](https://platform.ifttt.com/docs)
   - This one is a little tricky to setup. Maybe I'll provide cleaner documentation on how to do this later.

## 4. Create your key files

Create 2 files **"coinmarketcap.key"** & **"ifttt.key"**

Using terminal:

```shell
    touch coinmarketcap.key
    touch ifttt.key
```

copy & paste your respective keys into each file.

note:

``` shell
I'm using a .gitignore for all *.key files and I suggest you do the same to protect your API keys (However it should be included when you fork)
```

## 5. Running your code

The script is currently configured to run 1 time. You can modify it to run forever with a delay between messages.

``` shell
python3 crypto.py
```

## Future Ideas


- Autopurchase with a crytpo account  
    Open to Suggestions on this:
        - maybe coinbase
        - leaning towards uphold though

- Use Twitter API with an NLP model to predict the futures of Crypto
        - Use the [Twitter API Python Library](https://python-twitter.readthedocs.io/en/latest/)
