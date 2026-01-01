def update_metadata(item, description: str, tags: list[str]):
    item.update({
        "description": description,
        "tags": ",".join(tags)
    })
