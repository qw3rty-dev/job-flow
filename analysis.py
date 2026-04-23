import pandas as pd

def json_to_df(data):
    return pd.read_json(data)

def skill_filter(df,skill):

    results=df[df["title"].str.contains(skill,case=False,na=False)
                | df["description"].str.contains(skill,case=False,na=False)]
    return len(results)


def top_by_column(df,column,n):
    df=df.copy()
    if column=="location":
        df["location"]=df["location"].str.split(",").str[0] 
        df["location"]=df["location"].replace("Unknown",None)
        df["location"]=df["location"].replace("remote",None)
        df["location"]=df["location"].replace("Remote",None)
    top= df[column].value_counts(dropna=True).head(n)
    for i,(name,count) in enumerate(top.items(),1):
        print(f"{i}. {truncate(name,25):<30} {count:>3}")


def insights(df):
    print(f"\n{'='*15} Insights {'='*15}\n")
    
    print(f"{f'Total jobs: {len(df)}':>40} ")
    print("-"*40)

    print("Top companies\n".center(40))
    top_by_column(df,"company",5)
    print("-"*40)


    print("Top locations\n".center(40))
    top_by_column(df,"location",5)
    print("-"*40)

    
    temp=skill_filter(df,"python")
    print(f"Python jobs: {temp} ")

    temp=skill_filter(df,"java")
    print(f"Java jobs: {temp} ")

    temp=skill_filter(df,"remote")
    print(f"Remote jobs: {temp} ")

    temp=skill_filter(df,"internship")
    print(f"Internships: {temp} ")
    print("-"*40)





