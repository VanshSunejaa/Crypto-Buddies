# CryptoBuddies

CryptoBuddies is a cryptocurrency dashboard built using **Streamlit**, which allows users to explore the latest cryptocurrency data, get exchange details, and retrieve information about specific cryptocurrencies. The app fetches data from the **CoinMarketCap API** and displays it in a user-friendly interface, including logos, prices, market caps, 24-hour volumes, and more.

## Features

- **Cryptocurrency Data:** 
  - View the latest cryptocurrency listings, including prices in INR, market capitalization, 24-hour volumes, and circulating supply.
  - Navigate through pages of cryptocurrencies to explore more data.
  
- **Exchange Details:**
  - Fetch detailed information about cryptocurrency exchanges using an exchange ID, such as their description, website, Twitter, chat links, and more.
  
- **Cryptocurrency Info:**
  - Retrieve specific information about a cryptocurrency using its **slug** (e.g., `bitcoin`, `ethereum`). Displays details like name, symbol, supply data, and platform.

## Project Structure

```
CryptoBuddies/
│
├── main.py               # Main Streamlit app script
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

### Code Structure

1. **fetch_data()**: Fetches the latest cryptocurrency data from CoinMarketCap API.
2. **fetch_exchange_details()**: Retrieves exchange information using an exchange ID.
3. **fetch_crypto_info()**: Fetches detailed information about a specific cryptocurrency by its slug.
4. **display_crypto_data()**: Displays fetched cryptocurrency data in a paginated table with logos.
5. **display_exchange_details()**: Displays exchange details fetched from the API.
6. **display_crypto_info()**: Shows detailed information about a specific cryptocurrency.
7. **Main function**: Defines navigation between the Home, Cryptocurrency Data, Exchange Details, and Crypto Info sections using Streamlit sidebar options.

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: Framework used to create the interactive web application.
- **CoinMarketCap API**: Provides cryptocurrency data and exchange details.
- **Pandas**: For data manipulation and presentation.
- **Requests**: For making API calls.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository-url
   cd CryptoBuddies
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your CoinMarketCap API key:
   ```
   API_KEY=your_api_key_here
   ```

4. Run the app:
   ```bash
   streamlit run main.py
   ```

5. Navigate to the provided URL (usually http://localhost:8501) in your browser.

## Example Screenshots

1. **Cryptocurrency Data:**
   ![CryptoData]

2. **Exchange Details:**
   

3. **Crypto Info:**
   

## Key Learnings

While building this project, I learned about:
- **API Integration**: Fetching data from external APIs and handling responses.
- **Streamlit Framework**: Creating interactive dashboards using Python.
- **Pandas DataFrames**: Structuring and displaying data in a user-friendly table format.
- **Exception Handling**: Handling errors while interacting with external APIs.

## To-Do List

- Implement pagination for all sections.
- Add more cryptocurrency and exchange filtering options.
- Improve the UI/UX with better styling and layouts.

## Disclaimer

This project, **CryptoBuddies**, is built solely for **learning and educational purposes**. It is not intended for real-world financial or investment decisions. All data and information provided are sourced from external APIs, and accuracy may vary. Use it at your own risk.

---
