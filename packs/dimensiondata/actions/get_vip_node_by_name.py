from lib import actions

__all__ = [
    'GetVIPNodeByNameAction',
]


class GetVIPNodeByNameAction(actions.BaseAction):

    def run(self, region, node_name):
        driver = self._get_lb_driver(region)
        nodes = driver.ex_get_nodes()
        node = list(filter(lambda x: x.name == node_name,
                            nodes))[0]
        return self.resultsets.formatter(node)
