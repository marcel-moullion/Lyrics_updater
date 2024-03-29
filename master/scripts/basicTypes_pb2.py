# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: basicTypes.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='basicTypes.proto',
  package='rv.data',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x62\x61sicTypes.proto\x12\x07rv.data\"\xfb\x07\n\x03URL\x12\'\n\x08platform\x18\x03 \x01(\x0e\x32\x15.rv.data.URL.Platform\x12\x19\n\x0f\x61\x62solute_string\x18\x01 \x01(\tH\x00\x12\x17\n\rrelative_path\x18\x02 \x01(\tH\x00\x12/\n\x05local\x18\x04 \x01(\x0b\x32\x1e.rv.data.URL.LocalRelativePathH\x01\x12\x35\n\x08\x65xternal\x18\x05 \x01(\x0b\x32!.rv.data.URL.ExternalRelativePathH\x01\x1a\xfb\x02\n\x11LocalRelativePath\x12\x31\n\x04root\x18\x01 \x01(\x0e\x32#.rv.data.URL.LocalRelativePath.Root\x12\x0c\n\x04path\x18\x02 \x01(\t\"\xa4\x02\n\x04Root\x12\x10\n\x0cROOT_UNKNOWN\x10\x00\x12\x14\n\x10ROOT_BOOT_VOLUME\x10\x01\x12\x12\n\x0eROOT_USER_HOME\x10\x02\x12\x17\n\x13ROOT_USER_DOCUMENTS\x10\x03\x12\x17\n\x13ROOT_USER_DOWNLOADS\x10\x04\x12\x13\n\x0fROOT_USER_MUSIC\x10\x05\x12\x16\n\x12ROOT_USER_PICTURES\x10\x06\x12\x14\n\x10ROOT_USER_VIDEOS\x10\x07\x12\x15\n\x11ROOT_USER_DESKTOP\x10\x0b\x12\x19\n\x15ROOT_USER_APP_SUPPORT\x10\x08\x12\x0f\n\x0bROOT_SHARED\x10\t\x12\r\n\tROOT_SHOW\x10\n\x12\x19\n\x15ROOT_CURRENT_RESOURCE\x10\x0c\x1a\xb5\x02\n\x14\x45xternalRelativePath\x12\x44\n\x05macos\x18\x01 \x01(\x0b\x32\x35.rv.data.URL.ExternalRelativePath.MacOSExternalVolume\x12\x44\n\x05win32\x18\x02 \x01(\x0b\x32\x35.rv.data.URL.ExternalRelativePath.Win32ExternalVolume\x12\x0c\n\x04path\x18\x03 \x01(\t\x1a*\n\x13MacOSExternalVolume\x12\x13\n\x0bvolume_name\x18\x01 \x01(\t\x1aW\n\x13Win32ExternalVolume\x12\x14\n\x0c\x64rive_letter\x18\x01 \x01(\t\x12\x13\n\x0bvolume_name\x18\x02 \x01(\t\x12\x15\n\rnetwork_share\x18\x03 \x01(\x08\"Z\n\x08Platform\x12\x14\n\x10PLATFORM_UNKNOWN\x10\x00\x12\x12\n\x0ePLATFORM_MACOS\x10\x01\x12\x12\n\x0ePLATFORM_WIN32\x10\x02\x12\x10\n\x0cPLATFORM_WEB\x10\x03\x42\t\n\x07StorageB\x12\n\x10RelativeFilePath\"\"\n\x04URLs\x12\x1a\n\x04urls\x18\x01 \x03(\x0b\x32\x0c.rv.data.URL\"\x16\n\x04UUID\x12\x0e\n\x06string\x18\x01 \x01(\t\"&\n\x08IntRange\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\"@\n\x05\x43olor\x12\x0b\n\x03red\x18\x01 \x01(\x02\x12\r\n\x05green\x18\x02 \x01(\x02\x12\x0c\n\x04\x62lue\x18\x03 \x01(\x02\x12\r\n\x05\x61lpha\x18\x04 \x01(\x02\"]\n\x07Version\x12\x15\n\rmajor_version\x18\x01 \x01(\r\x12\x15\n\rminor_version\x18\x02 \x01(\r\x12\x15\n\rpatch_version\x18\x03 \x01(\r\x12\r\n\x05\x62uild\x18\x04 \x01(\t\"\xc4\x03\n\x0f\x41pplicationInfo\x12\x33\n\x08platform\x18\x01 \x01(\x0e\x32!.rv.data.ApplicationInfo.Platform\x12*\n\x10platform_version\x18\x02 \x01(\x0b\x32\x10.rv.data.Version\x12\x39\n\x0b\x61pplication\x18\x03 \x01(\x0e\x32$.rv.data.ApplicationInfo.Application\x12-\n\x13\x61pplication_version\x18\x04 \x01(\x0b\x32\x10.rv.data.Version\"L\n\x08Platform\x12\x16\n\x12PLATFORM_UNDEFINED\x10\x00\x12\x12\n\x0ePLATFORM_MACOS\x10\x01\x12\x14\n\x10PLATFORM_WINDOWS\x10\x02\"\x97\x01\n\x0b\x41pplication\x12\x19\n\x15\x41PPLICATION_UNDEFINED\x10\x00\x12\x1c\n\x18\x41PPLICATION_PROPRESENTER\x10\x01\x12\x13\n\x0f\x41PPLICATION_PVP\x10\x02\x12\x1e\n\x1a\x41PPLICATION_PROVIDEOSERVER\x10\x03\x12\x1a\n\x16\x41PPLICATION_SCOREBOARD\x10\x04\"V\n\x15\x43ollectionElementType\x12%\n\x0eparameter_uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x16\n\x0eparameter_name\x18\x02 \x01(\tb\x06proto3'
)



_URL_LOCALRELATIVEPATH_ROOT = _descriptor.EnumDescriptor(
  name='Root',
  full_name='rv.data.URL.LocalRelativePath.Root',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROOT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_BOOT_VOLUME', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_USER_HOME', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_USER_DOCUMENTS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_USER_DOWNLOADS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_USER_MUSIC', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_USER_PICTURES', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_USER_VIDEOS', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_USER_DESKTOP', index=8, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_USER_APP_SUPPORT', index=9, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_SHARED', index=10, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_SHOW', index=11, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_CURRENT_RESOURCE', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=322,
  serialized_end=614,
)
_sym_db.RegisterEnumDescriptor(_URL_LOCALRELATIVEPATH_ROOT)

_URL_PLATFORM = _descriptor.EnumDescriptor(
  name='Platform',
  full_name='rv.data.URL.Platform',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_MACOS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_WIN32', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_WEB', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=928,
  serialized_end=1018,
)
_sym_db.RegisterEnumDescriptor(_URL_PLATFORM)

_APPLICATIONINFO_PLATFORM = _descriptor.EnumDescriptor(
  name='Platform',
  full_name='rv.data.ApplicationInfo.Platform',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_MACOS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_WINDOWS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1535,
  serialized_end=1611,
)
_sym_db.RegisterEnumDescriptor(_APPLICATIONINFO_PLATFORM)

_APPLICATIONINFO_APPLICATION = _descriptor.EnumDescriptor(
  name='Application',
  full_name='rv.data.ApplicationInfo.Application',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='APPLICATION_UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APPLICATION_PROPRESENTER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APPLICATION_PVP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APPLICATION_PROVIDEOSERVER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APPLICATION_SCOREBOARD', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1614,
  serialized_end=1765,
)
_sym_db.RegisterEnumDescriptor(_APPLICATIONINFO_APPLICATION)


_URL_LOCALRELATIVEPATH = _descriptor.Descriptor(
  name='LocalRelativePath',
  full_name='rv.data.URL.LocalRelativePath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='root', full_name='rv.data.URL.LocalRelativePath.root', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='rv.data.URL.LocalRelativePath.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _URL_LOCALRELATIVEPATH_ROOT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=614,
)

_URL_EXTERNALRELATIVEPATH_MACOSEXTERNALVOLUME = _descriptor.Descriptor(
  name='MacOSExternalVolume',
  full_name='rv.data.URL.ExternalRelativePath.MacOSExternalVolume',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='volume_name', full_name='rv.data.URL.ExternalRelativePath.MacOSExternalVolume.volume_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=795,
  serialized_end=837,
)

_URL_EXTERNALRELATIVEPATH_WIN32EXTERNALVOLUME = _descriptor.Descriptor(
  name='Win32ExternalVolume',
  full_name='rv.data.URL.ExternalRelativePath.Win32ExternalVolume',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='drive_letter', full_name='rv.data.URL.ExternalRelativePath.Win32ExternalVolume.drive_letter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume_name', full_name='rv.data.URL.ExternalRelativePath.Win32ExternalVolume.volume_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network_share', full_name='rv.data.URL.ExternalRelativePath.Win32ExternalVolume.network_share', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=839,
  serialized_end=926,
)

_URL_EXTERNALRELATIVEPATH = _descriptor.Descriptor(
  name='ExternalRelativePath',
  full_name='rv.data.URL.ExternalRelativePath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='macos', full_name='rv.data.URL.ExternalRelativePath.macos', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='win32', full_name='rv.data.URL.ExternalRelativePath.win32', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='rv.data.URL.ExternalRelativePath.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_URL_EXTERNALRELATIVEPATH_MACOSEXTERNALVOLUME, _URL_EXTERNALRELATIVEPATH_WIN32EXTERNALVOLUME, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=617,
  serialized_end=926,
)

_URL = _descriptor.Descriptor(
  name='URL',
  full_name='rv.data.URL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='platform', full_name='rv.data.URL.platform', index=0,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='absolute_string', full_name='rv.data.URL.absolute_string', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relative_path', full_name='rv.data.URL.relative_path', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='local', full_name='rv.data.URL.local', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='external', full_name='rv.data.URL.external', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_URL_LOCALRELATIVEPATH, _URL_EXTERNALRELATIVEPATH, ],
  enum_types=[
    _URL_PLATFORM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Storage', full_name='rv.data.URL.Storage',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='RelativeFilePath', full_name='rv.data.URL.RelativeFilePath',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=30,
  serialized_end=1049,
)


_URLS = _descriptor.Descriptor(
  name='URLs',
  full_name='rv.data.URLs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='urls', full_name='rv.data.URLs.urls', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1051,
  serialized_end=1085,
)


_UUID = _descriptor.Descriptor(
  name='UUID',
  full_name='rv.data.UUID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='string', full_name='rv.data.UUID.string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1087,
  serialized_end=1109,
)


_INTRANGE = _descriptor.Descriptor(
  name='IntRange',
  full_name='rv.data.IntRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='rv.data.IntRange.start', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='rv.data.IntRange.end', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1111,
  serialized_end=1149,
)


_COLOR = _descriptor.Descriptor(
  name='Color',
  full_name='rv.data.Color',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='red', full_name='rv.data.Color.red', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='green', full_name='rv.data.Color.green', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blue', full_name='rv.data.Color.blue', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alpha', full_name='rv.data.Color.alpha', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=1151,
  serialized_end=1215,
)


_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='rv.data.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='major_version', full_name='rv.data.Version.major_version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minor_version', full_name='rv.data.Version.minor_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='patch_version', full_name='rv.data.Version.patch_version', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='build', full_name='rv.data.Version.build', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1217,
  serialized_end=1310,
)


_APPLICATIONINFO = _descriptor.Descriptor(
  name='ApplicationInfo',
  full_name='rv.data.ApplicationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='platform', full_name='rv.data.ApplicationInfo.platform', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='platform_version', full_name='rv.data.ApplicationInfo.platform_version', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='application', full_name='rv.data.ApplicationInfo.application', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='application_version', full_name='rv.data.ApplicationInfo.application_version', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _APPLICATIONINFO_PLATFORM,
    _APPLICATIONINFO_APPLICATION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1313,
  serialized_end=1765,
)


_COLLECTIONELEMENTTYPE = _descriptor.Descriptor(
  name='CollectionElementType',
  full_name='rv.data.CollectionElementType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameter_uuid', full_name='rv.data.CollectionElementType.parameter_uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameter_name', full_name='rv.data.CollectionElementType.parameter_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1767,
  serialized_end=1853,
)

_URL_LOCALRELATIVEPATH.fields_by_name['root'].enum_type = _URL_LOCALRELATIVEPATH_ROOT
_URL_LOCALRELATIVEPATH.containing_type = _URL
_URL_LOCALRELATIVEPATH_ROOT.containing_type = _URL_LOCALRELATIVEPATH
_URL_EXTERNALRELATIVEPATH_MACOSEXTERNALVOLUME.containing_type = _URL_EXTERNALRELATIVEPATH
_URL_EXTERNALRELATIVEPATH_WIN32EXTERNALVOLUME.containing_type = _URL_EXTERNALRELATIVEPATH
_URL_EXTERNALRELATIVEPATH.fields_by_name['macos'].message_type = _URL_EXTERNALRELATIVEPATH_MACOSEXTERNALVOLUME
_URL_EXTERNALRELATIVEPATH.fields_by_name['win32'].message_type = _URL_EXTERNALRELATIVEPATH_WIN32EXTERNALVOLUME
_URL_EXTERNALRELATIVEPATH.containing_type = _URL
_URL.fields_by_name['platform'].enum_type = _URL_PLATFORM
_URL.fields_by_name['local'].message_type = _URL_LOCALRELATIVEPATH
_URL.fields_by_name['external'].message_type = _URL_EXTERNALRELATIVEPATH
_URL_PLATFORM.containing_type = _URL
_URL.oneofs_by_name['Storage'].fields.append(
  _URL.fields_by_name['absolute_string'])
_URL.fields_by_name['absolute_string'].containing_oneof = _URL.oneofs_by_name['Storage']
_URL.oneofs_by_name['Storage'].fields.append(
  _URL.fields_by_name['relative_path'])
_URL.fields_by_name['relative_path'].containing_oneof = _URL.oneofs_by_name['Storage']
_URL.oneofs_by_name['RelativeFilePath'].fields.append(
  _URL.fields_by_name['local'])
_URL.fields_by_name['local'].containing_oneof = _URL.oneofs_by_name['RelativeFilePath']
_URL.oneofs_by_name['RelativeFilePath'].fields.append(
  _URL.fields_by_name['external'])
_URL.fields_by_name['external'].containing_oneof = _URL.oneofs_by_name['RelativeFilePath']
_URLS.fields_by_name['urls'].message_type = _URL
_APPLICATIONINFO.fields_by_name['platform'].enum_type = _APPLICATIONINFO_PLATFORM
_APPLICATIONINFO.fields_by_name['platform_version'].message_type = _VERSION
_APPLICATIONINFO.fields_by_name['application'].enum_type = _APPLICATIONINFO_APPLICATION
_APPLICATIONINFO.fields_by_name['application_version'].message_type = _VERSION
_APPLICATIONINFO_PLATFORM.containing_type = _APPLICATIONINFO
_APPLICATIONINFO_APPLICATION.containing_type = _APPLICATIONINFO
_COLLECTIONELEMENTTYPE.fields_by_name['parameter_uuid'].message_type = _UUID
DESCRIPTOR.message_types_by_name['URL'] = _URL
DESCRIPTOR.message_types_by_name['URLs'] = _URLS
DESCRIPTOR.message_types_by_name['UUID'] = _UUID
DESCRIPTOR.message_types_by_name['IntRange'] = _INTRANGE
DESCRIPTOR.message_types_by_name['Color'] = _COLOR
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['ApplicationInfo'] = _APPLICATIONINFO
DESCRIPTOR.message_types_by_name['CollectionElementType'] = _COLLECTIONELEMENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

URL = _reflection.GeneratedProtocolMessageType('URL', (_message.Message,), {

  'LocalRelativePath' : _reflection.GeneratedProtocolMessageType('LocalRelativePath', (_message.Message,), {
    'DESCRIPTOR' : _URL_LOCALRELATIVEPATH,
    '__module__' : 'basicTypes_pb2'
    # @@protoc_insertion_point(class_scope:rv.data.URL.LocalRelativePath)
    })
  ,

  'ExternalRelativePath' : _reflection.GeneratedProtocolMessageType('ExternalRelativePath', (_message.Message,), {

    'MacOSExternalVolume' : _reflection.GeneratedProtocolMessageType('MacOSExternalVolume', (_message.Message,), {
      'DESCRIPTOR' : _URL_EXTERNALRELATIVEPATH_MACOSEXTERNALVOLUME,
      '__module__' : 'basicTypes_pb2'
      # @@protoc_insertion_point(class_scope:rv.data.URL.ExternalRelativePath.MacOSExternalVolume)
      })
    ,

    'Win32ExternalVolume' : _reflection.GeneratedProtocolMessageType('Win32ExternalVolume', (_message.Message,), {
      'DESCRIPTOR' : _URL_EXTERNALRELATIVEPATH_WIN32EXTERNALVOLUME,
      '__module__' : 'basicTypes_pb2'
      # @@protoc_insertion_point(class_scope:rv.data.URL.ExternalRelativePath.Win32ExternalVolume)
      })
    ,
    'DESCRIPTOR' : _URL_EXTERNALRELATIVEPATH,
    '__module__' : 'basicTypes_pb2'
    # @@protoc_insertion_point(class_scope:rv.data.URL.ExternalRelativePath)
    })
  ,
  'DESCRIPTOR' : _URL,
  '__module__' : 'basicTypes_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.URL)
  })
_sym_db.RegisterMessage(URL)
_sym_db.RegisterMessage(URL.LocalRelativePath)
_sym_db.RegisterMessage(URL.ExternalRelativePath)
_sym_db.RegisterMessage(URL.ExternalRelativePath.MacOSExternalVolume)
_sym_db.RegisterMessage(URL.ExternalRelativePath.Win32ExternalVolume)

URLs = _reflection.GeneratedProtocolMessageType('URLs', (_message.Message,), {
  'DESCRIPTOR' : _URLS,
  '__module__' : 'basicTypes_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.URLs)
  })
_sym_db.RegisterMessage(URLs)

UUID = _reflection.GeneratedProtocolMessageType('UUID', (_message.Message,), {
  'DESCRIPTOR' : _UUID,
  '__module__' : 'basicTypes_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.UUID)
  })
_sym_db.RegisterMessage(UUID)

IntRange = _reflection.GeneratedProtocolMessageType('IntRange', (_message.Message,), {
  'DESCRIPTOR' : _INTRANGE,
  '__module__' : 'basicTypes_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.IntRange)
  })
_sym_db.RegisterMessage(IntRange)

Color = _reflection.GeneratedProtocolMessageType('Color', (_message.Message,), {
  'DESCRIPTOR' : _COLOR,
  '__module__' : 'basicTypes_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.Color)
  })
_sym_db.RegisterMessage(Color)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'basicTypes_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.Version)
  })
_sym_db.RegisterMessage(Version)

ApplicationInfo = _reflection.GeneratedProtocolMessageType('ApplicationInfo', (_message.Message,), {
  'DESCRIPTOR' : _APPLICATIONINFO,
  '__module__' : 'basicTypes_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.ApplicationInfo)
  })
_sym_db.RegisterMessage(ApplicationInfo)

CollectionElementType = _reflection.GeneratedProtocolMessageType('CollectionElementType', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONELEMENTTYPE,
  '__module__' : 'basicTypes_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.CollectionElementType)
  })
_sym_db.RegisterMessage(CollectionElementType)


# @@protoc_insertion_point(module_scope)
