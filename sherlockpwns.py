import utils.sys_utils as sys_utils

class SherlockPWNs():
    def __init__(self, cli=True):
        print("""\


    __ _               _            _        ___                     
    / _\ |__   ___ _ __| | ___   ___| | __   / _ \__      ___ __  ___ 
    \ \| '_ \ / _ \ '__| |/ _ \ / __| |/ /  / /_)/\ \ /\ / / '_ \/ __|
    _\ \ | | |  __/ |  | | (_) | (__|   <  / ___/  \ V  V /| | | \__ \
    \__/_| |_|\___|_|  |_|\___/ \___|_|\_\ \/       \_/\_/ |_| |_|___/



                        """)
        self.commands = {}
        self.threads = {}

    def run_cli(self):
        ip = sys_utils.get_private_ip()
        while True:
            command = input(f"sherlock_pwns {ip} > ")

    def install(self):
        pass

    def discovery(self):
        pass

