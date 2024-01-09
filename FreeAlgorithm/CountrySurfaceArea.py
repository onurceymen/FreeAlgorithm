country = input("Enter the name of the country: ")
area = input("Enter the area of the country: ")
earth = 148940000

percentile = (float(area) / earth) * 100

print(f"The landmass ratio of {country} is {percentile:.2f}% of Earth's landmass.")
