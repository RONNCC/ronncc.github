---
layout: post
title: Intro to Disk Drive Modeling
categories: ["Storage Systems"]
---

"An Introduction to Disk Drive Modeling"  - Ruemmler and Wilkes

Question: How good are disk drive simulation models?
Result: 
> Demonstrates and describes a calibrated, highquality disk drive model in which the overall error factor is 14 times smaller than that of a simple first order model

### Trends
- 40-60% microprocessor speedups / year 

### Modern Drive Characteristics
- State of the art in nonremovable magnetic disk drives with SCSI (small computer systems interconnect) controllers
	- Disk Drives have:
		- Mechanism: Recording components (disks / heads) and positioning components (assembly that moves heads & track following system)
		- Controller: Manages storage and retrieval of data from mechanism and performs logical address -> physical sector mappings
#### In Depth time
#####Recording:
	- Disk Sizes: 1.3-8" diameter [2.5, 3.5, 5.25 common]
	- Smaller disk = less {surface area, data}, less{ power, seek distance}, spin faster
		- As storage density increases, people prefer smaller disks
	- Increased storage density means:
		- Better Linear Recording Density : 50k bits/pinch. Determined by max rate of flux changes
		- Packing Data Tracks closer: 2.5k tracks/inch
	- Single disk has 1-12 platters spinning in lockstep
	- 3600-7200 rpm
	- Single r/w data channel that switches between heads that encodes/decodes data stream to magnetic phase changes
	- Multichannel disks are costly because of cross talk between concurrently active channels and keeping heads aligned simultaneously
#####Positioning:
	- Data stored as concentric circles (tracks)
	- Stack of tracks $k away on all platters is a cylinder
		- 3.5 inch disk ~ 2k cylinders
	- Data accessed by disk head over track
	- All disk arms are attached to same rotation pivot
	- Positioning system ensures head gets to the desired track and stays there no matter what external factors: e.g. vibrations, shocks, disk flaws
	- Seek time ~ power^2 & Arm's Stiffness (30-40g accelerations to achieve good seek times, and flexible arms can twist)
	
	pg5