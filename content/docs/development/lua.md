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
