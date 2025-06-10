import boa 
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
import os
from eth_account import Account

load_dotenv()

def main():
    rpc = os.getenv("RPC_URL")
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)

    key = os.getenv("KEY")
    my_account = Account.from_key(key)
    boa.env.add_account(my_account, force_eoa=True)

    fav_contract = boa.load("fav.vy")

    fav_contract.add_person("Alice", 10)


if __name__ == "__main__":
    main()
