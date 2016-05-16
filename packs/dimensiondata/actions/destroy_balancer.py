from lib import actions

__all__ = [
    'DestroyBalancerAction',
]


class DestroyBalancerAction(actions.BaseAction):

    def run(self, region, balancer_id):
        driver = self._get_lb_driver(region)
        balancers = driver.list_balancers()
        balancer = list(filter(lambda x: x.id == balancer_id,
                               balancers))[0]
        delete_record = driver.destroy_balancer(balancer)
        return self.resultsets.formatter(delete_record)
