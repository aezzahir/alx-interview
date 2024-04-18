### 0x01. Lockboxes
- Algorithm
- Python
© By aezzahir


*** You need to know if you can access all of the boxes, ie, can you get all of the keys?

Box zero starts unlocked, so you have access to the keys in box zero. If box zero has keys for box 1, 4, and 6, then you can open all those boxes and get the keys in those boxes too.

So, essentially you are collecting a group of keys from the boxes you have keys for. After you can no longer collect more keys, are all the boxes opened? The stopping point is either you have opened all the boxes and thus there are no more keys to collect (True) or there is no more boxes you can open with the keys you have (False)

Do note that the use of keys in the problem statement is referring to literal keys, not a programming term. The keys in this case are just box indicies that you can open.