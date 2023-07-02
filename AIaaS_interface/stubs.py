import grpc

from AIaaS_interface.platform_management.notification_server.email_pb2_grpc import NotificationEmailStub
from AIaaS_interface.ai_services.recom_server.recom_pb2_grpc import RecomaaSStub
from AIaaS_interface.platform_management.wallet_server_pb2_grpc import WalletStub



class Services:
	NOTIFICATION_EMAIL = {
		"host": "0.0.0.0",
		"port": 50051,
		"stub_class": NotificationEmailStub,
	}
	RECOMAA_S = {
		"host": "0.0.0.0",
		"port": 50052,
		"stub_class": RecomaaSStub,
	}
	WALLET = {
		"host": "0.0.0.0",
		"port": 50053,
		"stub_class": WalletStub,
	}



def get_stub(config: dict):
    channel = grpc.insecure_channel(config['host'] + ':' + str(config['port']))
    return config['stub_class'](channel)
