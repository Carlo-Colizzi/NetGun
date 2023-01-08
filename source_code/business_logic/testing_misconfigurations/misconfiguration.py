import pyautogui
import time
class Misconfiguration:

    def __int__(self):
        pass

    def print_toString(self):
        print("tool_installation: ",self.tool_installation)
        print("testType: ", self.testType)
        print("description: ",self.description)
        print("command: ",self.command)

    def test_misconfiguration(self):
        """Opens a new terminal and write in the command for execute the test"""
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(0.05)
        pyautogui.typewrite(self.command)


if __name__ == "__main__":
    m = Misconfiguration()
    m.command = "ftp 127.0.0.1"
    m.test_misconfiguration()
