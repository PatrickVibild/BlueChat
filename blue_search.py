import bluetooth


class BlueSearch:
    @staticmethod
    def search_device(search_time=8):
        print('Sreaching for nearby devices...')
        nearby_devices = bluetooth.discover_devices(duration=search_time, lookup_names=True,
                                                    flush_cache=True)
        print('found %d devices' % len(nearby_devices))

        pairing = []
        for addr, name in nearby_devices:
            try:
                pairing.append((addr, name))
                print(' %s - %s' % (addr, name))
            except:
                pairing.append((addr, name.encode('utf-8', 'replace')))
                print(' %s - %s' % (addr, name.encode('utf-8', 'replace')))

        return pairing