# web-driven-database-ephraim_benson_weijia_ma

A database-driven web project for cs257

## Description

This website searches breakfast cereals by name and range filters of their nutritional content.

The search results are displayed in grids, showing the details of each breakfast cereal.


### Usage: 

To open the website on perlman, inside the perlman folder under our name, type `python3 flask_app.py [port]` where port can be 5104, 5204, 5116, 5216.


## List of Features

- The home page allows search by keywords. The keyword search does not have to be word-by-word or case-sensitive. As long as the name of the cereal contains the input, that cereal will be displayed in the search result.

- The home page allows search by a few selective range filters of nutritional values on top of the keyword search. Leave the value blank for a more general search.

- The result page will show up after clicking the submit button.

- The search function in the result page functions in the same way that the search in the home page does.

- The result page displays all the cereals that satisfy the search criteria (keywords and range filters).

- The about page displays relevant bibliography and citations for the dataset

- User can go back and forth between the 3 pages by clicking the home, about buttons on the top. 

## Dataset

The dataset we are using for our website is a dataset of breakfast cereals. The information contained in the dataset includes nutritional information/characteristics such as calories, sugar, vitamin content, etc. The original dataset can be downloaded from: https://perso.telecom-paristech.fr/eagan/class/igr204/data/cereal.csv. The data was gathered by Petra Isenberg, Pierre Dragicevic, and Yvonne Jansen, and is licensed under a Creative Commons Attribution-ShareAlike 3.0 License, which states that anyone can copy and redistribute the material in any medium or format.


## Feature to be implemented

We did not manage to fully implement sliders for the range filters. We were able to output the slider values to html with JQuery, but we couldn't read it in to the flask script.
