from lib import actions

__all__ = [
    'DestroyPoolAction',
]


class DestroyPoolAction(actions.BaseAction):

    def run(self, region, pool_id):
        driver = self._get_lb_driver(region)
        pools = driver.ex_get_pools()
        pool = list(filter(lambda x: x.id == pool_id,
                               pools))[0]
        delete_record = driver.ex_destroy_pool(pool)
        return self.resultsets.formatter(delete_record)
