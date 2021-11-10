# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 9:05
# @Author  : 王天赐
# @Email   : 15565946702@163.com
# @File    : py_server.py.py
# @Software: PyCharm


from thrift import Thrift

from service_impl.PersonServiceImpl import PersonServiceImpl
from thrift_generator import PersonService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer

try:
    personServiceHandler = PersonServiceImpl()
    # 设置自定义实现类
    processor = PersonService.Processor(personServiceHandler)
    # 创建服务Socket
    # TODO 这里特别注意, 服务端必须指定 host 必须是ip, 否则会出现连接被拒绝
    serverSocket = TSocket.TServerSocket(host='127.0.0.1', port=8989)
    # 通道对象
    transportFactory = TTransport.TFramedTransportFactory()
    # 协议对象
    protocolFactory = TCompactProtocol.TCompactProtocolFactory()
    # 单线程服务, 用于测试
    server = TServer.TSimpleServer(processor, serverSocket, transportFactory, protocolFactory)
    server.serve()
    print("server start ...")

except Thrift.TException as tx:
    print(tx.message)
