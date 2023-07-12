# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ai_services/recom_server/recom.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$ai_services/recom_server/recom.proto\x12\x0crecom_server\x1a\x1cgoogle/protobuf/struct.proto\"6\n\x0fModelProperties\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x12\n\nmodel_name\x18\x02 \x01(\t\"S\n\x12\x43reateModelRequest\x12,\n\x05model\x18\x01 \x01(\x0b\x32\x1d.recom_server.ModelProperties\x12\x0f\n\x07verbose\x18\x02 \x01(\x08\"\x15\n\x13\x43reateModelResponse\"\xb5\x02\n\x0e\x64\x61taProperties\x12\x16\n\x0euser_info_path\x18\x01 \x01(\t\x12\x19\n\x11user_ratings_path\x18\x02 \x01(\t\x12\x16\n\x0eitem_info_path\x18\x03 \x01(\t\x12\x19\n\x11user_info_columns\x18\x04 \x03(\t\x12\x1c\n\x14user_ratings_columns\x18\x05 \x03(\t\x12\x19\n\x11item_info_columns\x18\x06 \x03(\t\x12\x1a\n\ruser_info_sep\x18\x07 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10user_ratings_sep\x18\x08 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08item_sep\x18\t \x01(\tH\x02\x88\x01\x01\x42\x10\n\x0e_user_info_sepB\x13\n\x11_user_ratings_sepB\x0b\n\t_item_sep\"\x82\x01\n\x15StartColdStartRequest\x12,\n\x05model\x18\x01 \x01(\x0b\x32\x1d.recom_server.ModelProperties\x12*\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1c.recom_server.dataProperties\x12\x0f\n\x07verbose\x18\x03 \x01(\x08\"\x18\n\x16StartColdStartResponse\"\xf1\x02\n\x18StartSimilarItemsRequest\x12,\n\x05model\x18\x01 \x01(\x0b\x32\x1d.recom_server.ModelProperties\x12*\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1c.recom_server.dataProperties\x12\x0f\n\x07verbose\x18\x03 \x01(\x08\x12\x11\n\x04\x61lgo\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x0e\n\x01k\x18\x05 \x01(\x05H\x01\x88\x01\x01\x12\x12\n\x05min_k\x18\x06 \x01(\x05H\x02\x88\x01\x01\x12\x31\n\x0bsim_options\x18\x07 \x01(\x0b\x32\x17.google.protobuf.StructH\x03\x88\x01\x01\x12\x31\n\x0b\x62sl_options\x18\x08 \x01(\x0b\x32\x17.google.protobuf.StructH\x04\x88\x01\x01\x12\x0e\n\x01n\x18\t \x01(\x05H\x05\x88\x01\x01\x42\x07\n\x05_algoB\x04\n\x02_kB\x08\n\x06_min_kB\x0e\n\x0c_sim_optionsB\x0e\n\x0c_bsl_optionsB\x04\n\x02_n\"\x1b\n\x19StartSimilarItemsResponse\"\xb0\x01\n\x18StartUserSpecificRequest\x12,\n\x05model\x18\x01 \x01(\x0b\x32\x1d.recom_server.ModelProperties\x12*\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1c.recom_server.dataProperties\x12\x0f\n\x07verbose\x18\x03 \x01(\x08\x12\t\n\x01k\x18\x04 \x01(\x05\x12\x0f\n\x07k_start\x18\x05 \x01(\x05\x12\r\n\x05k_end\x18\x06 \x01(\x05\"\x1b\n\x19StartUserSpecificResponse\"\\\n\x10\x43oldStartRequest\x12,\n\x05model\x18\x01 \x01(\x0b\x32\x1d.recom_server.ModelProperties\x12\x0f\n\x07verbose\x18\x02 \x01(\x08\x12\t\n\x01n\x18\x03 \x01(\x05\"Q\n\rColdStartItem\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x13\n\x0bmovie_title\x18\x02 \x01(\t\x12\x11\n\x04rate\x18\x03 \x01(\x05H\x00\x88\x01\x01\x42\x07\n\x05_rate\"?\n\x11\x43oldStartResponse\x12*\n\x05items\x18\x01 \x03(\x0b\x32\x1b.recom_server.ColdStartItem\"r\n\x13SimilarItemsRequest\x12,\n\x05model\x18\x01 \x01(\x0b\x32\x1d.recom_server.ModelProperties\x12\x0f\n\x07verbose\x18\x02 \x01(\x08\x12\t\n\x01n\x18\x03 \x01(\x05\x12\x11\n\titem_name\x18\x04 \x01(\t\"8\n\x10SimilarItemsItem\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x13\n\x0bmovie_title\x18\x02 \x01(\t\"E\n\x14SimilarItemsResponse\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.recom_server.SimilarItemsItem\"w\n\x13UserSpecificRequest\x12,\n\x05model\x18\x01 \x01(\x0b\x32\x1d.recom_server.ModelProperties\x12\x0f\n\x07verbose\x18\x02 \x01(\x08\x12\x16\n\x0e\x64\x61taset_userid\x18\x03 \x01(\x05\x12\t\n\x01n\x18\x04 \x01(\x05\"F\n\x10UserSpecificItem\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x13\n\x0bmovie_title\x18\x02 \x01(\t\x12\x0c\n\x04rate\x18\x03 \x01(\x05\"E\n\x14UserSpecificResponse\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.recom_server.UserSpecificItem2\x83\x05\n\x08RecomaaS\x12R\n\x0b\x43reateModel\x12 .recom_server.CreateModelRequest\x1a!.recom_server.CreateModelResponse\x12[\n\x0eStartColdStart\x12#.recom_server.StartColdStartRequest\x1a$.recom_server.StartColdStartResponse\x12\x64\n\x11StartSimilarItems\x12&.recom_server.StartSimilarItemsRequest\x1a\'.recom_server.StartSimilarItemsResponse\x12\x64\n\x11StartUserSpecific\x12&.recom_server.StartUserSpecificRequest\x1a\'.recom_server.StartUserSpecificResponse\x12L\n\tColdStart\x12\x1e.recom_server.ColdStartRequest\x1a\x1f.recom_server.ColdStartResponse\x12U\n\x0cSimilarItems\x12!.recom_server.SimilarItemsRequest\x1a\".recom_server.SimilarItemsResponse\x12U\n\x0cUserSpecific\x12!.recom_server.UserSpecificRequest\x1a\".recom_server.UserSpecificResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ai_services.recom_server.recom_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MODELPROPERTIES._serialized_start=84
  _MODELPROPERTIES._serialized_end=138
  _CREATEMODELREQUEST._serialized_start=140
  _CREATEMODELREQUEST._serialized_end=223
  _CREATEMODELRESPONSE._serialized_start=225
  _CREATEMODELRESPONSE._serialized_end=246
  _DATAPROPERTIES._serialized_start=249
  _DATAPROPERTIES._serialized_end=558
  _STARTCOLDSTARTREQUEST._serialized_start=561
  _STARTCOLDSTARTREQUEST._serialized_end=691
  _STARTCOLDSTARTRESPONSE._serialized_start=693
  _STARTCOLDSTARTRESPONSE._serialized_end=717
  _STARTSIMILARITEMSREQUEST._serialized_start=720
  _STARTSIMILARITEMSREQUEST._serialized_end=1089
  _STARTSIMILARITEMSRESPONSE._serialized_start=1091
  _STARTSIMILARITEMSRESPONSE._serialized_end=1118
  _STARTUSERSPECIFICREQUEST._serialized_start=1121
  _STARTUSERSPECIFICREQUEST._serialized_end=1297
  _STARTUSERSPECIFICRESPONSE._serialized_start=1299
  _STARTUSERSPECIFICRESPONSE._serialized_end=1326
  _COLDSTARTREQUEST._serialized_start=1328
  _COLDSTARTREQUEST._serialized_end=1420
  _COLDSTARTITEM._serialized_start=1422
  _COLDSTARTITEM._serialized_end=1503
  _COLDSTARTRESPONSE._serialized_start=1505
  _COLDSTARTRESPONSE._serialized_end=1568
  _SIMILARITEMSREQUEST._serialized_start=1570
  _SIMILARITEMSREQUEST._serialized_end=1684
  _SIMILARITEMSITEM._serialized_start=1686
  _SIMILARITEMSITEM._serialized_end=1742
  _SIMILARITEMSRESPONSE._serialized_start=1744
  _SIMILARITEMSRESPONSE._serialized_end=1813
  _USERSPECIFICREQUEST._serialized_start=1815
  _USERSPECIFICREQUEST._serialized_end=1934
  _USERSPECIFICITEM._serialized_start=1936
  _USERSPECIFICITEM._serialized_end=2006
  _USERSPECIFICRESPONSE._serialized_start=2008
  _USERSPECIFICRESPONSE._serialized_end=2077
  _RECOMAAS._serialized_start=2080
  _RECOMAAS._serialized_end=2723
# @@protoc_insertion_point(module_scope)
