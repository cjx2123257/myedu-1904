import allure
import pytest
from day004 import read_excel

excel_list = read_excel.read_excel_list('./day004/exe.xlsx')
ids_list = []
for i in range(len(excel_list)):
    ids_pop = excel_list[i].pop()
    ids_list.append(ids_pop)

@allure.feature('测试字符串')
class Test_bb:
    @allure.story('实际测试')
    @pytest.mark.parametrize('astr,msg',
                             [['成功','登录成功'],['错误','登录错误'],['错误','登录成功']],
                             ids= ['测试正确','测试正确','测试异常'])
    def test_dd(self,astr,msg):
        assert astr in msg

    @allure.story('实际测试参数化')
    @pytest.mark.parametrize('astr,msg',excel_list,ids=ids_list)
    def test_cjx(self,astr,msg):
        assert astr in msg




