# COMMANDS:

# [Koneko:](#koneko-1)

## [Utility/Debug:](#utilitydebug-2)

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


### [Other:](#other-2)

[credits](#credits)

[gif](#gif)

[image](#image)

[ping](#ping)

[ppap](#ppap)

[stats](#stats)


### [Deprecated:](#deprecated-1)

[climsg](#climsg)

[imgdan](#imgdan)

[imggel](#imggel)

[omgmt](#omgmt)


# [Kuroka:](#kuroka-1)

## [Utility/Debug:](#utilitydebug-3)

[vci](#vci)


### [Other:](#other-3)

[dice](#dice)


### [Music:](#music-1)

[join](#join)

[leave](#leave)

[pause](#pause)

[play](#play)

[stop](#stop)

[resume](#resume)




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
Usage: ```!image x Tags, tags, tags, etc.```

Grabs x images from Danbooru with specified tags where x is the number of images to grab and posts them in chat. You will first need to use the [setchan](#setchan) command in the channel you are trying to post images in before [Koneko](#koneko-1) will post images to it. Example: ```!image 5 hero``` will return 5 images with the tag 'hero'. You can have as many tags as you like but there is a limit of 100 images per request so if you need more just issue the command multiple times.

#### ping:
Usage: ```!ping```

Prints '🏓 Pong!' in chat.

#### ppap:
Usage: ```!ppap```

Prints 'Just for you, Gil: https://www.youtube.com/watch?v=0E00Zuayv9Q' in chat.

#### stats:
Usage: ```!stats```

Prints [Koenko](#koneko-1)'s stats in chat. The result will look somthing like this: 'I'm currently enjoying the privilege of being connected to 8 servers and I'm currently serving 172 lovely users! 😘'


### Deprecated:

#### climsg:
Usage: ```!climsg```

An older and lesser version of [anako](#anako).

#### imgdan:
Usage: ```!imgdan```

This and [imggel](#imggel) are both primitive precursors to [image](#image). How this command works is it generates a random interger from 1 to 3000000 and appends it to 'http://danbooru.donmai.us/posts/'.

#### imggel:
Usage: ```!imggel```

This and [imgdan](#imgdan) are both primitive precursors to [image](#image). How this command works is it generates a random interger from 1 to 4079175 and appends it to 'https://gelbooru.com/index.php?page=post&s=view&id='.

#### omgmt:
Usage: ```!omgmt```

Stands for once more get message test. Omgmt is a test in getting the id of a message [Koneko](#koneko-1) sent and then deleting her own message.



## Kuroka:

### Utility/Debug:

#### vci:
Usage: ```-vci```

Short for voice channel info. Returns info about the voice channel you are in so you must be in a voice channel in order for this to work. [Kuroka](#kuroka-1) will return somthing like this: '@Jupiter and Mars is connected to voice channel Test id: 440307901542957057'


### Other:

#### dice:
Usage: ```-dice x y```

Rolls x dice with y sides and posts [this gif](dice.gif). Example: ```-dice 5 6``` will roll five six-sided dice. The gif is posted first then the result looks somthing like this: 'You rolled 5 d6s. They landed on: \[5, 3, 5, 2, 3\] for a total of 18'


### Music:
The music command is a bit different then the other commands. It has six subcommands, the names of which are below:

#### join:
Usage: ```-music join```

Makes [Kuroka](#kuroka-1) join the voice channel you are currently connected to. This means you must be in a voice channel for this to work. PLEASE NOTE: If [Kuroka](#kuroka-1) is already in a voice channel, please use [leave](#leave) first as switching between voice channels is not yet supported.

#### leave:
Usage: ```-music leave```

Makes [Kuroka](#kuroka-1) leave the voice channel she is currently connected to.

### pause:
Usage: ```-music pause```

Pauses what is currently being played. The difference between this and [stop](#stop) is that if you use [pause](#pause) you can use [resume](#resume) to resume playing where as [stop](#stop) can't be resumed.
