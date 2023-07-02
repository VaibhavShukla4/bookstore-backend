echo "BUILD START"
python3.11 -m pip install -r requirements.txt
apt-get update
apt-get install -y sqlite3 libsqlite3-dev
python3.11 manage.py collectstatic --noinput --clear
echo "BUILD END"
