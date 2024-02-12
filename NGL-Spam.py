import requests
import os
import platform
from colorama import Fore, Style, init
import csv
import uuid
import random
import time
 
init(autoreset=True)

user_agents = []

    
with open('user-agent/1.csv', 'r', errors='ignore') as file:
    csv_reader = csv.DictReader(file)
    user_agents = [row['useragent'] for row in csv_reader]
    
with open('user-agent/2.csv', 'r', errors='ignore') as file:
    csv_reader = csv.DictReader(file)
    user_agents = [row['useragent'] for row in csv_reader]
    
def post(trgt, msg, count):
    
    try:    
        operating_system = platform.system()

        if operating_system == 'Windows':
            os.system('cls')
        elif operating_system == 'Linux' or operating_system == 'Darwin':
            os.system('clear')
        elif operating_system == 'Android':
            os.system('clear')
            
        
        i = 0
        while 1 <= count: 
            cookies = {
                'mp_e8e1a30fe6d7dacfa1353b45d6093a00_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18c3a29d602d12-00e76433d6ffc7-26031051-e1000-18c3a29d602d13%22%2C%22%24device_id%22%3A%20%2218c3a29d602d12-00e76433d6ffc7-26031051-e1000-18c3a29d602d13%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D',
                '_ga_5DV1ZR5ZHG': 'GS1.1.1701782871.1.0.1701782871.0.0.0',
                '_ga': 'GA1.1.73049771.1701782872',
            }

            headers = {
                'authority': 'ngl.link',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'mp_e8e1a30fe6d7dacfa1353b45d6093a00_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18c3a29d602d12-00e76433d6ffc7-26031051-e1000-18c3a29d602d13%22%2C%22%24device_id%22%3A%20%2218c3a29d602d12-00e76433d6ffc7-26031051-e1000-18c3a29d602d13%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; _ga_5DV1ZR5ZHG=GS1.1.1701782871.1.0.1701782871.0.0.0; _ga=GA1.1.73049771.1701782872',
                'origin': 'https://ngl.link',
                'referer': 'https://ngl.link/rhamaxx_',
                'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': str(random.choice(user_agents)),
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'username': trgt,
                'question': msg,
                'deviceId': str(uuid.uuid4),
                'gameSlug': '',
                'referrer': '',
            }

            response = requests.post('https://ngl.link/api/submit', cookies=cookies, headers=headers, data=data)

            if i != count:
                i+=1
                if response.status_code == 200:
                    print (f"{Fore.RED}[+]Success-{i}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}[+]Failed-{i}{Style.RESET_ALL}")
            else:
                break
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(f"{Fore.CYAN}Thank You :){Style.RESET_ALL}")


def main():
    while True:
        print(f'''{Fore.RED}
            
            __      _       __                       
        /\ \ \__ _| |     / _\_ __   __ _ _ __ ___  
        /  \/ / _` | |_____\ \| '_ \ / _` | '_ ` _ \ 
        / /\  / (_| | |_____|\ \ |_) | (_| | | | | | |
        \_\ \/ \__, |_|     \__/ .__/ \__,_|_| |_| |_|
            |___/           |_|                    

            Created By Xzionn
            {Style.RESET_ALL}              
                ''')
        target = input(f"{Fore.BLUE}Name User :{Style.RESET_ALL}")
        message = input(f"{Fore.BLUE}Message :{Style.RESET_ALL}")
        
        while True:
            try:
                count = int(input(f"{Fore.BLUE}Repeat :{Style.RESET_ALL}"))
                break
            except ValueError:
                print("Masukkan Angka")
        post(target, message, count)
        confirm = input("do you want to continue?(y/n)").lower()
        if confirm != "y":
            break
        else:
            if operating_system == 'Windows':
                os.system('cls')
            elif operating_system == 'Linux' or operating_system == 'Darwin':
                os.system('clear')
            elif operating_system == 'Android':
                os.system('clear')
        
main()
