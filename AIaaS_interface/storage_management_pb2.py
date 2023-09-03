# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storage_management.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18storage_management.proto\x12\x12storage_management\"?\n\x13RegisterUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x16\n\x0einitial_volume\x18\x02 \x01(\x03\"\x16\n\x14RegisterUserResponse\")\n\x15\x44\x65registerUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"\x18\n\x16\x44\x65registerUserResponse\"8\n\x10SetVolumeRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x12\n\nnew_volume\x18\x02 \x01(\x03\"\x13\n\x11SetVolumeResponse\"N\n\x16SetSystemVolumeRequest\x12\x14\n\x0ctotal_volume\x18\x01 \x01(\x03\x12\x1e\n\x16over_subscription_rate\x18\x02 \x01(\x02\"\x19\n\x17SetSystemVolumeResponse\"c\n\x0cVolumeReport\x12\x1e\n\x16total_allocated_volume\x18\x01 \x01(\x03\x12\x19\n\x11total_used_volume\x18\x02 \x01(\x03\x12\x18\n\x10remaining_volume\x18\x03 \x01(\x03\"$\n\x10GetVolumeRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"L\n\x11GetVolumeResponse\x12\x37\n\rvolume_report\x18\x01 \x01(\x0b\x32 .storage_management.VolumeReport\"J\n\x13\x43reateFolderRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x13\n\x0b\x66older_name\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\"\x16\n\x14\x43reateFolderResponse\"/\n\rRemoveRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"\x10\n\x0eRemoveResponse\"4\n\x12\x46orceRemoveRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"\x15\n\x13\x46orceRemoveResponse\"*\n\x16\x45mptyRecycleBinRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"\x19\n\x17\x45mptyRecycleBinResponse\"3\n\x11\x42rowseDataRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"&\n\x12\x42rowseDataResponse\x12\x10\n\x08\x63ontents\x18\x01 \x03(\t\"2\n\rSearchRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"4\n\x0eSearchResponse\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontent_type\x18\x02 \x01(\t\"\x1a\n\x18GetSystemicReportRequest\"\xa3\x01\n\x19GetSystemicReportResponse\x12\x14\n\x0ctotal_volume\x18\x01 \x01(\x03\x12\x1e\n\x16over_subscription_rate\x18\x02 \x01(\x02\x12\x17\n\x0fnumber_of_users\x18\x03 \x01(\x03\x12\x37\n\rvolume_report\x18\x04 \x01(\x0b\x32 .storage_management.VolumeReport\"N\n\x0b\x43opyRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x13\n\x0bsource_path\x18\x02 \x01(\t\x12\x18\n\x10\x64\x65stination_path\x18\x03 \x01(\t\"\x0e\n\x0c\x43opyResponse\"M\n\nCutRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x13\n\x0bsource_path\x18\x02 \x01(\t\x12\x18\n\x10\x64\x65stination_path\x18\x03 \x01(\t\"\r\n\x0b\x43utResponse\"5\n\x13\x44ownloadFileRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"*\n\x14\x44ownloadFileResponse\x12\x12\n\nchunk_data\x18\x01 \x01(\x0c\"O\n\x08MetaData\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x10\n\x08\x66ilename\x18\x03 \x01(\t\x12\x11\n\textension\x18\x04 \x01(\t\"f\n\x11UploadFileRequest\x12\x30\n\x08metadata\x18\x01 \x01(\x0b\x32\x1c.storage_management.MetaDataH\x00\x12\x14\n\nchunk_data\x18\x02 \x01(\x0cH\x00\x42\t\n\x07request\"\x14\n\x12UploadFileResponse2\xfc\x0b\n\x11StorageManagement\x12\x61\n\x0cRegisterUser\x12\'.storage_management.RegisterUserRequest\x1a(.storage_management.RegisterUserResponse\x12g\n\x0e\x44\x65registerUser\x12).storage_management.DeregisterUserRequest\x1a*.storage_management.DeregisterUserResponse\x12X\n\tSetVolume\x12$.storage_management.SetVolumeRequest\x1a%.storage_management.SetVolumeResponse\x12j\n\x0fSetSystemVolume\x12*.storage_management.SetSystemVolumeRequest\x1a+.storage_management.SetSystemVolumeResponse\x12^\n\x0fGetVolumeReport\x12$.storage_management.GetVolumeRequest\x1a%.storage_management.GetVolumeResponse\x12\x61\n\x0c\x43reateFolder\x12\'.storage_management.CreateFolderRequest\x1a(.storage_management.CreateFolderResponse\x12O\n\x06Remove\x12!.storage_management.RemoveRequest\x1a\".storage_management.RemoveResponse\x12^\n\x0b\x46orceRemove\x12&.storage_management.ForceRemoveRequest\x1a\'.storage_management.ForceRemoveResponse\x12j\n\x0f\x45mptyRecycleBin\x12*.storage_management.EmptyRecycleBinRequest\x1a+.storage_management.EmptyRecycleBinResponse\x12[\n\nBrowseData\x12%.storage_management.BrowseDataRequest\x1a&.storage_management.BrowseDataResponse\x12O\n\x06Search\x12!.storage_management.SearchRequest\x1a\".storage_management.SearchResponse\x12p\n\x11GetSystemicReport\x12,.storage_management.GetSystemicReportRequest\x1a-.storage_management.GetSystemicReportResponse\x12I\n\x04\x43opy\x12\x1f.storage_management.CopyRequest\x1a .storage_management.CopyResponse\x12\x46\n\x03\x43ut\x12\x1e.storage_management.CutRequest\x1a\x1f.storage_management.CutResponse\x12\x63\n\x0c\x44ownloadFile\x12\'.storage_management.DownloadFileRequest\x1a(.storage_management.DownloadFileResponse0\x01\x12]\n\nUploadFile\x12%.storage_management.UploadFileRequest\x1a&.storage_management.UploadFileResponse(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'storage_management_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGISTERUSERREQUEST._serialized_start=48
  _REGISTERUSERREQUEST._serialized_end=111
  _REGISTERUSERRESPONSE._serialized_start=113
  _REGISTERUSERRESPONSE._serialized_end=135
  _DEREGISTERUSERREQUEST._serialized_start=137
  _DEREGISTERUSERREQUEST._serialized_end=178
  _DEREGISTERUSERRESPONSE._serialized_start=180
  _DEREGISTERUSERRESPONSE._serialized_end=204
  _SETVOLUMEREQUEST._serialized_start=206
  _SETVOLUMEREQUEST._serialized_end=262
  _SETVOLUMERESPONSE._serialized_start=264
  _SETVOLUMERESPONSE._serialized_end=283
  _SETSYSTEMVOLUMEREQUEST._serialized_start=285
  _SETSYSTEMVOLUMEREQUEST._serialized_end=363
  _SETSYSTEMVOLUMERESPONSE._serialized_start=365
  _SETSYSTEMVOLUMERESPONSE._serialized_end=390
  _VOLUMEREPORT._serialized_start=392
  _VOLUMEREPORT._serialized_end=491
  _GETVOLUMEREQUEST._serialized_start=493
  _GETVOLUMEREQUEST._serialized_end=529
  _GETVOLUMERESPONSE._serialized_start=531
  _GETVOLUMERESPONSE._serialized_end=607
  _CREATEFOLDERREQUEST._serialized_start=609
  _CREATEFOLDERREQUEST._serialized_end=683
  _CREATEFOLDERRESPONSE._serialized_start=685
  _CREATEFOLDERRESPONSE._serialized_end=707
  _REMOVEREQUEST._serialized_start=709
  _REMOVEREQUEST._serialized_end=756
  _REMOVERESPONSE._serialized_start=758
  _REMOVERESPONSE._serialized_end=774
  _FORCEREMOVEREQUEST._serialized_start=776
  _FORCEREMOVEREQUEST._serialized_end=828
  _FORCEREMOVERESPONSE._serialized_start=830
  _FORCEREMOVERESPONSE._serialized_end=851
  _EMPTYRECYCLEBINREQUEST._serialized_start=853
  _EMPTYRECYCLEBINREQUEST._serialized_end=895
  _EMPTYRECYCLEBINRESPONSE._serialized_start=897
  _EMPTYRECYCLEBINRESPONSE._serialized_end=922
  _BROWSEDATAREQUEST._serialized_start=924
  _BROWSEDATAREQUEST._serialized_end=975
  _BROWSEDATARESPONSE._serialized_start=977
  _BROWSEDATARESPONSE._serialized_end=1015
  _SEARCHREQUEST._serialized_start=1017
  _SEARCHREQUEST._serialized_end=1067
  _SEARCHRESPONSE._serialized_start=1069
  _SEARCHRESPONSE._serialized_end=1121
  _GETSYSTEMICREPORTREQUEST._serialized_start=1123
  _GETSYSTEMICREPORTREQUEST._serialized_end=1149
  _GETSYSTEMICREPORTRESPONSE._serialized_start=1152
  _GETSYSTEMICREPORTRESPONSE._serialized_end=1315
  _COPYREQUEST._serialized_start=1317
  _COPYREQUEST._serialized_end=1395
  _COPYRESPONSE._serialized_start=1397
  _COPYRESPONSE._serialized_end=1411
  _CUTREQUEST._serialized_start=1413
  _CUTREQUEST._serialized_end=1490
  _CUTRESPONSE._serialized_start=1492
  _CUTRESPONSE._serialized_end=1505
  _DOWNLOADFILEREQUEST._serialized_start=1507
  _DOWNLOADFILEREQUEST._serialized_end=1560
  _DOWNLOADFILERESPONSE._serialized_start=1562
  _DOWNLOADFILERESPONSE._serialized_end=1604
  _METADATA._serialized_start=1606
  _METADATA._serialized_end=1685
  _UPLOADFILEREQUEST._serialized_start=1687
  _UPLOADFILEREQUEST._serialized_end=1789
  _UPLOADFILERESPONSE._serialized_start=1791
  _UPLOADFILERESPONSE._serialized_end=1811
  _STORAGEMANAGEMENT._serialized_start=1814
  _STORAGEMANAGEMENT._serialized_end=3346
# @@protoc_insertion_point(module_scope)
