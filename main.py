import kivy.app
from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from submit import submit
import ipaddress

LabelBase.register(name="DroidSansMono",
                   fn_regular="DroidSansMono.ttf"
                   )


class MainWindow(Screen):
    switch = 'ip'

    def submitbtn(self):
        try:
            ipaddress.IPv4Address(self.ip.text)
            ipaddress.IPv4Network(self.mask.text)
        except:
            return
        result = submit(self.ip.text, self.mask.text)
        popup = Popup(title='Result:',
                      content=Label(text=result, font_name="DroidSansMono", font_size=13),
                      size_hint=(.85, .6))
        popup.open()

    def switchToMask(self):
        try:
            ipaddress.IPv4Address(self.ip.text)
        except:
            return
        ip = [int(i) for i in self.ip.text.split('.')]
        MainWindow.switch = 'mask'
        if ip[0] < 128:
            self.mask.text = '255.'
        elif ip[0] < 192:
            self.mask.text = '255.255.'
        else:
            self.mask.text = '255.255.255.'
        self.masklable.text = 'Subnet Mask:'
        self.iplable.text = 'IP Address'
        # self.masklable.font_size = 16
        # self.iplable.font_size = 13

    def switchToIp(self):
        MainWindow.switch = 'ip'
        self.iplable.text = 'IP Address:'
        self.masklable.text = 'Subnet Mask'
        # self.iplable.font_size = 16
        # self.masklable.font_size = 13

    def one(self):
        if MainWindow.switch == 'ip':
            self.ip.text += '1'
        else:
            self.mask.text += '1'

    def two(self):
        if MainWindow.switch == 'ip':
            self.ip.text += '2'
        else:
            self.mask.text += '2'

    def three(self):
        if MainWindow.switch == 'ip':
            self.ip.text += '3'
        else:
            self.mask.text += '3'

    def four(self):
        if MainWindow.switch == 'ip':
            self.ip.text += '4'
        else:
            self.mask.text += '4'

    def five(self):
        if MainWindow.switch == 'ip':
            self.ip.text += '5'
        else:
            self.mask.text += '5'

    def six(self):
        if MainWindow.switch == 'ip':
            self.ip.text += '6'
        else:
            self.mask.text += '6'

    def seven(self):
        if MainWindow.switch == 'ip':
            self.ip.text += '7'
        else:
            self.mask.text += '7'

    def eight(self):
        if MainWindow.switch == 'ip':
            self.ip.text += '8'
        else:
            self.mask.text += '8'

    def nine(self):
        if MainWindow.switch == 'ip':
            self.ip.text += '9'
        else:
            self.mask.text += '9'

    def zero(self):
        if MainWindow.switch == 'ip':
            self.ip.text += '0'
        else:
            self.mask.text += '0'

    def dot(self):
        if MainWindow.switch == 'ip':
            self.ip.text += '.'
        else:
            self.mask.text += '.'

    def backspace(self):
        if MainWindow.switch == 'ip':
            self.ip.text = self.ip.text[:-1]
        else:
            self.mask.text = self.mask.text[:-1]


class IPConverter(kivy.app.App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    IPConverter().run()
