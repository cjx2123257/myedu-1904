import allure

@allure.feature("测试方法")

class Test_order2:

    @allure.story("下订单2")
    def test_order_add2(self):

        assert '失败' in  '操作失败'
    @allure.story("发货2")
    def test_order_to_wh2(self):

        assert '成功' in '操作成功'
