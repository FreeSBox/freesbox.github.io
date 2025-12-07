---
weight: 1
bookFlatSection: true
title: "Starfall"
---

# Functions

- ![(Shared)](https://github.com/user-attachments/assets/a356f942-57d7-4915-a8cc-559870a980fc) `Player:isBUILD()`
<br>
Checks if the player is in build mode.

- ![(Shared)](https://github.com/user-attachments/assets/a356f942-57d7-4915-a8cc-559870a980fc) `Player:isPVP()`
<br>
Checks if the player is in pvp mode.

- ![(Shared)](https://github.com/user-attachments/assets/a356f942-57d7-4915-a8cc-559870a980fc) `Player:getPVPModeEndTime()`
<br>
Gets the time when the player will leave PVP mode. <br>
Do `Player:getPVPModeEndTime()-timer.curtime()` to get time until we switch to build mode. <br>
This will return 0xFFAAAC if we won't switch to build yet.

- ![(Shared)](https://github.com/user-attachments/assets/a356f942-57d7-4915-a8cc-559870a980fc) `Player:getOriginalName()`
<br>
Returns the original name of the player.<br>
If the name is not modified the result will be the same as `Player:getName()`.

- ![(Shared)](https://github.com/user-attachments/assets/a356f942-57d7-4915-a8cc-559870a980fc) `Player:getNameTag()`
<br>
Returns the nametag of the player.<br>
Will be an empty string if the player doesn't have a nametag.
