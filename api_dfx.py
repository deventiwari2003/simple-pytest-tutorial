from numx.Dfx import Dfx
def prc_dfx():
    dct = {
        "name": ["Draco", "Ron", "Harry", "Hermione"],
        "sal": [11999, 10799, 13267, 16789],
    }
    dfx = Dfx()
    df = dfx.get_df(dct)
    df = dfx.get_df2(df)
    print(df.info())

if __name__ == "__main__":
    flag = True
    while flag:
        prc_dfx()
        strx = input("Continue (y/n) : ")
        if strx.lower() == "n":
            flag = False