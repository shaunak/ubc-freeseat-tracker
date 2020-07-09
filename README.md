# course-freeseat-tracker

This was created because some departments dont do waitlists (MATH) and I wanted to take Math 344 (Game theory). <br>

Instructions: <br>
You'll need a Twilio account: www.twilio.com/referral/KDkBss (this is my referral link :)) 

once you've set up a Twilio phone number, create a file called secrets.py like so:


    TWILIO_ACCOUNT_SID = ""

    TWILIO_AUTH_TOKEN = ""

    MY_PHONE_NUMBER = ""

    MY_TWILIO_NUMBER = ""



and fill out the fields appropriately. `MY_PHONE_NUMBER` is the number that will be texted.

In main.py, replace COURSE_URL with whatever UBC SSC link you want. <br>

You can use "sudo python3 -m pip install -r requirements.txt" to install the required dependencies on Linux.


if you dont want to deal with all the setup on your own machine, here is a repl -> https://repl.it/@shaunakt/ubc-freeseat-tracker#README.md
