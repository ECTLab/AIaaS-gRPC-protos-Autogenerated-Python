# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_storage/storage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x64\x61ta_storage/storage.proto\x12\x0c\x64\x61ta_storage\"?\n\x13RegisterUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x16\n\x0einitial_volume\x18\x02 \x01(\x03\"\x16\n\x14RegisterUserResponse\")\n\x15\x44\x65registerUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"\x18\n\x16\x44\x65registerUserResponse\"8\n\x10SetVolumeRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x12\n\nnew_volume\x18\x02 \x01(\x03\"\x13\n\x11SetVolumeResponse\"N\n\x16SetSystemVolumeRequest\x12\x14\n\x0ctotal_volume\x18\x01 \x01(\x03\x12\x1e\n\x16over_subscription_rate\x18\x02 \x01(\x02\"\x19\n\x17SetSystemVolumeResponse\"c\n\x0cVolumeReport\x12\x1e\n\x16total_allocated_volume\x18\x01 \x01(\x03\x12\x19\n\x11total_used_volume\x18\x02 \x01(\x03\x12\x18\n\x10remaining_volume\x18\x03 \x01(\x03\"$\n\x10GetVolumeRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"F\n\x11GetVolumeResponse\x12\x31\n\rvolume_report\x18\x01 \x01(\x0b\x32\x1a.data_storage.VolumeReport\"J\n\x13\x43reateFolderRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x13\n\x0b\x66older_name\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\"\x16\n\x14\x43reateFolderResponse\"/\n\rRemoveRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"\x10\n\x0eRemoveResponse\"4\n\x12\x46orceRemoveRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"\x15\n\x13\x46orceRemoveResponse\"*\n\x16\x45mptyRecycleBinRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"\x19\n\x17\x45mptyRecycleBinResponse\"3\n\x11\x42rowseDataRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"&\n\x12\x42rowseDataResponse\x12\x10\n\x08\x63ontents\x18\x01 \x03(\t\"2\n\rSearchRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"4\n\x0eSearchResponse\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontent_type\x18\x02 \x01(\t\"\x1a\n\x18GetSystemicReportRequest\"\x9d\x01\n\x19GetSystemicReportResponse\x12\x14\n\x0ctotal_volume\x18\x01 \x01(\x03\x12\x1e\n\x16over_subscription_rate\x18\x02 \x01(\x02\x12\x17\n\x0fnumber_of_users\x18\x03 \x01(\x03\x12\x31\n\rvolume_report\x18\x04 \x01(\x0b\x32\x1a.data_storage.VolumeReport\"N\n\x0b\x43opyRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x13\n\x0bsource_path\x18\x02 \x01(\t\x12\x18\n\x10\x64\x65stination_path\x18\x03 \x01(\t\"\x0e\n\x0c\x43opyResponse\"M\n\nCutRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x13\n\x0bsource_path\x18\x02 \x01(\t\x12\x18\n\x10\x64\x65stination_path\x18\x03 \x01(\t\"\r\n\x0b\x43utResponse\"5\n\x13\x44ownloadFileRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"*\n\x14\x44ownloadFileResponse\x12\x12\n\nchunk_data\x18\x01 \x01(\x0c\"O\n\x08MetaData\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x10\n\x08\x66ilename\x18\x03 \x01(\t\x12\x11\n\textension\x18\x04 \x01(\t\"`\n\x11UploadFileRequest\x12*\n\x08metadata\x18\x01 \x01(\x0b\x32\x16.data_storage.MetaDataH\x00\x12\x14\n\nchunk_data\x18\x02 \x01(\x0cH\x00\x42\t\n\x07request\"\x14\n\x12UploadFileResponse2\xb6\n\n\x0b\x44\x61taStorage\x12U\n\x0cRegisterUser\x12!.data_storage.RegisterUserRequest\x1a\".data_storage.RegisterUserResponse\x12[\n\x0e\x44\x65registerUser\x12#.data_storage.DeregisterUserRequest\x1a$.data_storage.DeregisterUserResponse\x12L\n\tSetVolume\x12\x1e.data_storage.SetVolumeRequest\x1a\x1f.data_storage.SetVolumeResponse\x12^\n\x0fSetSystemVolume\x12$.data_storage.SetSystemVolumeRequest\x1a%.data_storage.SetSystemVolumeResponse\x12R\n\x0fGetVolumeReport\x12\x1e.data_storage.GetVolumeRequest\x1a\x1f.data_storage.GetVolumeResponse\x12U\n\x0c\x43reateFolder\x12!.data_storage.CreateFolderRequest\x1a\".data_storage.CreateFolderResponse\x12\x43\n\x06Remove\x12\x1b.data_storage.RemoveRequest\x1a\x1c.data_storage.RemoveResponse\x12R\n\x0b\x46orceRemove\x12 .data_storage.ForceRemoveRequest\x1a!.data_storage.ForceRemoveResponse\x12^\n\x0f\x45mptyRecycleBin\x12$.data_storage.EmptyRecycleBinRequest\x1a%.data_storage.EmptyRecycleBinResponse\x12O\n\nBrowseData\x12\x1f.data_storage.BrowseDataRequest\x1a .data_storage.BrowseDataResponse\x12\x43\n\x06Search\x12\x1b.data_storage.SearchRequest\x1a\x1c.data_storage.SearchResponse\x12\x64\n\x11GetSystemicReport\x12&.data_storage.GetSystemicReportRequest\x1a\'.data_storage.GetSystemicReportResponse\x12=\n\x04\x43opy\x12\x19.data_storage.CopyRequest\x1a\x1a.data_storage.CopyResponse\x12:\n\x03\x43ut\x12\x18.data_storage.CutRequest\x1a\x19.data_storage.CutResponse\x12W\n\x0c\x44ownloadFile\x12!.data_storage.DownloadFileRequest\x1a\".data_storage.DownloadFileResponse0\x01\x12Q\n\nUploadFile\x12\x1f.data_storage.UploadFileRequest\x1a .data_storage.UploadFileResponse(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data_storage.storage_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGISTERUSERREQUEST._serialized_start=44
  _REGISTERUSERREQUEST._serialized_end=107
  _REGISTERUSERRESPONSE._serialized_start=109
  _REGISTERUSERRESPONSE._serialized_end=131
  _DEREGISTERUSERREQUEST._serialized_start=133
  _DEREGISTERUSERREQUEST._serialized_end=174
  _DEREGISTERUSERRESPONSE._serialized_start=176
  _DEREGISTERUSERRESPONSE._serialized_end=200
  _SETVOLUMEREQUEST._serialized_start=202
  _SETVOLUMEREQUEST._serialized_end=258
  _SETVOLUMERESPONSE._serialized_start=260
  _SETVOLUMERESPONSE._serialized_end=279
  _SETSYSTEMVOLUMEREQUEST._serialized_start=281
  _SETSYSTEMVOLUMEREQUEST._serialized_end=359
  _SETSYSTEMVOLUMERESPONSE._serialized_start=361
  _SETSYSTEMVOLUMERESPONSE._serialized_end=386
  _VOLUMEREPORT._serialized_start=388
  _VOLUMEREPORT._serialized_end=487
  _GETVOLUMEREQUEST._serialized_start=489
  _GETVOLUMEREQUEST._serialized_end=525
  _GETVOLUMERESPONSE._serialized_start=527
  _GETVOLUMERESPONSE._serialized_end=597
  _CREATEFOLDERREQUEST._serialized_start=599
  _CREATEFOLDERREQUEST._serialized_end=673
  _CREATEFOLDERRESPONSE._serialized_start=675
  _CREATEFOLDERRESPONSE._serialized_end=697
  _REMOVEREQUEST._serialized_start=699
  _REMOVEREQUEST._serialized_end=746
  _REMOVERESPONSE._serialized_start=748
  _REMOVERESPONSE._serialized_end=764
  _FORCEREMOVEREQUEST._serialized_start=766
  _FORCEREMOVEREQUEST._serialized_end=818
  _FORCEREMOVERESPONSE._serialized_start=820
  _FORCEREMOVERESPONSE._serialized_end=841
  _EMPTYRECYCLEBINREQUEST._serialized_start=843
  _EMPTYRECYCLEBINREQUEST._serialized_end=885
  _EMPTYRECYCLEBINRESPONSE._serialized_start=887
  _EMPTYRECYCLEBINRESPONSE._serialized_end=912
  _BROWSEDATAREQUEST._serialized_start=914
  _BROWSEDATAREQUEST._serialized_end=965
  _BROWSEDATARESPONSE._serialized_start=967
  _BROWSEDATARESPONSE._serialized_end=1005
  _SEARCHREQUEST._serialized_start=1007
  _SEARCHREQUEST._serialized_end=1057
  _SEARCHRESPONSE._serialized_start=1059
  _SEARCHRESPONSE._serialized_end=1111
  _GETSYSTEMICREPORTREQUEST._serialized_start=1113
  _GETSYSTEMICREPORTREQUEST._serialized_end=1139
  _GETSYSTEMICREPORTRESPONSE._serialized_start=1142
  _GETSYSTEMICREPORTRESPONSE._serialized_end=1299
  _COPYREQUEST._serialized_start=1301
  _COPYREQUEST._serialized_end=1379
  _COPYRESPONSE._serialized_start=1381
  _COPYRESPONSE._serialized_end=1395
  _CUTREQUEST._serialized_start=1397
  _CUTREQUEST._serialized_end=1474
  _CUTRESPONSE._serialized_start=1476
  _CUTRESPONSE._serialized_end=1489
  _DOWNLOADFILEREQUEST._serialized_start=1491
  _DOWNLOADFILEREQUEST._serialized_end=1544
  _DOWNLOADFILERESPONSE._serialized_start=1546
  _DOWNLOADFILERESPONSE._serialized_end=1588
  _METADATA._serialized_start=1590
  _METADATA._serialized_end=1669
  _UPLOADFILEREQUEST._serialized_start=1671
  _UPLOADFILEREQUEST._serialized_end=1767
  _UPLOADFILERESPONSE._serialized_start=1769
  _UPLOADFILERESPONSE._serialized_end=1789
  _DATASTORAGE._serialized_start=1792
  _DATASTORAGE._serialized_end=3126
# @@protoc_insertion_point(module_scope)
