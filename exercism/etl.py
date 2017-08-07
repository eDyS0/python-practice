def transform(etl):
    """
    `Transform` step of an Extract-Transform-Load.
    """

    d = {}
    for key in etl:
        for values in etl[key]:
            d[values.lower()] = key
    return
