import os
from web3 import Web3
from dotenv import load_dotenv
load_dotenv()

rpc_end_point = os.getenv("VAR_RPC_")
if rpc_end_point is None:
	raise RuntimeError("RPC_KEY_MISSING, check your .env file")
web3 = Web3(Web3.HTTPProvider(rpc_end_point))
if (web3.is_connected() == 0) :
	print("Please Connect your RPC end point ")
else : 
	print("RPC connected !")
print("-------------")

def is_contract(address: str) -> bool :
    addr = web3.to_checksum_address(address)
    code = web3.eth.get_code(addr)
    if len(code) > 0 :
        return(True)
    else :
        return(False)

def show_contract(address_contract, is__contract):
    if(address_contract == False):
        print("This is not a contract address")
        print("-------------")

    else :
        print("this is a contract address")
        print("-------------")
        print(f"Address balance is : {web3.eth.get_balance(address_contract)} eth")
        
get_address = input("enter your address : ")
show_contract(get_address, is_contract(get_address))