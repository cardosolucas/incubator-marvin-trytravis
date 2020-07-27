#!/usr/bin/env python
# coding=utf-8

# Copyright [2020] [Apache Software Foundation]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: daemon.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='daemon.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=b'\n\x0c\x64\x61\x65mon.proto\"\xf3\x01\n\x07\x43ommand\x12%\n\x07\x63ommand\x18\x01 \x01(\x0e\x32\x14.Command.CommandType\x12,\n\nparameters\x18\x02 \x03(\x0b\x32\x18.Command.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"`\n\x0b\x43ommandType\x12\n\n\x06\x44RYRUN\x10\x00\x12\x08\n\x04TEST\x10\x01\x12\x07\n\x03TDD\x10\x02\x12\x07\n\x03TOX\x10\x03\x12\x0c\n\x08NOTEBOOK\x10\x04\x12\x07\n\x03LAB\x10\x05\x12\x08\n\x04GRPC\x10\x06\x12\x08\n\x04HTTP\x10\x07\"\x0e\n\x0cInterruption\"\t\n\x07Request\"K\n\x06Status\x12\"\n\x06status\x18\x01 \x01(\x0e\x32\x12.Status.StatusType\"\x1d\n\nStatusType\x12\x06\n\x02OK\x10\x00\x12\x07\n\x03NOK\x10\x01\"-\n\x05State\x12\x13\n\x0b\x65ngine_name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t2z\n\x0b\x43ommandCall\x12\"\n\x0b\x63\x61llCommand\x12\x08.Command\x1a\x07.Status\"\x00\x12\'\n\x0bstopCommand\x12\r.Interruption\x1a\x07.Status\"\x00\x12\x1e\n\x08getState\x12\x08.Request\x1a\x06.State\"\x00\x62\x06proto3'
)


_COMMAND_COMMANDTYPE = _descriptor.EnumDescriptor(
    name='CommandType',
    full_name='Command.CommandType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='DRYRUN', index=0, number=0,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='TEST', index=1, number=1,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='TDD', index=2, number=2,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='TOX', index=3, number=3,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='NOTEBOOK', index=4, number=4,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='LAB', index=5, number=5,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='GRPC', index=6, number=6,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='HTTP', index=7, number=7,
            serialized_options=None,
            type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=164,
    serialized_end=260,
)
_sym_db.RegisterEnumDescriptor(_COMMAND_COMMANDTYPE)

_STATUS_STATUSTYPE = _descriptor.EnumDescriptor(
    name='StatusType',
    full_name='Status.StatusType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='OK', index=0, number=0,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='NOK', index=1, number=1,
            serialized_options=None,
            type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=335,
    serialized_end=364,
)
_sym_db.RegisterEnumDescriptor(_STATUS_STATUSTYPE)


_COMMAND_PARAMETERSENTRY = _descriptor.Descriptor(
    name='ParametersEntry',
    full_name='Command.ParametersEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='Command.ParametersEntry.key', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value', full_name='Command.ParametersEntry.value', index=1,
            number=2, type=9, cpp_type=9, label=1,
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
    serialized_options=b'8\001',
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=113,
    serialized_end=162,
)

_COMMAND = _descriptor.Descriptor(
    name='Command',
    full_name='Command',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='command', full_name='Command.command', index=0,
            number=1, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='parameters', full_name='Command.parameters', index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_COMMAND_PARAMETERSENTRY, ],
    enum_types=[
        _COMMAND_COMMANDTYPE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=17,
    serialized_end=260,
)


_INTERRUPTION = _descriptor.Descriptor(
    name='Interruption',
    full_name='Interruption',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
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
    serialized_start=262,
    serialized_end=276,
)


_REQUEST = _descriptor.Descriptor(
    name='Request',
    full_name='Request',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
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
    serialized_start=278,
    serialized_end=287,
)


_STATUS = _descriptor.Descriptor(
    name='Status',
    full_name='Status',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='status', full_name='Status.status', index=0,
            number=1, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _STATUS_STATUSTYPE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=289,
    serialized_end=364,
)


_STATE = _descriptor.Descriptor(
    name='State',
    full_name='State',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='engine_name', full_name='State.engine_name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='command', full_name='State.command', index=1,
            number=2, type=9, cpp_type=9, label=1,
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
    serialized_start=366,
    serialized_end=411,
)

_COMMAND_PARAMETERSENTRY.containing_type = _COMMAND
_COMMAND.fields_by_name['command'].enum_type = _COMMAND_COMMANDTYPE
_COMMAND.fields_by_name['parameters'].message_type = _COMMAND_PARAMETERSENTRY
_COMMAND_COMMANDTYPE.containing_type = _COMMAND
_STATUS.fields_by_name['status'].enum_type = _STATUS_STATUSTYPE
_STATUS_STATUSTYPE.containing_type = _STATUS
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Interruption'] = _INTERRUPTION
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['State'] = _STATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {

    'ParametersEntry': _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), {
        'DESCRIPTOR': _COMMAND_PARAMETERSENTRY,
        '__module__': 'daemon_pb2'
        # @@protoc_insertion_point(class_scope:Command.ParametersEntry)
    }),
    'DESCRIPTOR': _COMMAND,
    '__module__': 'daemon_pb2'
    # @@protoc_insertion_point(class_scope:Command)
})
_sym_db.RegisterMessage(Command)
_sym_db.RegisterMessage(Command.ParametersEntry)

Interruption = _reflection.GeneratedProtocolMessageType('Interruption', (_message.Message,), {
    'DESCRIPTOR': _INTERRUPTION,
    '__module__': 'daemon_pb2'
    # @@protoc_insertion_point(class_scope:Interruption)
})
_sym_db.RegisterMessage(Interruption)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
    'DESCRIPTOR': _REQUEST,
    '__module__': 'daemon_pb2'
    # @@protoc_insertion_point(class_scope:Request)
})
_sym_db.RegisterMessage(Request)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
    'DESCRIPTOR': _STATUS,
    '__module__': 'daemon_pb2'
    # @@protoc_insertion_point(class_scope:Status)
})
_sym_db.RegisterMessage(Status)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
    'DESCRIPTOR': _STATE,
    '__module__': 'daemon_pb2'
    # @@protoc_insertion_point(class_scope:State)
})
_sym_db.RegisterMessage(State)


_COMMAND_PARAMETERSENTRY._options = None

_COMMANDCALL = _descriptor.ServiceDescriptor(
    name='CommandCall',
    full_name='CommandCall',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=413,
    serialized_end=535,
    methods=[
        _descriptor.MethodDescriptor(
            name='callCommand',
            full_name='CommandCall.callCommand',
            index=0,
            containing_service=None,
            input_type=_COMMAND,
            output_type=_STATUS,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='stopCommand',
            full_name='CommandCall.stopCommand',
            index=1,
            containing_service=None,
            input_type=_INTERRUPTION,
            output_type=_STATUS,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='getState',
            full_name='CommandCall.getState',
            index=2,
            containing_service=None,
            input_type=_REQUEST,
            output_type=_STATE,
            serialized_options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_COMMANDCALL)

DESCRIPTOR.services_by_name['CommandCall'] = _COMMANDCALL

# @@protoc_insertion_point(module_scope)