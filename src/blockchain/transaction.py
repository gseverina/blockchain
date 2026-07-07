from dataclasses import dataclass
from decimal import Decimal

from blockchain.wallet import Wallet


@dataclass(frozen=True)
class Transaction:
    """Transferencia simple de valor entre dos wallets. Inmutable."""

    sender: Wallet
    recipient: Wallet
    amount: Decimal

    def __post_init__(self) -> None:
        if not isinstance(self.sender, Wallet):
            raise TypeError(f"sender debe ser Wallet, se recibió {type(self.sender).__name__}")
        if not isinstance(self.recipient, Wallet):
            raise TypeError(f"recipient debe ser Wallet, se recibió {type(self.recipient).__name__}")
        if self.sender == self.recipient:
            raise ValueError("sender y recipient no pueden ser la misma wallet")
        if self.amount <= 0:
            raise ValueError("amount debe ser positivo")
