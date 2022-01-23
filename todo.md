## Todo

Create a simple _discord bot_ with [discord.py](https://discordpy.readthedocs.io/en/stable/) with these features:

- `!scbot` as the prefix
- Contains *4 commands*
  - `myprofile` - the bot will `send username`, `user's nickname`, `user's profile`, and `user's roles`
  - `coin` - will randomly answer `head` or `tail`
  - `info` - will give out the information about the bot
    - `bot's uptime` - how long the bot been up
    - `bot's repo` - github repo link
  - `hi` - will say `hello` or `hallo` randomly
- Put any **sensitive information** about the bot inside `.env` using [dotenv](https://pypi.org/project/python-dotenv/)

### Future Development

- Displaying `bot status` as: **dnd** or **Do Not Distrub**
- Displaying `bot activity` as: **Watching !scbothelp**
- Logging any command related message to: `#logs` channel or something similar
- Add *4 new commands*
  - `setting` - the bot will show overall default setting
  - `set <value>` - to changes any related setting value
  - `delete <number>` - the bot will delete *n-number* of messages
  - `whoami` - alias for `myprofile` command
- Add ability for the bot to log any message that contain `sccukim`
- Setup proper permission on certain `admin` related commands