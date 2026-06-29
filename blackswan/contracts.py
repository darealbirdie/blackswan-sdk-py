from typing import Dict, Any

NETWORKS: Dict[str, Dict[str, Any]] = {
    "amoy": {
        "chain_id": 80002,
        "sbt": "0x6665e5E15Ee295d9de05C6D57c629F33653687D7",
        "lending": "0x7E04C0a283d372537E547086D37642776199C1DC",
    },
    "sepolia": {
        "chain_id": 11155111,
        "sbt": "0xf8D2F43227Ea25a7fD0B34E1b74FF6FF2722879F",
        "lending": "0x20D2E08E283FF4052B2B02A3475dda1B320cD26f",
    },
    "mainnet": {
        "chain_id": 137,
        "sbt": "0x0000000000000000000000000000000000000000",
        "lending": "0x0000000000000000000000000000000000000000",
    }
}