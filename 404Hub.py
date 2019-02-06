import requests, threading, os, sys, time
os.system("clear")
os.system("cowsay -f eyes '404' | lolcat")
print 55*"\033[34;5m="
print ("\033[37;5mExample: \033[33;5mgrab.github.io")
bcotan = raw_input("\033[32;5mTarget Domain/IP: \033[31;5m")
req = requests.get("https://api.hackertarget.com/reverseiplookup/?q=" + (bcotan))
try:
    open("List.txt", "r")
except:
    co = raw_input ("\033[31m[\033[32m-\033[31m] \033[39mYou Have File List.txt, Do You Want To Replace? [Y/n]: ")
    if co =="Y" or co =="y":
        os.system("rm -f List.txt")
    else:
        pass
create = open("List.txt", "a")
create.close()

tu = open("Voss.txt", "w")
tu.write(req.text)
tu.close()
cok = open("Voss.txt", "r")
cad = open("Voss.txt", "r")
leno = cad.read().split()
print ("\033[33;5mTotal Web: \033[37;5m" + str(len(leno)))
hoho = len(leno)
time.sleep(0.5)
tai = "Tai Lu Mwuehehe"
print ("\033[32;5m[\033[33;5m+\033[32;5m]\033[37;5mWaiting For Get \033[31;5m404 \033[37;5mWeb....")
print 55*"\033[32;5m_"
def mulai(tek):
        global p
        p = 0
        while True:
          try:
            p +=1
            yah = cok.readline().strip()
            v = "http://" + (yah)
            try:
              cat = requests.get(v)
            except:
              continue
            if p > hoho:
                print ('\033[39m[\033[31m+\033[39m] \033[32mSuccess \033[39mCreate file "List.txt"')
                raw_input("\033[39m[\033[31mENTER\033[39m]")
                os.system("python2 termux-deface.py")
            if cat.status_code ==404:
                print ("\033[34;5m" + yah + " \033[35;5m>> \033[32m404")
                ba = open("List.txt", "a")
                ba.write(yah + "\n")
                ba.close()
                continue
            else:
               continue
          except KeyboardInterrupt:
            print("\033[31;5m[!]Keluar")
            sys.exit()
threads = []
for x in tai:
    t = threading.Thread(target=mulai, args=(tai,))
    threads.append(t)
    t.start()
for t in threads:
    t.join
