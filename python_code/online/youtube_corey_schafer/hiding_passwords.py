import os

# ds_user = 'my_db_user'
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')

print(db_user)
print(db_password)

