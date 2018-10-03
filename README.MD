# Spotted Poster
Since Facebook blocked the apps to post on page, read more [here](https://developers.facebook.com/docs/pages/).
I need to use Selenium
## Linux
### Prerequisites
```
sudo apt update
sudo apt install python
sudo apt install python-pip
pip install --user requests
pip install --user selenium
pip install --user oauth2client
pip install --user --upgrade google-api-python-client
```
* Gecko Driver for Firefox
Download the selenium Driver for firefox [here](https://github.com/mozilla/geckodriver/releases).

## Windows
### Prerequisites
 * Install [Firefox](https://www.mozilla.org/pt-BR/firefox/new/)
 * Install [Gecko Driver](https://github.com/mozilla/geckodriver/releases) for Windows
 * Extract geckodriver.zip and move the geckodriver.exe to `C:\Program Files (x86)\Gecko Driver` (probably you will need to create this folder)
 * Install [python 3.7](https://www.python.org/downloads/)

    **Note**: You must ensure that you select **Add Python 3.7 to PATH** and then select **Install Now**.

 * Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py), Since you have already installed Python, Windows will now understand that this is a Python script (.py) and will allow you to run it. Just double-click the file and let it run. A command prompt-like window will open and do its thing before closing again.
 * Open de Command Prompt and run:
     ```
     pip install --user requests
     pip install --user selenium
     pip install --user oauth2client
     pip install --user --upgrade google-api-python-client
     ```

## Configuring
### Google API
#### Create a google drive API project:
  - Use this [wizard](https://console.developers.google.com/flows/enableapi?apiid=drive) to create or select a project in the Google Developers Console and automatically turn on the API.
  - Click Continue, then Go to credentials.
  - On the Add credentials to your project page, click the Cancel button.
  - At the top of the page, select the OAuth consent screen tab. - Select an Email address, enter a Product name if not already set, and click the Save button.
  - Select the Credentials tab, click the Create credentials button and select OAuth client ID.
  - Select the application type Other, enter the name "Drive API Quickstart", and click the Create button.
  - Click OK to dismiss the resulting dialog.
  - Click the file_download (Download JSON) button to the right of the client ID.
  - Move this file to your working directory.

### Facebook Credentials
#### Set the facebook credentials:
  - Write on the file facebook_credentials.txt the email and passwort to log in (see the example file)
  ```
  <Email>
  <Password>
  ```

### Google Spreadsheet
#### Select the spreadsheet to download (see about the spreadsheet id [here](https://developers.google.com/sheets/api/guides/concepts#spreadsheet_id) :
  - Write the spreadsheet id on the file sensitive_spreadSheet_data.txt
    ```
    <Spreadsheet id>
    ```
### Download Spreadsheet
#### Download the spreadsheet file using
```
python download_spotted.py --noauth_local_webserver
```

## Usage

```
python poster.py
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


* **Matheus Horstmann** - *Initial work* - [horstmannmat](https://github.com/horstmannmat)

See also the list of [contributors](https://github.com/horstmannmat/spottedPoster/graphs/contributors) who participated in this project.

## License

This project is licensed under the GPL v3 License - see the [LICENSE.md](LICENSE) file for details
