import logging
import pytest
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
    """Fixture for setting up the test client."""
    app = create_app()
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
        yield testing_client


def test_healthcheck(test_client):
    """Test the healthcheck endpoint."""
    response = test_client.get('/healthcheck')

    assert response.status_code == 200
    assert response.data.decode() == 'Hi, The Web REST API Service is up and running!'

    logger.info("Healthcheck endpoint test passed with message: %s", response.data.decode())


def test_add_student(test_client):
    """Test adding a new student."""
    response = test_client.post(
        '/api/v1/students',
        json={'name': 'Rajesh', 'age': 21, 'gender': 'male'}
    )
    assert response.status_code == 201
    response_json = response.get_json()
    assert response_json['name'] == 'Rajesh'
    assert response_json['age'] == 21
    assert response_json['gender'] == 'male'

    logger.info("Retrieved student: %s", response_json)


def test_get_student(test_client):
    """Test retrieving a student by ID."""
    response = test_client.post(
        '/api/v1/students',
        json={'name': 'Rajesh', 'age': 21, 'gender': 'male'}
    )
    assert response.status_code == 201
    added_student = response.get_json()
    student_id = added_student['id']

    response = test_client.get(f'/api/v1/students/{student_id}')
    assert response.status_code == 200

    response_json = response.get_json()
    assert response_json['name'] == 'Rajesh'
    assert response_json['age'] == 21
    assert response_json['gender'] == 'male'
    logger.info("Retrieved student: %s", response_json)


def test_update_student(test_client):
    """Test updating an existing student."""
    response = test_client.post(
        '/api/v1/students',
        json={'name': 'Jack Doe', 'age': 30, 'gender': 'male'}
    )
    response_json = response.get_json()
    student_id = response_json['id']
    response = test_client.put(
        f'/api/v1/students/{student_id}',
        json={'name': 'Jack Updated', 'age': 31, 'gender': 'male'}
    )
    assert response.status_code == 200
    response_json = response.get_json()
    assert response_json['name'] == 'Jack Updated'
    assert response_json['gender'] == 'male'
    logger.info("Updated student %d: %s", student_id, response_json)


def test_delete_student(test_client):
    """Test deleting a student."""
    response = test_client.post(
        '/api/v1/students',
                json={
            'name': 'Jill Doe',
            'age': 27,
            'gender': 'female'  # Change gender to female for diversity
        }
    )
    response_json = response.get_json()
    student_id = response_json['id']
    response = test_client.delete(f'/api/v1/students/{student_id}')
    assert response.status_code == 204
    response = test_client.get(f'/api/v1/students/{student_id}')
    assert response.status_code == 404
    logger.info("Deleted student %d", student_id)
