import yaml


def get_config():
    with open('config.yaml', 'r') as f:
        conf = yaml.load(f.read(), Loader=yaml.Loader)
    return conf


if __name__ == '__main__':
    config = get_config()
    ss = config['postgres']['db']
    print(ss)
