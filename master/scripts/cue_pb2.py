# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cue.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basicTypes_pb2 as basicTypes__pb2
import hotKey_pb2 as hotKey__pb2
import action_pb2 as action__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cue.proto',
  package='rv.data',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tcue.proto\x12\x07rv.data\x1a\x10\x62\x61sicTypes.proto\x1a\x0chotKey.proto\x1a\x0c\x61\x63tion.proto\"\xbc\x07\n\x03\x43ue\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x41\n\x16\x63ompletion_target_type\x18\x03 \x01(\x0e\x32!.rv.data.Cue.CompletionTargetType\x12-\n\x16\x63ompletion_target_uuid\x18\x04 \x01(\x0b\x32\r.rv.data.UUID\x12\x41\n\x16\x63ompletion_action_type\x18\x05 \x01(\x0e\x32!.rv.data.Cue.CompletionActionType\x12-\n\x16\x63ompletion_action_uuid\x18\x06 \x01(\x0b\x32\r.rv.data.UUID\x12/\n\x0ctrigger_time\x18\x07 \x01(\x0b\x32\x19.rv.data.Cue.TimecodeTime\x12 \n\x07hot_key\x18\x08 \x01(\x0b\x32\x0f.rv.data.HotKey\x12 \n\x07\x61\x63tions\x18\n \x03(\x0b\x32\x0f.rv.data.Action\x12\x39\n\x0fpending_imports\x18\x0b \x03(\x0b\x32 .rv.data.Cue.PendingImportsEntry\x12\x11\n\tisEnabled\x18\x0c \x01(\x08\x12\x17\n\x0f\x63ompletion_time\x18\r \x01(\x01\x1a\x1c\n\x0cTimecodeTime\x12\x0c\n\x04time\x18\x01 \x01(\x01\x1a@\n\x13PendingImportsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.rv.data.URLs\"\xbd\x01\n\x14\x43ompletionTargetType\x12\x1f\n\x1b\x43OMPLETION_TARGET_TYPE_NONE\x10\x00\x12\x1f\n\x1b\x43OMPLETION_TARGET_TYPE_NEXT\x10\x01\x12!\n\x1d\x43OMPLETION_TARGET_TYPE_RANDOM\x10\x02\x12\x1e\n\x1a\x43OMPLETION_TARGET_TYPE_CUE\x10\x03\x12 \n\x1c\x43OMPLETION_TARGET_TYPE_FIRST\x10\x04\"\xa9\x01\n\x14\x43ompletionActionType\x12 \n\x1c\x43OMPLETION_ACTION_TYPE_FIRST\x10\x00\x12\x1f\n\x1b\x43OMPLETION_ACTION_TYPE_LAST\x10\x01\x12\'\n#COMPLETION_ACTION_TYPE_AFTER_ACTION\x10\x02\x12%\n!COMPLETION_ACTION_TYPE_AFTER_TIME\x10\x03\x62\x06proto3'
  ,
  dependencies=[basicTypes__pb2.DESCRIPTOR,hotKey__pb2.DESCRIPTOR,action__pb2.DESCRIPTOR,])



_CUE_COMPLETIONTARGETTYPE = _descriptor.EnumDescriptor(
  name='CompletionTargetType',
  full_name='rv.data.Cue.CompletionTargetType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMPLETION_TARGET_TYPE_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLETION_TARGET_TYPE_NEXT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLETION_TARGET_TYPE_RANDOM', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLETION_TARGET_TYPE_CUE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLETION_TARGET_TYPE_FIRST', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=664,
  serialized_end=853,
)
_sym_db.RegisterEnumDescriptor(_CUE_COMPLETIONTARGETTYPE)

_CUE_COMPLETIONACTIONTYPE = _descriptor.EnumDescriptor(
  name='CompletionActionType',
  full_name='rv.data.Cue.CompletionActionType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMPLETION_ACTION_TYPE_FIRST', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLETION_ACTION_TYPE_LAST', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLETION_ACTION_TYPE_AFTER_ACTION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLETION_ACTION_TYPE_AFTER_TIME', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=856,
  serialized_end=1025,
)
_sym_db.RegisterEnumDescriptor(_CUE_COMPLETIONACTIONTYPE)


_CUE_TIMECODETIME = _descriptor.Descriptor(
  name='TimecodeTime',
  full_name='rv.data.Cue.TimecodeTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='rv.data.Cue.TimecodeTime.time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=567,
  serialized_end=595,
)

_CUE_PENDINGIMPORTSENTRY = _descriptor.Descriptor(
  name='PendingImportsEntry',
  full_name='rv.data.Cue.PendingImportsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='rv.data.Cue.PendingImportsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='rv.data.Cue.PendingImportsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=597,
  serialized_end=661,
)

_CUE = _descriptor.Descriptor(
  name='Cue',
  full_name='rv.data.Cue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='rv.data.Cue.uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='rv.data.Cue.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completion_target_type', full_name='rv.data.Cue.completion_target_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completion_target_uuid', full_name='rv.data.Cue.completion_target_uuid', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completion_action_type', full_name='rv.data.Cue.completion_action_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completion_action_uuid', full_name='rv.data.Cue.completion_action_uuid', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trigger_time', full_name='rv.data.Cue.trigger_time', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hot_key', full_name='rv.data.Cue.hot_key', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actions', full_name='rv.data.Cue.actions', index=8,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pending_imports', full_name='rv.data.Cue.pending_imports', index=9,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isEnabled', full_name='rv.data.Cue.isEnabled', index=10,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completion_time', full_name='rv.data.Cue.completion_time', index=11,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CUE_TIMECODETIME, _CUE_PENDINGIMPORTSENTRY, ],
  enum_types=[
    _CUE_COMPLETIONTARGETTYPE,
    _CUE_COMPLETIONACTIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=1025,
)

_CUE_TIMECODETIME.containing_type = _CUE
_CUE_PENDINGIMPORTSENTRY.fields_by_name['value'].message_type = basicTypes__pb2._URLS
_CUE_PENDINGIMPORTSENTRY.containing_type = _CUE
_CUE.fields_by_name['uuid'].message_type = basicTypes__pb2._UUID
_CUE.fields_by_name['completion_target_type'].enum_type = _CUE_COMPLETIONTARGETTYPE
_CUE.fields_by_name['completion_target_uuid'].message_type = basicTypes__pb2._UUID
_CUE.fields_by_name['completion_action_type'].enum_type = _CUE_COMPLETIONACTIONTYPE
_CUE.fields_by_name['completion_action_uuid'].message_type = basicTypes__pb2._UUID
_CUE.fields_by_name['trigger_time'].message_type = _CUE_TIMECODETIME
_CUE.fields_by_name['hot_key'].message_type = hotKey__pb2._HOTKEY
_CUE.fields_by_name['actions'].message_type = action__pb2._ACTION
_CUE.fields_by_name['pending_imports'].message_type = _CUE_PENDINGIMPORTSENTRY
_CUE_COMPLETIONTARGETTYPE.containing_type = _CUE
_CUE_COMPLETIONACTIONTYPE.containing_type = _CUE
DESCRIPTOR.message_types_by_name['Cue'] = _CUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Cue = _reflection.GeneratedProtocolMessageType('Cue', (_message.Message,), {

  'TimecodeTime' : _reflection.GeneratedProtocolMessageType('TimecodeTime', (_message.Message,), {
    'DESCRIPTOR' : _CUE_TIMECODETIME,
    '__module__' : 'cue_pb2'
    # @@protoc_insertion_point(class_scope:rv.data.Cue.TimecodeTime)
    })
  ,

  'PendingImportsEntry' : _reflection.GeneratedProtocolMessageType('PendingImportsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CUE_PENDINGIMPORTSENTRY,
    '__module__' : 'cue_pb2'
    # @@protoc_insertion_point(class_scope:rv.data.Cue.PendingImportsEntry)
    })
  ,
  'DESCRIPTOR' : _CUE,
  '__module__' : 'cue_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.Cue)
  })
_sym_db.RegisterMessage(Cue)
_sym_db.RegisterMessage(Cue.TimecodeTime)
_sym_db.RegisterMessage(Cue.PendingImportsEntry)


# @@protoc_insertion_point(module_scope)