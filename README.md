# LendUpChallenge
A coding challenge for LendUp, using Twilio's API to play the Fizz Buzz game.

## Overview
The provided code fulfills the first and second phases of the coding challenge. I used Flask as my microframework of choice (though this is my first time) to interact with Twilio's API and to handle the correct HTTP requests and responses. To test the application, I used ngrok as a tunnel to my local server. 

## How to Execute
To run the code, simply change the values in `config.py` as follows:
```
account_sid: Change to your Twilio SID
auth_token: Change to your Twilio authentication token
from_num: Change to your registered Twilio phone number in the form "+1XXXXXXXXXX"
greet_url: Change to the URL that hosts your greet() view
```

## Things to Note
Because I used ngrok as my tunnel, this created the issue of only having one URL that pointed to the root even though I needed another to redirect to the actual voice prompt (`greet()` and `fizz_buzz()`). This could be circumvented by using a service that allows for more than one URL, separating our `/` and `/greet` routes. For the future, I would look into finding such a service as well as implementing the final phases.
