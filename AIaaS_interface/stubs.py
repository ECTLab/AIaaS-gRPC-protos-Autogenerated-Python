import grpc

from AIaaS_interface.platform_management.notification_server.email_pb2_grpc import NotificationEmailStub
from AIaaS_interface.ai_services.recom_server.recom_pb2_grpc import RecomaaSStub
from AIaaS_interface.platform_management.wallet_server_pb2_grpc import WalletStub
from AIaaS_interface.platform_management.management_server_pb2_grpc import ManagementStub
from AIaaS_interface.data_storage.storage_pb2_grpc import DataStorageStub



class Services:
	NOTIFICATION_EMAIL = {
		"host": "notification_email_grpc_server",
		"port": 50051,
		"stub_class": NotificationEmailStub,
	}
	RECOMAA_S = {
		"host": "recomaas_grpc_server",
		"port": 50052,
		"stub_class": RecomaaSStub,
	}
	WALLET = {
		"host": "wallet_grpc_server",
		"port": 50053,
		"stub_class": WalletStub,
	}
	MANAGEMENT = {
		"host": "platform_management_grpc_server",
		"port": 50054,
		"stub_class": ManagementStub,
	}
	DATA_STORAGE = {
		"host": "data_storage_grpc_server",
		"port": 50055,
		"stub_class": DataStorageStub,
	}



def get_stub(config: dict):
    channel = grpc.insecure_channel(config['host'] + ':' + str(config['port']))
    return config['stub_class'](channel)
