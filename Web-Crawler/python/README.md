# Reddit and YouTube submodules

## Usage

There are two main ways to use these APIs:

- Use the data provided by us (mock accounts, volatile)
- Replace the data with your own

In order to use your own data:

- Reddit:
  - Create your own client id (personal use script) and secret key at [https://www.reddit.com/prefs/apps/](https://www.reddit.com/prefs/apps/)
  - Modify the `"authentication"` category in the [reddit.json](config/reddit.json) file
- YouTube:
  - Create your own API key at [https://console.cloud.google.com/apis/library/youtube.googleapis.com](https://console.cloud.google.com/apis/library/youtube.googleapis.com)
  - Modify the `"api_key"` property in the [youtube.json](config/youtube.json) file

The `"db_columns"` property should be an array of strings that represent the columns in the database. The values must be in the same order, and even if some are unused in this module, they must not be omitted

## Requirements

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
