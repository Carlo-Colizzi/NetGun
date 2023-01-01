import os

class Filter:
    __TRANSPORT_PROTOCOLS_SUPPORTED = {"tcp":"","udp":"-sU"}

    def __init__(self, transport_protocol: str = "tcp", advanced_options : list[str] = None, threads : int = 1):
        assert transport_protocol in Filter.__TRANSPORT_PROTOCOLS_SUPPORTED, "Invalid Transport Protocol Selected. Use TCP or UDP"
        self.transport_protocol = transport_protocol
        self.advanced_options = ""

        if advanced_options is not None:
            self.advanced_options += Filter.advanced_options_to_string(advanced_options)
        else:
            self.advanced_options = ""

        self.advanced_options += " " + Filter.__TRANSPORT_PROTOCOLS_SUPPORTED[transport_protocol]

        assert Filter.check_threads(threads) == True, "Invalid Threads Number check_threads(threads) failed"
        self.threads = threads


    @classmethod
    def advanced_options_to_string(self, advanced_options : list[str]):
        output = ""
        for option in advanced_options:
            output += " -" + option

        return output

    @classmethod
    def check_threads(cls, threads : int):
        effective_threads = os.cpu_count()
        if threads > 0 and threads < (effective_threads - 2):
            return True
        else:
            return False
