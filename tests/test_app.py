# tests/test_app.py
import unittest
import os
os.environ["TESTING"] = "true"

# Import the app directly instead of create_app
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        print("HTML CONTENT:\n", html) 
        assert "<title>MLH Fellow</title>" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert json["timeline_posts"] == []

    # TODO: Add more GET/POST route tests
    def test_malformed_timeline_post(self):
        # POST request with no content
        response = self.client.post("/api/timeline_post", data={
            "name": "Bruce",
            "email": "bw23@example.com",
            
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with no name
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": ""
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={
            "name": "Hal Jordan",
            "email": "thisisnotanemail",
            "content": "This is my email!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

    def test_timeline_post(self):
        # Valid POST
        response = self.client.post("/api/timeline_post", data={
            "name": "Clark Kent",
            "email": "ck45@example.com",
            "content": "Hello from CK!"
        })
        assert response.status_code == 200
        json = response.get_json()
        assert json["name"] == "Clark Kent"
        assert json["email"] == "ck45@example.com"
        assert json["content"] == "Hello from CK!"

        # GET to check it was added
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        data = response.get_json()
        assert len(data["timeline_posts"]) == 1
        assert data["timeline_posts"][0]["name"] == "Clark Kent"

if __name__ == '__main__':
    unittest.main()