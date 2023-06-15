from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (500, 700)

class SignUpScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class MenuScreen(Screen):
    pass

class login(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        self.sm = ScreenManager()

        self.sm.add_widget(LoginScreen(name='Login'))
        self.sm.add_widget(SignUpScreen(name='SignUpScreen'))
        self.sm.add_widget(MenuScreen(name='Menu'))

        return self.sm

    def send_data(self, email, password):
        from firebase import firebase
        # inicializar firebase
        firebase = firebase.FirebaseApplication('https://login-62f2e-default-rtdb.firebaseio.com/', None)
        # importar data
        data = {
            'Email': email,
            'Password': password
        }
        # postear data
        # nombre db/nombre tabla
        firebase.post('https://login-62f2e-default-rtdb.firebaseio.com/Users', data)

    def get_data(self, email, password):

        from firebase import firebase
        # inicializar firebase
        firebase = firebase.FirebaseApplication('https://login-62f2e-default-rtdb.firebaseio.com/', None)

        # Get data
        result = firebase.get('https://login-62f2e-default-rtdb.firebaseio.com/Users', '')
        # print(result)

        # verificar email y contraseña
        for i in result.keys():
            if result[i]['Email'] == email:
                if result[i]['Password'] == password:
                    self.sm.get_screen('Menu').ids.greeting_label.text = "Hola " + email
                    self.sm.current = 'Menu'
                else:
                    print("Wrong data")


if __name__ == '__main__':
    login().run()


'''
#importar data
data = {
    'Email':'gatito@gmail.com',
    'Password':'12345'
}

#postear data
#nombre db/nombre tabla
firebase.post('https://login-62f2e-default-rtdb.firebaseio.com/Users',data)
'''
'''
#Get data
result = firebase.get('https://login-62f2e-default-rtdb.firebaseio.com/Users', '')
#print(result)

#Get Specific column
for i in result.keys():
    print(result[i]['Email'])
'''