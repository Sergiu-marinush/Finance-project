import yahooquery
from domain.asset.asset import Asset


class AssetFactory:
    def make_new(self, ticker: str) -> Asset:
        try:
            t = yahooquery.Ticker(ticker)
            profile = t.summary_profile[ticker]
            name = self.__extract_name(profile)
            country = profile["country"]
            sector = profile["sector"]
            return Asset(
                ticker=ticker,
                nr=0,
                name=name,
                country=country,
                sector=sector,
            )
        except KeyError as e:
            raise ValueError(f"Invalid ticker symbol: {ticker}") from e
        except Exception as e:
            raise Exception(f"An error occurred while creating asset with ticker symbol {ticker}") from e

    @staticmethod
    def __extract_name(profile: dict) -> str:
        summary = profile["longBusinessSummary"]
        words = summary.split(" ")
        first_2_words = words[0:2]
        name = " ".join(first_2_words)
        return name
