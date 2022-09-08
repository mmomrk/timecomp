# timecomp 

## a script to compare time

usage: timecomp.py [-h] [-v] format date1 [date2] [format2]

This is a tool to handle varous data strings into unix time and to
compare data strings. If one date is given then output is its unix
seconds. If two dates are given then the result is {-1,0,1}
depending on d1>d2 resolution. Warning: it is awfully slow. Warning:
it seems like '%m 2 3' breaks the system already. Nobody's perfect!

positional arguments:
  format         format of the first date. According to
                 datetime.datetime.strptime method documentation
  date1          the first date to be parsed
  date2          the second date to be parsed
  format2        format of the second date

options:
  -h, --help     show this help message and exit
  -v, --verbose  show some debug info. Will break scripts


## Format string

Basically it is described here:
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

## Examples

```
$ ./timecomp.py "%Y-%m-%d_%H-%M-%S" 1970-01-01_03-00-05
>> 5
$ ./timecomp.py "%Y-%m-%d_%H-%M-%S" 1970-01-01_03-00-05 1970-01-01_03-04-05
>> 1
$ ./timecomp.py "%Y-%m-%d_%H-%M-%S" 1970-01-01_03-00-05 1970-01-01_03-04-05
>> -1
$ ./timecomp.py "%Y-%m-%d_%H-%M-%S" 1970-01-01_03-00-05 04-99 "%m-%y" 
>> -1
$ ./timecomp.py "%Y" 1022 99 "%y"
>> -1

```

## License

MIT

## Bugs

No known bugs are present. Hey, I even fixed one while writing this readme

## Possible improvements

- Add timezone
- Max/min date in the list given
- Time delta
- Relativity
- Add support of Moon, Mars etc
- Serve a sandwich
