import argparse

from bot.client import (
    BinanceFuturesClient
)

from bot.orders import (
    OrderManager
)

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.logging_config import (
    setup_logger
)


logger = setup_logger()


def print_response(response):

    print("\n===== ORDER RESPONSE =====")

    print(
        f"Order ID      : "
        f"{response.get('orderId')}"
    )

    print(
        f"Status        : "
        f"{response.get('status')}"
    )

    print(
        f"Executed Qty  : "
        f"{response.get('executedQty')}"
    )

    print(
        f"Avg Price     : "
        f"{response.get('avgPrice', 'N/A')}"
    )

    print("==========================\n")


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        required=True
    )

    parser.add_argument(
        "--price"
    )

    parser.add_argument(
        "--stop_price"
    )

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()

        side = validate_side(
            args.side
        )

        order_type = (
            validate_order_type(
                args.type
            )
        )

        quantity = (
            validate_quantity(
                args.quantity
            )
        )

        client = (
            BinanceFuturesClient()
            .client
        )

        balances = client.futures_account_balance()

        for asset in balances:
            if asset["asset"]=="USDT":
                print("USDT BALANCE:",asset)


        order_manager = (
            OrderManager(
                client,
                logger
            )
        )

        print(
            "\n===== ORDER REQUEST ====="
        )

        print(
            f"Symbol   : {symbol}"
        )

        print(
            f"Side     : {side}"
        )

        print(
            f"Type     : {order_type}"
        )

        print(
            f"Quantity : {quantity}"
        )

        if order_type == "MARKET":

            response = (
                order_manager
                .place_market_order(
                    symbol,
                    side,
                    quantity
                )
            )

        elif order_type == "LIMIT":

            price = validate_price(
                args.price
            )

            print(
                f"Price    : {price}"
            )

            response = (
                order_manager
                .place_limit_order(
                    symbol,
                    side,
                    quantity,
                    price
                )
            )

        elif order_type == "STOP":

            price = validate_price(
                args.price
            )

            stop_price = (
                validate_price(
                    args.stop_price
                )
            )

            print(
                f"Price      : {price}"
            )

            print(
                f"Stop Price : "
                f"{stop_price}"
            )

            response = (
                order_manager
                .place_stop_order(
                    symbol,
                    side,
                    quantity,
                    price,
                    stop_price
                )
            )

        print_response(response)

        print(
            "SUCCESS: Order placed"
        )

    except Exception as e:

        logger.error(str(e))

        print(
            f"FAILED: {e}"
        )
print("\nACCOUNT BALANCE:")


if __name__ == "__main__":
    main()