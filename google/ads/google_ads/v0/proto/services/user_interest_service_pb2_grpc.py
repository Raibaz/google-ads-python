# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v0.proto.resources import user_interest_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_user__interest__pb2
from google.ads.google_ads.v0.proto.services import user_interest_service_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_user__interest__service__pb2


class UserInterestServiceStub(object):
  """Service to fetch Google Ads User Interest.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetUserInterest = channel.unary_unary(
        '/google.ads.googleads.v0.services.UserInterestService/GetUserInterest',
        request_serializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_user__interest__service__pb2.GetUserInterestRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_user__interest__pb2.UserInterest.FromString,
        )


class UserInterestServiceServicer(object):
  """Service to fetch Google Ads User Interest.
  """

  def GetUserInterest(self, request, context):
    """Returns the requested user interest in full detail
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserInterestServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetUserInterest': grpc.unary_unary_rpc_method_handler(
          servicer.GetUserInterest,
          request_deserializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_user__interest__service__pb2.GetUserInterestRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_user__interest__pb2.UserInterest.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v0.services.UserInterestService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
