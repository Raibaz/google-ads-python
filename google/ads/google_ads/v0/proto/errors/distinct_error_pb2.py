# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/distinct_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/errors/distinct_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\n9google/ads/googleads_v0/proto/errors/distinct_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"m\n\x11\x44istinctErrorEnum\"X\n\rDistinctError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x15\n\x11\x44UPLICATE_ELEMENT\x10\x02\x12\x12\n\x0e\x44UPLICATE_TYPE\x10\x03\x42\xc8\x01\n\"com.google.ads.googleads.v0.errorsB\x12\x44istinctErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_DISTINCTERRORENUM_DISTINCTERROR = _descriptor.EnumDescriptor(
  name='DistinctError',
  full_name='google.ads.googleads.v0.errors.DistinctErrorEnum.DistinctError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_ELEMENT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_TYPE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=114,
  serialized_end=202,
)
_sym_db.RegisterEnumDescriptor(_DISTINCTERRORENUM_DISTINCTERROR)


_DISTINCTERRORENUM = _descriptor.Descriptor(
  name='DistinctErrorEnum',
  full_name='google.ads.googleads.v0.errors.DistinctErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DISTINCTERRORENUM_DISTINCTERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=202,
)

_DISTINCTERRORENUM_DISTINCTERROR.containing_type = _DISTINCTERRORENUM
DESCRIPTOR.message_types_by_name['DistinctErrorEnum'] = _DISTINCTERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DistinctErrorEnum = _reflection.GeneratedProtocolMessageType('DistinctErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _DISTINCTERRORENUM,
  __module__ = 'google.ads.google_ads.v0.proto.errors.distinct_error_pb2'
  ,
  __doc__ = """Container for enum describing possible distinct errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.DistinctErrorEnum)
  ))
_sym_db.RegisterMessage(DistinctErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB\022DistinctErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)