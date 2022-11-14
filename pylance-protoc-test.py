import protoc_gen.pet_pb2 as pb_protoc


def test_protoc_generated():
    pet = pb_protoc.Pet()
    pet.pet_id = "123"
    pet.name = "Fido"
    pet.pet_type = pb_protoc.PET_TYPE_DOG
    print(pet)


def main():
    test_protoc_generated()


if __name__ == "__main__":
    main()
