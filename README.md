# PyPet - a Pet Adoption API

This repository contains a Pet Adoption API developed with Python and Flask. This project is part of my studies in backend development, focusing on software architecture, SOLID principles, and object-oriented programming best practices. The API is published as a web service on Render.

## Endpoints

The API includes the following endpoints for managing pets and people:

- **List Pets**: `GET /pets` - Returns a list of all pets available for adoption.
- **Delete Pet**: `DELETE /pet/<name>` - Removes a pet from the adoption list by ID.
- **Create Person**: `POST /people` - Adds a new person to the database.
- **Get Person by ID**: `GET /people/<person_id>` - Retrieves details of a specific person by ID.

## Technologies Used

- **Programming Language**: Python
- **Unit Tests**: PyTest
- **Web Framework**: Flask
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Architecture**: MVC (Model-View-Controller)

## Architecture and Best Practices

### MVC Pattern

The project follows the **MVC** (Model-View-Controller) architecture pattern, organizing code into three main layers:
- **Models**: Defines data classes and interactions with the database.
- **Views**: Defines the endpoints that interact with users.
- **Controllers**: Handles business logic and integrates the Model and View layers.


### Advanced Concepts

1. **SOLID**: Code is structured with SOLID principles to ensure maintainability, scalability, and readability.
2. **Object-Oriented Programming**: The project uses classes, inheritance, and abstract classes to organize functionalities, reinforcing the use of the OOP paradigm.
3. **Best Practices**: The architecture and code organization follow development best practices, such as separation of concerns, modularity, and code reusability. The project also comprises unit tests for each layer, following **Test Driven Development**.
4. **Automated linting**: The project is configured to perform an automated linting on all python files to assure code quality and compliance with Python coding conventions best practices as well

### Project basic folder structure
```bash
.
├── LICENSE
├── init
│   └── schema.sql
├── requirements.txt
├── run.py
├── src
│   ├── controllers
│   │   ├── interfaces
│   │   │   ├── person_creator_controller.py
│   │   │   ├── person_finder_controller.py
│   │   │   ├── pet_delete_controller.py
│   │   │   └── pet_list_controller.py
│   │   ├── person_creator_controller.py
│   │   ├── person_creator_controller_test.py
│   │   ├── person_finder_controller.py
│   │   ├── person_finder_controller_test.py
│   │   ├── pet_delete_controller.py
│   │   ├── pet_delete_controller_test.py
│   │   ├── pet_list_controller.py
│   │   └── pet_list_controller_test.py
│   ├── errors
│   │   ├── error_handler.py
│   │   └── error_types
│   │       ├── http_bad_request.py
│   │       ├── http_not_found.py
│   │       └── http_unprocessable_entity.py
│   ├── main
│   │   ├── composer
│   │   │   ├── person_creator_composer.py
│   │   │   ├── person_finder_composer.py
│   │   │   ├── pet_delete_composer.py
│   │   │   └── pet_list_composer.py
│   │   ├── routes
│   │   │   ├── person_routes.py
│   │   │   └── pets_routes.py
│   │   └── server
│   │       └── server.py
│   ├── models
│   │   └── sqlite
│   │       ├── entities
│   │       │   ├── people.py
│   │       │   └── pets.py
│   │       ├── interfaces
│   │       │   ├── people_repository.py
│   │       │   └── pets_repository.py
│   │       ├── repositories
│   │       │   ├── people_repository.py
│   │       │   ├── people_repository_test.py
│   │       │   ├── pets_repository.py
│   │       │   ├── pets_repository_test.py
│   │       │   └── repositories_test.py
│   │       └── settings
│   │           ├── base.py
│   │           ├── connection.py
│   │           └── connection_test.py
│   ├── validators
│   │   ├── person_creator_validator.py
│   │   └── person_creator_validator_test.py
│   └── views
│       ├── http_types
│       │   ├── http_request.py
│       │   └── http_response.py
│       ├── interfaces
│       │   └── view_interface.py
│       ├── mock_http_request.py
│       ├── person_creator_view.py
│       ├── person_creator_view_test.py
│       ├── person_finder_view.py
│       ├── person_finder_view_test.py
│       ├── pet_delete_view.py
│       ├── pet_delete_view_test.py
│       ├── pet_list_view.py
│       └── pet_list_view_test.py
├── storage.db
└── tox.ini
```

## How to Run the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/py-pet-flask-api.git
    cd py-pet-flask-api
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Start the server:
    ```bash
    flask run
    ```

5. Access the API locally:
    ```
    http://127.0.0.1:3000
    ```

## Deployment

The API is published as a web service on Render and can be accessed at [PyPet - Pet Adoption API](https://py-pet-flask-api.onrender.com/)

## License

This project is licensed under the MIT License.
