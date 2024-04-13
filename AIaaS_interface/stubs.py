import grpc

from AIaaS_interface.platform_management.notification_server.email_pb2_grpc import NotificationEmailStub
from AIaaS_interface.ai_services.ai_models.recommendation_pb2_grpc import RecommendationStub
from AIaaS_interface.platform_management.wallet_server_pb2_grpc import WalletStub
from AIaaS_interface.platform_management.management_server_pb2_grpc import ManagementStub
from AIaaS_interface.storage_management_pb2_grpc import StorageManagementStub



class Services:
	NOTIFICATION_EMAIL = {
		"host": "notification-email-grpc-server",
		"port": 50051,
		"stub_class": NotificationEmailStub,
	}
	RECOMMENDATION = {
		"host": "recommendation-grpc-server",
		"port": 50052,
		"stub_class": RecommendationStub,
	}
	WALLET = {
		"host": "wallet-grpc-server",
		"port": 50053,
		"stub_class": WalletStub,
	}
	MANAGEMENT = {
		"host": "platform-management-grpc-server",
		"port": 50054,
		"stub_class": ManagementStub,
	}
	STORAGE_MANAGEMENT = {
		"host": "storage-management-grpc-server",
		"port": 50055,
		"stub_class": StorageManagementStub,
	}



from os import environ
USE_LOCALHOST = environ.get('AIAAS_GRPC_USE_LOCALHOST', 'False').lower() == 'true'

def get_stub(config: dict):
    host = '127.0.0.1' if USE_LOCALHOST else config['host']
    channel = grpc.insecure_channel(host + ':' + str(config['port']))
    return config['stub_class'](channel)
