import pandas as pd
import re

############################################
# INTENT DETECTION
############################################

def detect_intent(question):

    q = question.lower()

    if any(word in q for word in ["revenue", "sales", "income"]):
        return "revenue"

    if "average order value" in q or "aov" in q:
        return "aov"

    if "delivery time" in q:
        return "delivery_time"

    if "order volume" in q or "number of orders" in q:
        return "volume"

    if "rating" in q:
        return "ratings"

    if "payment method" in q:
        return "payment"

    if "category" in q:
        return "category"

    if "expand" in q or "expansion" in q:
        return "expansion"

    return "unknown"


############################################
# DIMENSION DETECTION
############################################

def detect_dimension(question):

    q = question.lower()

    if "platform" in q:
        return "platform"

    if "city" in q:
        return "city"

    if "category" in q:
        return "category"

    return None


############################################
# FILTER DETECTION
############################################

def detect_filters(df, mapper, question):

    filters = {}

    q = question.lower()

    if "lagos" in q:
        filters[mapper["city"]] = "Lagos"

    if "mumbai" in q:
        filters[mapper["city"]] = "Mumbai"

    if "new york" in q:
        filters[mapper["city"]] = "New York"

    if "jumia" in q:
        filters[mapper["platform"]] = "Jumia"

    if "instacart" in q:
        filters[mapper["platform"]] = "Instacart"

    return filters


############################################
# APPLY FILTERS
############################################

def apply_filters(df, filters):

    for column, value in filters.items():
        df = df[df[column].str.contains(value, case=False)]

    return df


############################################
# ANALYSIS ENGINE
############################################

def run_analysis(df, mapper, intent, dimension):

    if intent == "revenue":

        metric = mapper["order_value"]

        if dimension:
            dimension = mapper[dimension]
            return df.groupby(dimension)[metric].sum()

        return df[metric].sum()

    if intent == "aov":

        metric = mapper["order_value"]

        if dimension:
            dimension = mapper[dimension]
            return df.groupby(dimension)[metric].mean()

        return df[metric].mean()

    if intent == "delivery_time":

        metric = mapper["delivery_time"]

        if dimension:
            dimension = mapper[dimension]
            return df.groupby(dimension)[metric].mean()

        return df[metric].mean()

    if intent == "volume":

        if dimension:
            dimension = mapper[dimension]
            return df.groupby(dimension).size()

        return len(df)

    if intent == "ratings":

        metric = mapper["customer_rating"]

        if dimension:
            dimension = mapper[dimension]
            return df.groupby(dimension)[metric].mean()

        return df[metric].mean()

    if intent == "category":

        dimension = mapper["category"]

        return df[dimension].value_counts()

    if intent == "payment":

        dimension = mapper["payment_method"]

        return df[dimension].value_counts()

    return None


############################################
# STRATEGIC RECOMMENDATIONS
############################################

def strategic_recommendation(df, mapper):

    volume = df.groupby(mapper["city"]).size()

    rating = df.groupby(mapper["city"])[mapper["customer_rating"]].mean()

    score = volume * rating

    best_city = score.idxmax()

    return f"""
Recommended expansion city: {best_city}

Reason:
This city shows strong order demand and high customer satisfaction,
making it the best candidate for operational expansion.
"""


############################################
# MAIN AI FUNCTION
############################################

def ask_question(df, mapper, question):

    intent = detect_intent(question)

    dimension = detect_dimension(question)

    filters = detect_filters(df, mapper, question)

    df = apply_filters(df, filters)

    if intent == "expansion":

        return strategic_recommendation(df, mapper)

    result = run_analysis(df, mapper, intent, dimension)

    return result