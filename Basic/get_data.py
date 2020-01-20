import os
import yaml


def getData(funcname, file):

    # fileInfo = inspect.stack()[1]
    # fileName = fileInfo.filename
    # dotIndex = fileName.rfind(".")
    # underlineIndex = fileName.rfind("_")
    # fileName = fileName[underlineIndex:dotIndex]
    PATH = os.getcwd() + os.sep

    with open(PATH + 'Data/' + file + '.yaml', 'r', encoding="utf8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    # with open('./data/data'+fileName+'.yaml', 'r', encoding="utf8") as f:
    #     data = yaml.load(f, Loader=yaml.FullLoader)

    # 1 先将我们获取到的所有数据都存放在一个变量当中
    tmpdata = data[funcname]

    # 2 所以此时我们需要使用循环走进它的内心。
    res_arr = list()
    for value in tmpdata.values():
        tmp_arr = list()
        for j in value.values():
            tmp_arr.append(j)

        res_arr.append(tmp_arr)

    return res_arr