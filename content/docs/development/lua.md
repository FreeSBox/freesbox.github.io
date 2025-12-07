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

- ![(Server)](https://github.com/user-attachments/assets/d8fbe13a-6305-4e16-8698-5be874721ca1) `FSBEnterPVP(player)`
<br>
Called in `Player:PutIntoPVP()`, return false to prevent PVP.

- ![(Server)](https://github.com/user-attachments/assets/d8fbe13a-6305-4e16-8698-5be874721ca1) `FSBReadyForBuild(player)`
<br>
Called in `Player:MarkAsReadyForBuild()`, return false to prevent switching to build.

- ![(Shared)](https://github.com/user-attachments/assets/a356f942-57d7-4915-a8cc-559870a980fc) `NetIncoming(net_index, name, len, ply)`
<br>
Called before `net.Incoming` callback gets called. Returning any value other then nil will prevent the callback from being called.

- ![(Client)](https://github.com/user-attachments/assets/a5f6ba64-374d-42f0-b2f4-50e5c964e808) `FSBPlayerLeft(userid, networkid, name, reason)`
<br>
Called when a player has left.

- ![(Client)](https://github.com/user-attachments/assets/a5f6ba64-374d-42f0-b2f4-50e5c964e808) `FSBPlayerJoined(userid, networkid, name)`
<br>
Called when a player has joined.
