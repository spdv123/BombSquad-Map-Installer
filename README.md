# BombSquad Map Installer

* This project offers an easy way for BombSquad map modders to publish their works.
* _[BombSquad](http://www.froemling.net/apps/bombsquad) is a game by [Eric Froemling](http://www.froemling.net/about)_
* [中文版说明文档](README_CHS.md)

# Getting Started

1. Extract your map code from bsMap.py and save it as ```bsNewMap.py```, there's no need to modify bsMap.py ever.
The code should be something like the sample below
```python
# coding=utf-8
from bsMap import *  # Don't forget this line


class yourMapWhateverTheName(Map):
    # Your map define here
    pass


registerMap(yourMapWhateverTheName)
```

2. Put all your map files under a directory named like 'mapHello' without subdirectories, 
Files should be included:
    * ```*.bob``` Files for map models
    * ```*.cob``` Files for collide models
    * ```*Defs.py``` Python file contains your map's special points 
    * ```bsNewMap.py``` Define your map as described in 1.

3. Copy the ```installer.py``` as ```installYourMap.py``` and then your directory structure
should be like the following:
```
+ someDirectory
|
+---- installYourMap.py
|
+---- mapHello
```

4. Modify the uppercase field at the top of ```installYourMap.py```
    * ```NEW_MAP_DIRECTORY``` In this sample it shoud be 'mapHello'
    * ```NEW_MAP_NAME``` Your map name, keep it utf-8
    * ```SUPPORTED_PLATFORMS``` A list contains the platforms your map supports:
        * ```android``` Your map supports Android (has .ktx textures)
        * ```other``` Your map supports Win, Linux, Mac (has .dds textures)

5. Copy ```installYourMap.py``` and ```mapHello``` to the BombSquad modding directory,
restart your game, if everything goes well, publish it!

# Authors

* __[spdv123](https://github.com/spdv123)__

# Contributing

1. Fork the repo
2. Modify the ```installer.py```
3. Open a Pull Request

# License

```
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
```