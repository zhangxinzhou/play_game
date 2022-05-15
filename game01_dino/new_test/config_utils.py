import configparser

# 实例化configParser对象
config = configparser.ConfigParser()
# 读取ini文件
config.read('config.ini')


def get_config_str(section: str, option: str):
    return config.get(section, option)


def get_config_int(section: str, option: str):
    return config.getint(section, option)


def get_config_float(section: str, option: str):
    return config.getfloat(section, option)


def get_config_bool(section: str, option: str):
    return config.getboolean(section, option)


if __name__ == '__main__':
    val = get_config_str('postgres', 'db')
    print(val)
    print(type(val))
