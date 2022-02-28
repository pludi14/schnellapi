#/bin/sh
git -C /home/schnellapi/ pull -q
python3 -m uvicorn main:app --reload --port 8080
