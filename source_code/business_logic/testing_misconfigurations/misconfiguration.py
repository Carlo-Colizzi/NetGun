import pyautogui
import time
class Misconfiguration:

    def __int__(self):
        pass

    def print_toString(self):
        print(self.tool_installation)
        print(self.testType)
        print(self.description)
        print(self.command)

    def test_misconfiguration(self):
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(0.05)
        pyautogui.typewrite(self.command)


m = Misconfiguration()
m.command = "ftp 127.0.0.1"
m.test_misconfiguration()
