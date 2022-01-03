import pytest

pytest.main(['-s','-v','--reruns',"2",'--reruns-delay','5','--alluredir=allure','-m mark1'])
