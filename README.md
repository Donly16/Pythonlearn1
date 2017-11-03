# Pythonlearn1
This an Android Test using python unittest and appium
There is params excel file
It can auto make excel result files

手机的参数配置在 salon/params.py文件中
用户数据从excel中读入，可从excel中控制用例的执行
excel中可指定该条用例执行的结果期望是成功还是失败。如果实际执行结果和期望值一致，则表示该用例执行成功。
执行完成之后，每个用例的执行结果会额外保存在excel表格中
