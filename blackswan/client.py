from typing import Optional
from web3 import Web3
from .contracts import NETWORKS
from .abi import SBT_ABI, LENDING_ABI
from .models import CreditDashboard, CreditHistory, Reputation
from .utils import tier_from_score


class BlackSwanClient:
    def __init__(
        self,
        rpc_url: str,
        network: Optional[str] = None,
        sbt_address: Optional[str] = None,
        lending_address: Optional[str] = None
    ):
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.network = network
        
        if network and network in NETWORKS:
            self.sbt_address = sbt_address or NETWORKS[network]["sbt"]
            self.lending_address = lending_address or NETWORKS[network]["lending"]
        else:
            if not sbt_address or not lending_address:
                raise ValueError("Must provide either network parameter or both sbt_address and lending_address")
            self.sbt_address = sbt_address
            self.lending_address = lending_address
        
        self.sbt_contract = self.web3.eth.contract(address=self.sbt_address, abi=SBT_ABI)
        self.lending_contract = self.web3.eth.contract(address=self.lending_address, abi=LENDING_ABI)

    def get_credit_dashboard(self, wallet: str) -> CreditDashboard:
        result = self.sbt_contract.functions.getCreditDashboard(wallet).call()
        return CreditDashboard(
            trust_ratio=result[0],
            current_apr=result[1],
            borrowed_usd=result[2],
            repaid_usd=result[3],
            principal_repaid=result[4],
            interest_repaid=result[5],
            successful_loans=result[6],
            defaults=result[7],
            tier=result[8]
        )

    def get_trust_ratio(self, wallet: str) -> int:
        return self.sbt_contract.functions.getTrustRatio(wallet).call()

    def get_credit_score(self, wallet: str) -> int:
        return self.sbt_contract.functions.getTrustRatio(wallet).call()

    def get_current_apr(self, wallet: str) -> int:
        return self.sbt_contract.functions.getCurrentRisk(wallet).call()

    def get_reputation(self, wallet: str) -> Reputation:
        score = self.lending_contract.functions.getReputation(wallet).call()
        return Reputation(score=score, tier=tier_from_score(score))

    def get_credit_history(self, wallet: str) -> CreditHistory:
        result = self.sbt_contract.functions.getCreditHistory(wallet).call()
        return CreditHistory(loans=[{
            "loans_taken": result[0],
            "total_borrowed": result[1],
            "total_repaid": result[3]
        }])

    def balance_of(self, wallet: str) -> int:
        return self.sbt_contract.functions.balanceOf(wallet).call()