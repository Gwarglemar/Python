# Troy

Currently in the initial planning stages, this will be a full Character Management Tool for Dungeons & Dragons. 

## Why?

Something I've wanted to do for a long time (and started once for a UI/UX class in university) is build my own Dungeons & Dragons Character Management Tool. D&D is a favourite hobby of mine, which is why I've chosen this as a project for my free-time: I have extensive knowledge of the requirements, use-cases, context, etc, and have a personal interest in the material which will keep me engaged and working on this more than I might otherwise. 

There are currently many of these out there; my goal is to make it my own without investigating too deeply how they've implemented the tools, and to further expand on one major issue I have with most of the free versions of this: you can only access materials from the OGL SRD. I hope to make an interface to make things smoother and simpler, but include a depth of customization for those who want it. In addition to being able to add your own custom home-brew(custom) content, it will be easy to share what you've created as "modules" with others! 

## How?

Well, I'm still working on that. I have some rough plans in my head which I've started to put down on paper, and as I solidify things I'll be transfering them to documents and tools and posting them here. 

It will be a web-app with a Javascript front-end and a Python/Django backend. I haven't decided which JS framework I will use; I'll probably do initial dev with basic JS and Bootstrap front-end until I have my front-end UI/UX nailed down in more detail and then look into which framework best suits the app. Will probably a SQLite or PostgreSQL DB, but I need to model the data in more detail before making a firm decision on that. Most likely hosted on AWS as I don't expect to outgrow the free tier anytime soon. 

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

## Features in mind (listed in no particular order)

* Character Manager
  * can list various attacks/spells/abilities, their relative modifiers, etc
  * apply debuffs / buffs to your character and see those reflected in their stats/modifiers/etc
    * changes the colour of the stat/modifier/whatever on the page, mouse-over to see what math is applied to the item and where the modifiers are from
    * requires interface to add/remove status effects from a list, as well as create custom ones
    * have quick-list for simple/common things
  * Buttons for Take a Short Rest / Take a Long Rest / wait X days / etc, which apply the effects of those rests (certain abilities recharge, debuffs/diseases tick down)
    * requires some configuration about how long a short/long rest is in your game, including an option for "fluid" where each might be slightly different, if relevant.
    * Ties in to spellbook and Feature List, as those are what recharges on that time
    * also need to be able to configure the effects of the rest on a per-character basis, as different campaigns say a long rest restores full health, or 50% max health, or some other thing; some debuffs clear, some don't, etc etc.
* Ability/Feature/Usable Options list
  * similar to the spellbook, but specifically for not-spells; class abilities, features, special attacks, and various things usable X times per Y (once per day, twice per short rest, thirteen times per full-moon, whatever)
* Spellbook
  * need to account for the various spellcasting classes and either:
    * make a generic version that 
* Inventory Management
  * Option for multiple inventories ("x is in the bank, y is in the backpack, z is in the bag of holding")
  * Options to enable encumberance / carry capacity (some games play with it, some don't)
    * If not enabled, will have option somewhere to manually toggle the debuff, so that it's available if necessary
  * Manage quantities
  * Items in "on-person" inventories that have a use-effect (potions, items with abilities, etc) will have those options collated and added to the list of optinos / features / abilities for the character somewhere.
* "combat" manager
  * I need a better name for this; most of these features also apply outside of "combat". Most of these features are just things that you need to manage for the character.
  * includes an interface to list character options for Action/Movement/Bonus/Reaction
  * "optimization" option to show hypothetical average damage (or other success-rate) of various attacks/abilities
    * many players will leave this disabled, which will be the default, but those who want it can enable it.
* dice-roller app (for those monsters that don't want to roll their own physical dice)
  * basically a setting the user can set that will take effect in Combat Manager / skill checks / spell book / etc
  * when not toggled, instead of rolling the dice for you, it will just display the dice to roll and the modifiers to add to it (if any) when one of those other abilities/features is used.
* Notebook
  * A campaign can take months or years of real-world time. For any length of campaign, it's recommended to take notes. I've ended up with full coiled notebooks of notes for a single character in a campaign, including where they've been, what they've done, people they've met and all sorts of other things. 
  * A notebook module will be able to create Notes with a type of Place, Person, or "What We Did" (I'll figure out a name for that last one later)
  * Place and Person are intended to, at base-level, be the initial descriptors of the place. 
  * You can then tag your "What We Did" notes by the People and Places involved; then, when you go to view those People or Places in your notes, you'll see those "What We Did" notes listed as well. 
  * These will be time-stamped with real-world dates/times, because I don't think any campaign I've ever been in has had a consistent (or explained) calendar system that the players paid attention to.
  * You will also be able to view all notes for a specific real-world day, to see what you did in that session.
  * still working out a conceptual interface for this; I'm thinking full-page note-editor (similar to what I'm typing in in GitHub's website right now) with options to tag sections/lines based on highlighting? we'll see, it's one of the later features I intend to add.
