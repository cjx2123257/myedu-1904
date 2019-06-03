import pytest
from day004 import Shell

if __name__ == '__main__':
    # pytest.main(['-s','-q','./day004'])
    shell = Shell.Shell()

    pytest.main(['-s','-q','--alluredir','./Report/xml/','./day004'])
    shell.invoke('allure generate ./Report/xml -o ./report/html')

