from lib import actions

__all__ = [
    'GetPoolByNameAction',
]


class GetPoolByNameAction(actions.BaseAction):

    def run(self, region, pool_name):
        driver = self._get_lb_driver(region)
        pools = driver.get_pools()
        pool = list(filter(lambda x: x.name == pool_name,
                            pools))[0]
        return self.resultsets.formatter(pool)
