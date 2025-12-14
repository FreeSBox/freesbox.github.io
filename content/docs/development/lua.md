---
weight: 1
bookFlatSection: true
title: "Lua"
---

> [!WARNING]
> **Warning**
> <br>
> This is mostly an internal API and can change at any time.

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
