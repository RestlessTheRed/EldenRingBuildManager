# EldenRingBuildManager

Using this repository, you can setup a Twitch chatbot that handles build management for the video game Elden Ring (2022).

## Setting up

To set up the bot, you need to fill in the necessary values in `config.json`. Here is how you can do it:
0. If you don't have Python installed, you can get the latest version from here: https://www.python.org/downloads/
1. (Optional) If you want the bot to use a dedicated Twitch account, create one. You will need to give this account moderator privileges in your chat. You can also you your own account for the same purposes.
2. [Request an OAuth code](https://twitchapps.com/tmi/) for the account. You will need to log in and give the app permissions to generate it for you.
3. [Register your app with Twitch dev](https://dev.twitch.tv/console/apps/create) and request a client-id (so you can interface with Twitch's API). You can choose whatever name for the app, paste ` http://localhost` in the **OAuth Redirect URLs** field and choose the category _Chat Bot_.
4. (Optional) If you want the `!builds` command to work, the bot needs to know your user id on [Emilia](https://github.com/sovietspaceship)'s website. The easiest way to see it is by clicking on the cogwheel icon in the upper-right corner. It will open Settings. The UID will be at the bottom of this page. Here's the [link](https://er-inventory.nyasu.business/settings).
5. If for whatever reason you don't want the `!builds` command to work (for instance, you don't have any public builds on the website), simply remove this entry from the `config.json` file.
5. Now, fill in the values in the `config.json`. **ACCESS_TOKEN** is the token you obtained in point 2. **CLIENT_ID** is the ID you obtained in point 3. **BOT_NICK** is the username of the bot account on Twitch (or your own). **CHANNEL** is the name of the channel where you intend to use the bot. Finally, **ER_INVENTORY_USER_ID** is the token you obtained in point 4.

Here's an example of how a complete config file might look:
```json
{
  "ACCESS_TOKEN": <...>,
  "CLIENT_ID": <...>,
  "BOT_NICK": "restless__bot",
  "BOT_PREFIX": "!",
  "CHANNEL": "restless__mind",
  "ER_INVENTORY_USER_ID": "95f3ed89-f0c4-4675-b591-722cb5e9fcdf",
  "ER_INVENTORY_AUTH_TOKEN": "22ffd4a3-34c0-4989-9ec4-d9590b2e3bb4",
  "ER_INVENTORY_API_URL": "https://er-inventory-api.nyasu.business/inventories"
}
```

Additionally, you can change the **BOT_PREFIX** value if you want. The default is `!`, which means that commands need to be prefaced with an exclamation mark to work. This is, however, a standard for Twitch so I would not recommend it.

You don't need to change the values of the **ER_INVENTORY_AUTH_TOKEN** and **ER_INVENTORY_API_URL** variables. Leave them as is.

## Running
To run the bot, simply double-click the `run.py` script. The bot is not deployed anywhere, so you need to run it on your local machine whenever you want to access it.

You can use the command `!hi` to make sure the bot is connected to your Twitch chat.

## Commands

1. `!hi`


2. `!addbuild <link to the build on Emilia's website>`


3. `!addbuildfromtext <name> <RL> <regular weapon upgrade level> <(optional) link>`

Example: `!addbuildfromtext "Overpowered build" 200 25 https://imgur.com/a/dA5ZNS4`

Notice the quotation marks around the name of the build: they are necessary when the name contains spaces. Otherwise, they're not.

4. `!removebuild <name>`


5. `!setbuild`


6. `!build`

Prints the current build, if it is set, in the following format: `Beastmaster RL200 +25/+10 https://imgur.com/a/dA5ZNS4`

The bot automatically deduces the somber weapon upgrade level based on your regular weapon upgrade level.

7. `!rl` = `!sl`


8. `!stats`

This one only works when the current build has been added via the `!addbuild` command.

9. `!builds`

Pastes a link to the Emilia's website page with all of your public builds.


## Credit
The bot has been written by Restless, your humble servant, known as [restless__mind](https://www.twitch.tv/restless__mind) on Twitch. I also have a [YouTube](https://www.youtube.com/channel/UCgl8Ce_MBxeHVEmRyZtRuew). Here you can send me a [donation](https://www.donationalerts.com/r/restless__mind) if you feel like doing so (a notification will pop up if I'm live on Twitch).

The bot is heavily integrated with [Elden Ring Build & Inventory Planner](https://er-inventory.nyasu.business/) made by the amazing Emilia aka [sovietspaceship](https://github.com/sovietspaceship) who also consulted me on its API. She [streams on Twitch](https://www.twitch.tv/sovietspaceship).

The bot uses [TwitchIO](https://github.com/PythonistaGuild/TwitchIO/tree/master), an Async Bot/API wrapper for Twitch made in Python, created by [Pythonista](https://github.com/PythonistaGuild).

## Feedback

If you find any bugs or want to request new functionality being implemented, do not hesitate to contact me on Discord (`restless__mind`) or through my Twitch.
