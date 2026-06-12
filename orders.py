from binance.exceptions import (
    BinanceAPIException
)


class OrderManager:

    def __init__(self, client, logger):

        self.client = client
        self.logger = logger

    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):

        try:

            self.logger.info(
                f"MARKET ORDER | "
                f"{side} {symbol} "
                f"Qty={quantity}"
            )

            response = (
                self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )
            )

            self.logger.info(response)

            return response

        except BinanceAPIException as e:

            self.logger.error(str(e))
            raise

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        try:

            self.logger.info(
                f"LIMIT ORDER | "
                f"{side} {symbol} "
                f"Qty={quantity} "
                f"Price={price}"
            )

            response = (
                self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )
            )

            self.logger.info(response)

            return response

        except BinanceAPIException as e:

            self.logger.error(str(e))
            raise

    def place_stop_order(
        self,
        symbol,
        side,
        quantity,
        price,
        stop_price
    ):

        try:

            self.logger.info(
                f"STOP ORDER | "
                f"{side} {symbol} "
                f"Qty={quantity} "
                f"Price={price} "
                f"Stop={stop_price}"
            )

            response = (
                self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="STOP",
                    quantity=quantity,
                    price=price,
                    stopPrice=stop_price,
                    timeInForce="GTC"
                )
            )

            self.logger.info(response)

            return response

        except BinanceAPIException as e:

            self.logger.error(str(e))
            raise