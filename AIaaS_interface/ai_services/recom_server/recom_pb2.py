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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$ai_services/recom_server/recom.proto\x12\x0crecom_server\x1a\x1cgoogle/protobuf/struct.proto\"6\n\x0fModelProperties\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x12\n\nmodel_name\x18\x02 \x01(\x05\"S\n\x12\x43reateModelRequest\x12,\n\x05model\x18\x01 \x01(\x0b\x32\x1d.recom_server.ModelProperties\x12\x0f\n\x07verbose\x18\x02 \x01(\x08\"\x15\n\x13\x43reateModelResponse\"h\n\x15StartColdstartRequest\x12,\n\x05model\x18\x01 \x01(\x0b\x32\x1d.recom_server.ModelProperties\x12\x10\n\x08\x64\x61ta_dir\x18\x02 \x01(\t\x12\x0f\n\x07verbose\x18\x03 \x01(\x08\"\x18\n\x16StartColdstartResponse\"\xef\x01\n\x18StartSimilaritemsRequest\x12,\n\x05model\x18\x01 \x01(\x0b\x32\x1d.recom_server.ModelProperties\x12\x10\n\x08\x64\x61ta_dir\x18\x02 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x03 \x01(\t\x12\x0f\n\x07verbose\x18\x04 \x01(\x08\x12\t\n\x01k\x18\x05 \x01(\x05\x12\r\n\x05min_k\x18\x06 \x01(\x05\x12,\n\x0bsim_options\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0b\x62sl_options\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x1b\n\x19StartSimilaritemsResponse\"\x96\x01\n\x18StartUserspecificRequest\x12,\n\x05model\x18\x01 \x01(\x0b\x32\x1d.recom_server.ModelProperties\x12\x10\n\x08\x64\x61ta_dir\x18\x02 \x01(\t\x12\x0f\n\x07verbose\x18\x03 \x01(\x08\x12\t\n\x01k\x18\x04 \x01(\x05\x12\x0f\n\x07k_start\x18\x05 \x01(\x05\x12\r\n\x05k_end\x18\x06 \x01(\x05\"\x1b\n\x19StartUserspecificResponse\"\\\n\x10\x43oldstartRequest\x12,\n\x05model\x18\x01 \x01(\x0b\x32\x1d.recom_server.ModelProperties\x12\x0f\n\x07verbose\x18\x02 \x01(\x08\x12\t\n\x01n\x18\x03 \x01(\x05\"C\n\rColdstartItem\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x13\n\x0bmovie_title\x18\x02 \x01(\t\x12\x0c\n\x04rate\x18\x03 \x01(\x05\"?\n\x11\x43oldstartResponse\x12*\n\x05items\x18\x01 \x03(\x0b\x32\x1b.recom_server.ColdstartItem\"r\n\x13SimilaritemsRequest\x12,\n\x05model\x18\x01 \x01(\x0b\x32\x1d.recom_server.ModelProperties\x12\x0f\n\x07verbose\x18\x02 \x01(\x08\x12\t\n\x01n\x18\x03 \x01(\x05\x12\x11\n\titem_name\x18\x04 \x01(\t\"8\n\x10SimilaritemsItem\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x13\n\x0bmovie_title\x18\x02 \x01(\t\"E\n\x14SimilaritemsResponse\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.recom_server.SimilaritemsItem\"_\n\x13UserspecificRequest\x12,\n\x05model\x18\x01 \x01(\x0b\x32\x1d.recom_server.ModelProperties\x12\x0f\n\x07verbose\x18\x02 \x01(\x08\x12\t\n\x01n\x18\x03 \x01(\x05\"F\n\x10UserspecificItem\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x13\n\x0bmovie_title\x18\x02 \x01(\t\x12\x0c\n\x04rate\x18\x03 \x01(\x05\"E\n\x14UserspecificResponse\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.recom_server.UserspecificItem2\x83\x05\n\x08RecomaaS\x12R\n\x0b\x43reateModel\x12 .recom_server.CreateModelRequest\x1a!.recom_server.CreateModelResponse\x12[\n\x0eStartColdstart\x12#.recom_server.StartColdstartRequest\x1a$.recom_server.StartColdstartResponse\x12\x64\n\x11StartSimilaritems\x12&.recom_server.StartSimilaritemsRequest\x1a\'.recom_server.StartSimilaritemsResponse\x12\x64\n\x11StartUserspecific\x12&.recom_server.StartUserspecificRequest\x1a\'.recom_server.StartUserspecificResponse\x12L\n\tColdstart\x12\x1e.recom_server.ColdstartRequest\x1a\x1f.recom_server.ColdstartResponse\x12U\n\x0cSimilaritems\x12!.recom_server.SimilaritemsRequest\x1a\".recom_server.SimilaritemsResponse\x12U\n\x0cUserspecific\x12!.recom_server.UserspecificRequest\x1a\".recom_server.UserspecificResponseb\x06proto3')

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
  _STARTCOLDSTARTREQUEST._serialized_start=248
  _STARTCOLDSTARTREQUEST._serialized_end=352
  _STARTCOLDSTARTRESPONSE._serialized_start=354
  _STARTCOLDSTARTRESPONSE._serialized_end=378
  _STARTSIMILARITEMSREQUEST._serialized_start=381
  _STARTSIMILARITEMSREQUEST._serialized_end=620
  _STARTSIMILARITEMSRESPONSE._serialized_start=622
  _STARTSIMILARITEMSRESPONSE._serialized_end=649
  _STARTUSERSPECIFICREQUEST._serialized_start=652
  _STARTUSERSPECIFICREQUEST._serialized_end=802
  _STARTUSERSPECIFICRESPONSE._serialized_start=804
  _STARTUSERSPECIFICRESPONSE._serialized_end=831
  _COLDSTARTREQUEST._serialized_start=833
  _COLDSTARTREQUEST._serialized_end=925
  _COLDSTARTITEM._serialized_start=927
  _COLDSTARTITEM._serialized_end=994
  _COLDSTARTRESPONSE._serialized_start=996
  _COLDSTARTRESPONSE._serialized_end=1059
  _SIMILARITEMSREQUEST._serialized_start=1061
  _SIMILARITEMSREQUEST._serialized_end=1175
  _SIMILARITEMSITEM._serialized_start=1177
  _SIMILARITEMSITEM._serialized_end=1233
  _SIMILARITEMSRESPONSE._serialized_start=1235
  _SIMILARITEMSRESPONSE._serialized_end=1304
  _USERSPECIFICREQUEST._serialized_start=1306
  _USERSPECIFICREQUEST._serialized_end=1401
  _USERSPECIFICITEM._serialized_start=1403
  _USERSPECIFICITEM._serialized_end=1473
  _USERSPECIFICRESPONSE._serialized_start=1475
  _USERSPECIFICRESPONSE._serialized_end=1544
  _RECOMAAS._serialized_start=1547
  _RECOMAAS._serialized_end=2190
# @@protoc_insertion_point(module_scope)