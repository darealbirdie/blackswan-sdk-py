SBT_ABI = [
    {
        "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
        "name": "getTrustRatio",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "wallet", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
        "name": "getCreditDashboard",
        "outputs": [
            {"internalType": "uint256", "name": "trustRatio", "type": "uint256"},
            {"internalType": "uint256", "name": "currentApr", "type": "uint256"},
            {"internalType": "uint256", "name": "totalBorrowedUsd", "type": "uint256"},
            {"internalType": "uint256", "name": "totalRepaidUsd", "type": "uint256"},
            {"internalType": "uint256", "name": "principalRepaidUsd", "type": "uint256"},
            {"internalType": "uint256", "name": "interestRepaidUsd", "type": "uint256"},
            {"internalType": "uint256", "name": "successfulLoans", "type": "uint256"},
            {"internalType": "uint256", "name": "defaults", "type": "uint256"},
            {"internalType": "uint8", "name": "tier", "type": "uint8"}
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
        "name": "getCurrentRisk",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
        "name": "getTrustTier",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
        "name": "getCreditHistory",
        "outputs": [
            {"internalType": "uint256", "name": "loansTaken", "type": "uint256"},
            {"internalType": "uint256", "name": "totalBorrowed", "type": "uint256"},
            {"internalType": "uint256", "name": "_unused", "type": "uint256"},
            {"internalType": "uint256", "name": "totalRepaid", "type": "uint256"},
            {"internalType": "uint256", "name": "_unused2", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

LENDING_ABI = [
    {
        "inputs": [{"internalType": "address", "name": "wallet", "type": "address"}],
        "name": "getReputation",
        "outputs": [{"internalType": "uint256", "name": "score", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
]