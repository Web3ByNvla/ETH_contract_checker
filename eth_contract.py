import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

rpc_end_point = os.getenv("VAR_RPC_")
if rpc_end_point is None:
	raise RuntimeError("RPC_KEY_MISSING, check your .env file")
web3 = Web3(Web3.HTTPProvider(rpc_end_point))
if not(web3.is_connected()) :
	raise RuntimeError("Please Connect your RPC end point ")
else : 
	print("RPC connected !")
print("-------------")

def check_is_address_valid(address : str) -> bool:
    len_address = len(address)
    if(len_address != 42):
        return(False)
    if(address[0 : 2] != "0x"):
        return(False)
    return(True)

def is_contract(address: str) -> bool :
    code = web3.eth.get_code(address)
    if len(code) > 0 :
        return True
    else :
        return False
    
def show_contract(address_contract):
    if not(is_contract(address_contract)):
        print("This is not a contract address")
        print("-------------")

    else :
        print("This is a contract address")
        print("-------------")
        print(f"Address balance is : {web3.eth.get_balance(address_contract)} eth")

def main():
    get_address = input("Enter your address : ").strip()
    if not(check_is_address_valid(get_address)):
        raise RuntimeError("Invalid address format")
    get_address = web3.to_checksum_address(get_address)
    show_contract(get_address)

if __name__ == "__main__":
    main()