from sklearn.preprocessing import MinMaxScaler

def baseline_score(df):
    """
    Simple baseline scoring for prioritization.
    """
    scaler = MinMaxScaler()
    df["priority_score"] = scaler.fit_transform(
        df[["nn_dist_m"]].fillna(0)
    )
    return df
