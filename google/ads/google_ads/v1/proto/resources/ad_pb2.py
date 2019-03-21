# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/resources/ad.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v1.proto.common import ad_type_infos_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2
from google.ads.google_ads.v1.proto.common import custom_parameter_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_custom__parameter__pb2
from google.ads.google_ads.v1.proto.common import url_collection_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_url__collection__pb2
from google.ads.google_ads.v1.proto.enums import ad_type_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_ad__type__pb2
from google.ads.google_ads.v1.proto.enums import device_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_device__pb2
from google.ads.google_ads.v1.proto.enums import system_managed_entity_source_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_system__managed__entity__source__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/resources/ad.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v1.resourcesB\007AdProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources'),
  serialized_pb=_b('\n0google/ads/googleads_v1/proto/resources/ad.proto\x12!google.ads.googleads.v1.resources\x1a\x38google/ads/googleads_v1/proto/common/ad_type_infos.proto\x1a;google/ads/googleads_v1/proto/common/custom_parameter.proto\x1a\x39google/ads/googleads_v1/proto/common/url_collection.proto\x1a\x31google/ads/googleads_v1/proto/enums/ad_type.proto\x1a\x30google/ads/googleads_v1/proto/enums/device.proto\x1a\x46google/ads/googleads_v1/proto/enums/system_managed_entity_source.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xb7\x0f\n\x02\x41\x64\x12\'\n\x02id\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x30\n\nfinal_urls\x18\x02 \x03(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11\x66inal_mobile_urls\x18\x10 \x03(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x15tracking_url_template\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12N\n\x15url_custom_parameters\x18\n \x03(\x0b\x32/.google.ads.googleads.v1.common.CustomParameter\x12\x31\n\x0b\x64isplay_url\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12>\n\x04type\x18\x05 \x01(\x0e\x32\x30.google.ads.googleads.v1.enums.AdTypeEnum.AdType\x12\x37\n\x13\x61\x64\x64\x65\x64_by_google_ads\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12K\n\x11\x64\x65vice_preference\x18\x14 \x01(\x0e\x32\x30.google.ads.googleads.v1.enums.DeviceEnum.Device\x12\x46\n\x0furl_collections\x18\x1a \x03(\x0b\x32-.google.ads.googleads.v1.common.UrlCollection\x12*\n\x04name\x18\x17 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x82\x01\n\x1esystem_managed_resource_source\x18\x1b \x01(\x0e\x32Z.google.ads.googleads.v1.enums.SystemManagedResourceSourceEnum.SystemManagedResourceSource\x12=\n\x07text_ad\x18\x06 \x01(\x0b\x32*.google.ads.googleads.v1.common.TextAdInfoH\x00\x12N\n\x10\x65xpanded_text_ad\x18\x07 \x01(\x0b\x32\x32.google.ads.googleads.v1.common.ExpandedTextAdInfoH\x00\x12\x46\n\x0c\x63\x61ll_only_ad\x18\r \x01(\x0b\x32..google.ads.googleads.v1.common.CallOnlyAdInfoH\x00\x12\x61\n\x1a\x65xpanded_dynamic_search_ad\x18\x0e \x01(\x0b\x32;.google.ads.googleads.v1.common.ExpandedDynamicSearchAdInfoH\x00\x12?\n\x08hotel_ad\x18\x0f \x01(\x0b\x32+.google.ads.googleads.v1.common.HotelAdInfoH\x00\x12P\n\x11shopping_smart_ad\x18\x11 \x01(\x0b\x32\x33.google.ads.googleads.v1.common.ShoppingSmartAdInfoH\x00\x12T\n\x13shopping_product_ad\x18\x12 \x01(\x0b\x32\x35.google.ads.googleads.v1.common.ShoppingProductAdInfoH\x00\x12?\n\x08gmail_ad\x18\x15 \x01(\x0b\x32+.google.ads.googleads.v1.common.GmailAdInfoH\x00\x12?\n\x08image_ad\x18\x16 \x01(\x0b\x32+.google.ads.googleads.v1.common.ImageAdInfoH\x00\x12?\n\x08video_ad\x18\x18 \x01(\x0b\x32+.google.ads.googleads.v1.common.VideoAdInfoH\x00\x12V\n\x14responsive_search_ad\x18\x19 \x01(\x0b\x32\x36.google.ads.googleads.v1.common.ResponsiveSearchAdInfoH\x00\x12\x65\n\x1clegacy_responsive_display_ad\x18\x1c \x01(\x0b\x32=.google.ads.googleads.v1.common.LegacyResponsiveDisplayAdInfoH\x00\x12;\n\x06\x61pp_ad\x18\x1d \x01(\x0b\x32).google.ads.googleads.v1.common.AppAdInfoH\x00\x12W\n\x15legacy_app_install_ad\x18\x1e \x01(\x0b\x32\x36.google.ads.googleads.v1.common.LegacyAppInstallAdInfoH\x00\x12X\n\x15responsive_display_ad\x18\x1f \x01(\x0b\x32\x37.google.ads.googleads.v1.common.ResponsiveDisplayAdInfoH\x00\x42\t\n\x07\x61\x64_dataB\xf4\x01\n%com.google.ads.googleads.v1.resourcesB\x07\x41\x64ProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_custom__parameter__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_url__collection__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_ad__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_device__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_system__managed__entity__source__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_AD = _descriptor.Descriptor(
  name='Ad',
  full_name='google.ads.googleads.v1.resources.Ad',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v1.resources.Ad.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='final_urls', full_name='google.ads.googleads.v1.resources.Ad.final_urls', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='final_mobile_urls', full_name='google.ads.googleads.v1.resources.Ad.final_mobile_urls', index=2,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tracking_url_template', full_name='google.ads.googleads.v1.resources.Ad.tracking_url_template', index=3,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url_custom_parameters', full_name='google.ads.googleads.v1.resources.Ad.url_custom_parameters', index=4,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_url', full_name='google.ads.googleads.v1.resources.Ad.display_url', index=5,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v1.resources.Ad.type', index=6,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='added_by_google_ads', full_name='google.ads.googleads.v1.resources.Ad.added_by_google_ads', index=7,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_preference', full_name='google.ads.googleads.v1.resources.Ad.device_preference', index=8,
      number=20, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url_collections', full_name='google.ads.googleads.v1.resources.Ad.url_collections', index=9,
      number=26, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v1.resources.Ad.name', index=10,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system_managed_resource_source', full_name='google.ads.googleads.v1.resources.Ad.system_managed_resource_source', index=11,
      number=27, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_ad', full_name='google.ads.googleads.v1.resources.Ad.text_ad', index=12,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expanded_text_ad', full_name='google.ads.googleads.v1.resources.Ad.expanded_text_ad', index=13,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_only_ad', full_name='google.ads.googleads.v1.resources.Ad.call_only_ad', index=14,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expanded_dynamic_search_ad', full_name='google.ads.googleads.v1.resources.Ad.expanded_dynamic_search_ad', index=15,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_ad', full_name='google.ads.googleads.v1.resources.Ad.hotel_ad', index=16,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shopping_smart_ad', full_name='google.ads.googleads.v1.resources.Ad.shopping_smart_ad', index=17,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shopping_product_ad', full_name='google.ads.googleads.v1.resources.Ad.shopping_product_ad', index=18,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gmail_ad', full_name='google.ads.googleads.v1.resources.Ad.gmail_ad', index=19,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_ad', full_name='google.ads.googleads.v1.resources.Ad.image_ad', index=20,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_ad', full_name='google.ads.googleads.v1.resources.Ad.video_ad', index=21,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='responsive_search_ad', full_name='google.ads.googleads.v1.resources.Ad.responsive_search_ad', index=22,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='legacy_responsive_display_ad', full_name='google.ads.googleads.v1.resources.Ad.legacy_responsive_display_ad', index=23,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_ad', full_name='google.ads.googleads.v1.resources.Ad.app_ad', index=24,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='legacy_app_install_ad', full_name='google.ads.googleads.v1.resources.Ad.legacy_app_install_ad', index=25,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='responsive_display_ad', full_name='google.ads.googleads.v1.resources.Ad.responsive_display_ad', index=26,
      number=31, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='ad_data', full_name='google.ads.googleads.v1.resources.Ad.ad_data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=501,
  serialized_end=2476,
)

_AD.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_AD.fields_by_name['final_urls'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_AD.fields_by_name['final_mobile_urls'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_AD.fields_by_name['tracking_url_template'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_AD.fields_by_name['url_custom_parameters'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_custom__parameter__pb2._CUSTOMPARAMETER
_AD.fields_by_name['display_url'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_AD.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_ad__type__pb2._ADTYPEENUM_ADTYPE
_AD.fields_by_name['added_by_google_ads'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_AD.fields_by_name['device_preference'].enum_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_device__pb2._DEVICEENUM_DEVICE
_AD.fields_by_name['url_collections'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_url__collection__pb2._URLCOLLECTION
_AD.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_AD.fields_by_name['system_managed_resource_source'].enum_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_system__managed__entity__source__pb2._SYSTEMMANAGEDRESOURCESOURCEENUM_SYSTEMMANAGEDRESOURCESOURCE
_AD.fields_by_name['text_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._TEXTADINFO
_AD.fields_by_name['expanded_text_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._EXPANDEDTEXTADINFO
_AD.fields_by_name['call_only_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._CALLONLYADINFO
_AD.fields_by_name['expanded_dynamic_search_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._EXPANDEDDYNAMICSEARCHADINFO
_AD.fields_by_name['hotel_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._HOTELADINFO
_AD.fields_by_name['shopping_smart_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._SHOPPINGSMARTADINFO
_AD.fields_by_name['shopping_product_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._SHOPPINGPRODUCTADINFO
_AD.fields_by_name['gmail_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._GMAILADINFO
_AD.fields_by_name['image_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._IMAGEADINFO
_AD.fields_by_name['video_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._VIDEOADINFO
_AD.fields_by_name['responsive_search_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._RESPONSIVESEARCHADINFO
_AD.fields_by_name['legacy_responsive_display_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._LEGACYRESPONSIVEDISPLAYADINFO
_AD.fields_by_name['app_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._APPADINFO
_AD.fields_by_name['legacy_app_install_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._LEGACYAPPINSTALLADINFO
_AD.fields_by_name['responsive_display_ad'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_ad__type__infos__pb2._RESPONSIVEDISPLAYADINFO
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['text_ad'])
_AD.fields_by_name['text_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['expanded_text_ad'])
_AD.fields_by_name['expanded_text_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['call_only_ad'])
_AD.fields_by_name['call_only_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['expanded_dynamic_search_ad'])
_AD.fields_by_name['expanded_dynamic_search_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['hotel_ad'])
_AD.fields_by_name['hotel_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['shopping_smart_ad'])
_AD.fields_by_name['shopping_smart_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['shopping_product_ad'])
_AD.fields_by_name['shopping_product_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['gmail_ad'])
_AD.fields_by_name['gmail_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['image_ad'])
_AD.fields_by_name['image_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['video_ad'])
_AD.fields_by_name['video_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['responsive_search_ad'])
_AD.fields_by_name['responsive_search_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['legacy_responsive_display_ad'])
_AD.fields_by_name['legacy_responsive_display_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['app_ad'])
_AD.fields_by_name['app_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['legacy_app_install_ad'])
_AD.fields_by_name['legacy_app_install_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
_AD.oneofs_by_name['ad_data'].fields.append(
  _AD.fields_by_name['responsive_display_ad'])
_AD.fields_by_name['responsive_display_ad'].containing_oneof = _AD.oneofs_by_name['ad_data']
DESCRIPTOR.message_types_by_name['Ad'] = _AD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ad = _reflection.GeneratedProtocolMessageType('Ad', (_message.Message,), dict(
  DESCRIPTOR = _AD,
  __module__ = 'google.ads.googleads_v1.proto.resources.ad_pb2'
  ,
  __doc__ = """An ad.
  
  
  Attributes:
      id:
          The ID of the ad.
      final_urls:
          The list of possible final URLs after all cross-domain
          redirects for the ad.
      final_mobile_urls:
          The list of possible final mobile URLs after all cross-domain
          redirects for the ad.
      tracking_url_template:
          The URL template for constructing a tracking URL.
      url_custom_parameters:
          The list of mappings that can be used to substitute custom
          parameter tags in a ``tracking_url_template``, ``final_urls``,
          or ``mobile_final_urls``.
      display_url:
          The URL that appears in the ad description for some ad
          formats.
      type:
          The type of ad.
      added_by_google_ads:
          Indicates if this ad was automatically added by Google Ads and
          not by a user. For example, this could happen when ads are
          automatically created as suggestions for new ads based on
          knowledge of how existing ads are performing.
      device_preference:
          The device preference for the ad. You can only specify a
          preference for mobile devices. When this preference is set the
          ad will be preferred over other ads when being displayed on a
          mobile device. The ad can still be displayed on other device
          types, e.g. if no other ads are available. If unspecified (no
          device preference), all devices are targeted. This is only
          supported by some ad types.
      url_collections:
          Additional URLs for the ad that are tagged with a unique
          identifier that can be referenced from other fields in the ad.
      name:
          The name of the ad. This is only used to be able to identify
          the ad. It does not need to be unique and does not affect the
          served ad.
      system_managed_resource_source:
          If this ad is system managed, then this field will indicate
          the source. This field is read-only.
      ad_data:
          Details pertinent to the ad type. Exactly one value must be
          set.
      text_ad:
          Details pertaining to a text ad.
      expanded_text_ad:
          Details pertaining to an expanded text ad.
      call_only_ad:
          Details pertaining to a call-only ad.
      expanded_dynamic_search_ad:
          Details pertaining to an Expanded Dynamic Search Ad. This type
          of ad has its headline, final URLs, and display URL auto-
          generated at serving time according to domain name specific
          information provided by ``dynamic_search_ads_setting`` linked
          at the campaign level.
      hotel_ad:
          Details pertaining to a hotel ad.
      shopping_smart_ad:
          Details pertaining to a Smart Shopping ad.
      shopping_product_ad:
          Details pertaining to a Shopping product ad.
      gmail_ad:
          Details pertaining to a Gmail ad.
      image_ad:
          Details pertaining to an Image ad.
      video_ad:
          Details pertaining to a Video ad.
      responsive_search_ad:
          Details pertaining to a responsive search ad.
      legacy_responsive_display_ad:
          Details pertaining to a legacy responsive display ad.
      app_ad:
          Details pertaining to an app ad.
      legacy_app_install_ad:
          Details pertaining to a legacy app install ad.
      responsive_display_ad:
          Details pertaining to a responsive display ad.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.Ad)
  ))
_sym_db.RegisterMessage(Ad)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
