# Wats'on the Roof
_Mitigating disasters, one roof at a time._

## Inspiration
- Natural disasters are humanity's biggest concern. They can't be prevented by any means, but they can be *mitigated*. Proper management could help reduce risks and ensure faster recovery. 

- When a disaster strucks, firefighters, police force, volunteers and rescue team converge and all come together to help people and save lives. But which areas do they focus on? Where do people or areas are affected the most? Does the data being received reliable enough?  

- We thought of an idea to make these noble efforts more coordinated, deployed faster, more scalable and cheaper. If the people could have access to data that tells them where to go, where the most damage is, where help is needed the most, then the same help can reach people faster. Our solution, Wats'on the Roof aims to do just that.

## What it does
*Wats'on the Roof* uses *IBM Watson - Image recognition API* to classify image feeds coming from drones by flying over disaster-affected regions (pre-decided short flight paths) to help identify people stranded on the roofs due to excessive floods in that area and deploy rescue teams where help is needed the most.

*Using drones*, we aimed for decreasing response times by rescue teams and saving their lives in the process. As the area is quite unstable, and dangerous. The software made could be used on any standard model drone that has a camera, hence the model being scalable as well as very accessible. 

We went a *step ahead* to solve problems that occur because of *no network coverage* or *no internet connectivity*. We hacked around this problem by reducing the flight paths and letting the drone come back to us and transfer the data back to headquarters when needed. Due to a time limit at the hackathon (HackMIT 2018) where we built this, we just evolved the logic and presented the working of the software. Hence, there is no UI as such. 

## How it works
- Drones capture images when flying on pre-set paths through disaster affected zones at low altitude.
- Transfer data over the cloud if available and reach back to base if necessary. Classify the data received using IBM Watson API for visual recognition to identify people stranded on the roofs.
- Through amateur radio APRS beacons, we locate volunteers and rescue teams to coordinate and effectively automating the allocation of resources at disaster-affected regions and save lives.
- Interpreting the data streams received by data science techniques to create heat maps. This helps to get a bigger picture and organize resources need for disaster mgmt. team.

## How we scale
- The classifer could be better developed and evolved to detect any entity on the ground and not just people on the roof. 
- Different types of drones could be used. Some that carry Cargo as in food, Water, sand to put out fires for immediate assitance and manually operated.


Note: This project was conceived, created and finished in the span of 24 hours only at HackMIT 2018, hence I find reconfiguring commit history to be a bit disturbing to that fact. Please do ignore the same.  
