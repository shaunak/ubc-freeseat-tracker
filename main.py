import time
import re
from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

import secrets  # from secrets.py in this folder


def get_page_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page.content


def get_remaining_seats(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    tr_elem_list = list(soup.findAll("tr"))
    results = list(filter(lambda x: ("General Seats Remaining" in x.text or "Restricted Seats Remaining" in x.text), tr_elem_list))
    if len(results) < 2:
        return None
    seats = {"General": int(re.findall('\d+', results[0].text)[0]),
             "Restricted": int(re.findall('\d+', results[1].text)[0])}
    return seats



def setup_twilio_client():
    account_sid = secrets.TWILIO_ACCOUNT_SID
    auth_token = secrets.TWILIO_AUTH_TOKEN
    return Client(account_sid, auth_token)


def send_notification(general=False, restricted=False):
    twilio_client = setup_twilio_client()
    message = "There are seats availible of the following types: "
    if general:
        message += "GENERAL"
    if restricted:
        message += "RESTRICTED"
    print(message)
    twilio_client.messages.create(
        body=message,
        from_=secrets.MY_TWILIO_NUMBER,
        to=secrets.MY_PHONE_NUMBER
    )
    print('message sent')
    SystemExit()


def check_course_available():
    url = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=MATH&course=220&section=101"
    page_html = get_page_html(url)
    remaining_seats = get_remaining_seats(page_html)
    if remaining_seats["General"] != 0:
        send_notification(general=True)

    if remaining_seats["Restricted"] != 0:
        send_notification(restricted=True)
    else:
        print("General seats left: " + str(remaining_seats["General"]) + "\n Restricted seats left: "
              + str(remaining_seats["General"]))


while True:
    check_course_available()
    time.sleep(60)  # Wait a minute and try again
