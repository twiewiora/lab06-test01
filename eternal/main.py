import datetime
import sys
import argparse


def calculate(year, month, day):
    if isinstance(year, int) and isinstance(month, int) and isinstance(day, int):
        try:
            datetime.datetime(year=year,month=month,day=day)
        except ValueError:
            return -1
        m = 1 + (month + 9) % 12
        if m > 10:
            year = year - 1
        c = year // 100
        d = year % 100
        n = ((13 * m - 1) // 5 + d + d // 4 + c // 4 + 5 * c + day) % 7
        return n - 1
    return -1


def main(args):
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--year',
                            type=int,
                            required=True,
                            help='Year')
        parser.add_argument('--month',
                            type=int,
                            required=True,
                            help='Month')
        parser.add_argument('--day',
                            type=int,
                            required=True,
                            help='Day')

        parsed_args = parser.parse_args(args)

        weekday = calculate(parsed_args.year, parsed_args.month, parsed_args.day)
        print("Weekday {}".format(weekday))
    except:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
