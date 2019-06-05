# APP
FLASK_ENV = 'development'
DEBUG = True

# JWT
SECRET_KEY = '7PXsHcHGfa4e3kEs8Rvcv8ymjI0UeauX'
JWT_LEEWAY = 604800

# DB
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/jalan/lingkblog_test.db'
DATABASE = 'sqlite:////Users/jalan/lingkblog_test.db'