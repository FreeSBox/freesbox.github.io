---
weight: 1
bookFlatSection: true
title: "Starfall"
---

# Functions

- ![(Shared)](/states/shared.png) `fsb.getMSPT()`
<br>
Returns an average of how many milliseconds it took too process the last few ticks.

- ![(Shared)](/states/shared.png) `fsb.getTPS()`
<br>
Returns the current server TPS calculated from MSPT.

- ![(Shared)](/states/shared.png) `Player:isBUILD()`
<br>
Checks if the player is in build mode.

- ![(Shared)](/states/shared.png) `Player:isPVP()`
<br>
Checks if the player is in pvp mode.

- ![(Shared)](/states/shared.png) `Player:isGhostBanned()`
<br>
Checks if the player is ghostbanned.

- ![(Shared)](/states/shared.png) `Player:getGhostBannedBySteamID64()`
<br>
Returns the steamid64 of the admin that ghostbanned this player.

- ![(Shared)](/states/shared.png) `Player:getGhostBanDescription()`
<br>
Returns the reason for the ghostban.

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

- ![(Shared)](/states/shared.png) `Player:getTotalPlaytime()`
<br>
Returns the total amount of time the player has played on the server.<br>
Convert this to hours with `UNIT.GMOD_TIME`.

- ![(Shared)](/states/shared.png) `Player:getSessionPlaytime()`
<br>
Returns the time played on the server this session. Similar to `Player:getTimeConnnected()`.<br>
Convert this to hours with `UNIT.GMOD_TIME`.

- ![(Shared)](/states/shared.png) `Player:getBeforeSessionPlaytime()`
<br>
Returns playtime that doesn't count the current session.<br>
Convert this to hours with `UNIT.GMOD_TIME`.

- ![(Shared)](/states/shared.png) `Player:getBalance()`
<br>
Returns the player's balance.

# Hooks

- ![(Server)](/states/server.png) `FSBPlayerChangeName(player, old_name, new_name, persistent)`
<br>
Called when a player changes their name through FSB's custom name feature.
The `persistent` argument means that the new name will save after re-logging.

- ![(Server)](/states/server.png) `FSBPlayerChangeNameTag(player, old_name, new_name, persistent)`
<br>
Called when a player changes their name tag.
The `persistent` argument means that the new tag will save after re-logging.

- ![(Client)](/states/client.png) `FSBTransactionReceive(source, transaction_id, amount)`
<br>
Called when our client receives a transaction.  
The `source` argument contains the owner account, it is usually the player's steamid64 or the MONEY_SERVER_MONEYPRINTER account.

- ![(Client)](/states/client.png) `FSBTransactionAck(tmp_transaction_id, transaction_id, success)`
<br>
Called after we sent a transaction using `FSB.SendMoney`.
The `tmp_transaction_id` argument is the same as the return of `FSB.SendMoney` in Lua.
