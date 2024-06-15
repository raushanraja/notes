Nom: Parser

## Nom
- Used to build parsers and helps combine them using combinators.
- The nor parser takean and input and returns a result.
    - In result, it result 
        - `Ok` indicating gthe parser succssfully found what it was looking for.
        - `Err` indicating it could not found what it was looking for.
- When it's okay `Ok`, it restuls a tuple. 
    - First field: Contains everything that parser did not processed.
    - Second field everything parser processed. 
- When it fails `Err`, it resutls multiple errors (More on this lated)

- So the parsed process looks something like this, as given in figure and same this is represented by `IResult<I,O>` in code :
```md
                                   ┌─► Ok(
                                   │      what the parser didn't touch, # This is the first field of tuple
                                   │      what matched the regex        # The Second field of the tuple
                                   │   )
             ┌─────────┐           │
 my input───►│my parser├──►either──┤
             └─────────┘           └─► Err(...)
```


### IResult<I,O>
- Nom usages IResult<I,O> type to represent the model given in figure.
- The `Ok` variant takes two types `I` (=Input) and `O` (=Output).
- The `Err` variant stores an error 
- The type is import from as `use nom::IResult`


### Tags
- A collection of bytes in nom is call a tag. Example: "abc" is a tag and created as tag("abc")
- Tags are so common that there exists function called `tag` & `tag_no_case` in nom.
- It helps in parsing  when matching a string
- Warning: There are multiple definition of tag in nom, use the correct one.
- `pub use nom::bytes::complete::tag;`


### Characters
- Tags are useful but they are restrictive.
- Characters are pre-written parsers in nom, which allows to parse any group of characters.
- This differs from tag, as Characters allows to accept any group of characters, 
rather than just accepting characters in defined sequence.
- Some Selection of Characters Parsers:

| Function       | Character Symbol | Description |
|----------------|-|-------------------------------------------------------------------------------------------------------|
| `alpha0`       | `[a-zA-Z]`    | Recognizes zero or more lowercase and uppercase alphabetic characters: /[a-zA-Z]/. `alpha1` does the same but returns at least one character.|
| `alphanumeric0`| `[0-9a-zA-Z]` | Recognizes zero or more numerical and alphabetic characters: /[0-9a-zA-Z]/. `alphanumeric1` does the same but returns at least one character.|
| `digit0`       | `[0-9]`       | Recognizes zero or more numerical characters: /[0-9]/. `digit1` does the same but returns at least one character.|
| `multispace0`  |               | Recognizes zero or more spaces, tabs, carriage returns, and line feeds. `multispace1` does the same but returns at least one character.|
| `space0`       |               | Recognizes zero or more spaces and tabs. `space1` does the same but returns at least one character.|
| `line_ending`  | `\n & \r\n`   | Recognizes an end of line (both \n and \r\n).|
| `newline`      | `\n`          | Matches a newline character \n.|
| `tab`          | `\t`          | Matches a tab character \t.|



###  Alternatives and Composition
- Alternatives are used to choose between multiple parser untill one is succssfull.
- Composition is used to chian multiple parser and evaluate all of them.

- `Alternative`:
    - Nom provides`use nod::branch::alt;` which gives the ability to choose between parsers.
    - The `alt()` takes tuple (of parsers) as input 
        - and executes each parser untill it finds one the does not error (or parse succssfully).

- `Compoisition`:
    - Nom provides another built-in combinator `use nom::sequence::tuple;`, which gives the ability to run all the parsed and get result.
    - The tuple() combinator takes a tuple of parsers, 
        - and either returns Ok with a 
            - First field with all the not processed string 
            - Second, tuple of all of their successful parses as tuple
                - The length of this tuple depends of number of parser used in `tuple()`
                - The structure could also chage based on the praser used, I.E, when used a tag, it will in turn return a tuple 
        - or it returns the Err of the first failed parser.

- Other combinators:
    - `delimited` : Discard - Parse - Discard
    - `preceded` : Discard - Parse
    - `terminated` : Parse - Discard
    - `pair` : Parse - Parse
    - `seperated_pair` : Parse - Seperator (Discard) - Parse


### References:
- https://docs.rs/nom/latest/nom/character/complete/index.html
- https://docs.rs/nom/latest/nom/sequence/index.html#functions


id: cd7dc553aaee4a198e9fd8965dbdb67d
parent_id: 6260d9c9d06f4a5bb6de5be6751f3394
created_time: 2023-10-01T10:36:03.243Z
updated_time: 2024-04-20T17:44:00.803Z
is_conflict: 0
latitude: 23.79565310
longitude: 86.43038590
altitude: 0.0000
author: 
source_url: 
is_todo: 0
todo_due: 0
todo_completed: 0
source: joplin-desktop
source_application: net.cozic.joplin-desktop
application_data: 
order: 1696156563243
user_created_time: 2023-10-01T10:36:03.243Z
user_updated_time: 2024-04-20T17:44:00.803Z
encryption_cipher_text: 
encryption_applied: 0
markup_language: 1
is_shared: 0
share_id: 
conflict_original_id: 
master_key_id: 
user_data: 
type_: 1