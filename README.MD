# Facebook Page Poster
Since Facebook blocked the apps to post on page, read more [here](https://developers.facebook.com/docs/pages/).
I need to use Selenium
## Linux
### Prerequisites

* Gecko Driver for Firefox
Download the selenium Driver for firefox [here](https://github.com/mozilla/geckodriver/releases).

## Windows
### Prerequisites
 * Install [Firefox](https://www.mozilla.org/pt-BR/firefox/new/)
 * Install [Gecko Driver](https://github.com/mozilla/geckodriver/releases) for Windows
 * Extract geckodriver.zip and move the geckodriver.exe to `C:\Program Files (x86)\Gecko Driver` (probably you will need to create this folder)

### Facebook Credentials
#### Set the facebook credentials:
  - Write on the file credentials.txt the email and password to log in (see the example file)
  ```
  <Email>
  <Password>
  ```
## Usage

```
import FacebookPagePoster

poster = FacebookPagePoster()
poster.page_url = 'https://m.facebook.com/PAGE_URL/'
poster.email = 'YOUR_EMAIL'
poster.password = 'YOUR_PASSWORD'
poster.firing_up_driver()
poster.sign_in()
poster.post("YOUR MESSAGE")
poster.delete("POST_ID")
```
or you can use setup
```
import FacebookPagePoster

poster = FacebookPagePoster()

poster.setup('PAGE_ID','YOUR_EMAIL','YOUR_PASSWORD')
poster.post("YOUR MESSAGE")
poster.delete("POST_ID")

```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


* **Matheus Horstmann** - *Initial work* - [horstmannmat](https://github.com/horstmannmat)

See also the list of [contributors](https://github.com/horstmannmat/spottedPoster/graphs/contributors) who participated in this project.

## License

This project is licensed under the GPL v3 License - see the [LICENSE.md](LICENSE) file for details
