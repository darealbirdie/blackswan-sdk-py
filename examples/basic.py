from blackswan import BlackSwanClient

# Replace these values with your own
rpc_url = "https://polygon-amoy.g.alchemy.com/v2/YOUR_API_KEY"
wallet = "0xYourWalletAddressHere"

client = BlackSwanClient(
    network="amoy",
    rpc_url=rpc_url
)

dashboard = client.get_credit_dashboard(wallet)

print("Credit Dashboard:")
print(f"  Trust Ratio: {dashboard.trust_ratio}")
print(f"  Trust Tier: {dashboard.trust_tier}")
print(f"  Current APR: {dashboard.current_apr / 10000}%")
print(f"  Borrowed USD: ${dashboard.borrowed_usd}")
print(f"  Repaid USD: ${dashboard.repaid_usd}")
print(f"  Successful Loans: {dashboard.successful_loans}")
print(f"  Defaults: {dashboard.defaults}")
print(f"  Tier: {dashboard.tier}")

print(f"\nTrust Score: {client.get_trust_ratio(wallet)}")
print(f"Current APR: {client.get_current_apr(wallet) / 10000}%")

balance = client.balance_of(wallet)
print(f"\nSBT Balance: {balance}")