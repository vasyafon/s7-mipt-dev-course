import os


class Const:
    SERVICE_NAME = 'auth'
    DB_USER = os.getenv('DB_USER', 'auth')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'JIOFUJEDU32@4234')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'mipt')
    DB_SCHEMA = os.getenv('DB_SCHEMA', 'auth')
    AUTH_PUBLIC_KEY = None
    SESSION_KEY = None
