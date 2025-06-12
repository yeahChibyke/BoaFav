import boa 
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
import os
from eth_account import Account

load_dotenv()

GET_CONTRACT = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

def main():
    rpc = os.getenv("RPC_URL")
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)

    key = os.getenv("KEY")
    my_account = Account.from_key(key)
    boa.env.add_account(my_account, force_eoa=True)

    fav_deployer = boa.load_partial("fav.vy")
    fav_interact = fav_deployer.at(GET_CONTRACT)

    fav_interact_alice_fav_num = fav_interact.get_fav_num("Alice")
    print(f"Alice's favourite number for this particular interaction is: {fav_interact_alice_fav_num}")

if __name__ == "__main__":
    main()

