#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:
 @author: @1iu
 @contact: atliuning@gmail.com
 @date: 2019/11/1
"""

import toml
import os
import logging


class ClusterServer:

    def __init__(self, config_dict):
        self.username = ''
        self.password = ''
        self.hosts = []
        self.hostnames = []
        self.jdk_source = ''
        self.jdk_path = ''
        self.hadoop_source = ''
        self.hadoop_path = ''
        self.scala_source = ''
        self.scala_path = ''
        self.spark_source = ''
        self.spark_path = ''
        self.ntp_server = ''
        for k in config_dict:
            setattr(self, k, config_dict[k])


class SparkServer:

    def __init__(self, config_dict):
        self.master = ''
        self.port = ''
        self.spark_hosts = []
        self.spark_hostnames = []
        for k in config_dict:
            setattr(self, k, config_dict[k])


class ClusterConfig:

    def __init__(self, path):
        self.logger = logging.getLogger()
        if not os.path.exists(path):
            self.logger.error('no config in path: %s', path)
            raise FileNotFoundError
        self.config = toml.load(open(path, encoding='utf-8'))
        self.server = ClusterServer(self.config['server'])
        self.hadoop = self.config['hadoop']['hadoop_hosts']
        self.hadoop_hostname = self.config['hadoop']['hadoop_hostnames']
        self.hadoop_tmp_folder = self.config['hadoop']['tmp_folder']
        self.hadoop_data_folder = self.config['hadoop']['data_folder']
        self.hadoop_master = self.config['hadoop']['master']
        self.spark = SparkServer(self.config['spark'])


class PassPhrase:

    def __init__(self, path):
        self.logger = logging.getLogger()
        if not os.path.exists(path):
            self.logger.error('no passphrase in path: %s', path)
            raise FileNotFoundError
        config = toml.load(open(path, encoding='utf-8'))
        try:
            self.username = config['username']
            self.password = config['password']

        except KeyError as e:
            self.logger.error('Config key error: %s', e)
            raise e
