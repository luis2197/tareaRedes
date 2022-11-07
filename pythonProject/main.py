import time
import tweepy


time.sleep(600)
# apykey, secret apykey
auth= tweepy.OAuthHandler("27Wl8ZNkK9XBVsigy2In7OwZ2","XnGG6mdmOxQJSRgWhl4idfUirk1BUAIUI385A6hZwrv73Wrop6")
# access token, secret access token
auth.set_access_token("52285980-I1vRpGSv0atRmJub7ZT5hUqzwiPIHRYjrXp1xPpYI","kK7q9y27seFi8ThXnZzAin3HMI7xp6NZaaTXlKqk39sAL")
apiTweeter=tweepy.API(auth)
status = "#salvandoRedes2022IC \n-Emilio \n-Brian"
# posting the tweet
apiTweeter.update_status(status)