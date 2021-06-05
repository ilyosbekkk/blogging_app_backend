# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import posts_pb2 as posts__pb2


class PostServiceStub(object):
    """rpcs
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.uploadPost = channel.unary_unary(
                '/PostService/uploadPost',
                request_serializer=posts__pb2.UploadPost.Request.SerializeToString,
                response_deserializer=posts__pb2.UploadPost.Response.FromString,
                )
        self.fetchPostDetails = channel.unary_unary(
                '/PostService/fetchPostDetails',
                request_serializer=posts__pb2.FetchPostDetails.Request.SerializeToString,
                response_deserializer=posts__pb2.FetchPostDetails.Response.FromString,
                )
        self.fetchPosts = channel.unary_unary(
                '/PostService/fetchPosts',
                request_serializer=posts__pb2.FetchKPosts.Request.SerializeToString,
                response_deserializer=posts__pb2.FetchKPosts.Response.FromString,
                )


class PostServiceServicer(object):
    """rpcs
    """

    def uploadPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchPostDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchPosts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PostServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'uploadPost': grpc.unary_unary_rpc_method_handler(
                    servicer.uploadPost,
                    request_deserializer=posts__pb2.UploadPost.Request.FromString,
                    response_serializer=posts__pb2.UploadPost.Response.SerializeToString,
            ),
            'fetchPostDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.fetchPostDetails,
                    request_deserializer=posts__pb2.FetchPostDetails.Request.FromString,
                    response_serializer=posts__pb2.FetchPostDetails.Response.SerializeToString,
            ),
            'fetchPosts': grpc.unary_unary_rpc_method_handler(
                    servicer.fetchPosts,
                    request_deserializer=posts__pb2.FetchKPosts.Request.FromString,
                    response_serializer=posts__pb2.FetchKPosts.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PostService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PostService(object):
    """rpcs
    """

    @staticmethod
    def uploadPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PostService/uploadPost',
            posts__pb2.UploadPost.Request.SerializeToString,
            posts__pb2.UploadPost.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def fetchPostDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PostService/fetchPostDetails',
            posts__pb2.FetchPostDetails.Request.SerializeToString,
            posts__pb2.FetchPostDetails.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def fetchPosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PostService/fetchPosts',
            posts__pb2.FetchKPosts.Request.SerializeToString,
            posts__pb2.FetchKPosts.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
