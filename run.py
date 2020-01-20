import os
import shutil
import subprocess
import time
from Basic import Log
import pytest

PATH = os.path.split(os.path.realpath(__file__))[0]
xml_report_path = PATH + "/report/xml"
html_report_path = PATH + "/report/html"
tm = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))


def invoke(md):
    output, errors = subprocess.Popen(md,
                                      shell=True,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    return o


if __name__ == '__main__':
    log = Log.MyLog()
    log.info(
        "---------------------------START: %s------------------------------"
        % tm)
    shutil.rmtree(xml_report_path)
    args = ['-s', '-q', '--alluredir', xml_report_path]
    pytest.main(args)
    cmd = 'allure generate %s -o %s --clean' % (xml_report_path,
                                                html_report_path)
    invoke(cmd)
    log.info(
        "-----------------------------END: %s-------------------------------"
        % tm)
