import yaml

with open('config.yaml', 'r') as f:
    conf = yaml.load(f.read(), Loader=yaml.Loader)
    print(conf)

print(conf['postgres']['db'])
