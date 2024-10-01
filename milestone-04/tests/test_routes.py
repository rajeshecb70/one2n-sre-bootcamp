import logging
import pytest
from app import create_app, db
from app.models import Student

logger = logging.getLogger('app')
handler = logging.FileHandler('test_app.log')
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
        yield testing_client

def create_student(client, name='Rajesh', age=21, gender='male'):
    return client.post('/api/v1/students', json={'name': name, 'age': age, 'gender': gender})

def test_healthcheck(test_client):
    response = test_client.get('/healthcheck')
    assert response.status_code == 200
    assert response.data.decode() == 'API Service is up and running!'
    logger.info("Healthcheck test passed")

def test_add_student(test_client):
    response = create_student(test_client)
    assert response.status_code == 201
    response_json = response.get_json()
    assert response_json['name'] == 'Rajesh'
    assert response_json['age'] == 21
    assert response_json['gender'] == 'male'
    logger.info("Add student test passed")

def test_get_student(test_client):
    response = create_student(test_client)
    added_student = response.get_json()
    student_id = added_student['id']
    response = test_client.get(f'/api/v1/students/{student_id}')
    assert response.status_code == 200
    response_json = response.get_json()
    assert response_json['name'] == 'Rajesh'
    logger.info("Get student test passed")

def test_update_student(test_client):
    response = create_student(test_client, name='Jack Doe', age=30)
    student_id = response.get_json()['id']
    response = test_client.put(f'/api/v1/students/{student_id}', json={'name': 'Jack Updated', 'age': 31, 'gender': 'male'})
    assert response.status_code == 200
    logger.info("Update student test passed")

def test_delete_student(test_client):
    response = create_student(test_client, name='Jill Doe', age=27, gender='female')
    student_id = response.get_json()['id']
    response = test_client.delete(f'/api/v1/students/{student_id}')
    assert response.status_code == 204
    response = test_client.get(f'/api/v1/students/{student_id}')
    assert response.status_code == 404
    logger.info("Delete student test passed")
