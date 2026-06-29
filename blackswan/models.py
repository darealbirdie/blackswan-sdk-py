from dataclasses import dataclass
from typing import List, Optional
from .utils import tier_from_score


@dataclass
class CreditHistory:
    loans: List[dict]

    def to_dict(self) -> dict:
        return {"loans": self.loans}


@dataclass
class Loan:
    loan_id: int
    amount: int
    status: str
    borrowed_at: int

    @classmethod
    def from_tuple(cls, data: tuple) -> "Loan":
        return cls(
            loan_id=data[0],
            amount=data[1],
            status=data[2],
            borrowed_at=data[3]
        )


@dataclass
class CreditDashboard:
    trust_ratio: int
    current_apr: int
    borrowed_usd: int
    repaid_usd: int
    principal_repaid: int
    interest_repaid: int
    successful_loans: int
    defaults: int
    tier: int

    def to_dict(self) -> dict:
        apr = self.current_apr / 10000 if self.current_apr > 100 else self.current_apr
        return {
            "trustRatio": self.trust_ratio,
            "currentApr": apr,
            "borrowedUsd": self.borrowed_usd,
            "repaidUsd": self.repaid_usd,
            "principalRepaid": self.principal_repaid,
            "interestRepaid": self.interest_repaid,
            "successfulLoans": self.successful_loans,
            "defaults": self.defaults,
            "tier": self.tier
        }

    @property
    def trust_tier(self) -> str:
        return tier_from_score(self.trust_ratio)


@dataclass
class Reputation:
    score: int
    tier: str

    def to_dict(self) -> dict:
        return {"score": self.score, "tier": self.tier}