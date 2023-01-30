# HW1
1. SHop
Create a class called Shop. Upon initialization it should receive a name (string) and items (list). Create a method called get_items_count() which should return the number of items in the store.

2. Hero
Create a class called Hero. Upon initialization it should receive a name (string) and health (number). Create two methods:
• defend(damage) - reduce the given damage from the hero's health:
o if the health become 0 or less, set it to 0 and return "{name} was defeated"
• heal(amount) - increase the health of the hero with the given amount

3. Employee
Create class Employee. Upon initialization, it should receive id (number), first_name (string), last_name (string) and salary (number). Create 3 instance methods:
- get_full_name() - returns "{first_name} {last_name}"
- get_annual_salary() - returns the total salary for 12 months
- raise_salary(amount) - increases the salary by the given amount and returns the new salary

4. Cup
Create a class called Cup. Upon initialization it should receive size (number) and quantity (a number representing how much liquid is in it).
The class should have two methods:
• fill(milliliters) which will increase the amount of liquid in the cup with the given milliliters (if there is space in the cup, otherwise ignore).
• status() which will return the amount of free space left in the cup. Submit only the class in the judge system. Do not forget to test your code.

5. Flower
Create a class called Flower. Upon initialization, the class should receive name (string) and water_requirements (number). The flower should also have an instance attribute called is_happy (False by default). Add two methods to the class:
- water(quantity) - it will water the flower. Each time check if the quantity is greater than or equal to the required. If it is - the flower becomes happy (set is_happy to True).
- status() - it should return "{name} is happy" if the flower is happy, otherwise it should return "{name} is not happy".
Submit only the class in the judge system.

6. Steam User
Create a class called SteamUser. Upon initialization it should receive username (string) and games (list). It should also have an attribute called played_hours (0 by default). Add three methods to the class:
- play(game, hours)
o If the game is in the game list, increase the played_hours by the given hours and return
"{username} is playing {game}"
o Otherwise,return"{game}isnotinlibrary"
- buy_game(game)
o If the game is not in the game list, add it and return "{username} bought {game}" o Otherwisereturn"{game}isalreadyinyourlibrary"
- status() - returns the following:
"{username} has {games_count} games. Total play time: {played_hours}"
Submit only the class in the judge system.

7. Programmer
Create a class called Programmer. Upon initialization it should receive name (string), language (string), skills (integer). The class should have two methods:
- watch_course(course_name, language, skills_earned)
o If the programmer's language is the same as the one on the course, increase his skills with the
given amount and return a message "{name} watched {course_name}". o Otherwisereturn"{name}doesnotknow{language}".
- change_language(new_language, skills_needed)
o If the programmer has the skills and the new language is not the same as his, change his language
to the new one and return "{name} switched from {previous_language} to
{new_language}".
o If the programmer has the skills, but the given language is equal to his return "{name} already
knows {language}".
o In the last case the programmer does not have the skills, so return "{name} needs
{needed_skills} more skills" and do not change his language Submit only the class in the judge system.
