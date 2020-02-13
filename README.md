# Submission statement

Hi all fools!

Thanks for giving me the opprotunity to work on this.

I stopped myself around ~10 hours; While I believe that all acceptance criteria have been met many things can be changed or improved upon!

You'll notice a "notes.md" which is some of my initial impression on the project. These are jumbled notes and are just a showcase of how I start breaking things down.

I did not use _any_ javascript frameworks - this is all pure browser JS! Therefore, I make zero claims about compatability. This works on recent versions of Firefox and Chrome. 
In an ideal world an entire js build system would be used that ensure browser compatability.
On the topic of JS -> Using types is superior; On a larger project, it is way more scalable to use flow or typescript. I didn't do that here because I didn't want to spend hours trying to make it work. Trade offs.


I used the Skeleton CSS system; I'm not big on using this for larger projects but it is a no-frills way to get a grid system set up. [getskeleton.com]


I'm the first to admit I don't have a great eye for design. I focused on my strengths for this project which were making a great foundation + ensuring correctness in as many places as possible. After hitting all functional requirements I began to work on making the webapp react to your eyes better - but I hit my time limit so I left it functionally ugly ;).

Some things I'd work on given another few hours of time;
- Discovery experience on the index page - the text only approach isn't great; I think images would look great here.
- Frontend testing
- Stock quote sidebar needs love, particularly it needs some assets and styling so a user knows what they're even looking at
- Individual comments aren't all too bad but could use some more style
- For a more scalable project, I'd place this django app in a docker container
- UUIDs don't make pretty URLs - Slugification of the headline would, so I'd probably take a crack at making that a reality.
- Database is set to the default django SQLite implementation - for a real project I'd switch to postgres rather quickly.
- The tests aren't as unit-testy as I'd like - they regularly test one or two more levels of code than they should. I'd incorporate more method stubbing.
- There are a few low hanging fruits for caching - namely reading those content-api json files on the backend, as well as loading the same article in the frontend.
- A cool experiment might be to see how to incorporate GraphQL into this; I can definitely see a Graph relation between articles and comments.





--
WW


## Setup

Requirements:
pip
bash

`./quick_start.sh`

This will install pipenv, dependencies, create environment files, run tests and initiate the development server.

Tested on linux mint 19.1 Cinnamon (4.0.1)
Linux kernel 4.15.0-74-generic


Below is the og project question;


## Motley Fool Developer Interview Project

Hello!

Below you will find guidelines for a small website you will create. Included are two JSON files, content_api.json and quotes_api.json, which you should use to populate the website. Also included are two wireframe designs for a homepage and an article page as well as some basic HTML templates if you wish to use them, however please feel free to use your own creativity for the design of this website.

We would like to thank you for taking the time to complete this project. We will schedule your in-person interview after we have received your completed project. We are looking forward to discussing your experience and the completed project!

### General project guidelines
* Host your project on github.
* Create a Django app.
* Use any publicly available python packages that you need.
* Use any front-end scaffolding framework and any JS libraries excluding JS frameworks (angular, react, etc)
* Include a startup shell script that will install any dependencies and start the application.

### Homepage
* The top box on the homepage should be populated with the first article in the content API with the tag where slug=10-promise.
* The remaining three boxes should be populated with a random assortment of the remaining articles.
* The headline's of each article should link to the article page.

### Article Page
* Use content_api.json and quotes_api.json to populate the details for the individual article page.
* Use a URL schema that makes sense to you.
* Create a button below the Stock Quotes sidebar that, when clicked, will use javascript to shuffle the order of the stock quote 
items.
* Ability to add comments at the bottom of an article by anonymous users.

### Evaluation criteria
List of possible evaluation criteria.
* Front-end structure - Use of partials, CSS and JS structure.
* Django Framework usage.
* URL Structure.
* Any database use.
* Possible areas for future additions, improvement, or optimization.
* Anything you did to make make the application your own.

