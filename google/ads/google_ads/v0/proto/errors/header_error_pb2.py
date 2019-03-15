# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/header_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/errors/header_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v0.errorsB\020HeaderErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors\352\002\"Google::Ads::GoogleAds::V0::Errors'),
  serialized_pb=_b('\n7google/ads/googleads_v0/proto/errors/header_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"]\n\x0fHeaderErrorEnum\"J\n\x0bHeaderError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1d\n\x19INVALID_LOGIN_CUSTOMER_ID\x10\x03\x42\xeb\x01\n\"com.google.ads.googleads.v0.errorsB\x10HeaderErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errors\xea\x02\"Google::Ads::GoogleAds::V0::Errorsb\x06proto3')
)



_HEADERERRORENUM_HEADERERROR = _descriptor.EnumDescriptor(
  name='HeaderError',
  full_name='google.ads.googleads.v0.errors.HeaderErrorEnum.HeaderError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_LOGIN_CUSTOMER_ID', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=110,
  serialized_end=184,
)
_sym_db.RegisterEnumDescriptor(_HEADERERRORENUM_HEADERERROR)


_HEADERERRORENUM = _descriptor.Descriptor(
  name='HeaderErrorEnum',
  full_name='google.ads.googleads.v0.errors.HeaderErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HEADERERRORENUM_HEADERERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=184,
)

_HEADERERRORENUM_HEADERERROR.containing_type = _HEADERERRORENUM
DESCRIPTOR.message_types_by_name['HeaderErrorEnum'] = _HEADERERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HeaderErrorEnum = _reflection.GeneratedProtocolMessageType('HeaderErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _HEADERERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.header_error_pb2'
  ,
  __doc__ = """Container for enum describing possible header errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.HeaderErrorEnum)
  ))
_sym_db.RegisterMessage(HeaderErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)