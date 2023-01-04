import math
import speedtest

class Network_test:

    def __init__(self):
        self.network = speedtest.Speedtest()

    def test_download(self):
        bytes = self.network.download()
        mbps = Network_test.bytes_to_mbps(bytes)
        return mbps

    def test_upload(self):
        bytes = self.network.upload()
        mbps = Network_test.bytes_to_mbps(bytes)
        return mbps

    @classmethod
    def bytes_to_mbps(cls,bytes):
        i = int(math.floor(math.log(bytes, 1024)))
        power = math.pow(1024, i)
        mbps = round(bytes / power, 2)
        return mbps

if __name__ == "__main__":
    print("Starting Test")
    n = Network_test()
    print("Download: ", n.test_download(), " Mbps")
    print("Upload: ", n.test_upload(), " Mbps")