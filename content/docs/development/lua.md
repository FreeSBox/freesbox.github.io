---
weight: 1
bookFlatSection: true
title: "Lua"
---

> [!WARNING]
> **Warning**
> <br>
> This is mostly an internal API and can change at any time.

# Custom autorun

Have you ever wanted your ~~cheats~~ scripts to run automatically when you join the server?
Simply put your lua scripts into `lua/fsb/client/` or `lua/fsb/` and the server will load them.
This is called after all FSB scripts have loaded.

# Functions

- ![(Shared)](/states/shared.png) `Player:GetBalance()`
<br>
Returns the player's balance.

- ![(Shared)](/states/shared.png) `Player:IsTimingOut()`
<br>
Self explanatory.

- ![(Shared)](/states/shared.png) `Player:HasFocus()`
<br>
Basically a networked version of `system.HasFocus()`

- ![(Shared)](/states/shared.png) `Player:GetFocusLossTime()`
<br>
CurTime based timestamp of when the focus was lost. 0 if we have focus.

- ![(Shared)](/states/shared.png) `Player:IsActive()`
<br>
True if the player is not AFK. (pressing keys and has focus)

- ![(Shared)](/states/shared.png) `Player:GetLastActiveTime()`
<br>
CurTime based timestamp of the last activity from the player. 0 if we are active right now.

- ![(Shared)](/states/shared.png) `Player:InPVPMode()`
<br>
Self explanatory.

- ![(Shared)](/states/shared.png) `Player:GetOriginalName()`
<br>
Original player name from steam, unaffected by `Player:SetPlayerName`

- ![(Shared)](/states/shared.png) `Player:SetPlayerName(name, should_save = true)`
<br>
If called on the client it will always change the name of the local player.  
If `should_save` is set to false the name will not persist after rejoining the server.

- ![(Shared)](/states/shared.png) `Player:SetNameTag(name_tag, should_save = true)`
<br>
If called on the client it will always change the tag of the local player.  
If `should_save` is set to false the tag will not persist after rejoining the server.

- ![(Shared)](/states/shared.png) `Player:GetNameTag()`
<br>
Returns the tag set with `Player:SetNameTag` or the F2 menu.

- ![(Shared)](/states/shared.png) `Player:IsGhostBanned()`
<br>
Self explanatory.

- ![(Shared)](/states/shared.png) `Player:GetGhostBannedBySteamID64()`
<br>
SteamID64 of the admin that banned this player.

- ![(Shared)](/states/shared.png) `Player:GetGhostBanDescription()`
<br>
Ban description(reason).

- ![(Shared)](/states/shared.png) `Player:GetUTime()`
<br>
Playtime that doesn't count the current session.

- ![(Shared)](/states/shared.png) `Player:GetUTimeStart()`
<br>
`CurTime` at the moment of `PlayerInitialSpawn`.

- ![(Shared)](/states/shared.png) `Player:GetUTimeSessionTime()`
<br>
Playtime this session.  
Similar to `Player:TimeConnected()`

- ![(Shared)](/states/shared.png) `Player:GetUTimeTotalTime()`
<br>
Total playtime.

- ![(Shared)](/states/shared.png) `FSB.GetGlideVehicleFromSeat(seat)`
<br>
Glide vehicle if this is a seat, otherwise seat is returned.

- ![(Client)](/states/client.png) `FSB.CreateTimer(start_time, end_time, translation_label)`
<br>
Creates a progress bar on the screen that goes down as the time runs out.  
**Only 1 timer can exist at a time.**

- ![(Client)](/states/client.png) `FSB.OpenMoneySendDialog(target_ply, default_amount = 1)`
<br>
Opens the money send dialog with `target_ply` selected.

- ![(Client)](/states/client.png) `FSB.SendMoney(target, amount, send_notifications = true)`
<br>
Sends money to the target.  
`target` can be a `Player` or `SteamID64`, if it's neither of the two the money goes towards paying the national debt (you are not getting it back).

- ![(Client)](/states/client.png) `FSB.IsPetitionValid(petition_id)`
<br>
Checks if a petition with this index exists, it will return false if you don't have the petition list loaded.

- ![(Client)](/states/client.png) `FSB.GetPetition(petition_id)`
<br>
Gets a petition if it's cached, if the petition isn't cached it will request it and return nil.  
You can keep calling this until the petition is recieved.  

- ![(Client)](/states/client.png) `FSB.OpenPetition(petition_id)`
<br>
Opens the petition view window.  
The petition must be loaded when you call this function.

- ![(Server)](/states/server.png) `FSB.SetGroupBySteamID(steamid, usergroup)`
<br>
Sets the usergroup in the database.  
Made to replace the ULX system, as it doesn't account for SteamID spoofing, which is possible on FreeSBox.  
`steamid` can be a SteamID or SteamID64.

# Hooks

- ![(Server)](/states/server.png) `FSBEnterPVP(player)`
<br>
Called in `Player:PutIntoPVP()`, return false to prevent PVP.

- ![(Server)](/states/server.png) `FSBReadyForBuild(player)`
<br>
Called in `Player:MarkAsReadyForBuild()`, return false to prevent switching to build.

- ![(Shared)](/states/shared.png) `NetIncoming(net_index, name, len, ply)`
<br>
Called before `net.Incoming` callback gets called. Returning any value other then nil will prevent the callback from being called.

- ![(Client)](/states/client.png) `FSBPlayerLeft(userid, networkid, name, reason)`
<br>
Called when a player has left.

- ![(Client)](/states/client.png) `FSBPlayerJoined(userid, networkid, name)`
<br>
Called when a player has joined.

- ![(Server)](/states/server.png) `FSBUCLQuery(ply, access, hide)`
<br>
Called when ULib.ucl.query is called, return false to not allow the cmd.

- ![(Client)](/states/client.png) `FSBTimingOut(is_timing_out)`
<br>
Called when you start timing out or stop timing out.

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
The `tmp_transaction_id` argument is the same as the return of `FSB.SendMoney`.
