# Thread Plotter

Plots the sentiment of comments through the duration of a Reddit thread. Ideally used for sporting match threads.

(in progress)

## Usage

<!-- TODO -->

## Example

| ![qualy](https://user-images.githubusercontent.com/33743349/159139553-7fe8c60f-70c5-41c9-8b37-e1effd3bd5c9.png) |
| :-------------------------------------------------------------------------------------------------------------: |
|                                 _Formula 1 Qualifying Session for Bahrain 2022_                                 |

<sub>\*Added annotations separately</sub>

## Installation

Python 3.10+ is required to run this application.

To install the required dependencies:

```shell script
pipenv install
```

Praw will need several keys/tokens which can be generated [here](https://ssl.reddit.com/prefs/apps/):

```env
APP_ID = id
APP_SECRET = secret
USER_AGENT = app name
```

### Dependencies

-   [Requests](https://docs.python-requests.org/en/latest/) - Create the connection to a thread
-   [Praw](https://github.com/praw-dev/praw) - Parse comments
-   [TextBlob](https://github.com/sloria/TextBlob) - Get comment sentiment
-   [Pandas](https://github.com/pandas-dev/pandas) - Store comment information in a DataFrame
-   [Bokeh](https://github.com/bokeh/bokeh) - Create the plot
