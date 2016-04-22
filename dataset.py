#! /usr/bin/env python3

from os import path
import sys
import csv
import re
import statistics


CSV_FILES = [
    'links.csv',
    'movies.csv',
    'ratings.csv',
    'tags.csv',
]


MOVIE_CSV_FIELDS = ['movieId', 'title', 'genres']
RATINGS_CSV_FIELDS = ['movieId', 'rating']
NO_GENRE_TEXT = '(no genres listed)'
YEAR_IN_TITLE_PATTERN = re.compile('^(.*)\s*\((\d{4})\)\s*$')


def dataset_dir_is_valid(ds_path):
    return path.exists(ds_path) and \
           path.isdir(ds_path) and \
           all([path.exists(path.join(ds_path, f)) for f in CSV_FILES])


def load_dataset(ds_path):
    if not dataset_dir_is_valid(ds_path):
            raise ValueError(
                "Given path %s is not a valid MovieLens "
                "dataset top directory" % ds_path)
    movies = {}
    with open(path.join(ds_path, 'movies.csv')) as fmovies:
        reader = csv.DictReader(fmovies)
        for row in reader:
            m = MovieItem()
            m.update_with_csv_dict_item(row)
            movies[m.id] = m
    ratings = {}
    with open(path.join(ds_path, 'ratings.csv')) as fratings:
        reader = csv.DictReader(fratings)
        for row in reader:
            mid, rating = int(row['movieId']), float(row['rating'])
            if mid not in ratings:
                ratings[mid] = [rating]
            else:
                ratings[mid].append(rating)
    for k, vs in ratings.items():
        if k in movies:
            movies[k].mean_rating = statistics.mean(vs)

    full_list = sorted(list(movies.values()), key=lambda x: x.id)
    return DataSet(full_list)


class MovieItem:
    def __init__(self):
        self.id = 0
        self.title = ''
        self.year = 0
        self.genres = []
        self.mean_rating = 0.0

    def update_with_csv_dict_item(self, item):
        if not all([field in item for field in MOVIE_CSV_FIELDS]):
            raise ValueError("Required fields missed in given csv.")
        self.id = int(item['movieId'])
        title_text = item['title']
        matcher = re.match(YEAR_IN_TITLE_PATTERN, title_text)
        if not matcher:
            self.title = title_text
        else:
            groups = matcher.groups()
            self.title = groups[0].strip()
            self.year = int(groups[1].strip())
        genres_text = item['genres']
        if genres_text != NO_GENRE_TEXT:
            self.genres = [g.lower() for g in genres_text.split('|')]

    def __repr__(self):
        return "<%d> '%s', %d, %s, %f" % (
            self.id, self.title, self.year, self.genres, self.mean_rating)

    def __str__(self):
        return self.__repr__()


class DataSet:
    def __init__(self, movies):
        self.movies = movies
        self.size = len(movies)

    def __repr__(self):
        return "<%d movies set>" % self.size

    def __str__(self):
        return self.__repr__()

    def items(self, limit=20):
        real_limit = min(limit, self.size)
        to_print = self.movies[:real_limit]
        return '\n'.join([str(item) for item in to_print])


if __name__ == '__main__':
    ds_path = sys.argv[1]
    ds = load_dataset(ds_path)
    print(ds)
