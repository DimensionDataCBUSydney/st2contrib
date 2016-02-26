from lib import actions

__all__ = [
    'GetFirewallRuleByNameAction',
]


class GetFirewallRuleByNameAction(actions.BaseAction):

    def run(self, region, network_domain_id, rule_name):
        driver = self._get_compute_driver(region)
        network_domain = driver.ex_get_network_domain(network_domain_id)
        rules = driver.ex_list_firewall_rules(network_domain)
        rule = list(filter(lambda x: x.name == rule_name,
                               rules))[0]
        return self.resultsets.formatter(rule)
