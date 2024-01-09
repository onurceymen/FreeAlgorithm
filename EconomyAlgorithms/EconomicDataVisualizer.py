import requests
import pandas as pd
import matplotlib.pyplot as plt

class EconomicDataVisualizer:
    def __init__(self):
        self.countries = ['TR', 'US', 'DE', 'CN', 'RU', 'FR']
        self.indicators = {'unemployment_rate': 'SL.UEM.TOTL.ZS', 'gdp': 'NY.GDP.MKTP.CD'}
        self.start_year = 2010
        self.end_year = 2020
        self.df = pd.DataFrame()

    def fetch_data(self):
        for country_code in self.countries:
            data_dict = {}
            for indicator_name, indicator_code in self.indicators.items():
                url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?format=json&date={self.start_year}:{self.end_year}"
                response = requests.get(url)
                data = response.json()[1]
                for entry in data:
                    if entry['value'] is not None:
                        data_dict[entry['date']] = entry['value']

                df_country = pd.DataFrame(list(data_dict.items()), columns=['Date', country_code])
                df_country.set_index('Date', inplace=True)
                df_country = df_country.sort_index()
                self.df = pd.concat([self.df, df_country], axis=1)

    def plot_data(self):
        plt.figure(figsize=(12, 6))
        for country in self.countries:
            plt.plot(self.df.index, self.df[country], label=country)

        plt.title('10-Year Unemployment Rates (2010-2020)')
        plt.xlabel('Year')
        plt.ylabel('Unemployment Rate (%)')
        plt.legend()
        plt.show()

# Create an instance of EconomicDataVisualizer
economic_data_visualizer = EconomicDataVisualizer()

# Fetch and plot the data
economic_data_visualizer.fetch_data()
economic_data_visualizer.plot_data()
