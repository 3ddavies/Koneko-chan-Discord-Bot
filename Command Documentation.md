# COMMANDS:

# [Koneko:](#koneko-1)

## [Utility/Debug:](#utilitydebug-1)

[anako](#anako)

[arclog](#arclog)

[gab](#gab)

[getauth](#getauth)

[listtags](#listtags)

[logout](#logout)

[ostimes](#ostimes)

[restart](#restart)

[setchan](#setchan)

[ss](#ss)

[stsca](#stsca)

[time](#time)

[vomit](#vomit)


### [File Exploring:](#file-exploring-1)

[cd](#cd)

[ls](#ls)

[pwd](#pwd)


### [Other:](#other-1)

[credits](#credits)

[gif](#gif)

[image](#image)

[ppap](#ppap)

[stats](#stats)


### Deprecated:
#### climsg
#### imgdan
#### imggel
#### omgmt




## Koneko:

### Utility/Debug:

#### anako:
Usage: ```!anako```

Allows an admin to post a message as if it were [Koneko](#koneko-1). After issuing the command, if you have to correct permissions, you will get a message saying "Awaiting instruction". If you now switch to the command prompt, you will see 'Say: ' you can now type whatever you wish and upon pressing enter it will be posted from the bot's account. PLEASE NOTE: The bot cannot process other commands while in this mode so once you have finished typing, type ```/halt/``` in the command prompt to put allow [Koneko](#koneko-1) to continue processing commands.

#### arclog:
Usage: ```!arclog```

Archives the log.

#### gab:
Usage: ```!gab```

Short for 'Get allocated blocks'. Print's the result in chat.

#### getauth:
Usage: ```!getauth```

Short for 'Get author'. This exists as a test for the ```pass_context``` argument. Will print the author of the original message in chat.

#### listtags:
Usage: ```!listtags```

Lists Danbooru tags in chat.

#### logout:
Usage: ```logout```

Logs out [Koneko](#koneko-1).

#### ostimes:
Usage: ```!ostimes```

Prints the ostimes in chat. The result will be something like this:
```nt.times_result(user=3.203125, system=0.40625, children_user=0.0, children_system=0.0, elapsed=0.0)```

#### restart:
Usage: ```!restart```

Restarts both [Koneko](#koneko-1) and [Kuroka](#kuroka)

#### setchan:
Usage: ```!setchan```
Tells [Koneko](#koneko-1) that images can be posted in the channel the command is issued in. NOTE: [image](#image) will not work if this is not done first.

#### ss:
Usage: ```!ss args```

Sets the ingame status of [Koneko](#koneko-1). Example: ```!ss with fire``` will set [Koneko](#koneko)'s ingame status to 'playing with fire'


#### stsca:
Usage: ```!stsca arg```

Sets the escape argument for [anako](#anako). Example: ```!stsca /1234/``` sets the escape argument to ```/1234/```

#### time:
Usage: ```!time```

Prints the date and time in chat. the result will look somthing like this: 'The time is 11:43:27 and the date is 5/5/2018'

#### vomit:
Usage: ```!vomit```

Dumps the entire log into chat. This was created as a proof of concept. I recommend you never use this.


### File Exploring:

#### cd:
Usage: ```!cd```

Changes the [pwd](#pwd)

#### ls:
Usage: ```!ls```

Lists the contents of the [pwd](#pwd)

#### pwd:
Usage: ```!pwd```

Short for present working directory. Prints the [pwd](#pwd) in chat.


### Other:

#### credits:
Usage: ```!credits```
Prints 'Programmed by Gabe @Jupiter and Mars' in chat.

#### gif:
Usage: ```!gif```
This was a proof of concept that GIF images could be uploaded via [Koneko](#koneko-1). Posts [this gif](dancingmiku2.gif) in chat.

#### image:
Usage: ```!image```

#### ppap:
Usage: ```!ppap```

#### stats:
Usage: ```!stats```
