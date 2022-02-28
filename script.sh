#/bin/sh
git -C /home/schnellapi/ pull -q
uvicorn /home/schnellapi/carparkAPI.main:app --reload --port 8080
