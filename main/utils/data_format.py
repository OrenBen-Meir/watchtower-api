from flask_sqlalchemy import Pagination


def pagination_to_dict(page: Pagination) -> dict:
    if page.per_page > page.total:
        per_page = page.total
    else:
        per_page = page.per_page
    return {
        'items': page.items,
        'page': page.page,
        'per_page': per_page,
        'total': page.total
    }
