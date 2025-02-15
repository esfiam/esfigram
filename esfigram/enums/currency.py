from enum import Enum


class Currency(str, Enum):
    """
    Represents currencies supported by the Telegram Bot API.
    For a detailed list of supported currencies, visit:
    https://core.telegram.org/bots/payments#supported-currencies
    """
    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ARS = "ARS"
    AUD = "AUD"
    AZN = "AZN"
    BAM = "BAM"
    BDT = "BDT"
    BGN = "BGN"
    BND = "BND"
    BOB = "BOB"
    BRL = "BRL"
    BYN = "BYN"
    CAD = "CAD"
    CHF = "CHF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    CRC = "CRC"
    CZK = "CZK"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    ETB = "ETB"
    EUR = "EUR"
    GBP = "GBP"
    GEL = "GEL"
    GTQ = "GTQ"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    ISK = "ISK"
    JMD = "JMD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KRW = "KRW"
    KZT = "KZT"
    LBP = "LBP"
    LKR = "LKR"
    MAD = "MAD"
    MDL = "MDL"
    MNT = "MNT"
    MUR = "MUR"
    MVR = "MVR"
    MXN = "MXN"
    MYR = "MYR"
    MZN = "MZN"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    PAB = "PAB"
    PEN = "PEN"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    THB = "THB"
    TJS = "TJS"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    UYU = "UYU"
    UZS = "UZS"
    VND = "VND"
    YER = "YER"
    ZAR = "ZAR"

    @classmethod
    def list_currencies(cls):
        """
        Returns a list of all available currency codes.

        Returns:
            list[str]: A list of all currency codes.
        """
        return [currency.value for currency in cls]

