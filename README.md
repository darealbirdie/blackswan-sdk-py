# BlackSwan SDK for Python

SDK for interacting with BlackSwan Finance smart contracts.

## Installation

```bash
pip install blackswan-sdk
```

## Usage

```python
from blackswan import BlackSwanClient

# Amoy (Polygon testnet)
client = BlackSwanClient(
    network="amoy",
    rpc_url="https://polygon-amoy.g.alchemy.com/v2/your-api-key"
)

# Sepolia (Ethereum testnet)
client = BlackSwanClient(
    network="sepolia",
    rpc_url="https://eth-sepolia.g.alchemy.com/v2/your-api-key"
)

dashboard = client.get_credit_dashboard("0x...")
print(dashboard.trust_ratio)
```

## Methods

- `get_credit_dashboard(wallet)` - Returns CreditDashboard with trust_ratio, current_apr, borrowed_usd, repaid_usd, successful_loans, defaults, tier
- `get_trust_ratio(wallet)` - Returns trust score (0-10000)
- `get_current_apr(wallet)` - Returns current APR (raw value, divide by 10000 for percentage)
- `balance_of(wallet)` - Returns 1 if wallet has SBT, 0 otherwise