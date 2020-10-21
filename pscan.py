import socket
import threading
import concurrent.futures
import os

os.system('cls && title SteinsPScanner')

common_ports = {
    "21": "FTP",
    "22": "SSH",
    "23": "Telnet",
    "25": "SMTP",
    "53": "DNS",
    "80": "HTTP",
    "194": "IRC",
    "443": "HTTPS",
    "853": "DNS over TLS",
    "3306": "MySQL",
}
#     ^  This will be for the next update
#     |

intro = """


        \033[1;31;40m_____ _       _\033[0m                                                       
       \033[1;31;40m/  ___| |     (_)\033[0m                                                      
       \033[1;31;40m\ `--.| |_ ___ _ _ __  ___\033[0m   _ __  ___  ___ __ _ _ __  _ __   ___ _ __ 
        \033[1;31;40m`--. \ __/ _ \ | '_ \/ __|\033[0m | '_ \/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|
       \033[1;31;40m/\__/ / ||  __/ | | | \__ \ \033[0m| |_) \__ \ (_| (_| | | | | | | |  __/ |   
       \033[1;31;40m\____/ \__\___|_|_| |_|___/\033[0m | .__/|___/\___\__,_|_| |_|_| |_|\___|_|   
                                   | |           
                                   |_| 

        \033[1;35;40m- Team Steins : iwa , bsx , p1n , xozh , aki, ein.
        - Github : https://github.com/St3ins | https://github.com/iwalsd
        - Beginner developer.
        - Steins Port Scanner.
        - /!\ Make sure to use URL like that -> randomsite.com | and not https://randomsite.com\033[0m


"""

print(intro)

print_lock = threading.Lock()

ip = input("Enter the \033[1;31;40mIP\033[0m or \033[1;31;40mURL\033[0m to scan :\033[1;32;40m ")
print('\n\033[0m')

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(5)
    try:
        scanner.connect((ip, port))
        socket.gethostbyname(ip)
        scanner.close()
        with print_lock:
            print(f"[Port: {port}]" + " \033[1;32;40mOpen !\033[0m")
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
     for port in range(4000):   #For change the range of the port, edit the number "4000".
           executor.submit(scan, ip, port + 1)

print('\033[1m\033[4m\nThanks you for using the Steins Port Scanner\033[0m, cya soon ! o/\033[0m')