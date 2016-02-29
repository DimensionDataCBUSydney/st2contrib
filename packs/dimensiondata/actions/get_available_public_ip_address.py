from lib import actions
import netaddr

__all__ = [
    'GetAvailablePublicIPAddressAction',
]


class GetAvailablePublicIPAddressAction(actions.BaseAction):

    def run(self, region, network_domain_id):
        computedriver = self._get_compute_driver(region)        
        network_domain = computedriver.ex_get_network_domain(network_domain_id)
        publicIpBlocks = computedriver.ex_list_public_ip_blocks(network_domain)
        natRules =  computedriver.ex_list_nat_rules(network_domain)
        lbdriver = self._get_lb_driver(region)        
        balancers = lbdriver.list_balancers()
        availableIPAddress = []
        for ipBlock in publicIpBlocks:                        
            ipaddress1 = ipBlock.base_ip
            ipaddress2 = str(netaddr.IPAddress(int(netaddr.IPAddress(ipaddress1
                                                                     ))+1))
            ipaddress = [ipaddress1,ipaddress2]
            for ip in ipaddress:
                if (len(list(filter(lambda x: x.ip == ip, balancers))) == 0 &
                    len(list(filter(lambda x: x.external_ip == ip, natRules))) 
                    == 0):
                    availableIPAddress.append(ip)                  
        return availableIPAddress
