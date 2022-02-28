#/bin/sh
#git -C /home/schnellapi/ pull -q
python3 -m uvicorn carparkAPI.main:app --reload --port 8080
