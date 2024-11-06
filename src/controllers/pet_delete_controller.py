import src.models.sqlite.interfaces.pets_repository as intf


class PetDeleteController:
    def __init__(self, pet_repository: intf.PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def delete(self, name: str) -> None:
        self.__pet_repository.delete_pet(name)
