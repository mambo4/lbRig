# Bungie Rigging Notes

from [Tools-Based Rigging in Bungie's Destiny](https://www.youtube.com/watch?v=U_4u0kbf-JE&list=PLUJn3SlcLb95GR-4B7Lq9m5I2j-aFd2xs&index=2&t=1752s)
GDC 2015

 ## rig system elements
 ### bone chains
 bone chains are tracked with a _bone chain markup_ system
  * name independent system for identifying joints
  * probably connected to a network node via message attributes
  * uses [Maya Joint Labeling](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2018/ENU/Maya-CharacterAnimation/files/GUID-7F9A9EC5-A67A-4493-B11B-703202FFEF97-htm.html) for Side & Region
  * uses Maya string attributes on joints
     * Start
     * End
     * Root
     * Terminator
 ### regions
 Regions are the discreet parts of a rig: Arms, Legs, Chest per Joint Lables.
 Each Region has one or more bone chains:
 
| Region   |      Bone Chains      |
|----------|-------------:|
| Neck/head |  neck |
| Arms |   arms, clavicle   |
| Fingers| index, middle, ring, pinky, thumb |
| Chest | pelvis, spine |
| Legs | leg, toe |
| prop | grip

 ### components
 components are rigs for entire systems, covering one or more regions
 
 | FKIK component |   |  
 |----------------|---|
 |side: |Left, Right |
 |region:| Arm |
 |requires:| Joint Chain (length 3)|
 |Control Flags:| FK [...],  IK, PV, Switch |
 

 | Reverse Foot |  |
 |--------------|---|
 |side: |Left, Right |
 |region:| Leg |
 |requires:| Joint Chain(3) + foot chain + ground contact points|
 |Control Flags:| FK [...],  IK, PV, Switch, Toe FK|
 |notes:| FK/IK switch with offset pivots for ground contact and toe rotation |
  
 | RFK component |   |  
 |----------------|---|
 |side: |Center |
 |region:| Spine/neck |
 |requires:| Joint Chain (3+)|
 notes: | FK Top & Bottom Rotation evenly distributed via aim constraint. Middle ctrls still individually animatable. Middle Ctrls hidden by default on the detail flags layer. |
 |Control Flags:| Top, Bottom, middle [...]|
 
 