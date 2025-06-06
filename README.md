# Market Sentiment Tracker

A macOS application that tracks market sentiment across different markets including crypto, stocks, and economic indicators.

## Features

- Real-time cryptocurrency price and sentiment tracking (BTC, ETH)
- Stock market sentiment monitoring (S&P 500, VIX)
- Economic indicators tracking (PMI, Crypto Fear & Greed Index)
- Auto-updating data every minute
- Clean, modern interface with tabbed views

## Requirements

- Python 3.8 or higher
- macOS operating system

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd market_sentiment_tracker
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Activate the virtual environment if not already activated:
```bash
source venv/bin/activate
```

2. Run the application:
```bash
python src/main.py
```

## Data Sources

- Cryptocurrency data: Binance API
- Stock market data: Yahoo Finance
- Economic indicators: Various sources (PMI, CBBI)

## Notes

- The application updates data automatically every minute
- Some economic indicators are currently using placeholder data and would need to be connected to real data sources
- Make sure you have a stable internet connection for real-time data updates

## License

MIT License 