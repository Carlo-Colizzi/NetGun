import pytest
from source_code.business_logic.report.report import Report

def make_tesable(function):
    def wrapper(*args,**kwargs):
        try:
            return function()
        except BaseException:
            return False
    return wrapper
class Test_create_report:

    def test_max_lenght_path():
        path = "/home/pc_user/filenamedwdwfdwehfuoefhowhfsdhiuhviuehviushviuewqhfviuhewqipuhgbeuhwqvrbuoewqgbfuoewqyrcfbuhogqygbyuhgbqyfhgeyugcbqeuwydrgwycgvuwycevbquyhwgvbwuhdgvcuhdgvcquhdwvcuhdvbcuohwqvedbcuhqdvbcuqwvbcuhdqcbihqedrcbiqprjebnvciedskjcpkjamcnpkjndmcknsadcoknajdcnkjsdnc.txt"
        report = Report(path)
        report.create_report = make_tesable(report.create_report())
        assert report == True