# Incubeta Cloud City - Assignment - Marketing platform developer

This assignment consists of 3 parts. You will be creating code for a small application that can ingest data and 
output it in a way the customer wants. This assignment will use a real-life use-case that we also needed to solve 
for our existing client Accor. However, we simplified the scenario a bit to make it solvable within 3-4 hours.


## Before you start - preparation

- Make sure you book enough time for yourself to complete this assignment. Based on our experience maximum 3-4 hours should be enough to deliver a solution.
- Your solution should be in a private repository. Once you created one please don't forget to invite us, so we can track your progress. 
  - Our accounts: 
  - https://github.com/S4n3L
  - https://github.com/miguelosana
  - https://github.com/baspenny
  
- Use commits and commit messages as you would work in our team already. We intend to check your timestamps to know how much time you needed to spend with certain tasks.
- Please make sure that your application is runnable with a description how to actually achieve this.

***We wish you a great time with this assignment. Trust us: you have nothing to fear and we hope we can welcome you in our team soon! See you on the other side! :)***


## Assignment 1
In this assigment you will need to ingest a real API. This is the open API from Accor hotels and the code is already
a bit prepared for you to get you started 😉. The key will be sent to you in a seperate message.

The client (Accor) wants to get information about hotels that later will be used to feed creatives.  
You have the job to do the following:

1. Create funtionality that ingests the API 
2. Create a class that inherits from the ApiManager class that have class members that can do the following:

   - Can handle different languages via the header Accept-language
   - Can only handle the languages "nl", "fr" and "en" and must throw an exception
          when another language is being set
   - Can get a list of hotels from the endppoint 'catalog/v1/inventory/hotels' 
   - Can get information of a specific hotel on 'catalog/v1/inventory/hotels/${id}'
3. Create proper exception handling
4. Create an example script that illustrates the working of the classes by instantiating them

## Assignment 2
In this assignement you will be integrating the functionality that you've created in assignment 1 into 
Django Framework. Create objects of hotels and store them in the database. Create some way to invoke the
importing of the data into the database.

Also, the client wants to attach data from another source that contains images. Please make a script that 
imports the image data from the following source:

 https://jsonplaceholder.typicode.com/photos
 
## Assignment 3
This is the final step. We need to create a XML file with hotel data. 
The client needs the following information in the output file you’ll be creating:
- Hotel code (Data assignment 1)
- Hotel Name (Data assignment 1)
- Description of the hotels in the languages NL, FR and EN
- Country the hotel resides in (Data assignment 1)
- City the hotel resides (Data assignment 1)
- Album ID (Data assignment 2)
- Image title (Data assignment 2)

The client has given the following constraints:
- The mapping between ids is “id” in the photo API and “id” in the OpenAPI of Accor
- Only the hotels with the id between 1000 and 2000 need to be in the output
- The output is an XML file with a “Hotels” root node and “Hotel” nodes as children
- If a hotel is not present in the XML, add them to a log file

