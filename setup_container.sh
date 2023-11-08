docker pull postgres:15
docker pull python:3.10
docker-compose up --build -d
sleep 5s
docker exec flask_server flask init-db
