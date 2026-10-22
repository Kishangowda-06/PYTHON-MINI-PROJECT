import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("Housing.csv")

print("First 5 records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# --------------------------------------------------
# QUESTION 1
# Houses in different price ranges
# --------------------------------------------------

bins = [0, 2500000, 5000000, 7500000, 10000000, float("inf")]

labels = [
    "0-25 Lakhs",
    "26-50 Lakhs",
    "51-75 Lakhs",
    "76-100 Lakhs",
    ">100 Lakhs"
]

df["price_range"] = pd.cut(
    df["price"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

price_count = df["price_range"].value_counts().sort_index()

print("\nNumber of houses in each price range:")
print(price_count)

# Line chart
plt.figure(figsize=(9, 5))

plt.plot(
    price_count.index,
    price_count.values,
    marker="o",
    linewidth=2
)

plt.title("Number of Houses in Different Price Ranges")
plt.xlabel("Price Range")
plt.ylabel("Number of Houses")
plt.grid(True)

plt.show()


# --------------------------------------------------
# QUESTION 2
# Average house price for AC and Non-AC houses
# --------------------------------------------------

average_ac_price = df.groupby(
    "airconditioning"
)["price"].mean()

print("\nAverage price of AC and Non-AC houses:")
print(average_ac_price)

# Bar chart
plt.figure(figsize=(7, 5))

average_ac_price.plot(kind="bar")

plt.title("Average House Price: AC vs Non-AC")
plt.xlabel("Air Conditioning")
plt.ylabel("Average Price")
plt.xticks(rotation=0)

plt.show()


# --------------------------------------------------
# QUESTION 3
# Relationship between parking and house price
# --------------------------------------------------

parking_price = df.groupby("parking")["price"].mean()

print("\nAverage house price according to parking:")
print(parking_price)

# Bar chart
plt.figure(figsize=(8, 5))

parking_price.plot(kind="bar")

plt.title("Relationship Between Parking and House Price")
plt.xlabel("Number of Parking Spaces")
plt.ylabel("Average House Price")
plt.xticks(rotation=0)

plt.show()


# --------------------------------------------------
# QUESTION 4
# Price gap based on area and preferred area
# --------------------------------------------------

group1 = df[
    (df["area"] < 5000) &
    (df["prefarea"] == "no")
]

group2 = df[
    (df["area"] > 5000) &
    (df["prefarea"] == "yes")
]

average_group1 = group1["price"].mean()
average_group2 = group2["price"].mean()

price_gap = abs(average_group2 - average_group1)

print("\nAverage price: <5000 sqft and No Prefarea:")
print(average_group1)

print("\nAverage price: >5000 sqft and Prefarea:")
print(average_group2)

print("\nPrice Gap:")
print(price_gap)


# Comparison chart
groups = [
    "<5000 sqft + No Prefarea",
    ">5000 sqft + Prefarea"
]

prices = [
    average_group1,
    average_group2
]

plt.figure(figsize=(9, 5))

plt.bar(groups, prices)

plt.title("House Price Comparison")
plt.xlabel("House Category")
plt.ylabel("Average House Price")

plt.xticks(rotation=15)

plt.show()
