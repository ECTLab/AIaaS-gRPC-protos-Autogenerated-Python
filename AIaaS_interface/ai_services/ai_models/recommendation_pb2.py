# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ai_services/ai_models/recommendation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*ai_services/ai_models/recommendation.proto\x12\x0erecommendation\x1a\x1cgoogle/protobuf/struct.proto\"6\n\x0fModelProperties\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x12\n\nmodel_name\x18\x02 \x01(\t\"U\n\x12\x43reateModelRequest\x12.\n\x05model\x18\x01 \x01(\x0b\x32\x1f.recommendation.ModelProperties\x12\x0f\n\x07verbose\x18\x02 \x01(\x08\"\x15\n\x13\x43reateModelResponse\"\xb5\x02\n\x0e\x64\x61taProperties\x12\x16\n\x0euser_info_path\x18\x01 \x01(\t\x12\x19\n\x11user_ratings_path\x18\x02 \x01(\t\x12\x16\n\x0eitem_info_path\x18\x03 \x01(\t\x12\x19\n\x11user_info_columns\x18\x04 \x03(\t\x12\x1c\n\x14user_ratings_columns\x18\x05 \x03(\t\x12\x19\n\x11item_info_columns\x18\x06 \x03(\t\x12\x1a\n\ruser_info_sep\x18\x07 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10user_ratings_sep\x18\x08 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08item_sep\x18\t \x01(\tH\x02\x88\x01\x01\x42\x10\n\x0e_user_info_sepB\x13\n\x11_user_ratings_sepB\x0b\n\t_item_sep\"\x86\x01\n\x15StartColdStartRequest\x12.\n\x05model\x18\x01 \x01(\x0b\x32\x1f.recommendation.ModelProperties\x12,\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1e.recommendation.dataProperties\x12\x0f\n\x07verbose\x18\x03 \x01(\x08\"\x18\n\x16StartColdStartResponse\"\xf5\x02\n\x18StartSimilarItemsRequest\x12.\n\x05model\x18\x01 \x01(\x0b\x32\x1f.recommendation.ModelProperties\x12,\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1e.recommendation.dataProperties\x12\x0f\n\x07verbose\x18\x03 \x01(\x08\x12\x11\n\x04\x61lgo\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x0e\n\x01k\x18\x05 \x01(\x05H\x01\x88\x01\x01\x12\x12\n\x05min_k\x18\x06 \x01(\x05H\x02\x88\x01\x01\x12\x31\n\x0bsim_options\x18\x07 \x01(\x0b\x32\x17.google.protobuf.StructH\x03\x88\x01\x01\x12\x31\n\x0b\x62sl_options\x18\x08 \x01(\x0b\x32\x17.google.protobuf.StructH\x04\x88\x01\x01\x12\x0e\n\x01n\x18\t \x01(\x05H\x05\x88\x01\x01\x42\x07\n\x05_algoB\x04\n\x02_kB\x08\n\x06_min_kB\x0e\n\x0c_sim_optionsB\x0e\n\x0c_bsl_optionsB\x04\n\x02_n\"\x1b\n\x19StartSimilarItemsResponse\"\xb4\x01\n\x18StartUserSpecificRequest\x12.\n\x05model\x18\x01 \x01(\x0b\x32\x1f.recommendation.ModelProperties\x12,\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1e.recommendation.dataProperties\x12\x0f\n\x07verbose\x18\x03 \x01(\x08\x12\t\n\x01k\x18\x04 \x01(\x05\x12\x0f\n\x07k_start\x18\x05 \x01(\x05\x12\r\n\x05k_end\x18\x06 \x01(\x05\"\x1b\n\x19StartUserSpecificResponse\"^\n\x10\x43oldStartRequest\x12.\n\x05model\x18\x01 \x01(\x0b\x32\x1f.recommendation.ModelProperties\x12\x0f\n\x07verbose\x18\x02 \x01(\x08\x12\t\n\x01n\x18\x03 \x01(\x05\"Q\n\rColdStartItem\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x13\n\x0bmovie_title\x18\x02 \x01(\t\x12\x11\n\x04rate\x18\x03 \x01(\x05H\x00\x88\x01\x01\x42\x07\n\x05_rate\"A\n\x11\x43oldStartResponse\x12,\n\x05items\x18\x01 \x03(\x0b\x32\x1d.recommendation.ColdStartItem\"t\n\x13SimilarItemsRequest\x12.\n\x05model\x18\x01 \x01(\x0b\x32\x1f.recommendation.ModelProperties\x12\x0f\n\x07verbose\x18\x02 \x01(\x08\x12\t\n\x01n\x18\x03 \x01(\x05\x12\x11\n\titem_name\x18\x04 \x01(\t\"8\n\x10SimilarItemsItem\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x13\n\x0bmovie_title\x18\x02 \x01(\t\"G\n\x14SimilarItemsResponse\x12/\n\x05items\x18\x01 \x03(\x0b\x32 .recommendation.SimilarItemsItem\"y\n\x13UserSpecificRequest\x12.\n\x05model\x18\x01 \x01(\x0b\x32\x1f.recommendation.ModelProperties\x12\x0f\n\x07verbose\x18\x02 \x01(\x08\x12\x16\n\x0e\x64\x61taset_userid\x18\x03 \x01(\x05\x12\t\n\x01n\x18\x04 \x01(\x05\"F\n\x10UserSpecificItem\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x13\n\x0bmovie_title\x18\x02 \x01(\t\x12\x0c\n\x04rate\x18\x03 \x01(\x05\"G\n\x14UserSpecificResponse\x12/\n\x05items\x18\x01 \x03(\x0b\x32 .recommendation.UserSpecificItem2\xa5\x05\n\x0eRecommendation\x12V\n\x0b\x43reateModel\x12\".recommendation.CreateModelRequest\x1a#.recommendation.CreateModelResponse\x12_\n\x0eStartColdStart\x12%.recommendation.StartColdStartRequest\x1a&.recommendation.StartColdStartResponse\x12h\n\x11StartSimilarItems\x12(.recommendation.StartSimilarItemsRequest\x1a).recommendation.StartSimilarItemsResponse\x12h\n\x11StartUserSpecific\x12(.recommendation.StartUserSpecificRequest\x1a).recommendation.StartUserSpecificResponse\x12P\n\tColdStart\x12 .recommendation.ColdStartRequest\x1a!.recommendation.ColdStartResponse\x12Y\n\x0cSimilarItems\x12#.recommendation.SimilarItemsRequest\x1a$.recommendation.SimilarItemsResponse\x12Y\n\x0cUserSpecific\x12#.recommendation.UserSpecificRequest\x1a$.recommendation.UserSpecificResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ai_services.ai_models.recommendation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MODELPROPERTIES._serialized_start=92
  _MODELPROPERTIES._serialized_end=146
  _CREATEMODELREQUEST._serialized_start=148
  _CREATEMODELREQUEST._serialized_end=233
  _CREATEMODELRESPONSE._serialized_start=235
  _CREATEMODELRESPONSE._serialized_end=256
  _DATAPROPERTIES._serialized_start=259
  _DATAPROPERTIES._serialized_end=568
  _STARTCOLDSTARTREQUEST._serialized_start=571
  _STARTCOLDSTARTREQUEST._serialized_end=705
  _STARTCOLDSTARTRESPONSE._serialized_start=707
  _STARTCOLDSTARTRESPONSE._serialized_end=731
  _STARTSIMILARITEMSREQUEST._serialized_start=734
  _STARTSIMILARITEMSREQUEST._serialized_end=1107
  _STARTSIMILARITEMSRESPONSE._serialized_start=1109
  _STARTSIMILARITEMSRESPONSE._serialized_end=1136
  _STARTUSERSPECIFICREQUEST._serialized_start=1139
  _STARTUSERSPECIFICREQUEST._serialized_end=1319
  _STARTUSERSPECIFICRESPONSE._serialized_start=1321
  _STARTUSERSPECIFICRESPONSE._serialized_end=1348
  _COLDSTARTREQUEST._serialized_start=1350
  _COLDSTARTREQUEST._serialized_end=1444
  _COLDSTARTITEM._serialized_start=1446
  _COLDSTARTITEM._serialized_end=1527
  _COLDSTARTRESPONSE._serialized_start=1529
  _COLDSTARTRESPONSE._serialized_end=1594
  _SIMILARITEMSREQUEST._serialized_start=1596
  _SIMILARITEMSREQUEST._serialized_end=1712
  _SIMILARITEMSITEM._serialized_start=1714
  _SIMILARITEMSITEM._serialized_end=1770
  _SIMILARITEMSRESPONSE._serialized_start=1772
  _SIMILARITEMSRESPONSE._serialized_end=1843
  _USERSPECIFICREQUEST._serialized_start=1845
  _USERSPECIFICREQUEST._serialized_end=1966
  _USERSPECIFICITEM._serialized_start=1968
  _USERSPECIFICITEM._serialized_end=2038
  _USERSPECIFICRESPONSE._serialized_start=2040
  _USERSPECIFICRESPONSE._serialized_end=2111
  _RECOMMENDATION._serialized_start=2114
  _RECOMMENDATION._serialized_end=2791
# @@protoc_insertion_point(module_scope)
