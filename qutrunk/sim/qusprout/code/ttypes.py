#
# Autogenerated by Thrift Compiler (0.16.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class ErrCode(object):
    COM_SUCCESS = 0
    COM_OTHRE = 1
    COM_INVALID_PARAM = 2
    COM_TIMEOUT = 3
    COM_EXCEPTION = 4
    QUROOT_MEM_NOT_ENOUGH = 100
    QUROOT_NOT_INIT = 101
    QUROOT_NOT_REGISTER = 102
    QUROOT_NOT_RESOURCE = 103

    _VALUES_TO_NAMES = {
        0: "COM_SUCCESS",
        1: "COM_OTHRE",
        2: "COM_INVALID_PARAM",
        3: "COM_TIMEOUT",
        4: "COM_EXCEPTION",
        100: "QUROOT_MEM_NOT_ENOUGH",
        101: "QUROOT_NOT_INIT",
        102: "QUROOT_NOT_REGISTER",
        103: "QUROOT_NOT_RESOURCE",
    }

    _NAMES_TO_VALUES = {
        "COM_SUCCESS": 0,
        "COM_OTHRE": 1,
        "COM_INVALID_PARAM": 2,
        "COM_TIMEOUT": 3,
        "COM_EXCEPTION": 4,
        "QUROOT_MEM_NOT_ENOUGH": 100,
        "QUROOT_NOT_INIT": 101,
        "QUROOT_NOT_REGISTER": 102,
        "QUROOT_NOT_RESOURCE": 103,
    }


class BaseCode(object):
    """
    Attributes:
     - code
     - msg

    """


    def __init__(self, code=None, msg=None,):
        self.code = code
        self.msg = msg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.msg = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('BaseCode')
        if self.code is not None:
            oprot.writeFieldBegin('code', TType.I32, 1)
            oprot.writeI32(self.code)
            oprot.writeFieldEnd()
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRING, 2)
            oprot.writeString(self.msg.encode('utf-8') if sys.version_info[0] == 2 else self.msg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.code is None:
            raise TProtocolException(message='Required field code is unset!')
        if self.msg is None:
            raise TProtocolException(message='Required field msg is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(BaseCode)
BaseCode.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'code', None, None, ),  # 1
    (2, TType.STRING, 'msg', 'UTF8', None, ),  # 2
)
fix_spec(all_structs)
del all_structs