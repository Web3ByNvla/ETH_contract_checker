# Ethereum address checker

A small Python script that connects to an Ethereum node through RPC, asks for an address, and checks whether it belongs to a contract. If it does, the script also retrieves the contract's balance.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install web3 python-dotenv
```

## Configuration

Create a `.env` file in the project root and add your provider's RPC URL:

```env
VAR_RPC_=https://ton-endpoint-rpc
```

Keep this URL private if it contains an API key. Git ignores the `.env` file.

## Run

```bash
python eth_contract.py
```

The script first checks that the RPC node is reachable, then asks for an address. The address must start with `0x` and contain 42 characters.
