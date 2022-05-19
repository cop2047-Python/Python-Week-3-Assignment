# Author Name: James Lee
# Date: 5/29/2022
# Program Name: Lee_Diagnostic_Test.py
# Purpose: Implement Flu vs Allergies vs COVID-19 Diagnostic test

def main():
    # Get input: Does patient hava a fever?
    fever = input('\nDoes patient have a fever? <Yes or No> ')
    fever = fever.lower()

    if fever == 'yes':
        # Get input: Does patient have shortness of breath?
        short_breath = input('Is patient experiencing shortness of breath? <Yes or No> ')
        short_breath = short_breath.lower()

        # If fever and shortness of breath, patient may have COVID-19
        if short_breath == 'yes':
            print('\nDiagnosis: Patient may have COVID-19.', end=' ')
            print('Additional symptoms may include cough, fatigue, weakness, and/or exhaustion.')

        # If fever and no shortness of breath, patient may have the flu
        elif short_breath == 'no':
            print('\nDiagnosis: Patient may have the flu.', end=' ')
            print('Additional symptoms may include cough, fatigue, weakness, and/or exhaustion.')
        else:
            print('*** Invalid input entered, program ended ***')

    elif fever == 'no':
        # Get input: Does patient have itchy eyes?
        itchy_eyes = input('Does patient have itchy eyes? <Yes or No> ')
        itchy_eyes = itchy_eyes.lower()

        # If no fever and itchy eyes, patient may have allergies
        if itchy_eyes == 'yes':
            print('\nDiagnosis: Patient may have allergies.', end=' ')
            print('Additional symptoms may include sneezing and/or a runny nose.')

        # if no fever and no itchy eyes, patient may have a common cold
        elif itchy_eyes == 'no':
            print('\nDiagnosis: Patient may have a common cold.', end=' ')
            print('Additional symptoms may include sneezing, a runny nose, and/or mild chest discomfort.')
        else:
            print('*** Invalid input entered, program ended ***')

    else:
        print('*** Invalid input entered, program ended ***')


# Call the main function.
main()
