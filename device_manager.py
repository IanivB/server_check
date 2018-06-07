
class DeviceManager(object):
    def __init__(self):
        self.devices_users_mapping = []

    def get_all_devices(self):
        return self.devices_users_mapping

    def add_device(self, dev):
        # self.devices_users_mapping[dev] = ''
        self.devices_users_mapping.append(dev)

    def occupy_dev(self, occ_info):
        dev_ip = occ_info["ip"]
        user = occ_info["user"]

        for dev in self.devices_users_mapping:
            if (dev['ip'] == dev_ip) and (dev['user'] == ""):
                dev['user'] = user
