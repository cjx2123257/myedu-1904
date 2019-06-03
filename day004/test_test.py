import  allure

@allure.feature("测试功能")

class Test_order:

    @allure.story("下订单")
    def test_order_add(self):

        assert '失败' in  '操作失败'
    @allure.story("发货")
    def test_order_to_wh(self):

        assert '成功' in '操作成功'
