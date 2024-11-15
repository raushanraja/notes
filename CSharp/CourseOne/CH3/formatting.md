## Formatting
- Formatting in C# is the process of converting objects to string representation.
- The purpose is to display the resulting string, or deserialize to later restore the original data type.
- Ways to format a string
    - Using `ToString()` method
    - Using Format Syntax

| Format Item Syntax                  | Description                                                                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `{index[,alignment][:formatString]}` | Represents a placeholder in a composite format string. <br> `index` indicates which argument to include. <br> `alignment` (optional) specifies how it's aligned. <br> `formatString` (optional) specifies the format. |
| `{<interpolationExpression>[,<alignment>][:<formatString>]}` | Represents a placeholder in an interpolated string. <br> `<interpolationExpression>` is the variable or expression to include. <br> `<alignment>` (optional) specifies alignment. <br> `<formatString>` (optional) specifies the format. |
#### Explanation:
- **index**: 
  - The position of the argument in the list to be included.
- **interpolationExpression**:
  - The variable or expression enclosed within `{}` in an interpolated string, which gets replaced with its value.
- **alignment**: 
  - Optional. Determines the total length of the field and alignment. Positive for right-aligned, negative for left-aligned. If omitted, no leading or trailing spaces.
- **formatString**: 
  - Optional. Specifies the format of the argument's string representation. If not provided, uses the `ToString` method. If specified, the argument must implement `IFormattable`.

### Format Specifiers
#### Standard Numeric Format Specifiers
| Format Specifier | Name        | Example              |
|------------------|-------------|----------------------|
| "B" or "b"       | Binary      | 42 ("B") -> 101010  |
| "C" or "c"       | Currency    | 123.456 ("C", en-US) -> $123.46 |
| "D" or "d"       | Decimal     | 1234 ("D") -> 1234  |
| "E" or "e"       | Exponential | 1052.0329112756 ("E", en-US) -> 1.052033E+003 |
| "F" or "f"       | Fixed-point | 1234.567 ("F", en-US) -> 1234.57 |
| "G" or "g"       | General     | -123.456 ("G", en-US) -> -123.456 |
| "N" or "n"       | Number      | 1234.567 ("N", en-US) -> 1,234.57 |
| "P" or "p"       | Percent     | 1 ("P", en-US) -> 100.00 % |
| "R" or "r"       | Round-trip  | 123456789.12345678 ("R") -> 123456789.12345678 |
| "X" or "x"       | Hexadecimal | 255 ("X") -> FF |

#### Custom Format Specifiers
- Custom specifiers in C# are like special instructions to format numeric data in a way that's not covered by standard formats like currency or decimals.

| Format Specifier | Name                    | Example                                   |
|------------------|-------------------------|-------------------------------------------|
| "0"              | Zero placeholder        | 1234.5678 ("00000") -> 01235             |
| "#"              | Digit placeholder       | 1234.5678 ("#####") -> 1235              |
| "."              | Decimal point           | 0.45678 ("0.00", en-US) -> 0.46          |
| ","              | Group separator         | 2147483647 ("##,#", en-US) -> 2,147,483,647 |
| "%"              | Percentage placeholder  | 0.3697 ("%#0.00", en-US) -> %36.97       |
| "‰"              | Per mille placeholder   | 0.03697 ("#0.00‰", en-US) -> 36.97‰     |
| "E0", "E+0", "E-0", "e0", "e+0", "e-0" | Exponential notation | 987654 ("#0.0e0") -> 98.8e4       |
| "\"              | Escape character        | 987654 ("\###00\#") -> #987654#          |
| 'string'         | Literal string delimiter| 68 ("# 'degrees'") -> 68 degrees          |
| ;                | Section separator       | 12.345 ("#0.0#;(#0.0#);-\0-") -> 12.35   |
| Other            | All other characters   | 68 ("# °") -> 68 °                        |

#### Date Format Specifiers

| Character | Description                                       | Usage    | Example                                                  |
|-----------|---------------------------------------------------|----------|----------------------------------------------------------|
| "d"       | Short date pattern.                               | {0:d}    | 19-03-2021                                               |
| "D"       | Long date pattern.                                | {0:D}    | Friday, March 19, 2021                                   |
| "f"       | Full date/time pattern (short time).              | {0:f}    | Friday, March 19, 2021 12:15 PM                          |
| "F"       | Full date/time pattern (long time).               | {0:F}    | Friday, March 19, 2021 12:15:30 PM                       |
| "g"       | General date/time pattern (short time).           | {0:g}    | 19-03-2021 12:15 PM                                      |
| "G"       | General date/time pattern (long time).            | {0:G}    | 19-03-2021 12:15:30 PM                                   |
| "M", "m"  | Month/day pattern.                                | {0:M}    | March 19                                                 |
| "O", "o"  | Round-trip date/time pattern.                     | {0:O}    | 2021-03-19T12:15:30.0000000+02:00                        |
| "R", "r"  | RFC1123 pattern.                                  | {0:R}    | Fri, 19 Mar 2021 10:15:30 GMT                            |
| "s"       | Sortable date/time pattern.                       | {0:s}    | 2021-03-19T12:15:30                                      |
| "t"       | Short time pattern.                               | {0:t}    | 12:15 PM                                                 |
| "T"       | Long time pattern.                                | {0:T}    | 12:15:30 PM                                              |
| "u"       | Universal sortable date/time pattern.             | {0:u}    | 2021-03-19 12:15:30Z                                     |
| "U"       | Universal full date/time pattern.                 | {0:U}    | Friday, March 19, 2021 10:15:30 PM                       |
| "Y", "y"  | Year month pattern.                               | {0:Y}    | March 2021                                               |

#### Enum Format Specifiers

| Character | Description                                       | Usage    | Example                                                  |
|-----------|---------------------------------------------------|----------|----------------------------------------------------------|
| G or g    | Displays the enumeration entry as a string value or the integer value if string representation is not available. If FlagsAttribute is set, string values are concatenated. | ToString("G") | "7" or "Red"               |
| F or f    | Displays the enumeration entry as a string value or as a summation of valid entries separated by commas.                                                | ToString("F") | "Monday, Saturday" or "Blue" |
| D or d    | Displays the enumeration entry as an integer value.                                             | ToString("D") | "7" or "11"                |
| X or x    | Displays the enumeration entry as a hexadecimal value with leading zeros.                       | ToString("X") | "00000007" or "0000000B"  |

#### Example:

```c#
public enum Color { Red = 1, Blue = 2, Green = 3 };
Color myColor = Color.Green;

Console.WriteLine("The value of myColor is {0}.", myColor.ToString("G")); // The value of myColor is Green.
Console.WriteLine("The value of myColor is {0}.", myColor.ToString("F")); // The value of myColor is Green.
Console.WriteLine("The value of myColor is {0}.", myColor.ToString("D")); // The value of myColor is 3.
Console.WriteLine("The value of myColor is 0x{0}.", myColor.ToString("X")); // The value of myColor is 0x00000003.
```
