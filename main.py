import re
import urllib.request
import smtplib, ssl
import time

def siunciam_zinute(rasti_list):

    port = 465  # For SSL
    smtp_server = "smtp.hostinger.com"
    sender_email = "info@test.lt"  # Enter your address
    receiver_email = "info@test.com"  # Enter receiver address
    password = "test"
    # password = input("Type your password and press enter: ")
    message =f"""From: info@test.lt\nTo: info@test.com\nSubject: CVPP Tikrinimo program rado atitikmeni\nNaujas Airsoft atitikmuo CVPP feede"""

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print("Laiskas issiustas")
    except:
        print("Nepavyko issiusti laisko")
rasti_list=[0]
pauze=90
while True:
    print("Bandom")

    with urllib.request.urlopen('https://cvpp.eviesiejipirkimai.lt/Rss/Feed') as response:
        html = str(response.read().decode('utf8'))
        # compileris = re.compile(r'''Medicinos+.[\w ąčęėįšųūž]+</summary><published>2022\W\d{2}-\d{2}T\d{2}:\d{2}:\d{2}''',re.I)
        compileris = re.compile(r'''Airsoft+.[\w ąčęėįšųūž]+</summary><published>2022\W\d{2}-\d{2}''',re.I)
        result=compileris.findall(html)
        print(result)
        if result == []:
            print(f"Airsoft atitikmenu dar nera, programa uzdaroma po {pauze} sekundziu")
            time.sleep(pauze)
            break
        else:
            for rastas in result:
                with open("rasti.txt", "r", encoding="UTF-8") as failas:
                    # visi=failas.read()
                # print(rastas)
                    if rastas in failas.read():
                        print("Nieko naujo")
                    else:
                        print(f"Dar tokio nera irasom: {rastas}")
                        rasti_list.append(rastas)
                        with open("rasti.txt", "a+", encoding="UTF-8") as to_failas:
                            to_failas.write(f"{rastas}\n")
                        siunciam_zinute(rasti_list)
                        print(f"Programos Pauze {pauze} sekundziu")
                        time.sleep(pauze)
                        break

