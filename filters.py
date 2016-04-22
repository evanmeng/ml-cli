#! /usr/bin/env python3

FD_ID = 'id'
FD_YEAR = 'year'
FD_TITLE = 'title'
FD_GENRES = 'genres'
FD_RATING = 'rating'

VB_LIKE = 'like'
VB_CONTAINS = 'contains'
VB_IS = 'is'
VB_BTWN = 'between'
VB_LT = '<'
VB_GT = '>'


def ff_id_is(args):
    id = int(args[0])
    return (lambda i: i.id == id)


def ff_title_like(args):
    text = args[0]
    return (lambda i: text.lower() in i.title.lower())


def ff_year_is(args):
    year = int(args[0])
    return (lambda i: i.year == year)


def ff_year_btwn(args):
    y1 = int(args[0])
    y2 = int(args[1])
    return (lambda i: i.year >= y1 and i.year <= y2)


def ff_year_lt(args):
    y = int(args[0])
    return (lambda i: i.year < y)


def ff_year_gt(args):
    y = int(args[0])
    return (lambda i: i.year > y)


def ff_genres_contains(*args):
    g = args[0].lower()
    return (lambda i: g in i.genres)


def ff_rating_btwn(args):
    r1 = float(args[0])
    r2 = float(args[1])
    return (lambda i: i.mean_rating >= r1 and
            i.mean_rating <= r2)


def ff_rating_lt(*args):
    print("args: %s" % args)
    r = float(args[0])
    return (lambda i: i.mean_rating < r)


def ff_rating_gt(args):
    r = float(args[0])
    return (lambda i: i.mean_rating > r)


FILTER_FUNC_GENERATORS = {
    (FD_ID, VB_IS): ff_id_is,
    (FD_TITLE, VB_LIKE): ff_title_like,
    (FD_YEAR, VB_IS): ff_year_is,
    (FD_YEAR, VB_BTWN): ff_year_btwn,
    (FD_YEAR, VB_LT): ff_year_lt,
    (FD_YEAR, VB_GT): ff_year_gt,
    (FD_GENRES, VB_CONTAINS): ff_genres_contains,
    (FD_RATING, VB_BTWN): ff_rating_btwn,
    (FD_RATING, VB_LT): ff_rating_lt,
    (FD_RATING, VB_GT): ff_rating_gt,
}


def create_filter_func(field, verb, args):
    k = (field, verb)
    if k not in FILTER_FUNC_GENERATORS:
        raise ValueError("filter '%s %s' cannot be recognized"
                         % (field, verb))
    return FILTER_FUNC_GENERATORS[k](args)
