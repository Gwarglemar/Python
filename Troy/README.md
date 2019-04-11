# Troy

Currently in the initial planning stages, this will be a full Character Management Tool for Dungeons & Dragons. 

## Why?

Something I've wanted to do for a long time (and started once for a UI/UX class in university) is build my own Dungeons & Dragons Character Management Tool. D&D is a favourite hobby of mine, which is why I've chosen this as a project for my free-time: I have extensive knowledge of the requirements, use-cases, context, etc, and have a personal interest in the material which will keep me engaged and working on this more than I might otherwise. 

There are currently many of these out there; my goal is to make it my own without investigating too deeply how they've implemented the tools, and to further expand on one major issue I have with most of the free versions of this: you can only access materials from the OGL SRD. I hope to make an interface to make things smoother and simpler, but include a depth of customization for those who want it. In addition to being able to add your own custom home-brew(custom) content, it will be easy to share what you've created as "modules" with others! 

## How?

Well, I'm still working on that. I have some rough plans in my head which I've started to put down on paper, and as I solidify things I'll be transfering them to documents and tools and posting them here. 

It will be a Python/Django web-app. Probably a PostgreSQL DB, but I need to model the data in more detail before making a firm decision on that. Most likely hosted on AWS as I don't expect to outgrow the free tier anytime soon. 

## Roadmap!

The development plan I'm using is similar to that if a client approached me with an idea they want built that I can later convert into a SaaS solution: 
* Initially build the project specifically to manage my character Troy, while ensuring OOP practices and code reusability / genericness.
  * At this point, all customization will be done manually in the back-end, editing the files directly.
  * While in this state, build many of the features (potential features listed below) until it feels ready to be used by other people.
* Build in the Character creation options / level up options.
  * These are the basic functions to allow someone to pick from available modules and options to create a character.
  * At this point, custom content still needs to be hard-coded to be used, but other users will be able to use the system for basic characters.
  * Development up until now will have been done on localhost; I will implement a simple account-management system before setting up hosting and allowing other users access to the system.
* Add customization options so that users can build their own Character Classes/abilities/etc.
* Add export/import option for custom content a user creates.
  * This requires some module management interface and system. 
  * Current plan is that "Export" just provides a specific Module ID as well as direct-link with hash. 
  * The Import feature can take a specific Module ID (which will probably be a GUID) or the user can follow the direct-link with the hash to land on a page that imports the module for them.
* Up to this point it has been free-to-use with a Donation link somewhere on the site. 
  * When we reach a point that I feel the features are full enough, add some basic ads to the site, with an option for users to pay to disable(one-time or subscription?)
* Continue support while building out additional features. Run user surveys / collect feedback to determine features most-wanted by community (biggest value-add for the app)
