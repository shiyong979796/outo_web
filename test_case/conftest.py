#:@ TIME 2021/12/20   0:01
#:@FILE  conftest.py
#:@EMAIL  1557225637@QQ.COM
import pytest
import time
from common.log import logg

from selenium import webdriver
@pytest.fixture(scope='class')
def init_fixture():
    logg.info("==========   class级  前置条件：打开Chrome浏览器，访问登录页面    ==========")
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.azazie.com")
    time.sleep(2)
    yield driver
    logg.info("==========   class级  后置条件：关闭浏览器    ==========")
    driver.quit()

@pytest.fixture
def back_login_page(init_fixture):
    logg.info('==========   function级   前置条件：刷新浏览器')
    init_fixture.refresh()
    yield init_fixture


