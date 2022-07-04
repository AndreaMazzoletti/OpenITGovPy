# Download Italian government open data

A simple NodeJS program to dowload open data with a keyword from the government <a href="https://www.dati.gov.it/api"> open apis </a>.

WARNING: If you don't select a keyword to limit the research the program will dowload A LOT of data (the entire dataset actually) so be sure to set a keyword as explained further in this document.

## How it works

This program will download all the open data from the <a href="https://www.dati.gov.it/"> Italian government website </a> or from third parties that the website relies on (such as provinces, regions etc...) in a "data" folder that will be created inside the project folder.
You can limit the research by adding a keyword that represents what you want to search (e.g. "rome").

## How to set the keyword

When the program is started it will require you to enter the keyword to search and then press ENTER, you can leave the input field blank to download all the data but it may not work because it is currently not supported, use at your own risk.

## Installation

Install <a href="https://nodejs.org/en/"> NodeJS</a> on your machine.
Clone this repository and go inside the downloaded folder, then install the dependencies:

```
npm i 

```
## Usage

To start the program type this in your favourite terminal while you are in the project location

```
node index.js

```

The progress of the downloads will appear, now you just wait and then enjoy your data.
I'm not responsible for how you use this program, use it at your own risk and beware that i wrote it in a night and in a shot.

## Why?

I made this simple program because the search function on the website is not always functioning which is annoying, plus you can integrate this function in larger systems.
