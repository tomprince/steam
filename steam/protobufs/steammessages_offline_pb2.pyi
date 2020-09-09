# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from abc import (
    ABCMeta as abc___ABCMeta,
    abstractmethod as abc___abstractmethod,
)

from concurrent.futures import (
    Future as concurrent___futures___Future,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.service import (
    RpcChannel as google___protobuf___service___RpcChannel,
    RpcController as google___protobuf___service___RpcController,
    Service as google___protobuf___service___Service,
)

from typing import (
    Callable as typing___Callable,
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class COffline_GetOfflineLogonTicket_Request(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    priority: builtin___int = ...

    def __init__(self,
        *,
        priority : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"priority",b"priority"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"priority",b"priority"]) -> None: ...
type___COffline_GetOfflineLogonTicket_Request = COffline_GetOfflineLogonTicket_Request

class COffline_GetOfflineLogonTicket_Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    serialized_ticket: builtin___bytes = ...
    signature: builtin___bytes = ...

    def __init__(self,
        *,
        serialized_ticket : typing___Optional[builtin___bytes] = None,
        signature : typing___Optional[builtin___bytes] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"serialized_ticket",b"serialized_ticket",u"signature",b"signature"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"serialized_ticket",b"serialized_ticket",u"signature",b"signature"]) -> None: ...
type___COffline_GetOfflineLogonTicket_Response = COffline_GetOfflineLogonTicket_Response

class COffline_GetUnsignedOfflineLogonTicket_Request(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___COffline_GetUnsignedOfflineLogonTicket_Request = COffline_GetUnsignedOfflineLogonTicket_Request

class COffline_OfflineLogonTicket(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    accountid: builtin___int = ...
    rtime32_creation_time: builtin___int = ...

    def __init__(self,
        *,
        accountid : typing___Optional[builtin___int] = None,
        rtime32_creation_time : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"accountid",b"accountid",u"rtime32_creation_time",b"rtime32_creation_time"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"accountid",b"accountid",u"rtime32_creation_time",b"rtime32_creation_time"]) -> None: ...
type___COffline_OfflineLogonTicket = COffline_OfflineLogonTicket

class COffline_GetUnsignedOfflineLogonTicket_Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def ticket(self) -> type___COffline_OfflineLogonTicket: ...

    def __init__(self,
        *,
        ticket : typing___Optional[type___COffline_OfflineLogonTicket] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"ticket",b"ticket"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ticket",b"ticket"]) -> None: ...
type___COffline_GetUnsignedOfflineLogonTicket_Response = COffline_GetUnsignedOfflineLogonTicket_Response

class Offline(google___protobuf___service___Service, metaclass=abc___ABCMeta):
    @abc___abstractmethod
    def GetOfflineLogonTicket(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___COffline_GetOfflineLogonTicket_Request,
        done: typing___Optional[typing___Callable[[type___COffline_GetOfflineLogonTicket_Response], None]],
    ) -> concurrent___futures___Future[type___COffline_GetOfflineLogonTicket_Response]: ...
    @abc___abstractmethod
    def GetUnsignedOfflineLogonTicket(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___COffline_GetUnsignedOfflineLogonTicket_Request,
        done: typing___Optional[typing___Callable[[type___COffline_GetUnsignedOfflineLogonTicket_Response], None]],
    ) -> concurrent___futures___Future[type___COffline_GetUnsignedOfflineLogonTicket_Response]: ...
class Offline_Stub(Offline):
    def __init__(self, rpc_channel: google___protobuf___service___RpcChannel) -> None: ...
    def GetOfflineLogonTicket(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___COffline_GetOfflineLogonTicket_Request,
        done: typing___Optional[typing___Callable[[type___COffline_GetOfflineLogonTicket_Response], None]],
    ) -> concurrent___futures___Future[type___COffline_GetOfflineLogonTicket_Response]: ...
    def GetUnsignedOfflineLogonTicket(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___COffline_GetUnsignedOfflineLogonTicket_Request,
        done: typing___Optional[typing___Callable[[type___COffline_GetUnsignedOfflineLogonTicket_Response], None]],
    ) -> concurrent___futures___Future[type___COffline_GetUnsignedOfflineLogonTicket_Response]: ...