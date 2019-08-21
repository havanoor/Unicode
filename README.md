# Unicode Interview Tasks


### Task 1
For the first task we are going to use the split method to split the string into a list of binry numbers.
Then we iterate through the list converting every binary number to its equivalent decimal number.
Now we check whether it is divisible by 5 and then print the number if it is divisible.


### Task 2
We start this task by creating  a django project using the ```django-admin start app SpacexAPP``` commmand.
To access the spacex API we first import the ```request``` library and connect to the link [https://api.spacexdata.com/v3/launches](https://api.spacexdata.com/v3/launches).
We iterate through the JSON and accesss the 'flight_number','rocket_name','mission_patch'and 'launch_date_utc'.
These attributes are stored in a dictionary and a list of dictionaries is created . This list is then returned as an ```HttpResponse``` which displays the dictionaries on the webpage.

### Task 3
For this task we render an html page 'hello.html' to which we pass the list we created in task 2.We create a table in the html page and access the dictionary.We use the jinja template to iterate through the list of dictionaries.

### Task 4
We create  a model ```Space``` to create our database .
It has four fields, flight_number which is a IntegerField, mission_name,rocket_name and mission_patch whiich are CharField and time which is a DateTimeField.
To add data to our database we write a function called ```add_data```.
