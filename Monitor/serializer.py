# -*- coding: UTF-8 -*-

import Monitor.models
from django.core.exceptions import ObjectDoesNotExist

class ClientHandler(object):
    def __init__(self, client_id):
        self.client_id = client_id
        self.client_config = {
            "services":{}
        }

    def fetch_configs(self):
        try:
            host_obj = Monitor.models.Host.objects.get(id = self.client_id)
            # 主机列表
            template_list = list(host_obj.templates.select_related())
            for host_group in host_obj.host_groups.select_related():
                template_list.extend(list(host_group.templates.select_related()))
            print(template_list)
            # 去重
            for template in template_list:
                print(template.services.select_related())

                for service in template.services.select_related():
                    self.client_config['services'][service.name] = [service.plugin_name, service.interval]

        except ObjectDoesNotExist:
            pass

        return self.client_config

def get_host_triggers(host_obj):
    #host_obj = models.Host.objects.get(id=2)
    triggers = []
    for template in host_obj.templates.select_related():
        triggers.extend(template.triggers.select_related() )
    for group in host_obj.host_groups.select_related():
        for template in group.templates.select_related():
            triggers.extend(template.triggers.select_related())


    return set(triggers)