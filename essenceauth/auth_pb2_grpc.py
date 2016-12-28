import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2
import auth_pb2 as auth__pb2


class EssenceAuthStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AppGetUser = channel.unary_unary(
        '/essenceauth.EssenceAuth/AppGetUser',
        request_serializer=auth__pb2.AppUserRequest.SerializeToString,
        response_deserializer=auth__pb2.User.FromString,
        )
    self.AppGetApp = channel.unary_unary(
        '/essenceauth.EssenceAuth/AppGetApp',
        request_serializer=auth__pb2.App.SerializeToString,
        response_deserializer=auth__pb2.App.FromString,
        )
    self.AppUpdateApp = channel.unary_unary(
        '/essenceauth.EssenceAuth/AppUpdateApp',
        request_serializer=auth__pb2.App.SerializeToString,
        response_deserializer=auth__pb2.App.FromString,
        )
    self.ListApps = channel.unary_unary(
        '/essenceauth.EssenceAuth/ListApps',
        request_serializer=auth__pb2.Empty.SerializeToString,
        response_deserializer=auth__pb2.AppList.FromString,
        )
    self.GetApp = channel.unary_unary(
        '/essenceauth.EssenceAuth/GetApp',
        request_serializer=auth__pb2.App.SerializeToString,
        response_deserializer=auth__pb2.App.FromString,
        )
    self.CreateApp = channel.unary_unary(
        '/essenceauth.EssenceAuth/CreateApp',
        request_serializer=auth__pb2.App.SerializeToString,
        response_deserializer=auth__pb2.App.FromString,
        )
    self.PutApp = channel.unary_unary(
        '/essenceauth.EssenceAuth/PutApp',
        request_serializer=auth__pb2.AppChange.SerializeToString,
        response_deserializer=auth__pb2.App.FromString,
        )
    self.DeleteApp = channel.unary_unary(
        '/essenceauth.EssenceAuth/DeleteApp',
        request_serializer=auth__pb2.App.SerializeToString,
        response_deserializer=auth__pb2.Empty.FromString,
        )
    self.GetAppMembers = channel.unary_unary(
        '/essenceauth.EssenceAuth/GetAppMembers',
        request_serializer=auth__pb2.App.SerializeToString,
        response_deserializer=auth__pb2.Membership.FromString,
        )
    self.ListGroups = channel.unary_unary(
        '/essenceauth.EssenceAuth/ListGroups',
        request_serializer=auth__pb2.Empty.SerializeToString,
        response_deserializer=auth__pb2.GroupList.FromString,
        )
    self.GetGroup = channel.unary_unary(
        '/essenceauth.EssenceAuth/GetGroup',
        request_serializer=auth__pb2.Group.SerializeToString,
        response_deserializer=auth__pb2.Group.FromString,
        )
    self.CreateGroup = channel.unary_unary(
        '/essenceauth.EssenceAuth/CreateGroup',
        request_serializer=auth__pb2.Group.SerializeToString,
        response_deserializer=auth__pb2.Group.FromString,
        )
    self.PutGroup = channel.unary_unary(
        '/essenceauth.EssenceAuth/PutGroup',
        request_serializer=auth__pb2.GroupChange.SerializeToString,
        response_deserializer=auth__pb2.Group.FromString,
        )
    self.DeleteGroup = channel.unary_unary(
        '/essenceauth.EssenceAuth/DeleteGroup',
        request_serializer=auth__pb2.Group.SerializeToString,
        response_deserializer=auth__pb2.Empty.FromString,
        )
    self.GetGroupMembers = channel.unary_unary(
        '/essenceauth.EssenceAuth/GetGroupMembers',
        request_serializer=auth__pb2.Group.SerializeToString,
        response_deserializer=auth__pb2.Membership.FromString,
        )
    self.ListUsers = channel.unary_unary(
        '/essenceauth.EssenceAuth/ListUsers',
        request_serializer=auth__pb2.Empty.SerializeToString,
        response_deserializer=auth__pb2.UserList.FromString,
        )
    self.GetUser = channel.unary_unary(
        '/essenceauth.EssenceAuth/GetUser',
        request_serializer=auth__pb2.User.SerializeToString,
        response_deserializer=auth__pb2.User.FromString,
        )
    self.CreateUser = channel.unary_unary(
        '/essenceauth.EssenceAuth/CreateUser',
        request_serializer=auth__pb2.UserChange.SerializeToString,
        response_deserializer=auth__pb2.User.FromString,
        )
    self.PutUser = channel.unary_unary(
        '/essenceauth.EssenceAuth/PutUser',
        request_serializer=auth__pb2.UserChange.SerializeToString,
        response_deserializer=auth__pb2.User.FromString,
        )
    self.DeleteUser = channel.unary_unary(
        '/essenceauth.EssenceAuth/DeleteUser',
        request_serializer=auth__pb2.User.SerializeToString,
        response_deserializer=auth__pb2.Empty.FromString,
        )
    self.ResetUserPassword = channel.unary_unary(
        '/essenceauth.EssenceAuth/ResetUserPassword',
        request_serializer=auth__pb2.User.SerializeToString,
        response_deserializer=auth__pb2.UserChange.FromString,
        )


class EssenceAuthServicer(object):

  def AppGetUser(self, request, context):
    """Application endpoints. These are for applications to perform requests related to
    themselves.

    Used by an application to fetch information about a user using their JWT.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AppGetApp(self, request, context):
    """An application can get info about itself.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AppUpdateApp(self, request, context):
    """Allows an application to provide information about its available permissions.
    Those permissions can then be given to groups and therefore users.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListApps(self, request, context):
    """Service administration endpoints. These require a user JWT to be provided as a GRPC metadata
    key, "authorization". If using REST this can be provided with the header "Grpc-Metadata-Authorization".


    Applications


    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetApp(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateApp(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutApp(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteApp(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAppMembers(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListGroups(self, request, context):
    """
    Groups


    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetGroup(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateGroup(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutGroup(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteGroup(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetGroupMembers(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListUsers(self, request, context):
    """
    Users


    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUser(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateUser(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutUser(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteUser(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ResetUserPassword(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EssenceAuthServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AppGetUser': grpc.unary_unary_rpc_method_handler(
          servicer.AppGetUser,
          request_deserializer=auth__pb2.AppUserRequest.FromString,
          response_serializer=auth__pb2.User.SerializeToString,
      ),
      'AppGetApp': grpc.unary_unary_rpc_method_handler(
          servicer.AppGetApp,
          request_deserializer=auth__pb2.App.FromString,
          response_serializer=auth__pb2.App.SerializeToString,
      ),
      'AppUpdateApp': grpc.unary_unary_rpc_method_handler(
          servicer.AppUpdateApp,
          request_deserializer=auth__pb2.App.FromString,
          response_serializer=auth__pb2.App.SerializeToString,
      ),
      'ListApps': grpc.unary_unary_rpc_method_handler(
          servicer.ListApps,
          request_deserializer=auth__pb2.Empty.FromString,
          response_serializer=auth__pb2.AppList.SerializeToString,
      ),
      'GetApp': grpc.unary_unary_rpc_method_handler(
          servicer.GetApp,
          request_deserializer=auth__pb2.App.FromString,
          response_serializer=auth__pb2.App.SerializeToString,
      ),
      'CreateApp': grpc.unary_unary_rpc_method_handler(
          servicer.CreateApp,
          request_deserializer=auth__pb2.App.FromString,
          response_serializer=auth__pb2.App.SerializeToString,
      ),
      'PutApp': grpc.unary_unary_rpc_method_handler(
          servicer.PutApp,
          request_deserializer=auth__pb2.AppChange.FromString,
          response_serializer=auth__pb2.App.SerializeToString,
      ),
      'DeleteApp': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteApp,
          request_deserializer=auth__pb2.App.FromString,
          response_serializer=auth__pb2.Empty.SerializeToString,
      ),
      'GetAppMembers': grpc.unary_unary_rpc_method_handler(
          servicer.GetAppMembers,
          request_deserializer=auth__pb2.App.FromString,
          response_serializer=auth__pb2.Membership.SerializeToString,
      ),
      'ListGroups': grpc.unary_unary_rpc_method_handler(
          servicer.ListGroups,
          request_deserializer=auth__pb2.Empty.FromString,
          response_serializer=auth__pb2.GroupList.SerializeToString,
      ),
      'GetGroup': grpc.unary_unary_rpc_method_handler(
          servicer.GetGroup,
          request_deserializer=auth__pb2.Group.FromString,
          response_serializer=auth__pb2.Group.SerializeToString,
      ),
      'CreateGroup': grpc.unary_unary_rpc_method_handler(
          servicer.CreateGroup,
          request_deserializer=auth__pb2.Group.FromString,
          response_serializer=auth__pb2.Group.SerializeToString,
      ),
      'PutGroup': grpc.unary_unary_rpc_method_handler(
          servicer.PutGroup,
          request_deserializer=auth__pb2.GroupChange.FromString,
          response_serializer=auth__pb2.Group.SerializeToString,
      ),
      'DeleteGroup': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteGroup,
          request_deserializer=auth__pb2.Group.FromString,
          response_serializer=auth__pb2.Empty.SerializeToString,
      ),
      'GetGroupMembers': grpc.unary_unary_rpc_method_handler(
          servicer.GetGroupMembers,
          request_deserializer=auth__pb2.Group.FromString,
          response_serializer=auth__pb2.Membership.SerializeToString,
      ),
      'ListUsers': grpc.unary_unary_rpc_method_handler(
          servicer.ListUsers,
          request_deserializer=auth__pb2.Empty.FromString,
          response_serializer=auth__pb2.UserList.SerializeToString,
      ),
      'GetUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetUser,
          request_deserializer=auth__pb2.User.FromString,
          response_serializer=auth__pb2.User.SerializeToString,
      ),
      'CreateUser': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUser,
          request_deserializer=auth__pb2.UserChange.FromString,
          response_serializer=auth__pb2.User.SerializeToString,
      ),
      'PutUser': grpc.unary_unary_rpc_method_handler(
          servicer.PutUser,
          request_deserializer=auth__pb2.UserChange.FromString,
          response_serializer=auth__pb2.User.SerializeToString,
      ),
      'DeleteUser': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteUser,
          request_deserializer=auth__pb2.User.FromString,
          response_serializer=auth__pb2.Empty.SerializeToString,
      ),
      'ResetUserPassword': grpc.unary_unary_rpc_method_handler(
          servicer.ResetUserPassword,
          request_deserializer=auth__pb2.User.FromString,
          response_serializer=auth__pb2.UserChange.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'essenceauth.EssenceAuth', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
