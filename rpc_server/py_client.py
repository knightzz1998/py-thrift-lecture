# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 8:16
# @Author  : 王天赐
# @Email   : 15565946702@163.com
# @File    : py_client.py
# @Software: PyCharm

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

from thrift_generator import PersonService

try:
    tSocket = TSocket.TSocket('localhost', 8899)
    # 定义传输对象
    transport = TTransport.TFramedTransport(tSocket)
    # 创建协议对象
    protocol = TCompactProtocol.TCompactProtocol(transport)
    # 创建客户端
    client = PersonService.Client(protocol)
    # 开启通道
    transport.open()

    person = client.getPersonByUsername(username="张三")
    print(person.username)
    print(person.age)
    print(person.married)

    print("====================> ")

    # 关闭通道
    transport.close()

except Thrift.TException as tx:
    print(tx.message)
