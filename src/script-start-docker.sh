docker kill $(docker ps -qf expose=8585) || docker build -t ecointet/api-python . && docker run -p 8585:8585 -d -e PORT=8585 ecointet/api-python