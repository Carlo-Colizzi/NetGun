import pytest

from source_code.business_logic.report.report import Report

class Test_create_report:

    @pytest.mark.TC1_3_01
    def test_max_lenght_path(self):
        path = "/home/pc_user/filenamedwdwfdwehfuoefhowhfsdhiuhviuehviushviuewqhfviuhewqipuhgbeuhwqvrbuoewqgbfuoewqyrcfbuhogqygbyuhgbqyfhgeyugcbqeuwydrgwycgvuwycevbquyhwgvbwuhdgvcuhdgvcquhdwvcuhdvbcuohwqvedbcuhqdvbcuqwvbcuhdqcbihqedrcbiqprjebnvciedskjcpkjamcnpkjndmcknsadcoknajdcnkjsdnc.txt"
        assert Report.check_path(path) == False

    @pytest.mark.TC1_3_02
    def test_standard_path(self):
        path = "/home/users/Documents/filename.txt"
        assert Report.check_path(path) == True

    @pytest.mark.TC1_3_03
    def test_multiple_slash(self):
        path = "/home/users///Documents///filenamedwdwfdwehfuoefhowhfsdhiuhviuehviushviuewqhfviuhewqipuhgbeuhwqvrbuoewqgbfuoewqyrcfbuhogqygbyuhgbqyfhgeyugcbqeuwydrgwycgvuwycevbquyhwgvbwuhdgvcuhdgvcquhdwvcuhdvbcuohwqvedbcuhqdvbcuqwvbcuhdqcbihqedrcbiqprjebnvciedskjcpkjamcnpkjndmcknsadcoknajdcnkjsdnc.txt"
        assert Report.check_path(path) == False

    @pytest.mark.TC1_3_04
    def test_inverted_slash(self):
        path =  "//home\pcexp//filereport.txt"
        assert Report.check_path(path) == False




