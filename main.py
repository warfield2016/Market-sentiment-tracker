import sys
import yfinance as yf
import ccxt
import pandas as pd
from datetime import datetime, timedelta
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QLabel, QPushButton, QComboBox,
                            QTabWidget, QGridLayout)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont

class MarketSentimentTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Market Sentiment Tracker")
        self.setGeometry(100, 100, 1200, 800)
        
        # Initialize exchange for crypto data
        self.exchange = ccxt.binance()
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Create tab widget
        tabs = QTabWidget()
        layout.addWidget(tabs)
        
        # Create different market tabs
        self.crypto_tab = QWidget()
        self.stock_tab = QWidget()
        self.economic_tab = QWidget()
        
        tabs.addTab(self.crypto_tab, "Crypto Market")
        tabs.addTab(self.stock_tab, "Stock Market")
        tabs.addTab(self.economic_tab, "Economic Indicators")
        
        # Setup each tab
        self.setup_crypto_tab()
        self.setup_stock_tab()
        self.setup_economic_tab()
        
        # Setup refresh timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_all_data)
        self.timer.start(60000)  # Update every minute
        
        # Initial data load
        self.update_all_data()
    
    def setup_crypto_tab(self):
        layout = QGridLayout(self.crypto_tab)
        
        # Create labels for crypto data
        self.btc_price = QLabel("BTC Price: Loading...")
        self.eth_price = QLabel("ETH Price: Loading...")
        self.btc_sentiment = QLabel("BTC Sentiment: Loading...")
        self.eth_sentiment = QLabel("ETH Sentiment: Loading...")
        
        # Add labels to layout
        layout.addWidget(QLabel("Bitcoin"), 0, 0)
        layout.addWidget(self.btc_price, 0, 1)
        layout.addWidget(self.btc_sentiment, 0, 2)
        layout.addWidget(QLabel("Ethereum"), 1, 0)
        layout.addWidget(self.eth_price, 1, 1)
        layout.addWidget(self.eth_sentiment, 1, 2)
    
    def setup_stock_tab(self):
        layout = QGridLayout(self.stock_tab)
        
        # Create labels for stock data
        self.spy_price = QLabel("S&P 500: Loading...")
        self.vix_price = QLabel("VIX: Loading...")
        self.spy_sentiment = QLabel("S&P 500 Sentiment: Loading...")
        
        # Add labels to layout
        layout.addWidget(QLabel("S&P 500"), 0, 0)
        layout.addWidget(self.spy_price, 0, 1)
        layout.addWidget(self.spy_sentiment, 0, 2)
        layout.addWidget(QLabel("VIX"), 1, 0)
        layout.addWidget(self.vix_price, 1, 1)
    
    def setup_economic_tab(self):
        layout = QGridLayout(self.economic_tab)
        
        # Create labels for economic indicators
        self.pmi_label = QLabel("PMI: Loading...")
        self.cbbi_label = QLabel("CBBI: Loading...")
        
        # Add labels to layout
        layout.addWidget(QLabel("Purchasing Managers' Index"), 0, 0)
        layout.addWidget(self.pmi_label, 0, 1)
        layout.addWidget(QLabel("Crypto Fear & Greed Index"), 1, 0)
        layout.addWidget(self.cbbi_label, 1, 1)
    
    def update_all_data(self):
        self.update_crypto_data()
        self.update_stock_data()
        self.update_economic_data()
    
    def update_crypto_data(self):
        try:
            # Get BTC and ETH prices
            btc_ticker = self.exchange.fetch_ticker('BTC/USDT')
            eth_ticker = self.exchange.fetch_ticker('ETH/USDT')
            
            self.btc_price.setText(f"BTC Price: ${btc_ticker['last']:,.2f}")
            self.eth_price.setText(f"ETH Price: ${eth_ticker['last']:,.2f}")
            
            # Calculate simple sentiment based on 24h change
            btc_change = btc_ticker['percentage']
            eth_change = eth_ticker['percentage']
            
            self.btc_sentiment.setText(f"BTC Sentiment: {'Bullish' if btc_change > 0 else 'Bearish'} ({btc_change:.2f}%)")
            self.eth_sentiment.setText(f"ETH Sentiment: {'Bullish' if eth_change > 0 else 'Bearish'} ({eth_change:.2f}%)")
        except Exception as e:
            print(f"Error updating crypto data: {e}")
    
    def update_stock_data(self):
        try:
            # Get S&P 500 and VIX data
            spy = yf.Ticker("^GSPC")
            vix = yf.Ticker("^VIX")
            
            spy_data = spy.history(period="1d")
            vix_data = vix.history(period="1d")
            
            if not spy_data.empty and not vix_data.empty:
                spy_price = spy_data['Close'].iloc[-1]
                vix_price = vix_data['Close'].iloc[-1]
                
                self.spy_price.setText(f"S&P 500: ${spy_price:,.2f}")
                self.vix_price.setText(f"VIX: {vix_price:.2f}")
                
                # Simple sentiment based on VIX
                if vix_price < 15:
                    sentiment = "Very Bullish"
                elif vix_price < 20:
                    sentiment = "Bullish"
                elif vix_price < 30:
                    sentiment = "Neutral"
                elif vix_price < 40:
                    sentiment = "Bearish"
                else:
                    sentiment = "Very Bearish"
                
                self.spy_sentiment.setText(f"S&P 500 Sentiment: {sentiment}")
        except Exception as e:
            print(f"Error updating stock data: {e}")
    
    def update_economic_data(self):
        try:
            # For PMI, we would typically use an API, but for demo purposes:
            self.pmi_label.setText("PMI: 50.2 (Expansion)")
            self.cbbi_label.setText("CBBI: 65 (Greed)")
        except Exception as e:
            print(f"Error updating economic data: {e}")

def main():
    app = QApplication(sys.argv)
    window = MarketSentimentTracker()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 