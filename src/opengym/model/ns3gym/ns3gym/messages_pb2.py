# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='ns3opengym',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0emessages.proto\x12\nns3opengym\x1a\x19google/protobuf/any.proto\"j\n\x10SpaceDescription\x12#\n\x04type\x18\x01 \x01(\x0e\x32\x15.ns3opengym.SpaceType\x12#\n\x05space\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04name\x18\x03 \x01(\t\"\x1a\n\rDiscreteSpace\x12\t\n\x01n\x18\x01 \x01(\x05\"V\n\x08\x42oxSpace\x12\x0b\n\x03low\x18\x01 \x01(\x02\x12\x0c\n\x04high\x18\x02 \x01(\x02\x12 \n\x05\x64type\x18\x03 \x01(\x0e\x32\x11.ns3opengym.Dtype\x12\r\n\x05shape\x18\x04 \x03(\r\";\n\nTupleSpace\x12-\n\x07\x65lement\x18\x01 \x03(\x0b\x32\x1c.ns3opengym.SpaceDescription\":\n\tDictSpace\x12-\n\x07\x65lement\x18\x01 \x03(\x0b\x32\x1c.ns3opengym.SpaceDescription\"f\n\rDataContainer\x12#\n\x04type\x18\x01 \x01(\x0e\x32\x15.ns3opengym.SpaceType\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04name\x18\x03 \x01(\t\"%\n\x15\x44iscreteDataContainer\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x05\"\x8d\x01\n\x10\x42oxDataContainer\x12 \n\x05\x64type\x18\x01 \x01(\x0e\x32\x11.ns3opengym.Dtype\x12\r\n\x05shape\x18\x02 \x03(\r\x12\x0f\n\x07intData\x18\x03 \x03(\x05\x12\x10\n\x08uintData\x18\x04 \x03(\r\x12\x11\n\tfloatData\x18\x05 \x03(\x02\x12\x12\n\ndoubleData\x18\x06 \x03(\x01\"@\n\x12TupleDataContainer\x12*\n\x07\x65lement\x18\x01 \x03(\x0b\x32\x19.ns3opengym.DataContainer\"?\n\x11\x44ictDataContainer\x12*\n\x07\x65lement\x18\x01 \x03(\x0b\x32\x19.ns3opengym.DataContainer\"\x9d\x01\n\nSimInitMsg\x12\x14\n\x0csimProcessId\x18\x01 \x01(\x04\x12\x19\n\x11wafShellProcessId\x18\x02 \x01(\x04\x12.\n\x08obsSpace\x18\x03 \x01(\x0b\x32\x1c.ns3opengym.SpaceDescription\x12.\n\x08\x61\x63tSpace\x18\x04 \x01(\x0b\x32\x1c.ns3opengym.SpaceDescription\".\n\nSimInitAck\x12\x0c\n\x04\x64one\x18\x01 \x01(\x08\x12\x12\n\nstopSimReq\x18\x02 \x01(\x08\"\xc6\x01\n\x0b\x45nvStateMsg\x12*\n\x07obsData\x18\x01 \x01(\x0b\x32\x19.ns3opengym.DataContainer\x12\x0e\n\x06reward\x18\x02 \x01(\x02\x12\x12\n\nisGameOver\x18\x03 \x01(\x08\x12.\n\x06reason\x18\x04 \x01(\x0e\x32\x1e.ns3opengym.EnvStateMsg.Reason\x12\x0c\n\x04info\x18\x05 \x01(\t\")\n\x06Reason\x12\x11\n\rSimulationEnd\x10\x00\x12\x0c\n\x08GameOver\x10\x01\"K\n\tEnvActMsg\x12*\n\x07\x61\x63tData\x18\x01 \x01(\x0b\x32\x19.ns3opengym.DataContainer\x12\x12\n\nstopSimReq\x18\x02 \x01(\x08*\x9c\x01\n\x07MsgType\x12\x0b\n\x07Unknown\x10\x00\x12\x08\n\x04Init\x10\x01\x12\x0f\n\x0b\x41\x63tionSpace\x10\x02\x12\x14\n\x10ObservationSpace\x10\x03\x12\x0e\n\nIsGameOver\x10\x04\x12\x0f\n\x0bObservation\x10\x05\x12\n\n\x06Reward\x10\x06\x12\r\n\tExtraInfo\x10\x07\x12\n\n\x06\x41\x63tion\x10\x08\x12\x0b\n\x07StopEnv\x10\t*H\n\tSpaceType\x12\x0f\n\x0bNoSpaceType\x10\x00\x12\x0c\n\x08\x44iscrete\x10\x01\x12\x07\n\x03\x42ox\x10\x02\x12\t\n\x05Tuple\x10\x03\x12\x08\n\x04\x44ict\x10\x04*>\n\x05\x44type\x12\x0b\n\x07NoDType\x10\x00\x12\x07\n\x03INT\x10\x01\x12\x08\n\x04UINT\x10\x02\x12\t\n\x05\x46LOAT\x10\x03\x12\n\n\x06\x44OUBLE\x10\x04\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])

_MSGTYPE = _descriptor.EnumDescriptor(
  name='MsgType',
  full_name='ns3opengym.MsgType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Init', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActionSpace', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationSpace', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IsGameOver', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Observation', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Reward', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ExtraInfo', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Action', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StopEnv', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1307,
  serialized_end=1463,
)
_sym_db.RegisterEnumDescriptor(_MSGTYPE)

MsgType = enum_type_wrapper.EnumTypeWrapper(_MSGTYPE)
_SPACETYPE = _descriptor.EnumDescriptor(
  name='SpaceType',
  full_name='ns3opengym.SpaceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoSpaceType', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Discrete', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Box', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Tuple', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Dict', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1465,
  serialized_end=1537,
)
_sym_db.RegisterEnumDescriptor(_SPACETYPE)

SpaceType = enum_type_wrapper.EnumTypeWrapper(_SPACETYPE)
_DTYPE = _descriptor.EnumDescriptor(
  name='Dtype',
  full_name='ns3opengym.Dtype',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoDType', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1539,
  serialized_end=1601,
)
_sym_db.RegisterEnumDescriptor(_DTYPE)

Dtype = enum_type_wrapper.EnumTypeWrapper(_DTYPE)
Unknown = 0
Init = 1
ActionSpace = 2
ObservationSpace = 3
IsGameOver = 4
Observation = 5
Reward = 6
ExtraInfo = 7
Action = 8
StopEnv = 9
NoSpaceType = 0
Discrete = 1
Box = 2
Tuple = 3
Dict = 4
NoDType = 0
INT = 1
UINT = 2
FLOAT = 3
DOUBLE = 4


_ENVSTATEMSG_REASON = _descriptor.EnumDescriptor(
  name='Reason',
  full_name='ns3opengym.EnvStateMsg.Reason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SimulationEnd', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GameOver', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1186,
  serialized_end=1227,
)
_sym_db.RegisterEnumDescriptor(_ENVSTATEMSG_REASON)


_SPACEDESCRIPTION = _descriptor.Descriptor(
  name='SpaceDescription',
  full_name='ns3opengym.SpaceDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ns3opengym.SpaceDescription.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='space', full_name='ns3opengym.SpaceDescription.space', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ns3opengym.SpaceDescription.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=163,
)


_DISCRETESPACE = _descriptor.Descriptor(
  name='DiscreteSpace',
  full_name='ns3opengym.DiscreteSpace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n', full_name='ns3opengym.DiscreteSpace.n', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=191,
)


_BOXSPACE = _descriptor.Descriptor(
  name='BoxSpace',
  full_name='ns3opengym.BoxSpace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='low', full_name='ns3opengym.BoxSpace.low', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='ns3opengym.BoxSpace.high', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='ns3opengym.BoxSpace.dtype', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='ns3opengym.BoxSpace.shape', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=279,
)


_TUPLESPACE = _descriptor.Descriptor(
  name='TupleSpace',
  full_name='ns3opengym.TupleSpace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='element', full_name='ns3opengym.TupleSpace.element', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=340,
)


_DICTSPACE = _descriptor.Descriptor(
  name='DictSpace',
  full_name='ns3opengym.DictSpace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='element', full_name='ns3opengym.DictSpace.element', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=400,
)


_DATACONTAINER = _descriptor.Descriptor(
  name='DataContainer',
  full_name='ns3opengym.DataContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ns3opengym.DataContainer.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='ns3opengym.DataContainer.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ns3opengym.DataContainer.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=504,
)


_DISCRETEDATACONTAINER = _descriptor.Descriptor(
  name='DiscreteDataContainer',
  full_name='ns3opengym.DiscreteDataContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='ns3opengym.DiscreteDataContainer.data', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=506,
  serialized_end=543,
)


_BOXDATACONTAINER = _descriptor.Descriptor(
  name='BoxDataContainer',
  full_name='ns3opengym.BoxDataContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dtype', full_name='ns3opengym.BoxDataContainer.dtype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='ns3opengym.BoxDataContainer.shape', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intData', full_name='ns3opengym.BoxDataContainer.intData', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uintData', full_name='ns3opengym.BoxDataContainer.uintData', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floatData', full_name='ns3opengym.BoxDataContainer.floatData', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='doubleData', full_name='ns3opengym.BoxDataContainer.doubleData', index=5,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=546,
  serialized_end=687,
)


_TUPLEDATACONTAINER = _descriptor.Descriptor(
  name='TupleDataContainer',
  full_name='ns3opengym.TupleDataContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='element', full_name='ns3opengym.TupleDataContainer.element', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=689,
  serialized_end=753,
)


_DICTDATACONTAINER = _descriptor.Descriptor(
  name='DictDataContainer',
  full_name='ns3opengym.DictDataContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='element', full_name='ns3opengym.DictDataContainer.element', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=755,
  serialized_end=818,
)


_SIMINITMSG = _descriptor.Descriptor(
  name='SimInitMsg',
  full_name='ns3opengym.SimInitMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simProcessId', full_name='ns3opengym.SimInitMsg.simProcessId', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wafShellProcessId', full_name='ns3opengym.SimInitMsg.wafShellProcessId', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obsSpace', full_name='ns3opengym.SimInitMsg.obsSpace', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actSpace', full_name='ns3opengym.SimInitMsg.actSpace', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=821,
  serialized_end=978,
)


_SIMINITACK = _descriptor.Descriptor(
  name='SimInitAck',
  full_name='ns3opengym.SimInitAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='done', full_name='ns3opengym.SimInitAck.done', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stopSimReq', full_name='ns3opengym.SimInitAck.stopSimReq', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=980,
  serialized_end=1026,
)


_ENVSTATEMSG = _descriptor.Descriptor(
  name='EnvStateMsg',
  full_name='ns3opengym.EnvStateMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='obsData', full_name='ns3opengym.EnvStateMsg.obsData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward', full_name='ns3opengym.EnvStateMsg.reward', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isGameOver', full_name='ns3opengym.EnvStateMsg.isGameOver', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='ns3opengym.EnvStateMsg.reason', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='ns3opengym.EnvStateMsg.info', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENVSTATEMSG_REASON,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1029,
  serialized_end=1227,
)


_ENVACTMSG = _descriptor.Descriptor(
  name='EnvActMsg',
  full_name='ns3opengym.EnvActMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actData', full_name='ns3opengym.EnvActMsg.actData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stopSimReq', full_name='ns3opengym.EnvActMsg.stopSimReq', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1229,
  serialized_end=1304,
)

_SPACEDESCRIPTION.fields_by_name['type'].enum_type = _SPACETYPE
_SPACEDESCRIPTION.fields_by_name['space'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_BOXSPACE.fields_by_name['dtype'].enum_type = _DTYPE
_TUPLESPACE.fields_by_name['element'].message_type = _SPACEDESCRIPTION
_DICTSPACE.fields_by_name['element'].message_type = _SPACEDESCRIPTION
_DATACONTAINER.fields_by_name['type'].enum_type = _SPACETYPE
_DATACONTAINER.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_BOXDATACONTAINER.fields_by_name['dtype'].enum_type = _DTYPE
_TUPLEDATACONTAINER.fields_by_name['element'].message_type = _DATACONTAINER
_DICTDATACONTAINER.fields_by_name['element'].message_type = _DATACONTAINER
_SIMINITMSG.fields_by_name['obsSpace'].message_type = _SPACEDESCRIPTION
_SIMINITMSG.fields_by_name['actSpace'].message_type = _SPACEDESCRIPTION
_ENVSTATEMSG.fields_by_name['obsData'].message_type = _DATACONTAINER
_ENVSTATEMSG.fields_by_name['reason'].enum_type = _ENVSTATEMSG_REASON
_ENVSTATEMSG_REASON.containing_type = _ENVSTATEMSG
_ENVACTMSG.fields_by_name['actData'].message_type = _DATACONTAINER
DESCRIPTOR.message_types_by_name['SpaceDescription'] = _SPACEDESCRIPTION
DESCRIPTOR.message_types_by_name['DiscreteSpace'] = _DISCRETESPACE
DESCRIPTOR.message_types_by_name['BoxSpace'] = _BOXSPACE
DESCRIPTOR.message_types_by_name['TupleSpace'] = _TUPLESPACE
DESCRIPTOR.message_types_by_name['DictSpace'] = _DICTSPACE
DESCRIPTOR.message_types_by_name['DataContainer'] = _DATACONTAINER
DESCRIPTOR.message_types_by_name['DiscreteDataContainer'] = _DISCRETEDATACONTAINER
DESCRIPTOR.message_types_by_name['BoxDataContainer'] = _BOXDATACONTAINER
DESCRIPTOR.message_types_by_name['TupleDataContainer'] = _TUPLEDATACONTAINER
DESCRIPTOR.message_types_by_name['DictDataContainer'] = _DICTDATACONTAINER
DESCRIPTOR.message_types_by_name['SimInitMsg'] = _SIMINITMSG
DESCRIPTOR.message_types_by_name['SimInitAck'] = _SIMINITACK
DESCRIPTOR.message_types_by_name['EnvStateMsg'] = _ENVSTATEMSG
DESCRIPTOR.message_types_by_name['EnvActMsg'] = _ENVACTMSG
DESCRIPTOR.enum_types_by_name['MsgType'] = _MSGTYPE
DESCRIPTOR.enum_types_by_name['SpaceType'] = _SPACETYPE
DESCRIPTOR.enum_types_by_name['Dtype'] = _DTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpaceDescription = _reflection.GeneratedProtocolMessageType('SpaceDescription', (_message.Message,), {
  'DESCRIPTOR' : _SPACEDESCRIPTION,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ns3opengym.SpaceDescription)
  })
_sym_db.RegisterMessage(SpaceDescription)

DiscreteSpace = _reflection.GeneratedProtocolMessageType('DiscreteSpace', (_message.Message,), {
  'DESCRIPTOR' : _DISCRETESPACE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ns3opengym.DiscreteSpace)
  })
_sym_db.RegisterMessage(DiscreteSpace)

BoxSpace = _reflection.GeneratedProtocolMessageType('BoxSpace', (_message.Message,), {
  'DESCRIPTOR' : _BOXSPACE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ns3opengym.BoxSpace)
  })
_sym_db.RegisterMessage(BoxSpace)

TupleSpace = _reflection.GeneratedProtocolMessageType('TupleSpace', (_message.Message,), {
  'DESCRIPTOR' : _TUPLESPACE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ns3opengym.TupleSpace)
  })
_sym_db.RegisterMessage(TupleSpace)

DictSpace = _reflection.GeneratedProtocolMessageType('DictSpace', (_message.Message,), {
  'DESCRIPTOR' : _DICTSPACE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ns3opengym.DictSpace)
  })
_sym_db.RegisterMessage(DictSpace)

DataContainer = _reflection.GeneratedProtocolMessageType('DataContainer', (_message.Message,), {
  'DESCRIPTOR' : _DATACONTAINER,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ns3opengym.DataContainer)
  })
_sym_db.RegisterMessage(DataContainer)

DiscreteDataContainer = _reflection.GeneratedProtocolMessageType('DiscreteDataContainer', (_message.Message,), {
  'DESCRIPTOR' : _DISCRETEDATACONTAINER,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ns3opengym.DiscreteDataContainer)
  })
_sym_db.RegisterMessage(DiscreteDataContainer)

BoxDataContainer = _reflection.GeneratedProtocolMessageType('BoxDataContainer', (_message.Message,), {
  'DESCRIPTOR' : _BOXDATACONTAINER,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ns3opengym.BoxDataContainer)
  })
_sym_db.RegisterMessage(BoxDataContainer)

TupleDataContainer = _reflection.GeneratedProtocolMessageType('TupleDataContainer', (_message.Message,), {
  'DESCRIPTOR' : _TUPLEDATACONTAINER,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ns3opengym.TupleDataContainer)
  })
_sym_db.RegisterMessage(TupleDataContainer)

DictDataContainer = _reflection.GeneratedProtocolMessageType('DictDataContainer', (_message.Message,), {
  'DESCRIPTOR' : _DICTDATACONTAINER,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ns3opengym.DictDataContainer)
  })
_sym_db.RegisterMessage(DictDataContainer)

SimInitMsg = _reflection.GeneratedProtocolMessageType('SimInitMsg', (_message.Message,), {
  'DESCRIPTOR' : _SIMINITMSG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ns3opengym.SimInitMsg)
  })
_sym_db.RegisterMessage(SimInitMsg)

SimInitAck = _reflection.GeneratedProtocolMessageType('SimInitAck', (_message.Message,), {
  'DESCRIPTOR' : _SIMINITACK,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ns3opengym.SimInitAck)
  })
_sym_db.RegisterMessage(SimInitAck)

EnvStateMsg = _reflection.GeneratedProtocolMessageType('EnvStateMsg', (_message.Message,), {
  'DESCRIPTOR' : _ENVSTATEMSG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ns3opengym.EnvStateMsg)
  })
_sym_db.RegisterMessage(EnvStateMsg)

EnvActMsg = _reflection.GeneratedProtocolMessageType('EnvActMsg', (_message.Message,), {
  'DESCRIPTOR' : _ENVACTMSG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ns3opengym.EnvActMsg)
  })
_sym_db.RegisterMessage(EnvActMsg)


# @@protoc_insertion_point(module_scope)