from pyspark import SparkConf
import configparser

def get_config(env):
    config = configparser.ConfigParser()
    config.read("conf/sbdl.conf")
    conf = {}
    for (key,val) in config.items(env):
        conf[key] = val

    return conf


