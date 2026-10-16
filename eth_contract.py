import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()
RPC_END_POINT = os.getenv("VAR_RPC_")
get_address = None

if RPC_END_POINT is None:
	raise RuntimeError("RPC_KEY_MISSING, check your .env file")
web3 = Web3(Web3.HTTPProvider(RPC_END_POINT))
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
    
def calculate_eth(balance) :
    balance = balance / 1000000000000000000
    return balance

def show_contract(address_contract, url):
    if not(is_contract(address_contract)):
        print("This is not a contract address")
        print("This is an EOA Address")
        print(f"Address balance is : {calculate_eth(web3.eth.get_balance(address_contract))} eth")
        print(f"\033]8;;{url}\033\\{address_contract}\033]8;;\033\\")   
        print("-------------")

    else :
        print("This is a contract address")
        print("-------------")
        print(f"Address balance is : {web3.eth.get_balance(address_contract)} eth")
        print(f"\033]8;;{url}\033\\{address_contract}\033]8;;\033\\")   


def main(get_address: str):
    while(1) :
        get_address = input("Enter your address : ").strip()
        if(get_address == "exit"):
                    raise SystemExit("Thanks for using our address tracker !!\nCoded by NVLA team ;)")
        if(check_is_address_valid(get_address)):
            get_address = web3.to_checksum_address(get_address)
            url = f"https://sepolia.etherscan.io/address/{get_address}"
            show_contract(get_address, url)
            
if __name__ == "__main__":
    main(get_address)
