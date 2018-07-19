import configparser

config=configparser.ConfigParser()
config.read('config.ini') #a.cfg a.ini a.cnf

# print(config.sections())
# print(config.options('egon'))
# print(config.items('egon'))


# res=config.get('egon','age')
# res=config.getint('egon','age')
# print(res,type(res))

# res=config.getfloat('egon','salary')
# print(res,type(res))

# res=config.getboolean('egon','is_beautiful')
# print(res,type(res))