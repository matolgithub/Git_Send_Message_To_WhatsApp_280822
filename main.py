import pywhatkit
import datetime


class WhatsAppMessage:
    def __init__(self, message_immediately='Hello, its immediately message!', message_after_time='Hi, its '
        'message after 1 minutes!', mobile_number='+7*******', email='*********@mail.ru'):
        self.message_immediately = message_immediately
        self.message_after_time = message_after_time
        self.mobile_number = mobile_number
        self.email = email


    def send_imm_message(self):
        imm_message = self.message_immediately
        pywhatkit.sendwhatmsg_instantly(phone_no=self.mobile_number, message=imm_message)
        print(f'The message: "{imm_message}" will be send to mobile number: {self.mobile_number}.')

    def send_after_time_message(self):
        hour = str(datetime.datetime.now().time())
        need_hour = int(hour[: 2])
        need_minutes = int(hour[3: 5]) + 1
        after_time_message = self.message_after_time
        pywhatkit.sendwhatmsg(phone_no=self.mobile_number, message=after_time_message, time_hour=need_hour,
                                        time_min=need_minutes)
        print(f'The message: "{after_time_message}" will be send to mobile number: {self.mobile_number}.')


    def send_email(self):
        pywhatkit.send_mail(email_sender=self.email, password='********', subject='Letter',
                            message='Hello', email_receiver=self.email)
        print(f'The letter send to {self.email} at {datetime.datetime.now()}.')

    def send_image(self):
        image_path = 'https://myt-info.ru/userfiles/proekty/20201230082951666072.jpg'
        file_name = image_path.split('/')[-1]
        pywhatkit.sendwhats_image(receiver=self.mobile_number, img_path=image_path, caption='shatun')
        print(f'Image {file_name} send to mobile: {self.mobile_number} at {datetime.datetime.now()}.')


if __name__ == '__main__':
    send_message_obj_1 = WhatsAppMessage()
    send_message_obj_1.send_imm_message()

    send_message_obj_2 = WhatsAppMessage()
    send_message_obj_2.send_after_time_message()

    send_message_obj_3 = WhatsAppMessage()
    send_message_obj_3.send_email()

    send_message_obj_4 = WhatsAppMessage()
    send_message_obj_4.send_image()
