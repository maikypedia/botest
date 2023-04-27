#!/usr/bin/python3

# IMPORT LIBRARIES
import requests
import re
import argparse
import time
import json

s = requests.session()

def hw():
        print("""
   __  ______ _    __   ____        __ 
  / / / / __ \ |  / /  / __ )____  / /_
 / / / / /_/ / | / /  / __  / __ \/ __/
/ /_/ / ____/| |/ /  / /_/ / /_/ / /_  
\____/_/     |___/  /_____/\____/\__/  
                                       
@maiky : Me gusta el Jagger, el reggeaton y los ordenadores. En ese orden.
    """)
# 1. DEFAULT DATA
pattern = '(?i)(?<=<td>)(.*)(?=<br>Solo)'
valid_pattern = '(?i)(?<=celista">)(.*)(?=<br>Solo)'
url = "https://intranet.upv.es:443/pls/soalu/sic_depact.HSemActividades?p_campus=V&p_tipoact=6607&p_codacti=20705&p_vista=intranet&p_idioma=c&p_solo_matricula_sn=&p_anc=filtro_actividad"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0", 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3", 
    "Accept-Encoding": "gzip, deflate", 
    "Referer": "https://intranet.upv.es/pls/soalu/sic_depact.HSemActividades?p_campus=V&p_tipoact=6607&p_vista=intranet&p_idioma=c&p_solo_matricula_sn=&p_anc=filtro_programa", 
    "Upgrade-Insecure-Requests": "1", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "same-origin", 
    "Sec-Fetch-User": "?1", 
    "Te": "trailers", 
    "Author": "maiky",
    "Connection": "close"
}
days = ["Lunes", "Martes", "Miércoles","Jueves","Viernes","Viernes"]

def login(user, passwd):
    login_url = "https://intranet.upv.es:443/pls/soalu/est_aute.intraalucomp"
    login_data = {"id": "c", "estilo": "500", "vista": '', "param": '', "cua": "miupv", "dni": user, "clau": passwd}
    s.post(login_url, data=login_data)

# 2.2 Returns an array with all those available MUXXX
def get_schedule():
    global r
    r = s.get(url)#, headers=headers, cookies=cookies)
    schedule = re.findall(valid_pattern, r.text)
    return schedule

def calc_time(i,id):
    time = id != 14 and id%14 or 14
    day = id > 14 and int(id/14) or 0
    time = time > 3 and "%s:30-%s:30" % (time+7, time+8) or "%s:30-%s:30" % (time+6, time+7)
    print(("[+] %s : %s : %s" % (days[day], time, i)))
    return [days[day], time]

# 3. Returns the time wit
def get_time(schedule):
    global links
    result = []
    for item in schedule:
        id = int(''.join(filter(str.isdigit, str(item))))

        time = id != 14 and id%14 or 14
        day = id > 14 and int(id/14) or 0
        time = time > 3 and "%s:30-%s:30" % (time+7, time+8) or "%s:30-%s:30" % (time+6, time+7)
        result.append("[+] %s : %s : %s" % (days[day], time, item))
    
    return result # sorted(result)

def reservar(item):
    link_pattern = '(?i)(?<=<a href=")(.*)(?=" class="upv_enlacelista">%s)' % str(item[-5:])
    link = re.findall(link_pattern, r.text)
    if len(link) != 0:
            s.get("https://intranet.upv.es/pls/soalu/" + link[0])
            print(item + " --> RESERVADO!")

def loop_reserva(item):
    while True:
        r = s.get(url)
        link_pattern = '(?i)(?<=<a href=")(.*)(?=" class="upv_enlacelista">%s)' % str(item[-5:])
        link = re.findall(link_pattern, r.text)
        if len(link) != 0:
            s.get("https://intranet.upv.es/pls/soalu/" + link[0])
            print(item + " --> RESERVADO!")
            break

def check_reserva():
    global r
    r = s.get(url)
    reserva_pattern = '(?i)MUSCULACIÓN \d{3}'
    reserva = re.findall(reserva_pattern, r.text)
    print("\n[?] Tus reservas :")
    for i in reserva:
        id = int(i[-3:])
        calc_time(i, id)
    return reserva 

def holy_func():
    for i in preferences:
            for x in items:
                if i in x:
                    reservar(x)
                    time.sleep(3)
                    check_reserva()
                    break

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--user', help='Username', required=True)
    parser.add_argument('-p','--password', help='PIN to login', required=True)
    parser.add_argument('-l','--list', help='List available schedule (Y/N)')
    parser.add_argument('-x','--preferencias', help='"MU002,MU003,MU025,MU026,MU053,MU054"')
    parser.add_argument('-b','--loop', help='Intentarlo hasta que esté disponible (Y/N)')
    args = parser.parse_args()
    user = args.user
    passwd = args.password
    list = args.list
    pref = args.preferencias
    loop = args.loop

    login(user, passwd)
    if (list == "Y" ):
        for i in get_time(get_schedule()):
            print(i)

    if pref:
        preferences = pref.split(",")
    else:
        preferences = []

    hw()

    items = get_time(get_schedule())

    if loop:
        while True:
            holy_func()
    else:
        holy_func()

