# Kural Tabanlı Sınıflandırma


import pandas as pd

df = pd.read_csv("persona.csv")
df.head()
df.tail()
df.describe().T
df.size
df.ndim
df.values
df.dtypes
df.shape
df.info()
df.columns
df.isnull().values.any()



df["SOURCE"].nunique()
df["SOURCE"].value_counts()



df["PRICE"].nunique()



df["PRICE"].value_counts()



df["COUNTRY"].value_counts()



df.groupby("COUNTRY")["PRICE"].agg(sum)


df["SOURCE"].value_counts()



df.groupby("COUNTRY")["PRICE"].mean()



df.groupby("SOURCE")["PRICE"].agg("mean")


df.groupby(["COUNTRY", "SOURCE"])["PRICE"].mean()


df.groupby([col for col in df.columns[df.columns != 'PRICE']]).mean()



agg_df = df.groupby([col for col in df.columns[df.columns != 'PRICE']]).mean()
agg_df.sort_values("PRICE", ascending=False, inplace=True)
agg_df.head()



agg_df.reset_index(inplace=True)


agg_df["AGE"] = agg_df["AGE"].astype("object")
agg_df["AGE"].dtype
ranges = ["0_18", "19_23", "24_30", "31_40", "41_70"]
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], [0, 18, 23, 30, 40, 70], labels=ranges)
agg_df.head()



liste= [agg_df["COUNTRY"], agg_df["SOURCE"], agg_df["SEX"], agg_df["AGE_CAT"]]
agg_df["customer_level_based"] = [agg_df["COUNTRY"]+agg_df["SOURCE"]+agg_df["SEX"]+agg_df["AGE_CAT"] for row in agg_df.values]
agg_df
type(agg_df["AGE_CAT"])
agg_df["customer_level_based"] = [row[2].upper() + str("_") + row[0].upper() + str("_") + row[1].upper() + str("_") + row[5].upper() for row in agg_df.values]


agg_df["SEGMENT"]=pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df
agg_df.groupby("customer_level_based")["PRICE"].mean()
agg_list = ["max", "min", "sum"]
agg_df.groupby("customer_level_based")["PRICE"].agg(agg_list)
C_SEGMENT=agg_df[agg_df['SEGMENT']=="C"]
C_SEGMENT.mean()
C_SEGMENT.describe().T




