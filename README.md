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

- `get_credit_dashboard(wallet)` - Returns CreditDashboard with all credit metrics: `trust_ratio`, `current_apr`, `borrowed_usd`, `repaid_usd`, `successful_loans`, `defaults`, `tier`
- `get_trust_ratio(wallet)` - Returns trust score (0-10000)
- `get_current_apr(wallet)` - Returns current APR (raw value, divide by 10000 for percentage)
- `balance_of(wallet)` - Returns 1 if wallet has SBT, 0 otherwise

### CreditDashboard Properties

| Property | Type | Description |
|----------|------|-------------|
| `trust_ratio` | int | Trust score (0-10000) |
| `current_apr` | int | Current APR in basis points (divide by 10000 for percentage) |
| `borrowed_usd` | int | Total USD borrowed |
| `repaid_usd` | int | Total USD repaid |
| `successful_loans` | int | Number of successful loans |
| `defaults` | int | Number of defaults |
| `tier` | int | User tier (0-4) |

### Example Usage

```python
from blackswan import BlackSwanClient

client = BlackSwanClient(
    network="amoy",
    rpc_url="https://polygon-amoy.g.alchemy.com/v2/your-api-key"
)

wallet = "0x..."

dashboard = client.get_credit_dashboard(wallet)
print(f"Trust: {dashboard.trust_ratio} ({dashboard.trust_tier})")
print(f"APR: {dashboard.current_apr / 10000}%")
print(f"Loans: {dashboard.successful_loans} successful, {dashboard.defaults} defaults")
```

### Sample Output

```
Credit Dashboard:
  Trust Ratio: 7700
  Trust Tier: C
  Current APR: 0.0142%
  Borrowed USD: $99
  Repaid USD: $99
  Successful Loans: 1
  Defaults: 0
  Tier: 0
```