import json

from conftest import client, app


class TestObjectMgr:
    objects_number = 100

    def test_init_command(self, app, runner):
        with app.app_context():
            result = runner.invoke(args="init-db")
        assert "Initialized the database." in result.output

    def test_set_object_pool(self, app, client):
        data = {
            'objects_number': self.objects_number
        }
        with app.app_context():
            response = client.post('/object_mgr/set_object_pool', json=data)
        assert response.status_code == 200
        assert response.json['message'] == 'Success'

    def test_get_object(self, client, app):
        with app.app_context():
            response = client.get('/object_mgr/get_object')
        obj = json.loads(response.data)
        assert response.status_code == 200
        assert obj['value'] in [i for i in range(1, self.objects_number + 1)]

    def test_free_object(self, app, client):
        # obj_val = self.obj["value"]
        with app.app_context():
            response = client.get('/object_mgr/get_object')
            obj = json.loads(response.data)
            obj_val = obj["value"]
            response = client.post('/object_mgr/free_object/{}'.format(obj_val))

        assert response.status_code == 200
        assert response.json['message'] == 'Success'

    def test_exception_handler_wrong_object(self, app, client):
        obj_val = 1
        with app.app_context():
            response = client.post('/object_mgr/free_object/{}'.format(obj_val))
        assert response.status_code == 400
        assert 'message' in json.loads(response.data)

    def test_exception_handler_not_found_object(self, app, client):
        obj_val = self.objects_number + 100
        with app.app_context():
            response = client.post('/object_mgr/free_object/{}'.format(obj_val))
        assert response.status_code == 400
        assert 'message' in json.loads(response.data)
