#/bin/sh
#git -C /home/schnellapi/ pull -q
python3.10 -m uvicorn carparkAPI.main:app --reload --port 8080 --host 0.0.0.0
