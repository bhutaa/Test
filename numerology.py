class NameNumbers(object):
    value_dict = {1: ['a', 'i', 'j', 'q', 'y'],
                  2: ['b', 'k', 'r'],
                  3: ['c', 'g', 'l', 's'],
                  4: ['d', 'm', 't'],
                  5: ['e', 'h', 'n', 'x'],
                  6: ['u', 'v', 'w'],
                  7: ['o', 'z'],
                  8: ['f', 'p']}

    planets_dict = {1: 'Sun',
                    2: 'Moon',
                    3: 'Jupiter',
                    4: 'Uranus/Rahu',
                    5: 'Mercury',
                    6: 'Venus',
                    7: 'Neptune/Ketu',
                    8: 'Saturn',
                    9: 'Mars'}

    def __init__(self, name):
        self.name = name

    def __call__(self):
        name_parts = self.name.split(' ')
        name_compound_number = 0
        print '\n'
        for sub_str in name_parts:
            sub_str_compound_value = 0
            for letter in sub_str.lower():
                for key, value in self.value_dict.items():
                    if letter in value:
                        sub_str_compound_value += key
                        break
            print 'Compound number for {} is [{}]\n'.format(sub_str.upper(), sub_str_compound_value)
            if sub_str_compound_value > 9:
                sub_str_single_value = (sub_str_compound_value / 10) + (sub_str_compound_value % 10)
                if sub_str_single_value > 9:
                    sub_str_single_value = (sub_str_single_value / 10) + (sub_str_single_value % 10)
                name_single_number = sub_str_single_value
                name_compound_number += sub_str_single_value
                print 'Single Number for {} is [{}]\n'.format(sub_str.upper(), sub_str_single_value)
            else:
                name_single_number = sub_str_compound_value
                name_compound_number += sub_str_compound_value
                print 'Single Number for {} is [{}]\n'.format(sub_str.upper(), sub_str_compound_value)
        if len(name_parts) > 1:
            print 'Compound Number for {} is [{}]\n'.format(self.name.upper(), name_compound_number)
            if name_compound_number > 9:
                name_single_number = (name_compound_number / 10) + (name_compound_number % 10)
            else:
                name_single_number = name_compound_number
            if name_single_number > 9:
                name_single_number = (name_single_number / 10) + (name_single_number % 10)
        print 'Single Number for {} is [{}] and it corresponds to "{}"\n'.format(self.name.upper(), name_single_number, self.planets_dict[name_single_number])


class Numerology(object):

    planets_dict = {1: 'Sun',
                    2: 'Moon',
                    3: 'Jupiter',
                    4: 'Uranus/Rahu',
                    5: 'Mercury',
                    6: 'Venus',
                    7: 'Neptune/Ketu',
                    8: 'Saturn',
                    9: 'Mars'}

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.name_numbers = NameNumbers(self.name)
        self.birth_number = 0
        self.destiny_number = 0

    def print_name_numbers(self):
        self.name_numbers()

    def calculate_birth_destiny_numbers(self):
        dob = self.dob.split('.')

        date = dob[0]
        if int(date) < 9:
            self.birth_number = int(date)
        else:
            self.birth_number = (int(date) / 10) + (int(date) % 10)
            if int(self.birth_number) < 9:
                pass
            else:
                self.birth_number = (int(self.birth_number) / 10) + (int(self.birth_number) % 10)

        month = dob[1]
        if int(month) > 9:
            month = (int(month) / 10) + (int(month) % 10)
        else:
            month = int(month)

        sum = 0
        for digit in dob[2]:
            sum += int(digit)
        year = sum

        self.destiny_number = self.birth_number + month + year
        sum = 0
        for digit in str(self.destiny_number):
            sum += int(digit)
        self.destiny_number = sum
        if self.destiny_number > 9:
            self.destiny_number = (int(self.destiny_number)/10) + (int(self.destiny_number)%10)

    def __call__(self, *args, **kwargs):
        self.print_name_numbers()
        self.calculate_birth_destiny_numbers()
        print 'Birth Number is [{}] Corresponding to "{}"\n'.format(self.birth_number, self.planets_dict[self.birth_number])
        print 'Destiny Number is [{}] Corresponding to "{}"\n'.format(self.destiny_number, self.planets_dict[self.destiny_number])


def execute_options():
    incorrect_option = True
    while incorrect_option:
        option = raw_input(
            "\033[1m" + "\nPlease select what you want to do "
                        "\n\n1: Calculate Name Numbers \n\n2: Do Numerology\n" + "\033[0m")

        if option == '1':
            incorrect_option = False
            name = raw_input("\nPlease enter name separated by spaces\n")
            name_numbers = NameNumbers(name)
            print '=' * 50
            name_numbers()
            print '=' * 50
        elif option == '2':
            incorrect_option = False
            name = raw_input("\nPlease enter name separated by spaces:\n")
            dob = raw_input("\nPlease enter Date of Birth dd.mm.yyyy:\n")
            print '=' * 50
            name_numerology = Numerology(name, dob)
            name_numerology()
            print '=' * 50
        else:
            print "\n" + "\033[1m" + "Incorrect Option, Please Enter 1 or 2" + "\033[0m"


if __name__ == "__main__":
    exit_now = False
    while not exit_now:
        print "+++++++ Welcome to Numerology +++++++"
        execute_options()
        next_option = raw_input(
            '\033[1m' + '\n\nWhat do you want to do Next :'
                        '\n\n1: Continue doing Numerology \n\n2: Exit\n\nEnter 1 or 2' + '\033[0m')
        if next_option == '1':
            execute_options()
        elif next_option == '2':
            print '+' * 16
            print '   THANK YOU   '
            print '+' * 16
            exit_now = True
        else:
            print '\n' + '\033[1m' + 'Incorrect Option, Please Enter 1 or 2' + '\033[0m'
