from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# ==============================================================
# BASE DE DATOS DE DEUDAS POR CLIENTE
# Agrega o modifica el monto de cada usuario individualmente.
# ==============================================================
DEUDAS_CLIENTES = {
    "Hum001": "15.00 Bs",
    "Hum004": "35.50 Bs",
    "Hum264": "120.00 Bs",
    # Agrega los demás usuarios siguiendo la misma estructura
}

# Monto que se mostrará si el usuario no tiene una deuda específica registrada
MONTO_POR_DEFECTO = "0.00 Bs"
# ==============================================================

KV = '''
ScreenManager:
    LoginScreen:
    PaymentScreen:

<LoginScreen>:
    name: 'login'
    canvas.before:
        Color:
            rgba: 0.98, 0.98, 0.98, 1
        Rectangle:
            pos: self.pos
            size: self.size
    
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20

        Label:
            text: "Acceso de Clientes"
            font_size: '28sp'
            color: 0.1, 0.1, 0.1, 1
            size_hint_y: 0.3

        TextInput:
            id: username
            hint_text: "Username (Ej: Hum001)"
            multiline: False
            size_hint_y: None
            height: '50dp'
            background_color: 1, 1, 1, 1

        TextInput:
            id: password
            hint_text: "Contraseña"
            password: True
            multiline: False
            size_hint_y: None
            height: '50dp'
            background_color: 1, 1, 1, 1

        Label:
            id: error_msg
            text: ""
            color: 1, 0, 0, 1
            size_hint_y: 0.1

        Button:
            text: "ENTRAR"
            bold: True
            size_hint_y: None
            height: '50dp'
            background_color: 0.8, 0.2, 0.2, 1
            on_release: root.verificar_credenciales()

        Label:
            text: "By: JP13"
            color: 0.4, 0.4, 0.4, 1
            size_hint_y: 0.2

<PaymentScreen>:
    name: 'payment'
    canvas.before:
        Color:
            rgba: 0.8, 0.15, 0.15, 1
        Rectangle:
            pos: self.pos
            size: self.size
    
    BoxLayout:
        orientation: 'vertical'
        padding: 30
        spacing: 20

        Label:
            id: lbl_deuda
            text: ""
            font_size: '35sp'
            bold: True
            halign: 'center'
            color: 1, 1, 1, 1
            size_hint_y: 0.4

        Label:
            text: "DATOS DEL PAGO MÓVIL:\\n\\nBanco Venezuela\\n0412-1136982\\n10.641.109\\n\\n¡Envía comprobante al mismo número!"
            font_size: '20sp'
            halign: 'center'
            color: 1, 1, 1, 1
            size_hint_y: 0.5

        Button:
            text: "CERRAR SESIÓN"
            bold: True
            size_hint_y: None
            height: '50dp'
            background_color: 0.2, 0.2, 0.2, 1
            on_release: app.root.current = 'login'
'''

class LoginScreen(Screen):
    def verificar_credenciales(self):
        user = self.ids.username.text.strip()
        password = self.ids.password.text.strip()
        
        if password != "1905":
            self.ids.error_msg.text = "Contraseña incorrecta"
            return
        
        if user.startswith("Hum"):
            try:
                num_str = user[3:]
                num = int(num_str)
                if 1 <= num <= 500:
                    self.ids.error_msg.text = ""
                    
                    # Buscar la deuda correspondiente a este usuario
                    monto_usuario = DEUDAS_CLIENTES.get(user, MONTO_POR_DEFECTO)
                    
                    # Pasar el monto y el usuario a la pantalla de pago
                    payment_screen = self.manager.get_screen('payment')
                    payment_screen.ids.lbl_deuda.text = f"DEBES:\\n{monto_usuario}"
                    
                    self.ids.username.text = ""
                    self.ids.password.text = ""
                    self.manager.current = 'payment'
                    return
            except ValueError:
                pass
        
        self.ids.error_msg.text = "Username inválido"

class PaymentScreen(Screen):
    pass

class VentaDulcesApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    VentaDulcesApp().run()
