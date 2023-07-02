echo "BUILD START"
python3 -m pip install -r requirements.txt
python3 -m pip install pysqlite3
python3 manage.py collectstatic --noinput --clear
echo "BUILD END"
