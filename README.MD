# Spotted Poster
Since Facebook blocked the apps to post on page, read more [here](https://developers.facebook.com/docs/pages/).
I found a workaround, post on twitter and make twitter post on facebook.

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

### Running
0) Create a google drive API project:
  - Use this [wizard](https://console.developers.google.com/flows/enableapi?apiid=drive) to create or select a project in the Google Developers Console and automatically turn on the API.
  - Click Continue, then Go to credentials.
  - On the Add credentials to your project page, click the Cancel button.
  - At the top of the page, select the OAuth consent screen tab. - Select an Email address, enter a Product name if not already set, and click the Save button.
  - Select the Credentials tab, click the Create credentials button and select OAuth client ID.
  - Select the application type Other, enter the name "Drive API Quickstart", and click the Create button.
  - Click OK to dismiss the resulting dialog.
  - Click the file_download (Download JSON) button to the right of the client ID.
  - Move this file to your working directory.

1) Set the facebook credentials:
  - Write on the file facebook_credentials.txt the email and passwort to log in (see the example file)
  ```
  <Email>
  <Password>
  ```

2) Select the spreadsheet to download:
  - Write the spreadsheet id on the file sensitive_spreadSheet_data.txt
    ```
    <Spreadsheet id>
    ```

3) Download the spreadsheet file using
```
python download_spotted.py --noauth_local_webserver
```
4) Download the selenium driver [here](https://github.com/mozilla/geckodriver/releases). (we are using the Firefox driver)

5) Run the poster:
```
python poster.py
```


* **Matheus Horstmann** - *Initial work* - [horstmannmat](https://github.com/horstmannmat)

See also the list of [contributors](https://github.com/horstmannmat/spottedPoster/graphs/contributors) who participated in this project.

## License

This project is licensed under the GPL v3 License - see the [LICENSE.md](LICENSE) file for details
