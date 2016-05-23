from lib.actions import BaseAction

__all__ = [
    'CreatePoolAction'
]


class CreatePoolAction(BaseAction):

    def run(self, region, network_domain_id, name, balancer_method, ex_description, health_monitors,
            service_down_action, slow_ramp_time):
        driver = self._get_lb_driver(region)
        driver.network_domain_id = network_domain_id
        health_monitors_list = driver.ex_get_default_health_monitors(network_domain_id)
        monitors = list()
        for monitor in health_monitors.split(","):
            for available_monitor in health_monitors_list:
                if available_monitor.name.lower() == ("ccdefault." + monitor.lower().strip()):
                    monitors.append(available_monitor)
        record = driver.ex_create_pool(network_domain_id = network_domain_id,
                                       name = name,
                                       balancer_method = balancer_method,
                                       ex_description = ex_description,
                                       health_monitors=monitors,
                                       service_down_action=service_down_action,
                                       slow_ramp_time=slow_ramp_time
                                      )
        return self.resultsets.formatter(record)
