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

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
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
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CCredentials_TestAvailablePassword_Request(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    password: typing___Text = ...
    sha_digest_password: builtin___bytes = ...
    account_name: typing___Text = ...

    def __init__(self,
        *,
        password : typing___Optional[typing___Text] = None,
        sha_digest_password : typing___Optional[builtin___bytes] = None,
        account_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"account_name",b"account_name",u"password",b"password",u"sha_digest_password",b"sha_digest_password"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"account_name",b"account_name",u"password",b"password",u"sha_digest_password",b"sha_digest_password"]) -> None: ...
type___CCredentials_TestAvailablePassword_Request = CCredentials_TestAvailablePassword_Request

class CCredentials_TestAvailablePassword_Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    is_valid: builtin___bool = ...

    def __init__(self,
        *,
        is_valid : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"is_valid",b"is_valid"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"is_valid",b"is_valid"]) -> None: ...
type___CCredentials_TestAvailablePassword_Response = CCredentials_TestAvailablePassword_Response

class CCredentials_GetSteamGuardDetails_Request(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    include_new_authentications: builtin___bool = ...
    webcookie: typing___Text = ...
    timestamp_minimum_wanted: builtin___int = ...
    ipaddress: builtin___int = ...

    def __init__(self,
        *,
        include_new_authentications : typing___Optional[builtin___bool] = None,
        webcookie : typing___Optional[typing___Text] = None,
        timestamp_minimum_wanted : typing___Optional[builtin___int] = None,
        ipaddress : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"include_new_authentications",b"include_new_authentications",u"ipaddress",b"ipaddress",u"timestamp_minimum_wanted",b"timestamp_minimum_wanted",u"webcookie",b"webcookie"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"include_new_authentications",b"include_new_authentications",u"ipaddress",b"ipaddress",u"timestamp_minimum_wanted",b"timestamp_minimum_wanted",u"webcookie",b"webcookie"]) -> None: ...
type___CCredentials_GetSteamGuardDetails_Request = CCredentials_GetSteamGuardDetails_Request

class CCredentials_GetSteamGuardDetails_Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class NewAuthentication(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        timestamp_steamguard_enabled: builtin___int = ...
        is_web_cookie: builtin___bool = ...
        ipaddress: builtin___int = ...
        geoloc_info: typing___Text = ...
        is_remembered: builtin___bool = ...
        machine_name_user_supplied: typing___Text = ...
        status: builtin___int = ...

        def __init__(self,
            *,
            timestamp_steamguard_enabled : typing___Optional[builtin___int] = None,
            is_web_cookie : typing___Optional[builtin___bool] = None,
            ipaddress : typing___Optional[builtin___int] = None,
            geoloc_info : typing___Optional[typing___Text] = None,
            is_remembered : typing___Optional[builtin___bool] = None,
            machine_name_user_supplied : typing___Optional[typing___Text] = None,
            status : typing___Optional[builtin___int] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"geoloc_info",b"geoloc_info",u"ipaddress",b"ipaddress",u"is_remembered",b"is_remembered",u"is_web_cookie",b"is_web_cookie",u"machine_name_user_supplied",b"machine_name_user_supplied",u"status",b"status",u"timestamp_steamguard_enabled",b"timestamp_steamguard_enabled"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"geoloc_info",b"geoloc_info",u"ipaddress",b"ipaddress",u"is_remembered",b"is_remembered",u"is_web_cookie",b"is_web_cookie",u"machine_name_user_supplied",b"machine_name_user_supplied",u"status",b"status",u"timestamp_steamguard_enabled",b"timestamp_steamguard_enabled"]) -> None: ...
    type___NewAuthentication = NewAuthentication

    class SessionData(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        machine_id: builtin___int = ...
        machine_name_userchosen: typing___Text = ...
        timestamp_machine_steamguard_enabled: builtin___int = ...
        authentication_exists_from_geoloc_before_mintime: builtin___bool = ...
        authentication_exists_from_same_ip_before_mintime: builtin___bool = ...
        public_ipv4: builtin___int = ...
        public_ip_address: typing___Text = ...

        @property
        def newauthentication(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___CCredentials_GetSteamGuardDetails_Response.NewAuthentication]: ...

        def __init__(self,
            *,
            machine_id : typing___Optional[builtin___int] = None,
            machine_name_userchosen : typing___Optional[typing___Text] = None,
            timestamp_machine_steamguard_enabled : typing___Optional[builtin___int] = None,
            authentication_exists_from_geoloc_before_mintime : typing___Optional[builtin___bool] = None,
            newauthentication : typing___Optional[typing___Iterable[type___CCredentials_GetSteamGuardDetails_Response.NewAuthentication]] = None,
            authentication_exists_from_same_ip_before_mintime : typing___Optional[builtin___bool] = None,
            public_ipv4 : typing___Optional[builtin___int] = None,
            public_ip_address : typing___Optional[typing___Text] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"authentication_exists_from_geoloc_before_mintime",b"authentication_exists_from_geoloc_before_mintime",u"authentication_exists_from_same_ip_before_mintime",b"authentication_exists_from_same_ip_before_mintime",u"machine_id",b"machine_id",u"machine_name_userchosen",b"machine_name_userchosen",u"public_ip_address",b"public_ip_address",u"public_ipv4",b"public_ipv4",u"timestamp_machine_steamguard_enabled",b"timestamp_machine_steamguard_enabled"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"authentication_exists_from_geoloc_before_mintime",b"authentication_exists_from_geoloc_before_mintime",u"authentication_exists_from_same_ip_before_mintime",b"authentication_exists_from_same_ip_before_mintime",u"machine_id",b"machine_id",u"machine_name_userchosen",b"machine_name_userchosen",u"newauthentication",b"newauthentication",u"public_ip_address",b"public_ip_address",u"public_ipv4",b"public_ipv4",u"timestamp_machine_steamguard_enabled",b"timestamp_machine_steamguard_enabled"]) -> None: ...
    type___SessionData = SessionData

    is_steamguard_enabled: builtin___bool = ...
    timestamp_steamguard_enabled: builtin___int = ...
    deprecated_machine_name_userchosen: typing___Text = ...
    deprecated_timestamp_machine_steamguard_enabled: builtin___int = ...
    deprecated_authentication_exists_from_geoloc_before_mintime: builtin___bool = ...
    deprecated_machine_id: builtin___int = ...
    is_twofactor_enabled: builtin___bool = ...
    timestamp_twofactor_enabled: builtin___int = ...
    is_phone_verified: builtin___bool = ...

    @property
    def deprecated_newauthentication(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___CCredentials_GetSteamGuardDetails_Response.NewAuthentication]: ...

    @property
    def session_data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___CCredentials_GetSteamGuardDetails_Response.SessionData]: ...

    def __init__(self,
        *,
        is_steamguard_enabled : typing___Optional[builtin___bool] = None,
        timestamp_steamguard_enabled : typing___Optional[builtin___int] = None,
        deprecated_newauthentication : typing___Optional[typing___Iterable[type___CCredentials_GetSteamGuardDetails_Response.NewAuthentication]] = None,
        deprecated_machine_name_userchosen : typing___Optional[typing___Text] = None,
        deprecated_timestamp_machine_steamguard_enabled : typing___Optional[builtin___int] = None,
        deprecated_authentication_exists_from_geoloc_before_mintime : typing___Optional[builtin___bool] = None,
        deprecated_machine_id : typing___Optional[builtin___int] = None,
        session_data : typing___Optional[typing___Iterable[type___CCredentials_GetSteamGuardDetails_Response.SessionData]] = None,
        is_twofactor_enabled : typing___Optional[builtin___bool] = None,
        timestamp_twofactor_enabled : typing___Optional[builtin___int] = None,
        is_phone_verified : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"deprecated_authentication_exists_from_geoloc_before_mintime",b"deprecated_authentication_exists_from_geoloc_before_mintime",u"deprecated_machine_id",b"deprecated_machine_id",u"deprecated_machine_name_userchosen",b"deprecated_machine_name_userchosen",u"deprecated_timestamp_machine_steamguard_enabled",b"deprecated_timestamp_machine_steamguard_enabled",u"is_phone_verified",b"is_phone_verified",u"is_steamguard_enabled",b"is_steamguard_enabled",u"is_twofactor_enabled",b"is_twofactor_enabled",u"timestamp_steamguard_enabled",b"timestamp_steamguard_enabled",u"timestamp_twofactor_enabled",b"timestamp_twofactor_enabled"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"deprecated_authentication_exists_from_geoloc_before_mintime",b"deprecated_authentication_exists_from_geoloc_before_mintime",u"deprecated_machine_id",b"deprecated_machine_id",u"deprecated_machine_name_userchosen",b"deprecated_machine_name_userchosen",u"deprecated_newauthentication",b"deprecated_newauthentication",u"deprecated_timestamp_machine_steamguard_enabled",b"deprecated_timestamp_machine_steamguard_enabled",u"is_phone_verified",b"is_phone_verified",u"is_steamguard_enabled",b"is_steamguard_enabled",u"is_twofactor_enabled",b"is_twofactor_enabled",u"session_data",b"session_data",u"timestamp_steamguard_enabled",b"timestamp_steamguard_enabled",u"timestamp_twofactor_enabled",b"timestamp_twofactor_enabled"]) -> None: ...
type___CCredentials_GetSteamGuardDetails_Response = CCredentials_GetSteamGuardDetails_Response

class CCredentials_NewMachineNotificationDialog_Request(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    is_approved: builtin___bool = ...
    is_wizard_complete: builtin___bool = ...

    def __init__(self,
        *,
        is_approved : typing___Optional[builtin___bool] = None,
        is_wizard_complete : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"is_approved",b"is_approved",u"is_wizard_complete",b"is_wizard_complete"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"is_approved",b"is_approved",u"is_wizard_complete",b"is_wizard_complete"]) -> None: ...
type___CCredentials_NewMachineNotificationDialog_Request = CCredentials_NewMachineNotificationDialog_Request

class CCredentials_NewMachineNotificationDialog_Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___CCredentials_NewMachineNotificationDialog_Response = CCredentials_NewMachineNotificationDialog_Response

class CCredentials_ValidateEmailAddress_Request(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    stoken: typing___Text = ...

    def __init__(self,
        *,
        stoken : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"stoken",b"stoken"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"stoken",b"stoken"]) -> None: ...
type___CCredentials_ValidateEmailAddress_Request = CCredentials_ValidateEmailAddress_Request

class CCredentials_ValidateEmailAddress_Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    was_validated: builtin___bool = ...

    def __init__(self,
        *,
        was_validated : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"was_validated",b"was_validated"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"was_validated",b"was_validated"]) -> None: ...
type___CCredentials_ValidateEmailAddress_Response = CCredentials_ValidateEmailAddress_Response

class CCredentials_SteamGuardPhishingReport_Request(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    param_string: typing___Text = ...
    ipaddress_actual: builtin___int = ...

    def __init__(self,
        *,
        param_string : typing___Optional[typing___Text] = None,
        ipaddress_actual : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"ipaddress_actual",b"ipaddress_actual",u"param_string",b"param_string"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ipaddress_actual",b"ipaddress_actual",u"param_string",b"param_string"]) -> None: ...
type___CCredentials_SteamGuardPhishingReport_Request = CCredentials_SteamGuardPhishingReport_Request

class CCredentials_SteamGuardPhishingReport_Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ipaddress_loginattempt: builtin___int = ...
    countryname_loginattempt: typing___Text = ...
    statename_loginattempt: typing___Text = ...
    cityname_loginattempt: typing___Text = ...
    ipaddress_actual: builtin___int = ...
    countryname_actual: typing___Text = ...
    statename_actual: typing___Text = ...
    cityname_actual: typing___Text = ...
    steamguard_code: typing___Text = ...

    def __init__(self,
        *,
        ipaddress_loginattempt : typing___Optional[builtin___int] = None,
        countryname_loginattempt : typing___Optional[typing___Text] = None,
        statename_loginattempt : typing___Optional[typing___Text] = None,
        cityname_loginattempt : typing___Optional[typing___Text] = None,
        ipaddress_actual : typing___Optional[builtin___int] = None,
        countryname_actual : typing___Optional[typing___Text] = None,
        statename_actual : typing___Optional[typing___Text] = None,
        cityname_actual : typing___Optional[typing___Text] = None,
        steamguard_code : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"cityname_actual",b"cityname_actual",u"cityname_loginattempt",b"cityname_loginattempt",u"countryname_actual",b"countryname_actual",u"countryname_loginattempt",b"countryname_loginattempt",u"ipaddress_actual",b"ipaddress_actual",u"ipaddress_loginattempt",b"ipaddress_loginattempt",u"statename_actual",b"statename_actual",u"statename_loginattempt",b"statename_loginattempt",u"steamguard_code",b"steamguard_code"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cityname_actual",b"cityname_actual",u"cityname_loginattempt",b"cityname_loginattempt",u"countryname_actual",b"countryname_actual",u"countryname_loginattempt",b"countryname_loginattempt",u"ipaddress_actual",b"ipaddress_actual",u"ipaddress_loginattempt",b"ipaddress_loginattempt",u"statename_actual",b"statename_actual",u"statename_loginattempt",b"statename_loginattempt",u"steamguard_code",b"steamguard_code"]) -> None: ...
type___CCredentials_SteamGuardPhishingReport_Response = CCredentials_SteamGuardPhishingReport_Response

class CCredentials_LastCredentialChangeTime_Request(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    user_changes_only: builtin___bool = ...

    def __init__(self,
        *,
        user_changes_only : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"user_changes_only",b"user_changes_only"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"user_changes_only",b"user_changes_only"]) -> None: ...
type___CCredentials_LastCredentialChangeTime_Request = CCredentials_LastCredentialChangeTime_Request

class CCredentials_LastCredentialChangeTime_Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    timestamp_last_password_change: builtin___int = ...
    timestamp_last_email_change: builtin___int = ...
    timestamp_last_password_reset: builtin___int = ...

    def __init__(self,
        *,
        timestamp_last_password_change : typing___Optional[builtin___int] = None,
        timestamp_last_email_change : typing___Optional[builtin___int] = None,
        timestamp_last_password_reset : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"timestamp_last_email_change",b"timestamp_last_email_change",u"timestamp_last_password_change",b"timestamp_last_password_change",u"timestamp_last_password_reset",b"timestamp_last_password_reset"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"timestamp_last_email_change",b"timestamp_last_email_change",u"timestamp_last_password_change",b"timestamp_last_password_change",u"timestamp_last_password_reset",b"timestamp_last_password_reset"]) -> None: ...
type___CCredentials_LastCredentialChangeTime_Response = CCredentials_LastCredentialChangeTime_Response

class CCredentials_GetAccountAuthSecret_Request(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___CCredentials_GetAccountAuthSecret_Request = CCredentials_GetAccountAuthSecret_Request

class CCredentials_GetAccountAuthSecret_Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    secret_id: builtin___int = ...
    secret: builtin___bytes = ...

    def __init__(self,
        *,
        secret_id : typing___Optional[builtin___int] = None,
        secret : typing___Optional[builtin___bytes] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"secret",b"secret",u"secret_id",b"secret_id"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"secret",b"secret",u"secret_id",b"secret_id"]) -> None: ...
type___CCredentials_GetAccountAuthSecret_Response = CCredentials_GetAccountAuthSecret_Response

class Credentials(google___protobuf___service___Service, metaclass=abc___ABCMeta):
    @abc___abstractmethod
    def TestAvailablePassword(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___CCredentials_TestAvailablePassword_Request,
        done: typing___Optional[typing___Callable[[type___CCredentials_TestAvailablePassword_Response], None]],
    ) -> concurrent___futures___Future[type___CCredentials_TestAvailablePassword_Response]: ...
    @abc___abstractmethod
    def GetSteamGuardDetails(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___CCredentials_GetSteamGuardDetails_Request,
        done: typing___Optional[typing___Callable[[type___CCredentials_GetSteamGuardDetails_Response], None]],
    ) -> concurrent___futures___Future[type___CCredentials_GetSteamGuardDetails_Response]: ...
    @abc___abstractmethod
    def NewMachineNotificationDialogResult(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___CCredentials_NewMachineNotificationDialog_Request,
        done: typing___Optional[typing___Callable[[type___CCredentials_NewMachineNotificationDialog_Response], None]],
    ) -> concurrent___futures___Future[type___CCredentials_NewMachineNotificationDialog_Response]: ...
    @abc___abstractmethod
    def ValidateEmailAddress(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___CCredentials_ValidateEmailAddress_Request,
        done: typing___Optional[typing___Callable[[type___CCredentials_ValidateEmailAddress_Response], None]],
    ) -> concurrent___futures___Future[type___CCredentials_ValidateEmailAddress_Response]: ...
    @abc___abstractmethod
    def SteamGuardPhishingReport(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___CCredentials_SteamGuardPhishingReport_Request,
        done: typing___Optional[typing___Callable[[type___CCredentials_SteamGuardPhishingReport_Response], None]],
    ) -> concurrent___futures___Future[type___CCredentials_SteamGuardPhishingReport_Response]: ...
    @abc___abstractmethod
    def GetCredentialChangeTimeDetails(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___CCredentials_LastCredentialChangeTime_Request,
        done: typing___Optional[typing___Callable[[type___CCredentials_LastCredentialChangeTime_Response], None]],
    ) -> concurrent___futures___Future[type___CCredentials_LastCredentialChangeTime_Response]: ...
    @abc___abstractmethod
    def GetAccountAuthSecret(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___CCredentials_GetAccountAuthSecret_Request,
        done: typing___Optional[typing___Callable[[type___CCredentials_GetAccountAuthSecret_Response], None]],
    ) -> concurrent___futures___Future[type___CCredentials_GetAccountAuthSecret_Response]: ...
class Credentials_Stub(Credentials):
    def __init__(self, rpc_channel: google___protobuf___service___RpcChannel) -> None: ...
    def TestAvailablePassword(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___CCredentials_TestAvailablePassword_Request,
        done: typing___Optional[typing___Callable[[type___CCredentials_TestAvailablePassword_Response], None]],
    ) -> concurrent___futures___Future[type___CCredentials_TestAvailablePassword_Response]: ...
    def GetSteamGuardDetails(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___CCredentials_GetSteamGuardDetails_Request,
        done: typing___Optional[typing___Callable[[type___CCredentials_GetSteamGuardDetails_Response], None]],
    ) -> concurrent___futures___Future[type___CCredentials_GetSteamGuardDetails_Response]: ...
    def NewMachineNotificationDialogResult(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___CCredentials_NewMachineNotificationDialog_Request,
        done: typing___Optional[typing___Callable[[type___CCredentials_NewMachineNotificationDialog_Response], None]],
    ) -> concurrent___futures___Future[type___CCredentials_NewMachineNotificationDialog_Response]: ...
    def ValidateEmailAddress(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___CCredentials_ValidateEmailAddress_Request,
        done: typing___Optional[typing___Callable[[type___CCredentials_ValidateEmailAddress_Response], None]],
    ) -> concurrent___futures___Future[type___CCredentials_ValidateEmailAddress_Response]: ...
    def SteamGuardPhishingReport(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___CCredentials_SteamGuardPhishingReport_Request,
        done: typing___Optional[typing___Callable[[type___CCredentials_SteamGuardPhishingReport_Response], None]],
    ) -> concurrent___futures___Future[type___CCredentials_SteamGuardPhishingReport_Response]: ...
    def GetCredentialChangeTimeDetails(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___CCredentials_LastCredentialChangeTime_Request,
        done: typing___Optional[typing___Callable[[type___CCredentials_LastCredentialChangeTime_Response], None]],
    ) -> concurrent___futures___Future[type___CCredentials_LastCredentialChangeTime_Response]: ...
    def GetAccountAuthSecret(self,
        rpc_controller: google___protobuf___service___RpcController,
        request: type___CCredentials_GetAccountAuthSecret_Request,
        done: typing___Optional[typing___Callable[[type___CCredentials_GetAccountAuthSecret_Response], None]],
    ) -> concurrent___futures___Future[type___CCredentials_GetAccountAuthSecret_Response]: ...