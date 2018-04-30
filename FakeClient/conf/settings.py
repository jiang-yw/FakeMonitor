# -*- coding: UTF-8 -*-

configs = {
    'HostID': 1,
    'Server': "localhost",
    'ServerPort': '8000',
    'urls': {
        'get_configs': ['api/client/config','get'],
        'service_report': ['api/client/service/report/','post'],
    },
    'RequestTimeout': 30,
    'ConfigUpdateInterval': 300, #300s
}