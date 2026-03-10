def expansion_recommendation(df, mapper):

    volume = df.groupby(mapper["city"]).size()

    rating = df.groupby(mapper["city"])[mapper["customer_rating"]].mean()

    score = volume * rating

    best_city = score.idxmax()

    return f"""
Recommended expansion city: {best_city}

Reason:
High order demand combined with strong
customer satisfaction indicates strong
market potential.
"""