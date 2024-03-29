# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hotKey.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hotKey.proto',
  package='rv.data',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0chotKey.proto\x12\x07rv.data\"\xe7\x15\n\x06HotKey\x12%\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x17.rv.data.HotKey.KeyCode\x12\x1a\n\x12\x63ontrol_identifier\x18\x02 \x01(\t\"\x99\x15\n\x07KeyCode\x12\x14\n\x10KEY_CODE_UNKNOWN\x10\x00\x12\x13\n\x0fKEY_CODE_ANSI_A\x10\x01\x12\x13\n\x0fKEY_CODE_ANSI_B\x10\x02\x12\x13\n\x0fKEY_CODE_ANSI_C\x10\x03\x12\x13\n\x0fKEY_CODE_ANSI_D\x10\x04\x12\x13\n\x0fKEY_CODE_ANSI_E\x10\x05\x12\x13\n\x0fKEY_CODE_ANSI_F\x10\x06\x12\x13\n\x0fKEY_CODE_ANSI_G\x10\x07\x12\x13\n\x0fKEY_CODE_ANSI_H\x10\x08\x12\x13\n\x0fKEY_CODE_ANSI_I\x10\t\x12\x13\n\x0fKEY_CODE_ANSI_J\x10\n\x12\x13\n\x0fKEY_CODE_ANSI_K\x10\x0b\x12\x13\n\x0fKEY_CODE_ANSI_L\x10\x0c\x12\x13\n\x0fKEY_CODE_ANSI_M\x10\r\x12\x13\n\x0fKEY_CODE_ANSI_N\x10\x0e\x12\x13\n\x0fKEY_CODE_ANSI_O\x10\x0f\x12\x13\n\x0fKEY_CODE_ANSI_P\x10\x10\x12\x13\n\x0fKEY_CODE_ANSI_Q\x10\x11\x12\x13\n\x0fKEY_CODE_ANSI_R\x10\x12\x12\x13\n\x0fKEY_CODE_ANSI_S\x10\x13\x12\x13\n\x0fKEY_CODE_ANSI_T\x10\x14\x12\x13\n\x0fKEY_CODE_ANSI_U\x10\x15\x12\x13\n\x0fKEY_CODE_ANSI_V\x10\x16\x12\x13\n\x0fKEY_CODE_ANSI_W\x10\x17\x12\x13\n\x0fKEY_CODE_ANSI_X\x10\x18\x12\x13\n\x0fKEY_CODE_ANSI_Y\x10\x19\x12\x13\n\x0fKEY_CODE_ANSI_Z\x10\x1a\x12\x13\n\x0fKEY_CODE_ANSI_0\x10\x1b\x12\x13\n\x0fKEY_CODE_ANSI_1\x10\x1c\x12\x13\n\x0fKEY_CODE_ANSI_2\x10\x1d\x12\x13\n\x0fKEY_CODE_ANSI_3\x10\x1e\x12\x13\n\x0fKEY_CODE_ANSI_4\x10\x1f\x12\x13\n\x0fKEY_CODE_ANSI_5\x10 \x12\x13\n\x0fKEY_CODE_ANSI_6\x10!\x12\x13\n\x0fKEY_CODE_ANSI_7\x10\"\x12\x13\n\x0fKEY_CODE_ANSI_8\x10#\x12\x13\n\x0fKEY_CODE_ANSI_9\x10$\x12\x17\n\x13KEY_CODE_ANSI_EQUAL\x10%\x12\x17\n\x13KEY_CODE_ANSI_MINUS\x10&\x12\x1f\n\x1bKEY_CODE_ANSI_RIGHT_BRACKET\x10\'\x12\x1e\n\x1aKEY_CODE_ANSI_LEFT_BRACKET\x10(\x12\x17\n\x13KEY_CODE_ANSI_QUOTE\x10)\x12\x1b\n\x17KEY_CODE_ANSI_SEMICOLON\x10*\x12\x1b\n\x17KEY_CODE_ANSI_BACKSLASH\x10+\x12\x17\n\x13KEY_CODE_ANSI_COMMA\x10,\x12\x17\n\x13KEY_CODE_ANSI_SLASH\x10-\x12\x18\n\x14KEY_CODE_ANSI_PERIOD\x10.\x12\x17\n\x13KEY_CODE_ANSI_GRAVE\x10/\x12 \n\x1cKEY_CODE_ANSI_KEYPAD_DECIMAL\x10\x30\x12\x1d\n\x19KEY_CODE_ANSI_KEYPAD_PLUS\x10\x31\x12\x1e\n\x1aKEY_CODE_ANSI_KEYPAD_CLEAR\x10\x32\x12\x1f\n\x1bKEY_CODE_ANSI_KEYPAD_DIVIDE\x10\x33\x12\x1e\n\x1aKEY_CODE_ANSI_KEYPAD_ENTER\x10\x34\x12\x1e\n\x1aKEY_CODE_ANSI_KEYPAD_MINUS\x10\x35\x12\x1f\n\x1bKEY_CODE_ANSI_KEYPAD_EQUALS\x10\x36\x12\x1a\n\x16KEY_CODE_ANSI_KEYPAD_0\x10\x37\x12\x1a\n\x16KEY_CODE_ANSI_KEYPAD_1\x10\x38\x12\x1a\n\x16KEY_CODE_ANSI_KEYPAD_2\x10\x39\x12\x1a\n\x16KEY_CODE_ANSI_KEYPAD_3\x10:\x12\x1a\n\x16KEY_CODE_ANSI_KEYPAD_4\x10;\x12\x1a\n\x16KEY_CODE_ANSI_KEYPAD_5\x10<\x12\x1a\n\x16KEY_CODE_ANSI_KEYPAD_6\x10=\x12\x1a\n\x16KEY_CODE_ANSI_KEYPAD_7\x10>\x12\x1a\n\x16KEY_CODE_ANSI_KEYPAD_8\x10?\x12\x1a\n\x16KEY_CODE_ANSI_KEYPAD_9\x10@\x12\x0f\n\x0bKEY_CODE_F1\x10\x41\x12\x0f\n\x0bKEY_CODE_F2\x10\x42\x12\x0f\n\x0bKEY_CODE_F3\x10\x43\x12\x0f\n\x0bKEY_CODE_F4\x10\x44\x12\x0f\n\x0bKEY_CODE_F5\x10\x45\x12\x0f\n\x0bKEY_CODE_F6\x10\x46\x12\x0f\n\x0bKEY_CODE_F7\x10G\x12\x0f\n\x0bKEY_CODE_F8\x10H\x12\x0f\n\x0bKEY_CODE_F9\x10I\x12\x10\n\x0cKEY_CODE_F10\x10J\x12\x10\n\x0cKEY_CODE_F11\x10K\x12\x10\n\x0cKEY_CODE_F12\x10L\x12\x10\n\x0cKEY_CODE_F13\x10M\x12\x10\n\x0cKEY_CODE_F14\x10N\x12\x10\n\x0cKEY_CODE_F15\x10O\x12\x10\n\x0cKEY_CODE_F16\x10P\x12\x10\n\x0cKEY_CODE_F17\x10Q\x12\x10\n\x0cKEY_CODE_F18\x10R\x12\x10\n\x0cKEY_CODE_F19\x10S\x12\x10\n\x0cKEY_CODE_F20\x10T\x12\x15\n\x11KEY_CODE_FUNCTION\x10U\x12\x13\n\x0fKEY_CODE_RETURN\x10V\x12\x10\n\x0cKEY_CODE_TAB\x10W\x12\x12\n\x0eKEY_CODE_SPACE\x10X\x12\x13\n\x0fKEY_CODE_DELETE\x10Y\x12\x13\n\x0fKEY_CODE_ESCAPE\x10Z\x12\x14\n\x10KEY_CODE_COMMAND\x10[\x12\x12\n\x0eKEY_CODE_SHIFT\x10\\\x12\x16\n\x12KEY_CODE_CAPS_LOCK\x10]\x12\x13\n\x0fKEY_CODE_OPTION\x10^\x12\x14\n\x10KEY_CODE_CONTROL\x10_\x12\x18\n\x14KEY_CODE_RIGHT_SHIFT\x10`\x12\x19\n\x15KEY_CODE_RIGHT_OPTION\x10\x61\x12\x1a\n\x16KEY_CODE_RIGHT_CONTROL\x10\x62\x12\x16\n\x12KEY_CODE_VOLUME_UP\x10\x63\x12\x18\n\x14KEY_CODE_VOLUME_DOWN\x10\x64\x12\x11\n\rKEY_CODE_MUTE\x10\x65\x12\x11\n\rKEY_CODE_HELP\x10\x66\x12\x11\n\rKEY_CODE_HOME\x10g\x12\x14\n\x10KEY_CODE_PAGE_UP\x10h\x12\x1b\n\x17KEY_CODE_FORWARD_DELETE\x10i\x12\x10\n\x0cKEY_CODE_END\x10j\x12\x16\n\x12KEY_CODE_PAGE_DOWN\x10k\x12\x17\n\x13KEY_CODE_LEFT_ARROW\x10l\x12\x18\n\x14KEY_CODE_RIGHT_ARROW\x10m\x12\x17\n\x13KEY_CODE_DOWN_ARROW\x10n\x12\x15\n\x11KEY_CODE_UP_ARROW\x10o\x12\x1a\n\x16KEY_CODE_ISO_SELECTION\x10p\x12\x14\n\x10KEY_CODE_JIS_YEN\x10q\x12\x1b\n\x17KEY_CODE_JIS_UNDERSCORE\x10r\x12\x1d\n\x19KEY_CODE_JIS_KEYPAD_COMMA\x10s\x12\x15\n\x11KEY_CODE_JIS_EISU\x10t\x12\x15\n\x11KEY_CODE_JIS_KANA\x10ub\x06proto3'
)



_HOTKEY_KEYCODE = _descriptor.EnumDescriptor(
  name='KeyCode',
  full_name='rv.data.HotKey.KeyCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_A', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_B', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_C', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_D', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_E', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_F', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_G', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_H', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_I', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_J', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_K', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_L', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_M', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_N', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_O', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_P', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_Q', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_R', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_S', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_T', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_U', index=21, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_V', index=22, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_W', index=23, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_X', index=24, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_Y', index=25, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_Z', index=26, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_0', index=27, number=27,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_1', index=28, number=28,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_2', index=29, number=29,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_3', index=30, number=30,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_4', index=31, number=31,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_5', index=32, number=32,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_6', index=33, number=33,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_7', index=34, number=34,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_8', index=35, number=35,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_9', index=36, number=36,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_EQUAL', index=37, number=37,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_MINUS', index=38, number=38,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_RIGHT_BRACKET', index=39, number=39,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_LEFT_BRACKET', index=40, number=40,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_QUOTE', index=41, number=41,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_SEMICOLON', index=42, number=42,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_BACKSLASH', index=43, number=43,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_COMMA', index=44, number=44,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_SLASH', index=45, number=45,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_PERIOD', index=46, number=46,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_GRAVE', index=47, number=47,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_DECIMAL', index=48, number=48,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_PLUS', index=49, number=49,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_CLEAR', index=50, number=50,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_DIVIDE', index=51, number=51,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_ENTER', index=52, number=52,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_MINUS', index=53, number=53,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_EQUALS', index=54, number=54,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_0', index=55, number=55,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_1', index=56, number=56,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_2', index=57, number=57,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_3', index=58, number=58,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_4', index=59, number=59,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_5', index=60, number=60,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_6', index=61, number=61,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_7', index=62, number=62,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_8', index=63, number=63,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ANSI_KEYPAD_9', index=64, number=64,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F1', index=65, number=65,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F2', index=66, number=66,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F3', index=67, number=67,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F4', index=68, number=68,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F5', index=69, number=69,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F6', index=70, number=70,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F7', index=71, number=71,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F8', index=72, number=72,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F9', index=73, number=73,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F10', index=74, number=74,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F11', index=75, number=75,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F12', index=76, number=76,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F13', index=77, number=77,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F14', index=78, number=78,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F15', index=79, number=79,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F16', index=80, number=80,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F17', index=81, number=81,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F18', index=82, number=82,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F19', index=83, number=83,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_F20', index=84, number=84,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_FUNCTION', index=85, number=85,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_RETURN', index=86, number=86,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_TAB', index=87, number=87,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_SPACE', index=88, number=88,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_DELETE', index=89, number=89,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ESCAPE', index=90, number=90,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_COMMAND', index=91, number=91,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_SHIFT', index=92, number=92,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_CAPS_LOCK', index=93, number=93,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_OPTION', index=94, number=94,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_CONTROL', index=95, number=95,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_RIGHT_SHIFT', index=96, number=96,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_RIGHT_OPTION', index=97, number=97,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_RIGHT_CONTROL', index=98, number=98,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_VOLUME_UP', index=99, number=99,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_VOLUME_DOWN', index=100, number=100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_MUTE', index=101, number=101,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_HELP', index=102, number=102,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_HOME', index=103, number=103,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_PAGE_UP', index=104, number=104,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_FORWARD_DELETE', index=105, number=105,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_END', index=106, number=106,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_PAGE_DOWN', index=107, number=107,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_LEFT_ARROW', index=108, number=108,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_RIGHT_ARROW', index=109, number=109,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_DOWN_ARROW', index=110, number=110,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_UP_ARROW', index=111, number=111,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_ISO_SELECTION', index=112, number=112,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_JIS_YEN', index=113, number=113,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_JIS_UNDERSCORE', index=114, number=114,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_JIS_KEYPAD_COMMA', index=115, number=115,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_JIS_EISU', index=116, number=116,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_CODE_JIS_KANA', index=117, number=117,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=104,
  serialized_end=2817,
)
_sym_db.RegisterEnumDescriptor(_HOTKEY_KEYCODE)


_HOTKEY = _descriptor.Descriptor(
  name='HotKey',
  full_name='rv.data.HotKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='rv.data.HotKey.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='control_identifier', full_name='rv.data.HotKey.control_identifier', index=1,
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
    _HOTKEY_KEYCODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=2817,
)

_HOTKEY.fields_by_name['code'].enum_type = _HOTKEY_KEYCODE
_HOTKEY_KEYCODE.containing_type = _HOTKEY
DESCRIPTOR.message_types_by_name['HotKey'] = _HOTKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HotKey = _reflection.GeneratedProtocolMessageType('HotKey', (_message.Message,), {
  'DESCRIPTOR' : _HOTKEY,
  '__module__' : 'hotKey_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.HotKey)
  })
_sym_db.RegisterMessage(HotKey)


# @@protoc_insertion_point(module_scope)
