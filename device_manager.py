
class DeviceManager(object):
    def __init__(self):
        self.devices_users_mapping = {}

    def get_all_devices(self):
        return self.devices_users_mapping

    def add_device(self, dev):
        self.devices_users_mapping[dev] = ''

    def occupy_dev(self, occ_info):
        # dev_ip = occ_info.keys()[0]
        # user = occ_info[dev_ip]
        dev_ip = occ_info[0]
        user = occ_info[1]

        for dev in self.devices_users_mapping.values() :
            if (dev == dev_ip) and (self.devices_users_mapping[dev] == ""):
                self.devices_users_mapping[dev] = user
