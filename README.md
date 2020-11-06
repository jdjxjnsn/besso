# BotShell

[![N|Solid](https://miroi.ml/micodev/botShell/master/images/MIRO.png?token=AEF6B4UU3ONGVXAPOKR2VDS7CMQMW)](https://t.me/anime19)

> 👏 Thanks in advance for any support you make for this project

BotShell is a pluggable telegram bot based on [telethon](https://github.com/LonamiWebs/Telethon).

- speed & fast.
- pluggable plugins (no need to restart).
- asynchronous bot.

## Installation

> The source can be installed now from `(linux,termux)`.

BotShell requires [Python3.8+](https://www.python.org/about/gettingstarted/) to run.

First thing first install the dependencies.

```sh
$ # linux (terminal)
$ sudo screen -S SoPro
$ git clone https://github.com/micodev/botShell.git && cd botShell && sudo apt install screen && sudo chmod +x bot.sh
$ bash bot.sh
$ # press ctrl+a+d
```

For termux you can use

```sh
 $ pkg install git #when using termux only
 $ git clone https://github.com/micodev/botShell.git && cd botShell && chmod +x bot.sh && bash bot.sh
``` 

```sh
 $ Insert api hash (https://my.telegram.org) : your_app_hash
 $ Insert api id : your_app_id
 $ Insert the id of main user (you id) : your_id
 $ Please enter your phone (or bot token): enter_phoneNumber_or_Token
```
When the window print the above output fill it with the required field.

To update to latest version of our source backup your store file if exist then do the command below. (run this inside `botShell` directory).

```sh
$ git reset --hard && git pull 
```

## Plugins

BotShell is currently extended with the following plugins,feel free to make some and pull request it or send to developers of this source to insert it in.

| Plugin | README |
| ------ | ------ |
| cronJob | Simple implementation of cron job.|
| getBook | Get book from [libgen](http://libgen.li/).|
| help | By sending `/help` you can get a message with all command available or its usage.|
| img2pdf | You can convert **20** of images to pdf.|
| marquee | Text that send by bot (if using cli) or from user to bot will be marquee.|
| ocr | Get text from image (arabic supported the english going to be `rtl`).|
| plugins | Show, enable,disable plugins exist in [plugins](https://github.com/micodev/botShell/tree/master/plugins) folder.|
| squareSnake | Using this plugin bot can make square message using emoji with black white square emoji.|
|tagAll| Tag all users exist in group.|
|typing| Make message like someone typing it at realtime.|
|weather| Get weather from [OpenWeather](https://openweathermap.org).|
|heartAnimation|Heart replacement animation.|
|moonAnimation|Edit message with moon phases.|
|msgCount|Get actual user's message count.**(cli only)**|
|clockAnimation|Edit message with clock emoji phases.|
|boxFlashing|Make flashing box by editing message.|
|zakhrafa|Make english zakhrfa.|
|castingAnimation|Send then cast content for a period of time.|
|tempMessage|Send msgs for a period of time.|
|photoFromName|Generate photo from name from website.|
|earthAnimation|Earth with moon and sun turn around it.|
|profileChange|Change profile info.|
|qoute|get qoutes from internet by tag.|
|tagAdmins|Tag all admins in group.|
|welcome|Show message when person joined.|
|youtube|Download from youtube (reply to youtube url).|
|shellCommand|Run your beautiful command using the bot and get output at runtime.|
|uploadMe|Upload your plugins from anywhere in bot by reply to msg.|
|update|Update the server for users that does not edit the source.|
|screenshot|Take a screenshot of a website.|
|akonet|Get net status from isp in Iraq.|
|getWallpaper|Get multi sizes wallpaper.|
|bingSearch|Get images from bing.com.|
|getFileServer|Download file from server to Telegram.|
|mutePersonal|Mute/unmute users in chat.|
|devAdded|Make someone dev at bot.|
|sysInfo|Get current system information.|
|wordDictionary|Get meaning of word with is spell and pronunciation.|
|externalYoutube[1,2,3]|Fast way downloading audio from youtube.|
|execTest|Test your python code here.|
|whois|Show information about user.|
|text2speech|Voice from text maker.|
|lyrics|Show The lyrics of a music.|
## Development

Want to contribute? Great!
Contract with us from here : [Ibrahim Ayad](https://t.me/anime19).

**Note:** this bot is still being under development so keep up with updates.

License
----

MIT (Personal use only).


**Totally free software..**
