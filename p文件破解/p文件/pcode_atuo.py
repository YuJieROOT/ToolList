
import json
import requests
import time
#  r = requests.post(url='',data={'type':'file','name':'value2'},headers={'Content-Type':'application/x-www-form-urlencoded'})

# requests.post(url='',data={'key1':'value1','key2':'value2'},headers={'Content-Type':'multipart/form-data'})
from requests_toolbelt import MultipartEncoder
import os

# 当前目录
base_dir = 'E:\\RL_highway_ws\\CANedge\\examples\\data-processing\\MQ\\'
mDirectory = 'E:\\RL_highway_ws\\CANedge\\examples\\data-processing\\MQ_fail_m\\'#os.path.dirname(path)
base_dir = 'E:\\RL_highway_ws\\CANedge\examples\\data-processing\\fail_pfile\\'
# 获取当前目录下的所有文件
filepaths = [os.path.join(base_dir, file) for file in os.listdir(base_dir)]
url = 'http://web-service.sippey.org//cgi-bin//de_pcode.py'
fail_fileName = list()
# 遍历文件列表，输出文件名
for file in filepaths[0:]:
    print(file)
# file_p = {'file': open(file, 'rb')}

    body = MultipartEncoder(
        fields={'pfile': ('fdBasicsRoot.p', open(file, 'rb'), 'text/plain')}
    )
    r = requests.post(url, data=body ,headers={'Content-Type': body.content_type})    # 'multipart/form-data'
    # r = requests.post(url, files=files )
    # 使用open()函数创建文件并打开，指定文件名和打开模式为“写”（'w'）
    # 如果文件不存在则新建，如果文件存在则覆盖原有内容
    time.sleep(0.1)
    filename = os.path.basename(file)
    file_m_path = mDirectory+filename[0:-1]+'m'
    file_m = open(file_m_path, "w")
    # 使用write()函数将数据写入文件
    try:
        file_m.write(r.text)
    except:
        fail_fileName.append(file_m_path)
        print(f'fail file write{file_m_path}')
    finally:
        file_m.close()
    fail_fileName.append(file_m_path)


    # 关闭文件

