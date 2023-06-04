import grpc

from AIaaS_interface.platform_management.notification_server.email_pb2_grpc import NotificationEmailStub



class Services:
	NOTIFICATION_EMAIL = {
		"host": "0.0.0.0",
		"port": 50051,
		"stub_class": NotificationEmailStub,
	}



def get_stub(config: dict):
    channel = grpc.insecure_channel(config['host'] + ':' + str(config['port']))
    return config['stub_class'](channel)
