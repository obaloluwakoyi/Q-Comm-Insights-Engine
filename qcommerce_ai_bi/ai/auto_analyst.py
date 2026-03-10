import pandas as pd

############################################
# METRIC CALCULATIONS
############################################

def calculate_metrics(df, mapper):

    metrics = {}

    metrics["total_revenue"] = df[mapper["order_value"]].sum()

    metrics["average_order_value"] = df[mapper["order_value"]].mean()

    metrics["total_orders"] = len(df)

    metrics["average_delivery_time"] = df[mapper["delivery_time"]].mean()

    metrics["average_rating"] = df[mapper["customer_rating"]].mean()

    return metrics


############################################
# TOP PERFORMERS
############################################

def top_platforms(df, mapper):

    return df.groupby(mapper["platform"])[mapper["order_value"]].sum().sort_values(ascending=False)


def top_cities(df, mapper):

    return df.groupby(mapper["city"]).size().sort_values(ascending=False)


def top_categories(df, mapper):

    return df[mapper["category"]].value_counts()


############################################
# STRATEGIC INSIGHTS
############################################

def generate_insights(metrics, platforms, cities):

    insights = []

    top_platform = platforms.idxmax()
    top_city = cities.idxmax()

    insights.append(
        f"The leading platform by revenue is {top_platform}."
    )

    insights.append(
        f"The city with the highest order volume is {top_city}."
    )

    if metrics["average_delivery_time"] > 30:

        insights.append(
            "Delivery time is relatively high, suggesting logistics optimization opportunities."
        )

    if metrics["average_rating"] < 4:

        insights.append(
            "Customer satisfaction is below ideal levels and should be monitored."
        )

    return insights


############################################
# EXPANSION RECOMMENDATION
############################################

def expansion_recommendation(df, mapper):

    volume = df.groupby(mapper["city"]).size()

    rating = df.groupby(mapper["city"])[mapper["customer_rating"]].mean()

    score = volume * rating

    best_city = score.idxmax()

    return f"Recommended expansion city: {best_city}"


############################################
# MAIN AUTO ANALYST
############################################

def auto_analyze(df, mapper):

    report = {}

    metrics = calculate_metrics(df, mapper)

    platforms = top_platforms(df, mapper)

    cities = top_cities(df, mapper)

    categories = top_categories(df, mapper)

    insights = generate_insights(metrics, platforms, cities)

    recommendation = expansion_recommendation(df, mapper)

    report["metrics"] = metrics
    report["platforms"] = platforms
    report["cities"] = cities
    report["categories"] = categories
    report["insights"] = insights
    report["recommendation"] = recommendation

    return report