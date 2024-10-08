from .handle import NotificationHandle
from CEACStatusBot.request import query_status
from CEACStatusBot.utils import read, write
from CEACStatusBot.captcha import CaptchaHandle,OnnxCaptchaHandle

class NotificationManager():
    def __init__(self,location:str,number:str,passport_number:str,surname:str,captchaHandle:CaptchaHandle=OnnxCaptchaHandle("captcha.onnx")) -> None:
        self.__handleList = []
        self.__location = location
        self.__number = number
        self.__captchaHandle = captchaHandle
        self.__passport_number = passport_number
        self.__surname = surname

    def addHandle(self, notificationHandle:NotificationHandle) -> None:
        self.__handleList.append(notificationHandle)

    def send(self,) -> None:
        res = query_status(self.__location, self.__number, self.__passport_number, self.__surname, self.__captchaHandle)

        status = read()
        if status == res['status']:
            print("No status change")
            return
        write_result = write(res['status'])
        print(write_result)

        for notificationHandle in self.__handleList:
            notificationHandle.send(res)
