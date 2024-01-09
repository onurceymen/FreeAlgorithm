import requests
import pandas as pd
import matplotlib.pyplot as plt

# Ülkeler ve göstergeleri belirleyelim
countries = [ 'US']
indicators = {'unemployment_rate': 'SL.UEM.TOTL.ZS', 'gdp': 'NY.GDP.MKTP.CD'}

# Veri aralığı
start_year = 2010
end_year = 2020

# Boş bir DataFrame oluşturalım
df = pd.DataFrame()

# Her ülke ve gösterge için verileri alalım
for country_code in countries:
    data_dict = {}
    for indicator_name, indicator_code in indicators.items():
        url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?format=json&date={start_year}:{end_year}"
        response = requests.get(url)
        data = response.json()[1]
        for entry in data:
            if entry['value'] is not None:
                data_dict[entry['date']] = entry['value']

    # Verileri DataFrame'e ekleyelim
    df_country = pd.DataFrame(list(data_dict.items()), columns=['Date', country_code])
    df_country.set_index('Date', inplace=True)
    df = pd.concat([df, df_country], axis=1)

# Verileri çizgi grafik olarak gösterelim
plt.figure(figsize=(12, 6))
for country in countries:
    plt.plot(df.index, df[country], label=country)

# Grafik başlığı ve eksen etiketlerini ekleyelim
plt.title('10 Yıllık İşsizlik Oranları (2010-2020)')
plt.xlabel('Yıl')
plt.ylabel('İşsizlik Oranı (%)')

# Efsaneyi ekleyelim
plt.legend()

# Grafiği gösterelim
plt.show()

import requests
import pandas as pd
import matplotlib.pyplot as plt

# Ülkeler ve göstergeleri belirleyelim
countries = ['TR', 'US', 'DE', 'CN', 'RU', 'FR']
indicators = {'unemployment_rate': 'SL.UEM.TOTL.ZS', 'gdp': 'NY.GDP.MKTP.CD'}

# Veri aralığı
start_year = 2010
end_year = 2020

# Boş bir DataFrame oluşturalım
df = pd.DataFrame()

# Her ülke ve gösterge için verileri alalım
for country_code in countries:
    data_dict = {}
    for indicator_name, indicator_code in indicators.items():
        url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?format=json&date={start_year}:{end_year}"
        response = requests.get(url)
        data = response.json()[1]
        for entry in data:
            if entry['value'] is not None:
                data_dict[entry['date']] = entry['value']

    # Verileri DataFrame'e ekleyelim
    df_country = pd.DataFrame(list(data_dict.items()), columns=['Date', country_code])
    df_country.set_index('Date', inplace=True)
    df_country = df_country.sort_index()  # Verileri doğru sırayla sıralayalım
    df = pd.concat([df, df_country], axis=1)

# Verileri çizgi grafik olarak gösterelim
plt.figure(figsize=(12, 6))
for country in countries:
    plt.plot(df.index, df[country], label=country)

# Grafik başlığı ve eksen etiketlerini ekleyelim
plt.title('10 Yıllık İşsizlik Oranları (2010-2020)')
plt.xlabel('Yıl')
plt.ylabel('İşsizlik Oranı (%)')

# Efsaneyi ekleyelim
plt.legend()

# Grafiği gösterelim
plt.show()
