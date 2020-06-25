# ansara-connect-api
API for Ansara Connect, a professional networking platform for alumni.

## Quick Start.

1. Clone this repository.
    ```git clone```
2. Navigate into the project directory (```cd ansara-connect-api```) & install Django and Django REST Framework requirements.
      ```pip install -r requirements.txt```
3. Create a superuser account.
    ```python manage.py createsuperuser```
4. Migrate the database to reflect user record changes.
    ```python manage.py migrate```
5. Run the development server.
    ```python manage.py runserver```
6. The API is now accessible under ```http://localhost:8000```

## Testing the API

### Using CLI

Run ```curl -H 'Accept: application/json; indent=4' -u <username>:<password> http://localhost/users/```

## Development Notes

1. Next steps includes integration with LinkedIn API to retrieve member's linked LinkedIn profiles. This indirectly includes the development of an authentication endpoints.
2. OAuth2 will be this API's aunthentication framework.

Project started on 24 June 2020.

See the [frontend](https://github.com/mirzanorazman/ansara-connect/ "by Mirza Nor Azman").