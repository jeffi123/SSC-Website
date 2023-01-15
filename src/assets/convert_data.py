import pandas as pd

df = pd.read_csv("indus_glyphs.csv", encoding="utf-8")
df = df.set_index("code")
df = df.infer_objects()
df = df.fillna(' ')

df["unicode_vals"] = df.apply(
    lambda x: " ".join("&#x{:X};".format(ord(i)) for i in str(x.iloc[0])), axis=1
)


df = df.replace("&#x20;", " ")
df["unicode_vals"].to_json("indus_glyphs.json")
df = df["unicode_vals"]
df1 = pd.read_csv("valid.csv")
df2 = ( 
    df1.text.str.partition("+")[2]
    .str.rpartition("+")[0]
    .str.split("-|/")
    .apply(
        lambda x: " ".join(
            df.loc[int(i)]
            if i and not i.isspace() and df.keys().isin([int(i)]).any()
            else " "
            for i in x
        )
    )
)

df2.to_json("epigraphica_glyphs.json")
