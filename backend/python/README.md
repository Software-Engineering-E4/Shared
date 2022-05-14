# Reddit and YouTube submodules

## Usage

In order to use your own data for the APIs:

- Reddit:
  - Create your own client id (personal use script) and secret key at [https://www.reddit.com/prefs/apps/](https://www.reddit.com/prefs/apps/)
  - Modify the `"authentication"` category in the [reddit.json](../config/reddit.json) file
- YouTube:
  - Create your own API key at [https://console.cloud.google.com/apis/library/youtube.googleapis.com](https://console.cloud.google.com/apis/library/youtube.googleapis.com)
  - Modify the `"authentication"` property in the [youtube.json](../config/youtube.json) file

The `"tables"` property should be an array of table names that contain a map of the columns in the database. The values do not necessarily need to be in the same order as in the database, however their names must be the same. Inner properties format:

- `"type"` should have one of the following values: `"string"`, `"number"` or `"date"`
- `"translate"` should be a boolean value, if set to `true`, that field will the translated and its value will be inserted in a `*column*_translated` column. Note: translations greatly increase running time, only translate what is absolutely necessary
- `"actualName"` specifies the name of the item from the response (it is recommended that the names from the response coincide with the columns in the database)

## Requirements

Quick linux install at [python_dependencies.sh](../../python_dependencies.sh).

Languages:

- python `3.10.0 64bit`

Libraries:

- mysql `8.0.28`

    ```bash
    pip install mysql-connector-python
    ```

- google api client `2.42.0`

    ```bash
    pip install google-api-python-client
    ```

- levenshtein `0.18.1`

    ```bash
    pip install Levenshtein
    ```

- translator `5.1.1`

    ```bash
    pip install translators
    ```
