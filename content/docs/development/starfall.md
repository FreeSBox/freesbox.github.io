---
weight: 1
bookFlatSection: true
title: "Starfall"
---

# Functions

- ![(Shared)](/states/shared.png) `Player:isBUILD()`
<br>
Checks if the player is in build mode.

- ![(Shared)](/states/shared.png) `Player:isPVP()`
<br>
Checks if the player is in pvp mode.

- ![(Shared)](/states/shared.png) `Player:getPVPModeEndTime()`
<br>
Gets the time when the player will leave PVP mode. <br>
Do `Player:getPVPModeEndTime()-timer.curtime()` to get time until we switch to build mode. <br>
This will return 0xFFAAAC if we won't switch to build yet.

- ![(Shared)](/states/shared.png) `Player:getOriginalName()`
<br>
Returns the original name of the player.<br>
If the name is not modified the result will be the same as `Player:getName()`.

- ![(Shared)](/states/shared.png) `Player:getNameTag()`
<br>
Returns the nametag of the player.<br>
Will be an empty string if the player doesn't have a nametag.
