'''
    add path of this folder to os for solving import errors in python autogenerated package
    DO NOT CHANGE THIS FILE !!!
'''
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, '')
sys.path.append(output_dir)

import storage_management_pb2_grpc
import storage_management_pb2
import platform_management
import stubs
import ai_services
