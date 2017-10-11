import unittest
from function import *
from BSTestRunner import BSTestRunner
import time



report_dir='./test_report'
test_dir='./test_case'

print("start run test case")
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_useraction.py")

now=time.strftime("%Y-%m-%d %H_%M_%S")
report_name=report_dir+'/'+now+'result.html'

print("start write report..")
with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title="Test report",description="220前端的测试报告")
    runner.run(discover)
    f.closed
print("end")
# print("find lastest report")
# latest_report=latest_report(report_dir)
#
# print("send email report...")
# send_mail(latest_report)
#
# print("end")


