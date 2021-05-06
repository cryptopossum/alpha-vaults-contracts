from brownie import accounts, PassiveRebalanceVault


POOL = "0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8"  # USDC / ETH

BASE_THRESHOLD = 1800
LIMIT_THRESHOLD = 600
MAX_TWAP_DEVIATION = 100
TWAP_DURATION = 1
REBALANCE_COOLDOWN = 23 * 60 * 60
MAX_TOTAL_SUPPLY = 1e18


def main():
    deployer = accounts.load("deployer")

    vault = deployer.deploy(
        PassiveRebalanceVault,
        POOL,
        BASE_THRESHOLD,
        LIMIT_THRESHOLD,
        MAX_TWAP_DEVIATION,
        TWAP_DURATION,
        REBALANCE_COOLDOWN,
        MAX_TOTAL_SUPPLY,
        publish_source=False
    )
    print(f"Vault address: {vault.address}")
