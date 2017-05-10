# HTMLTestRunner
HTMLTestRunner Python 3.6+ Code

HTMLTestRunner is a tool for getting nice, presentable HTML reports while running Selenium tests using PyUnit.

HTMLTestRunner was based on Python 2.0, so it was not being used for Python 3.0+ tests.

Now I have ported the code to Python 3.0+ compatible format.

All license are in name of Wai Yip Tung.

Fixed by akui 2017-05-10：The name should be HTMLTestRunner.
运行案例:
确保Python3.6+已经安装
双击"runcmd.bat"

运行：python TestComputer.py
你会看到HTML结果被打印到了终端上。

运行：python TestComputer.py > result.html
将输出结果重定向到result.html文件。运行结束你会看到有一个result.html的文件生成了。双击可以通过浏览器打开生成的结果文件。

运行：python TestComputerSuite.py
你会看到生成来了一个HTML报告computerTest.html。
