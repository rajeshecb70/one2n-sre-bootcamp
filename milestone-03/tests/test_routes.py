import pytest
import logging
from app import create_app, db
from app.models import Student

# Configure logging for tests
logger = logging.getLogger('app')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('test_app.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)
logger.addHandler(handler)


@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
        yield testing_client

def test_healthcheck(test_client):
    # Make a GET request to the /healthcheck endpoint
    response = test_client.get('/healthcheck')

    # Assert that the status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response data is the expected healthcheck message
    assert response.data.decode() == 'Hi, The Web REST API Service is up and running!'

    # Optionally, log the result
    logger.info("Healthcheck endpoint test passed with message: %s", response.data.decode())


def test_add_student(test_client):
    # Test with phone_number as integer
    response = test_client.post(
        '/api/v1/students',
        json={'name': 'Rajesh', 'age': 21, 'phone_number': '1234567890'}
    )
    assert response.status_code == 201
    response_json = response.get_json()
    assert response_json['name'] == 'Rajesh'
    assert response_json['age'] == 21
    assert response_json['phone_number'] == 1234567890
    logger.info(f"Added student with phone number: {response_json['phone_number']}")

def test_get_student(test_client):
    # First, add a student to ensure we have a record to retrieve
    response = test_client.post(
        '/api/v1/students',
        json={'name': 'Rajesh', 'age': 21, 'phone_number': '1234567890'}
    )
    assert response.status_code == 201
    added_student = response.get_json()
    student_id = added_student['id']  # Assuming the student record includes an 'id'

    # Now, make a GET request to retrieve the student by ID
    response = test_client.get(f'/api/v1/students/{student_id}')
    
    # Assert that the status code is 200 (OK)
    assert response.status_code == 200
    
    # Assert that the response contains the correct student data
    response_json = response.get_json()
    assert response_json['name'] == 'Rajesh'
    assert response_json['age'] == 21
    assert response_json['phone_number'] == 1234567890
    
    # Log the result
    logger.info(f"Retrieved student: {response_json}")

def test_update_student(test_client):
    response = test_client.post(
        '/api/v1/students',
        json={'name': 'Jack Doe', 'age': 30, 'phone_number': '1234567890'}
    )
    response_json = response.get_json()
    student_id = response_json['id']
    response = test_client.put(
        f'/api/v1/students/{student_id}',
        json={'name': 'Jack Updated', 'age': 31, 'phone_number': '5559999'}
    )
    assert response.status_code == 200
    response_json = response.get_json()
    assert response_json['name'] == 'Jack Updated'
    assert response_json['phone_number'] == 5559999
    logger.info(f"Updated student {student_id}: {response_json}")


def test_delete_student(test_client):
    response = test_client.post(
        '/api/v1/students',
        json={'name': 'Jill Doe', 'age': 27, 'phone_number': '1234567890'}
    )
    response_json = response.get_json()
    student_id = response_json['id']
    response = test_client.delete(f'/api/v1/students/{student_id}')
    assert response.status_code == 204
    response = test_client.get(f'/api/v1/students/{student_id}')
    assert response.status_code == 404
    logger.info(f"Deleted student {student_id}")

