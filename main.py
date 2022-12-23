import requests
from datetime import datetime
import smtplib

MY_LAT = 23.634501
MY_LONG = -102.552788
#http://open-notify.org/Open-Notify-API/ISS-Location-Now/

def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()

#ISS_POSITION

    iss_longitude=float(data["iss_position"]["longitude"])
    iss_latitude=float(data["iss_position"]["latitude"])



#MEXICO


    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LONG-5<=iss_longitude<=MY_LONG+5:
        return True



def is_night():
    parameters={
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0,
    }
    currentDateAndTime =datetime.now()


    response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()


    sunrise=int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset=int(data['results']['sunset'].split("T")[1].split(":")[0])

    currentTime = datetime.now().hour

    #print("The current time is", currentTime)



    if currentTime>=sunset and currentTime<=sunrise:

        return True



if is_night() and is_iss_overhead():
    my_email="anaidbrachomolina@gmail.com"
    password="jnlxikwrixoxbrux"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="itzelbrachomolina@gmail.com",
            msg=f"Subject:Look up \n\n The ISS is above in the sky")







