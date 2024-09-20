import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the CoinMarketCap API key from the environment variable
CMC_API_KEY = os.getenv('CMC_API_KEY')

# Function to fetch cryptocurrency data
def fetch_data(start=1, limit=10):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': start,
        'limit': limit,
        'convert': 'INR'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': CMC_API_KEY,
    }

    try:
        response = requests.get(url, params=parameters, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['data']
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return []

# Function to fetch exchange details
def fetch_exchange_details(exchange_id):
    url = 'https://pro-api.coinmarketcap.com/v1/exchange/info'
    parameters = {
        'id': exchange_id
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': CMC_API_KEY,
    }

    try:
        response = requests.get(url, params=parameters, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return {}

# Function to fetch cryptocurrency info
def fetch_crypto_info(slug):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'

    parameters = {
        'slug': slug
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': CMC_API_KEY,
    }

    try:
        response = requests.get(url, params=parameters, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return {}

# Function to get logo URL
def get_logo_url(symbol):
    logo_urls = {
        'BTC': 'https://cryptologos.cc/logos/bitcoin-btc-logo.png',
        'ETH': 'https://cryptologos.cc/logos/ethereum-eth-logo.png',
        'BNB': 'https://cryptologos.cc/logos/bnb-bnb-logo.png?v=033',
        'USDT': 'https://cryptologos.cc/logos/tether-usdt-logo.png',
        'SOL': 'https://cryptologos.cc/logos/solana-sol-logo.png',
        'USDC': 'https://cryptologos.cc/logos/usd-coin-usdc-logo.png',
        'XRP': 'https://cryptologos.cc/logos/xrp-xrp-logo.png?v=033',
        'DOGE': 'https://cryptologos.cc/logos/dogecoin-doge-logo.png',
        'TRX': 'https://cryptologos.cc/logos/tron-trx-logo.png',
        'TON': 'https://cryptologos.cc/logos/toncoin-ton-logo.png',
    }
    return logo_urls.get(symbol, 'https://via.placeholder.com/50')

# Function to display cryptocurrency data
def display_crypto_data(data):
    names = []
    symbols = []
    prices = []
    market_caps = []
    volumes = []
    supplies = []
    logos = []

    for currency in data:
        names.append(currency['name'])
        symbols.append(currency['symbol'])
        prices.append(f"₹{currency['quote']['INR']['price']:.2f}")
        market_caps.append(f"₹{currency['quote']['INR']['market_cap']:.2f}")
        volumes.append(f"₹{currency['quote']['INR']['volume_24h']:.2f}")
        supplies.append(currency['circulating_supply'])
        logos.append(get_logo_url(currency['symbol']))

    df = pd.DataFrame({
        'Name': names,
        'Symbol': symbols,
        'Price (INR)': prices,
        'Market Cap': market_caps,
        '24h Volume': volumes,
        'Circulating Supply': supplies,
        'Logo': [f'<img src="{logo}" width="50" height="50">' for logo in logos]
    })

    st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

    # Pagination controls
    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.page > 1:
            if st.button('Previous Page'):
                st.session_state.page -= 1
                st.experimental_rerun()

    with col2:
        if len(data) == st.session_state.limit:
            if st.button('Next Page'):
                st.session_state.page += 1
                st.experimental_rerun()

# Function to display exchange details
def display_exchange_details(data, exchange_id):
    exchange = data.get('data', {}).get(exchange_id, {})

    if exchange:
        name = exchange.get('name', 'N/A')
        slug = exchange.get('slug', 'N/A')
        description = exchange.get('description', 'N/A')
        logo = exchange.get('logo', 'N/A')
        website = exchange.get('urls', {}).get('website', ['N/A'])[0]
        twitter = exchange.get('urls', {}).get('twitter', ['N/A'])[0]
        fee_schedule = exchange.get('urls', {}).get('fee', ['N/A'])[0]
        chat = exchange.get('urls', {}).get('chat', ['N/A'])[0]

        st.write(f"**Name:** {name}")
        st.write(f"**Slug:** {slug}")
        st.write(f"**Description:** {description}")
        st.image(logo, width=100)
        st.write(f"**Website:** [Link]({website})")
        st.write(f"**Twitter:** [Link]({twitter})")
        st.write(f"**Fee Schedule:** [Link]({fee_schedule})")
        st.write(f"**Chat:** [Link]({chat})")
    else:
        st.write("No exchange data found.")

# Function to display cryptocurrency info
def display_crypto_info(data):
    crypto_info = data.get('data', {})

    if crypto_info:
        for slug, details in crypto_info.items():
            st.write(f"**Name:** {details.get('name', 'N/A')}")
            st.write(f"**Symbol:** {details.get('symbol', 'N/A')}")
            st.write(f"**Slug:** {details.get('slug', 'N/A')}")
            st.write(f"**Description:** {details.get('description', 'N/A')}")
            st.write(f"**Max Supply:** {details.get('max_supply', 'N/A')}")
            st.write(f"**Circulating Supply:** {details.get('circulating_supply', 'N/A')}")
            st.write(f"**Total Supply:** {details.get('total_supply', 'N/A')}")
            st.write(f"**Tags:** {', '.join(details.get('tags', []))}")
            st.write(f"**Platform:** {details.get('platform', 'N/A')}")
            st.write(f"**Date Added:** {details.get('date_added', 'N/A')}")
            st.write(f"**Last Updated:** {details.get('last_updated', 'N/A')}")
            st.write(f"**Logo URL:** {details.get('logo', 'N/A')}")
            st.image(details.get('logo', 'https://via.placeholder.com/100'), width=100)
    else:
        st.write("No cryptocurrency information found.")

# Main function
def main():
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = 1
    if 'limit' not in st.session_state:
        st.session_state.limit = 10
    if 'selected_option' not in st.session_state:
        st.session_state.selected_option = None

    st.sidebar.title("Menu")
    selected_option = st.sidebar.radio(
        "Select an option:",
        ["Home", "Cryptocurrency Data", "Exchange Details", "Crypto Info"]
    )

    st.session_state.selected_option = selected_option

    if st.session_state.selected_option == "Home":
        st.title("Welcome to the CryptoBuddies")
        st.write(" CryptoBuddies!! This tool allows you to explore various aspects of the cryptocurrency market. Use the menu on the left to navigate through different features:")

        st.write("### Cryptocurrency Data")
        st.write("Fetch and view the latest cryptocurrency data including prices, market caps, 24h volumes, and more. You can navigate through pages to see more cryptocurrencies.")

        st.write("### Exchange Details")
        st.write("Fetch and view detailed information about a specific cryptocurrency exchange by entering its ID.")

        st.write("### Crypto Info")
        st.write("Fetch and view detailed information about a specific cryptocurrency by entering its slug (e.g., bitcoin).")

    elif st.session_state.selected_option == "Cryptocurrency Data":
        st.title("Cryptocurrency Data")
        data = fetch_data(start=(st.session_state.page - 1) * st.session_state.limit + 1, limit=st.session_state.limit)
        display_crypto_data(data)

    elif st.session_state.selected_option == "Exchange Details":
        st.title("Exchange Details")
        exchange_id = st.text_input("Enter exchange ID:", "")
        if st.button("Fetch Exchange Details"):
            if exchange_id:
                data = fetch_exchange_details(exchange_id)
                display_exchange_details(data, exchange_id)
            else:
                st.write("Please enter a valid exchange ID.")

    elif st.session_state.selected_option == "Crypto Info":
        st.title("Crypto Info")
        slug = st.text_input("Enter cryptocurrency slug (e.g., bitcoin):", "")
        if st.button("Fetch Crypto Info"):
            if slug:
                data = fetch_crypto_info(slug)
                display_crypto_info(data)
            else:
                st.write("Please enter a valid cryptocurrency slug.")

if __name__ == "__main__":
    main()
