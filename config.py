
class Config:
	SECRET_KEY = 'B!1weNAt1T^%KVHuI*S^'

class DevelopmentConfig(Config):
	DEBUG=True 
	MYSQL_HOST = 'localhost'
	MYSQL_USER = 'root'
	MYSQL_PORT = 3308
	MYSQL_PASSWORD = ''
	MYSQL_DB = 'personas'


config={
	'development':DevelopmentConfig
}

