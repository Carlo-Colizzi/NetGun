import math
import speedtest

class Network_test:
    """Class used for Test Network Performance"""

    def __init__(self):
        try:
            self.network = speedtest.Speedtest()
        except:
            raise ConnectionError("The internet connection seems to be down")
    def test_download(self):
        """Test the upload speed of the connection"""
        bytes = self.network.download()
        mbps = Network_test.bytes_to_mbps(bytes)
        return mbps

    def test_upload(self):
        """Test the download speed of the connection"""
        bytes = self.network.upload()
        mbps = Network_test.bytes_to_mbps(bytes)
        return mbps

    @classmethod
    def bytes_to_mbps(cls,bytes):
        """Convert from bytes to Mbps"""
        i = int(math.floor(math.log(bytes, 1024)))
        power = math.pow(1024, i)
        mbps = round(bytes / power, 2)
        return mbps

if __name__ == "__main__":
    print("Starting Test")
    n = Network_test()
    print("Download: ", n.test_download(), " Mbps")
    print("Upload: ", n.test_upload(), " Mbps")