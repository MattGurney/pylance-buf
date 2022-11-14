# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pet.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tpet.proto\x12\x06pet.v1\"F\n\x03Pet\x12!\n\x08pet_type\x18\x01 \x01(\x0e\x32\x0f.pet.v1.PetType\x12\x0e\n\x06pet_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\x1f\n\rGetPetRequest\x12\x0e\n\x06pet_id\x18\x01 \x01(\t\"*\n\x0eGetPetResponse\x12\x18\n\x03pet\x18\x01 \x01(\x0b\x32\x0b.pet.v1.Pet\"@\n\rPutPetRequest\x12!\n\x08pet_type\x18\x01 \x01(\x0e\x32\x0f.pet.v1.PetType\x12\x0c\n\x04name\x18\x02 \x01(\t\"*\n\x0ePutPetResponse\x12\x18\n\x03pet\x18\x01 \x01(\x0b\x32\x0b.pet.v1.Pet\"\"\n\x10\x44\x65letePetRequest\x12\x0e\n\x06pet_id\x18\x01 \x01(\t\"\x13\n\x11\x44\x65letePetResponse\"$\n\x12PurchasePetRequest\x12\x0e\n\x06pet_id\x18\x01 \x01(\t\"\x15\n\x13PurchasePetResponse*q\n\x07PetType\x12\x18\n\x14PET_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cPET_TYPE_CAT\x10\x01\x12\x10\n\x0cPET_TYPE_DOG\x10\x02\x12\x12\n\x0ePET_TYPE_SNAKE\x10\x03\x12\x14\n\x10PET_TYPE_HAMSTER\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pet_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PETTYPE._serialized_start=398
  _PETTYPE._serialized_end=511
  _PET._serialized_start=21
  _PET._serialized_end=91
  _GETPETREQUEST._serialized_start=93
  _GETPETREQUEST._serialized_end=124
  _GETPETRESPONSE._serialized_start=126
  _GETPETRESPONSE._serialized_end=168
  _PUTPETREQUEST._serialized_start=170
  _PUTPETREQUEST._serialized_end=234
  _PUTPETRESPONSE._serialized_start=236
  _PUTPETRESPONSE._serialized_end=278
  _DELETEPETREQUEST._serialized_start=280
  _DELETEPETREQUEST._serialized_end=314
  _DELETEPETRESPONSE._serialized_start=316
  _DELETEPETRESPONSE._serialized_end=335
  _PURCHASEPETREQUEST._serialized_start=337
  _PURCHASEPETREQUEST._serialized_end=373
  _PURCHASEPETRESPONSE._serialized_start=375
  _PURCHASEPETRESPONSE._serialized_end=396
# @@protoc_insertion_point(module_scope)