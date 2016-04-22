This is an interactive command-line client for filtering MovieLens dataset to find the movies meet your requirement.

## Requirement

You will need Python 3.4+ (just because I used `statistics` module which only exists after Python 3.4) to run this program.

## Usage

1. Download MovieLens CSV files and extract them to a directory.
2. Clone this repo.
3. In the root directory of this repo, run `python mlcli.py <movie_lens_csv_dir>` in your terminal. (Please replace `python` with the correct python interpreter installed on your system.)
4. An interactive shell should be started. Type the following commands
   * `quit` to exit the repl.
   * `filter <filter to apply>` to apply a filter on last filtered movies. (See 'Filters' section for details of filters)
   * `stack` to list all the filtered movies history.
   * `it` to show the current filtered movies (for now, it only print the first 20 items if there are more.)
   * `back` to step back to last filtered movies, then you can apply new filters.
   * `reset` to clear all the history, then you can apply filters on the full dataset (all movies)


## Filters

So far only a little filters are supported, they are:

* `id is <id>` get movies whose id equals to given `<id>`
* `title like <text>` get movies whose title contains given text (case-insensitive)
* `genres contains <genre>` get movies whose genres include given `<genre>`
* `year between <year1> <year2>` get movies whose publish year is between given `<year1>` and `<year2>` (inclusive)
* `year < <year>` get movies whose publish year is less than given `<year>`
* `year > <year>` get movies whose publish year is greater than given `<year>`
* `rating between <rating1> <rating2>` get movies whose mean rating is between given `<rating1>` and `<rating2>` (inclusive)
* `rating < <rating>` get movies whose mean rating is less than given `<rating>`
* `rating > <rating>` get movies whose mean rating is greater than given `<rating>`

## Notes

This is just a prove of concept, it is not optimized, and will need several minutes and quite some CPU & Memory to load the full dataset. 

