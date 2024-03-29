# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: presentationSlide.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import slide_pb2 as slide__pb2
import basicTypes_pb2 as basicTypes__pb2
import alignmentGuide_pb2 as alignmentGuide__pb2
import effects_pb2 as effects__pb2
import graphicsData_pb2 as graphicsData__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='presentationSlide.proto',
  package='rv.data',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17presentationSlide.proto\x12\x07rv.data\x1a\x0bslide.proto\x1a\x10\x62\x61sicTypes.proto\x1a\x14\x61lignmentGuide.proto\x1a\reffects.proto\x1a\x12graphicsData.proto\"\xbc\x02\n\x11PresentationSlide\x12\"\n\nbase_slide\x18\x01 \x01(\x0b\x32\x0e.rv.data.Slide\x12/\n\x05notes\x18\x02 \x01(\x0b\x32 .rv.data.PresentationSlide.Notes\x12\x34\n\x13template_guidelines\x18\x03 \x03(\x0b\x32\x17.rv.data.AlignmentGuide\x12!\n\x0b\x63hord_chart\x18\x04 \x01(\x0b\x32\x0c.rv.data.URL\x12\'\n\ntransition\x18\x05 \x01(\x0b\x32\x13.rv.data.Transition\x1aP\n\x05Notes\x12\x10\n\x08rtf_data\x18\x01 \x01(\x0c\x12\x35\n\nattributes\x18\x02 \x01(\x0b\x32!.rv.data.Graphics.Text.Attributesb\x06proto3'
  ,
  dependencies=[slide__pb2.DESCRIPTOR,basicTypes__pb2.DESCRIPTOR,alignmentGuide__pb2.DESCRIPTOR,effects__pb2.DESCRIPTOR,graphicsData__pb2.DESCRIPTOR,])




_PRESENTATIONSLIDE_NOTES = _descriptor.Descriptor(
  name='Notes',
  full_name='rv.data.PresentationSlide.Notes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rtf_data', full_name='rv.data.PresentationSlide.Notes.rtf_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='rv.data.PresentationSlide.Notes.attributes', index=1,
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
  serialized_start=361,
  serialized_end=441,
)

_PRESENTATIONSLIDE = _descriptor.Descriptor(
  name='PresentationSlide',
  full_name='rv.data.PresentationSlide',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_slide', full_name='rv.data.PresentationSlide.base_slide', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notes', full_name='rv.data.PresentationSlide.notes', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='template_guidelines', full_name='rv.data.PresentationSlide.template_guidelines', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chord_chart', full_name='rv.data.PresentationSlide.chord_chart', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transition', full_name='rv.data.PresentationSlide.transition', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PRESENTATIONSLIDE_NOTES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=441,
)

_PRESENTATIONSLIDE_NOTES.fields_by_name['attributes'].message_type = graphicsData__pb2._GRAPHICS_TEXT_ATTRIBUTES
_PRESENTATIONSLIDE_NOTES.containing_type = _PRESENTATIONSLIDE
_PRESENTATIONSLIDE.fields_by_name['base_slide'].message_type = slide__pb2._SLIDE
_PRESENTATIONSLIDE.fields_by_name['notes'].message_type = _PRESENTATIONSLIDE_NOTES
_PRESENTATIONSLIDE.fields_by_name['template_guidelines'].message_type = alignmentGuide__pb2._ALIGNMENTGUIDE
_PRESENTATIONSLIDE.fields_by_name['chord_chart'].message_type = basicTypes__pb2._URL
_PRESENTATIONSLIDE.fields_by_name['transition'].message_type = effects__pb2._TRANSITION
DESCRIPTOR.message_types_by_name['PresentationSlide'] = _PRESENTATIONSLIDE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PresentationSlide = _reflection.GeneratedProtocolMessageType('PresentationSlide', (_message.Message,), {

  'Notes' : _reflection.GeneratedProtocolMessageType('Notes', (_message.Message,), {
    'DESCRIPTOR' : _PRESENTATIONSLIDE_NOTES,
    '__module__' : 'presentationSlide_pb2'
    # @@protoc_insertion_point(class_scope:rv.data.PresentationSlide.Notes)
    })
  ,
  'DESCRIPTOR' : _PRESENTATIONSLIDE,
  '__module__' : 'presentationSlide_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.PresentationSlide)
  })
_sym_db.RegisterMessage(PresentationSlide)
_sym_db.RegisterMessage(PresentationSlide.Notes)


# @@protoc_insertion_point(module_scope)
