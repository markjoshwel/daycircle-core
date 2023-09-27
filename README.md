# daycircle

beautifully chart your average day over a period of time

## usage

point daycircle to a multiple [daycircle plaintext files](#daycircle-plaintext-file-format)
and it will work its magic.

```text
$ ls samples
25-10-2023  26-10-2023
$ daycircle samples/*
```

see [command-line usage](#command-line-usage) for more information.

### command-line usage

TODO CLI HELP

### daycircle plaintext file format

daycircle plaintext files follow a simple key-value format:

```text
# psuedo-grammar

root     = metadata
         | key <whitespace> value
         ;

metadata = "day" <whitespace> date
         | "#" <string> <whitespace> rgbhex
         ;
key      = <string>
         | "@" <string>
         ;
value    = time           # single time for @<key> (marker) events
         | time "-" time  # time range for <key> (range) events
         ;
date     = <0-9> <0-9> "-"          # dd-
           <0-9> <0-9> "-"          # mm-
           <0-9> <0-9> <0-9> <0-9>  # yyyy
         ;
time     = <0-9> <0-9> <0-9> <0-9>  # 24h time format (e.g, 0000, 2359)
         ;
rgbhex   = <0-F> <0-F> <0-F> <0-F> <0-F> <0-F>  # 6-digit hex colour code
         ;
```

there are four types of keys:

1. **the metadata `day` key** (required)

   specifies the date of which the events took place.

   this key is not required to be the first key in the file, but it must be present.  
   for daycircle plaintext files that will be passed to `--colours`, this key will not be
   checked for unlike files passed to the `targets` argument.

2. **the metadata colour key** (optional)

   specifies the 6-digit hex colour code to use as the primary colour when generating the
   output graph colour palette.

3. **the range event key** (optional)

   specifies a range of time in which the event took place.

   examples: sleeping, school, work, outside, etc.

4. **the marker event key** (optional)

    specifies a single point in time in which the event took place. this is useful for
    events that one would like to mark, but do not have a specific start and end time.

    example: eating

example:

```text
#sleep  e2531b
#out    9593D9
#work   A40E4C
#ate    0F4C5C
day     25-10-2023
out     0000-0330
@eat    0600
sleep   0700-1730
out     1715-1740
@eat    2000
work    2030-2330
```
