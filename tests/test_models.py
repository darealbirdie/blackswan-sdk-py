import pytest
from blackswan.models import CreditDashboard, CreditHistory, Reputation, Loan
from blackswan.utils import tier_from_score


class TestCreditDashboard:
    def test_to_dict(self):
        dashboard = CreditDashboard(
            trust_ratio=7700,
            current_apr=14200,
            borrowed_usd=99,
            repaid_usd=99,
            principal_repaid=99,
            interest_repaid=0,
            successful_loans=1,
            defaults=0,
            tier=0
        )
        result = dashboard.to_dict()
        assert result["trustRatio"] == 7700
        assert result["currentApr"] == 1.42
        assert result["borrowedUsd"] == 99
        assert result["successfulLoans"] == 1

    def test_trust_tier_property(self):
        dashboard = CreditDashboard(
            trust_ratio=7700,
            current_apr=14200,
            borrowed_usd=99,
            repaid_usd=99,
            principal_repaid=99,
            interest_repaid=0,
            successful_loans=1,
            defaults=0,
            tier=0
        )
        assert dashboard.trust_tier == "C"

        dashboard_high = CreditDashboard(
            trust_ratio=9500,
            current_apr=14200,
            borrowed_usd=99,
            repaid_usd=99,
            principal_repaid=99,
            interest_repaid=0,
            successful_loans=1,
            defaults=0,
            tier=0
        )
        assert dashboard_high.trust_tier == "A"


class TestReputation:
    def test_to_dict(self):
        rep = Reputation(score=8500, tier="B")
        result = rep.to_dict()
        assert result["score"] == 8500
        assert result["tier"] == "B"


class TestLoan:
    def test_from_tuple(self):
        loan = Loan.from_tuple((1, 1000, "active", 1234567890))
        assert loan.loan_id == 1
        assert loan.amount == 1000
        assert loan.status == "active"
        assert loan.borrowed_at == 1234567890


class TestTierFromScore:
    def test_score_a(self):
        assert tier_from_score(9000) == "A"
        assert tier_from_score(9500) == "A"

    def test_score_b(self):
        assert tier_from_score(8000) == "B"
        assert tier_from_score(8500) == "B"

    def test_score_c(self):
        assert tier_from_score(7000) == "C"
        assert tier_from_score(7500) == "C"

    def test_score_d(self):
        assert tier_from_score(6000) == "D"
        assert tier_from_score(6500) == "D"

    def test_score_e(self):
        assert tier_from_score(5000) == "E"
        assert tier_from_score(0) == "E"