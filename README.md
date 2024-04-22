
# Django_investing_list

## Project Description

Django_investing_list is a Django application designed to manage client investment data. It features an efficient PostgreSQL backend and implements a secure login and logout system. The interfaces and front-end are styled with Django and Crispy Bootstrap for a user-friendly experience.

## Installation

To install the project, you need to install the dependencies listed in the `requirements.txt` file. You can do this by running the following command:

```bash
pip3 install -r requirements.txt
```

## Usage

The application allows you to register investments in a table-like format. You can record the investments you've made, such as buying a car and its value, and whether it's paid off or not.

To start the application, run the following command:

```bash
python3 manage.py runserver
```

## Key Features

- **Investment Registration**: Allows users to register their investments in a table-like format.
- **Login and Logout System**: A secure login and logout system is implemented for user authentication.
- **PostgreSQL Database**: An efficient PostgreSQL database is used for backend operations.

## Code Details

The application is structured into various key files:

- `base.html`: This file extends the 'investments/base.html' and contains the HTML structure of the investment listing page.
- `views.py`: This file contains the main views for the application, including the investment view, detail view, create view, edit view, and delete view. It uses Django's built-in login_required decorator to ensure that only authenticated users can create, edit, and delete investments.

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Author

👤 Joao Melo

- Github: @johnmelodev
- LinkedIn: @joao-melo-dev

## Show your support

Give a ⭐️ if this project helped you!
```
