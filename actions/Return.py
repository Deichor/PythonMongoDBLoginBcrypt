from getpass import getpass
from actions import DataChecker
from database import Database
from configuration import Configuration


class Returner():

    def check_lenght(self, lgt):
        self.lgt = lgt
        if(len(lgt) > 5 and len(lgt) < 20):
            return True
        else:
            return False


    def get_name(self):
        
        db = Database.Database().db

        name_input = input('Kullanıcı ismi giriniz:')
        bool_lenght = Returner().check_lenght(name_input)
        cfg = Configuration.Configuration()
        dchecker = DataChecker.DataChecker(cfg.colltag + "users")
        

        if(bool_lenght == True):
            if(dchecker.check_name(name_input) == True):
                print("Kullanıcı ismi başarılı.")
                return name_input
            else:
                print("Kullanıcı ismi bulunamadı.")
                Returner().get_name()
        else:
            print("Kullanıcı ismi 5 karakterden kısa ve 20 karakterden uzun olamaz.")
            Returner().get_name()

    def get_password(self, name):

        password = getpass("Şifre giriniz:")
        bool_lenght = Returner().check_lenght(password)
        cfg = Configuration.Configuration()
        dchecker = DataChecker.DataChecker(cfg.colltag + "users")


        if(bool_lenght == True):
            if(dchecker.check_password(name, password) == True):
                return True
            else:
                print("Hatalı şifre girdiniz. Program sonlandı.")

                
        else:
            print("Şifre 5 karakterden kısa ve 20 karakterden uzun olamaz.")
            Returner().get_password(name)


    def get_input(self):

        name = Returner().get_name()
        password = Returner().get_password(name)
        if(password == True):
            print("Giriş başarılı.")
        

