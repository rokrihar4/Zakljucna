import requests
import time
import smtplib


# The URL you want to check
url = "https://telemach.si/naprave/iphone-15"

# Delay in seconds between each check
delay_seconds = 60  # Adjust this to your preferred delay (e.g., 60 seconds)

def link_exists(url):
    try:
        response = requests.head(url)
        if response.status_code >= 200 and response.status_code < 300:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

while True:
    if link_exists(url):
        print("Obstaja.")

        # # Your email sending code here
        # gmail_uporabnik = 'rok.rihar123@gmail.com'
        # gmail_geslo = 'sias wvap jcbr dzxt'

        # pošiljatelj_email = gmail_uporabnik
        # prejemnik_email = gmail_uporabnik

        # email_subject = "LAHKO KUPS IPHONE 15 BRTTTT!!"
        # email_message = "CIM PREJ ZRIHTI!"

        # try:
        #     with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        #         smtp.ehlo()
        #         smtp.starttls()
        #         smtp.login(gmail_uporabnik, gmail_geslo)
        #         smtp.sendmail(pošiljatelj_email, prejemnik_email, f"Subject: {email_subject}\n\n{email_message}")
        #         print('E-pošta je bila poslana uspešno!')
        # except Exception as e:
        #     print(e)

    else:
        print("Ne obstaja.")

    # Wait for the specified delay before checking again
    time.sleep(delay_seconds)
