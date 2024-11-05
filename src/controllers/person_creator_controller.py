import src.models.sqlite.interfaces.people_repository as interface


class PersonCreatorController:
    def __init__(self, people_repository:
                 interface.PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def get(self):
        return self.__people_repository
