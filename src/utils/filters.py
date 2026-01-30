def sort_results(results, field):
    return sorted(
        results,
        key=lambda x: x.get(field, "")
        key=lambda x: x.get(field) or ""
    )
