import gen.pet_pb2 as pet_pb2


def main():
    pet = pet_pb2.Pet()
    pet.pet_id = "123"
    pet.name = "Fido"
    pet.pet_type = pet_pb2.PET_TYPE_DOG
    print(pet)


if __name__ == "__main__":
    main()
