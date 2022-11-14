import buf_gen.pet_pb2 as pet_pb2


def test_buf_generated():
    pet = pet_pb2.Pet()
    pet.pet_id = "123"
    pet.name = "Fido"
    pet.pet_type = pet_pb2.PET_TYPE_DOG
    print(pet)


def main():
    test_buf_generated()


if __name__ == "__main__":
    main()
