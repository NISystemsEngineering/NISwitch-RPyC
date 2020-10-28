
import sys
import clr
import rpyc
import importlib


class NISwitchService(rpyc.Service):
    exposed_clr = clr
    exposed_sys = sys
    exposed_argparse = importlib.import_module('argparse')

    # Import NI Switch modules
    exposed_NISwitch = importlib.import_module('niswitch')


# start the server
if __name__ == "__main__":
    port = 18867
    print("Starting NISwitchService on port " + str(port) + '.')
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(NISwitchService, port=port, protocol_config={
        "allow_all_attrs": True,
        "allow_setattr": True,
        "sync_request_timeout": 60,
        "allow_pickle": True
    })    
    try:
        t.start()
    except:
        pass
    t.close()
    print("NISwitchService stopped.")
