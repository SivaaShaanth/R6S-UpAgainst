OUTPUT="$(ls $PATHTOSS | tail -n 1 )"
FINAL="$PATHTOSS/$OUTPUT"
KEY="AIzaSyAGFIGVwz7Nlkr6ZTPpSwIvYyEsQKzz6kM"
python cloudvisreq.py "$KEY" "$FINAL"
python r6db-req.py
