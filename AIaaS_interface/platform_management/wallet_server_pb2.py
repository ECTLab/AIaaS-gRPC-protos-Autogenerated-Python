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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'platform_management/wallet_server.proto\x12\rwallet_server\")\n\x16\x43reateNewWalletRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"\x19\n\x17\x43reateNewWalletResponse\"7\n\x14OnlinePaymentRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\"3\n\x15OnlinePaymentResponse\x12\x1a\n\x12online_payment_url\x18\x01 \x01(\t\".\n\x1aVerifyOnlinePaymentRequest\x12\x10\n\x08track_id\x18\x01 \x01(\t\"5\n\x1bVerifyOnlinePaymentResponse\x12\x16\n\x0ewas_successful\x18\x01 \x01(\x08\x32\xb4\x02\n\x06Wallet\x12`\n\x0f\x43reateNewWallet\x12%.wallet_server.CreateNewWalletRequest\x1a&.wallet_server.CreateNewWalletResponse\x12Z\n\rOnlinePayment\x12#.wallet_server.OnlinePaymentRequest\x1a$.wallet_server.OnlinePaymentResponse\x12l\n\x13VerifyOnlinePayment\x12).wallet_server.VerifyOnlinePaymentRequest\x1a*.wallet_server.VerifyOnlinePaymentResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'platform_management.wallet_server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATENEWWALLETREQUEST._serialized_start=58
  _CREATENEWWALLETREQUEST._serialized_end=99
  _CREATENEWWALLETRESPONSE._serialized_start=101
  _CREATENEWWALLETRESPONSE._serialized_end=126
  _ONLINEPAYMENTREQUEST._serialized_start=128
  _ONLINEPAYMENTREQUEST._serialized_end=183
  _ONLINEPAYMENTRESPONSE._serialized_start=185
  _ONLINEPAYMENTRESPONSE._serialized_end=236
  _VERIFYONLINEPAYMENTREQUEST._serialized_start=238
  _VERIFYONLINEPAYMENTREQUEST._serialized_end=284
  _VERIFYONLINEPAYMENTRESPONSE._serialized_start=286
  _VERIFYONLINEPAYMENTRESPONSE._serialized_end=339
  _WALLET._serialized_start=342
  _WALLET._serialized_end=650
# @@protoc_insertion_point(module_scope)
