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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tpet.proto\x12\x06pet.v1\"\\\n\x03Pet\x12*\n\x08pet_type\x18\x01 \x01(\x0e\x32\x0f.pet.v1.PetTypeR\x07petType\x12\x15\n\x06pet_id\x18\x02 \x01(\tR\x05petId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\"&\n\rGetPetRequest\x12\x15\n\x06pet_id\x18\x01 \x01(\tR\x05petId\"/\n\x0eGetPetResponse\x12\x1d\n\x03pet\x18\x01 \x01(\x0b\x32\x0b.pet.v1.PetR\x03pet\"O\n\rPutPetRequest\x12*\n\x08pet_type\x18\x01 \x01(\x0e\x32\x0f.pet.v1.PetTypeR\x07petType\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"/\n\x0ePutPetResponse\x12\x1d\n\x03pet\x18\x01 \x01(\x0b\x32\x0b.pet.v1.PetR\x03pet\")\n\x10\x44\x65letePetRequest\x12\x15\n\x06pet_id\x18\x01 \x01(\tR\x05petId\"\x13\n\x11\x44\x65letePetResponse\"+\n\x12PurchasePetRequest\x12\x15\n\x06pet_id\x18\x01 \x01(\tR\x05petId\"\x15\n\x13PurchasePetResponse*q\n\x07PetType\x12\x18\n\x14PET_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cPET_TYPE_CAT\x10\x01\x12\x10\n\x0cPET_TYPE_DOG\x10\x02\x12\x12\n\x0ePET_TYPE_SNAKE\x10\x03\x12\x14\n\x10PET_TYPE_HAMSTER\x10\x04\x42O\n\ncom.pet.v1B\x08PetProtoP\x01\xa2\x02\x03PXX\xaa\x02\x06Pet.V1\xca\x02\x06Pet\\V1\xe2\x02\x12Pet\\V1\\GPBMetadata\xea\x02\x07Pet::V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pet_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\ncom.pet.v1B\010PetProtoP\001\242\002\003PXX\252\002\006Pet.V1\312\002\006Pet\\V1\342\002\022Pet\\V1\\GPBMetadata\352\002\007Pet::V1'
  _PETTYPE._serialized_start=466
  _PETTYPE._serialized_end=579
  _PET._serialized_start=21
  _PET._serialized_end=113
  _GETPETREQUEST._serialized_start=115
  _GETPETREQUEST._serialized_end=153
  _GETPETRESPONSE._serialized_start=155
  _GETPETRESPONSE._serialized_end=202
  _PUTPETREQUEST._serialized_start=204
  _PUTPETREQUEST._serialized_end=283
  _PUTPETRESPONSE._serialized_start=285
  _PUTPETRESPONSE._serialized_end=332
  _DELETEPETREQUEST._serialized_start=334
  _DELETEPETREQUEST._serialized_end=375
  _DELETEPETRESPONSE._serialized_start=377
  _DELETEPETRESPONSE._serialized_end=396
  _PURCHASEPETREQUEST._serialized_start=398
  _PURCHASEPETREQUEST._serialized_end=441
  _PURCHASEPETRESPONSE._serialized_start=443
  _PURCHASEPETRESPONSE._serialized_end=464
# @@protoc_insertion_point(module_scope)
