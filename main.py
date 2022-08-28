import os
import pywhatkit
import datetime


class WhatsAppMessage:
    def __init__(self, message_immediately='Hello, its immediately message!', message_after_time='Hi, its '
        'message after 30 seconds!', mobile_number='+79175955650'):
        self.message_immediately = message_immediately
        self.message_after_time = message_after_time
        self.mobile_number = mobile_number

    def send_imm_message(self):
        pass

    def send_after_time_message(self):
        pass


if __name__ == '__main__':
    send_message_obj_1 = WhatsAppMessage()
    send_message_obj_1.send_imm_message()

    send_message_obj_2 = WhatsAppMessage()
    send_message_obj_2.send_after_time_message()
