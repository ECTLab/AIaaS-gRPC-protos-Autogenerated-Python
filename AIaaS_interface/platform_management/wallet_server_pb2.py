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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'platform_management/wallet_server.proto\x12\x13notification_server\")\n\x16\x43reateNewWalletRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"\x19\n\x17\x43reateNewWalletResponse2v\n\x06Wallet\x12l\n\x0f\x43reateNewWallet\x12+.notification_server.CreateNewWalletRequest\x1a,.notification_server.CreateNewWalletResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'platform_management.wallet_server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATENEWWALLETREQUEST._serialized_start=64
  _CREATENEWWALLETREQUEST._serialized_end=105
  _CREATENEWWALLETRESPONSE._serialized_start=107
  _CREATENEWWALLETRESPONSE._serialized_end=132
  _WALLET._serialized_start=134
  _WALLET._serialized_end=252
# @@protoc_insertion_point(module_scope)
