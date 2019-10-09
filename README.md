# targetDate

Python script to get the target date when a date and number of dates are given in the command line as arguments

# Algorithm

 * A date is taken in 'YYYY/MM/DD' format as the second argument, the number of days is taken as a third argument, 
and also an optional argument as [--step].
 * First the number of command line arguments are checked and if the number is more or less than expected 'usage()' is called and the program exits.
 * If usage is valid and there are three arguments in total it checks for the length of the third argument.
    *  If length is 10 the bonus functionality is operated else the normal functionality is operated.
        *  For the bonus functionality number of days argument will be in 'YYY/MM/DD' format.
        *  The after function will be looped through from low date to high date until they become even and a variable will keep count of the days.
         * Then the number of days will be outputed and the program will exit.
    *  If it's the normal functionality then first the date will be validated using 'valid_date()'.
         * If there is an error the error message will be shown and the program will exit,
        *  else the 'dbda()' function is called.
     * Same happens if there are four command line arguments with the second argument being the optional [--step],
     * additionally a flag named step will be set to true and then call the 'dbda()' function.
         * Inside the 'dbda()' function first it checks for the flag of step to identify what output is needed.
        *  If the flag is false then the program checks for the sign of the number of days to determine whether to call before or after functions.
            *  If positive it calls the after function and if negative it calls the before function.
             * The function called is looped for the total number of days provided in the days argument to get the target date.
                *  Both 'before()' and 'after()' functions first gets the date and splits it from '/' to get year,month and date into string variables.
                *  Then they are converted to integers for calculations.
                *  Then 'days_in_mon()' is called to get the days for all the months of the particular year.
                 * In 'days_in_mon()', 'leap_year()' is called to check if the year is a leap year or not.
                 * The following logic applies to being a leap year,
                    *  if year divides by 4, 100, 400 without a remainder it is a leap year,
                    *  if year divides by 4 without a remainder and divides by 100 with a remainder it is a leap year,
                    *  if year divides by 4 and 100 without a remainder, but divides by 400 with a remainder it is not a leap year,
                    *  if year divides by 4 with a remainder it is not a leap year.
                *  This logic is used to return true or false in 'leap_year()' function.
                *  If return is true feb_max(days in february) is set to 29 else to 28.
                *  Then 'days_in_mon()' return a list object of 12 containing month index and their corresponding days.
            *  In 'after()' the tmp_day variable keeps the day ahead of provided day, 
                *  and if this exceeds the max days of the particular month next_day is set to 1 and month is increased by 1.
                *  else next_day is set to tmp_day.
                *  If the month that was changed accordingly exceeds 12 then month is reset to 1 and then year is increased by 1.
                 * This total procedure gets the next date which is combined into a string in 'YYYY/MM/DD' format and returned to 'dbda()' function.
            *  In 'before()' function tmp_day is decremented by 1 of the parameter day.
                *  If day and month are 1 month is set to 12, day is set to max days in the 12th month and the year is decremented by 1.
                *  else if day is 1 and month is not 1 month is decremented by 1 and day is set to max in the decremented month.
                *  This total procedure gets the previous date which is combined into a string in 'YYYY/MM/DD' format and returned to 'dbda()' function.
    *  Finally the target date will be returned to the main and then printed out as the output.
    *  Same procedure is undergone if the step flag is true. Additionally in every loop calling 'before()' or 'after()' functions,
    it will print out the outputs of the return dates.
