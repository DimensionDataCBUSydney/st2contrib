from libcloud.loadbalancer.base import Algorithm

from lib.actions import BaseAction

__all__ = [
    'CreateVirtualListenerAction'
]


class CreateVirtualListenerAction(BaseAction):

    def run(self, region, network_domain_id, name, port, ex_description, protocol,
            pool_id, connection_limit, connection_rate_limit, source_port_preservation,
            listener_ip_address, persistence_profile_id=None, fallback_persistence_profile_id=None,
            irule_id=None):
        driver = self._get_lb_driver(region)
        driver.network_domain_id = network_domain_id
        pool = driver.ex_get_pool(pool_id)
        record = driver.ex_create_virtual_listener(network_domain_id=network_domain_id,
                                                   name=name,
                                                   ex_description=ex_description,
                                                   port=port,
                                                   pool=pool,
                                                   listener_ip_address= listener_ip_address,
                                                   persistence_profile=None,
                                                   fallback_persistence_profile=None,
                                                   irule=None,
                                                   protocol=protocol,
                                                   connection_limit=connection_limit,
                                                   connection_rate_limit=connection_rate_limit,
                                                   source_port_preservation=source_port_preservation
                                                   )

        return self.resultsets.formatter(record)
