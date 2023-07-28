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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'platform_management/wallet_server.proto\x12\rwallet_server\x1a\x1fgoogle/protobuf/timestamp.proto\")\n\x16\x43reateNewWalletRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"\x19\n\x17\x43reateNewWalletResponse\"\'\n\x14HasUserWalletRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"+\n\x15HasUserWalletResponse\x12\x12\n\nhas_wallet\x18\x01 \x01(\x08\"7\n\x14OnlinePaymentRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\"3\n\x15OnlinePaymentResponse\x12\x1a\n\x12online_payment_url\x18\x01 \x01(\t\".\n\x1aVerifyOnlinePaymentRequest\x12\x10\n\x08track_id\x18\x01 \x01(\x03\"5\n\x1bVerifyOnlinePaymentResponse\x12\x16\n\x0ewas_successful\x18\x01 \x01(\x08\"*\n\x17GetWalletBalanceRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"+\n\x18GetWalletBalanceResponse\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x03\"\xc4\x01\n\x0bTransaction\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x03\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x04kind\x18\x03 \x01(\x0e\x32\x1e.wallet_server.TransactionKind\x12\x30\n\x06status\x18\x04 \x01(\x0e\x32 .wallet_server.TransactionStatus\x12\x15\n\rai_model_name\x18\x05 \x01(\t\"0\n\x1dGetTransactionsHistoryRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"R\n\x1eGetTransactionsHistoryResponse\x12\x30\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x1a.wallet_server.Transaction*c\n\x0fTransactionKind\x12\x10\n\x0cUNKNOWN_KIND\x10\x00\x12\x0b\n\x07\x44\x45POSIT\x10\x01\x12\x0c\n\x08WITHDRAW\x10\x02\x12\x11\n\rAI_MODEL_COST\x10\x03\x12\x10\n\x0cSTORAGE_COST\x10\x04*P\n\x11TransactionStatus\x12\x12\n\x0eUNKNOWN_STATUS\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0e\n\nSUCCESSFUL\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x32\xec\x04\n\x06Wallet\x12`\n\x0f\x43reateNewWallet\x12%.wallet_server.CreateNewWalletRequest\x1a&.wallet_server.CreateNewWalletResponse\x12Z\n\rHasUserWallet\x12#.wallet_server.HasUserWalletRequest\x1a$.wallet_server.HasUserWalletResponse\x12Z\n\rOnlinePayment\x12#.wallet_server.OnlinePaymentRequest\x1a$.wallet_server.OnlinePaymentResponse\x12l\n\x13VerifyOnlinePayment\x12).wallet_server.VerifyOnlinePaymentRequest\x1a*.wallet_server.VerifyOnlinePaymentResponse\x12\x63\n\x10GetWalletBalance\x12&.wallet_server.GetWalletBalanceRequest\x1a\'.wallet_server.GetWalletBalanceResponse\x12u\n\x16GetTransactionsHistory\x12,.wallet_server.GetTransactionsHistoryRequest\x1a-.wallet_server.GetTransactionsHistoryResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'platform_management.wallet_server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TRANSACTIONKIND._serialized_start=882
  _TRANSACTIONKIND._serialized_end=981
  _TRANSACTIONSTATUS._serialized_start=983
  _TRANSACTIONSTATUS._serialized_end=1063
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
  _WALLET._serialized_start=1066
  _WALLET._serialized_end=1686
# @@protoc_insertion_point(module_scope)
