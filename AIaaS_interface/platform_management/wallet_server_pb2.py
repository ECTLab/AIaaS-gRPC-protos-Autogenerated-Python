# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: platform_management/wallet_server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'platform_management/wallet_server.proto\x12\rwallet_server\x1a\x1fgoogle/protobuf/timestamp.proto\")\n\x16\x43reateNewWalletRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\r\"\x19\n\x17\x43reateNewWalletResponse\"\'\n\x14HasUserWalletRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\r\"+\n\x15HasUserWalletResponse\x12\x12\n\nhas_wallet\x18\x01 \x01(\x08\"7\n\x14OnlinePaymentRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x04\"3\n\x15OnlinePaymentResponse\x12\x1a\n\x12online_payment_url\x18\x01 \x01(\t\".\n\x1aVerifyOnlinePaymentRequest\x12\x10\n\x08track_id\x18\x01 \x01(\x04\"5\n\x1bVerifyOnlinePaymentResponse\x12\x16\n\x0ewas_successful\x18\x01 \x01(\x08\"*\n\x17GetWalletBalanceRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\r\"+\n\x18GetWalletBalanceResponse\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x04\"\xc4\x01\n\x0bTransaction\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x04\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x04kind\x18\x03 \x01(\x0e\x32\x1e.wallet_server.TransactionKind\x12\x30\n\x06status\x18\x04 \x01(\x0e\x32 .wallet_server.TransactionStatus\x12\x15\n\rai_model_name\x18\x05 \x01(\t\"0\n\x1dGetTransactionsHistoryRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\r\"R\n\x1eGetTransactionsHistoryResponse\x12\x30\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x1a.wallet_server.Transaction\"J\n\x1bSetAIModelCostPerReqRequest\x12\x15\n\rai_model_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63ost_per_req\x18\x02 \x01(\r\"\x1e\n\x1cSetAIModelCostPerReqResponse\"6\n\x1cGetAIModelsCostPerReqRequest\x12\x16\n\x0e\x61i_model_names\x18\x01 \x03(\t\"\x95\x01\n\x1dGetAIModelsCostPerReqResponse\x12\x46\n\x05\x63osts\x18\x01 \x03(\x0b\x32\x37.wallet_server.GetAIModelsCostPerReqResponse.CostsEntry\x1a,\n\nCostsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"j\n\x1b\x42uyAIModelReqPackageRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\r\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x15\n\rai_model_name\x18\x03 \x01(\t\x12\x11\n\treq_count\x18\x04 \x01(\x04\"\x1e\n\x1c\x42uyAIModelReqPackageResponse*c\n\x0fTransactionKind\x12\x10\n\x0cUNKNOWN_KIND\x10\x00\x12\x0b\n\x07\x44\x45POSIT\x10\x01\x12\x0c\n\x08WITHDRAW\x10\x02\x12\x11\n\rAI_MODEL_COST\x10\x03\x12\x10\n\x0cSTORAGE_COST\x10\x04*P\n\x11TransactionStatus\x12\x12\n\x0eUNKNOWN_STATUS\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0e\n\nSUCCESSFUL\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x32\xc2\x07\n\x06Wallet\x12`\n\x0f\x43reateNewWallet\x12%.wallet_server.CreateNewWalletRequest\x1a&.wallet_server.CreateNewWalletResponse\x12Z\n\rHasUserWallet\x12#.wallet_server.HasUserWalletRequest\x1a$.wallet_server.HasUserWalletResponse\x12Z\n\rOnlinePayment\x12#.wallet_server.OnlinePaymentRequest\x1a$.wallet_server.OnlinePaymentResponse\x12l\n\x13VerifyOnlinePayment\x12).wallet_server.VerifyOnlinePaymentRequest\x1a*.wallet_server.VerifyOnlinePaymentResponse\x12\x63\n\x10GetWalletBalance\x12&.wallet_server.GetWalletBalanceRequest\x1a\'.wallet_server.GetWalletBalanceResponse\x12u\n\x16GetTransactionsHistory\x12,.wallet_server.GetTransactionsHistoryRequest\x1a-.wallet_server.GetTransactionsHistoryResponse\x12o\n\x14SetAIModelCostPerReq\x12*.wallet_server.SetAIModelCostPerReqRequest\x1a+.wallet_server.SetAIModelCostPerReqResponse\x12r\n\x15GetAIModelsCostPerReq\x12+.wallet_server.GetAIModelsCostPerReqRequest\x1a,.wallet_server.GetAIModelsCostPerReqResponse\x12o\n\x14\x42uyAIModelReqPackage\x12*.wallet_server.BuyAIModelReqPackageRequest\x1a+.wallet_server.BuyAIModelReqPackageResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'platform_management.wallet_server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETAIMODELSCOSTPERREQRESPONSE_COSTSENTRY._options = None
  _GETAIMODELSCOSTPERREQRESPONSE_COSTSENTRY._serialized_options = b'8\001'
  _TRANSACTIONKIND._serialized_start=1338
  _TRANSACTIONKIND._serialized_end=1437
  _TRANSACTIONSTATUS._serialized_start=1439
  _TRANSACTIONSTATUS._serialized_end=1519
  _CREATENEWWALLETREQUEST._serialized_start=91
  _CREATENEWWALLETREQUEST._serialized_end=132
  _CREATENEWWALLETRESPONSE._serialized_start=134
  _CREATENEWWALLETRESPONSE._serialized_end=159
  _HASUSERWALLETREQUEST._serialized_start=161
  _HASUSERWALLETREQUEST._serialized_end=200
  _HASUSERWALLETRESPONSE._serialized_start=202
  _HASUSERWALLETRESPONSE._serialized_end=245
  _ONLINEPAYMENTREQUEST._serialized_start=247
  _ONLINEPAYMENTREQUEST._serialized_end=302
  _ONLINEPAYMENTRESPONSE._serialized_start=304
  _ONLINEPAYMENTRESPONSE._serialized_end=355
  _VERIFYONLINEPAYMENTREQUEST._serialized_start=357
  _VERIFYONLINEPAYMENTREQUEST._serialized_end=403
  _VERIFYONLINEPAYMENTRESPONSE._serialized_start=405
  _VERIFYONLINEPAYMENTRESPONSE._serialized_end=458
  _GETWALLETBALANCEREQUEST._serialized_start=460
  _GETWALLETBALANCEREQUEST._serialized_end=502
  _GETWALLETBALANCERESPONSE._serialized_start=504
  _GETWALLETBALANCERESPONSE._serialized_end=547
  _TRANSACTION._serialized_start=550
  _TRANSACTION._serialized_end=746
  _GETTRANSACTIONSHISTORYREQUEST._serialized_start=748
  _GETTRANSACTIONSHISTORYREQUEST._serialized_end=796
  _GETTRANSACTIONSHISTORYRESPONSE._serialized_start=798
  _GETTRANSACTIONSHISTORYRESPONSE._serialized_end=880
  _SETAIMODELCOSTPERREQREQUEST._serialized_start=882
  _SETAIMODELCOSTPERREQREQUEST._serialized_end=956
  _SETAIMODELCOSTPERREQRESPONSE._serialized_start=958
  _SETAIMODELCOSTPERREQRESPONSE._serialized_end=988
  _GETAIMODELSCOSTPERREQREQUEST._serialized_start=990
  _GETAIMODELSCOSTPERREQREQUEST._serialized_end=1044
  _GETAIMODELSCOSTPERREQRESPONSE._serialized_start=1047
  _GETAIMODELSCOSTPERREQRESPONSE._serialized_end=1196
  _GETAIMODELSCOSTPERREQRESPONSE_COSTSENTRY._serialized_start=1152
  _GETAIMODELSCOSTPERREQRESPONSE_COSTSENTRY._serialized_end=1196
  _BUYAIMODELREQPACKAGEREQUEST._serialized_start=1198
  _BUYAIMODELREQPACKAGEREQUEST._serialized_end=1304
  _BUYAIMODELREQPACKAGERESPONSE._serialized_start=1306
  _BUYAIMODELREQPACKAGERESPONSE._serialized_end=1336
  _WALLET._serialized_start=1522
  _WALLET._serialized_end=2484
# @@protoc_insertion_point(module_scope)
