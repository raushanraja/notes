## string:
- string is immutable object of type String, whose value is text.
- Internally, the text is stored as sequence of readonly `Char` object.
- There is no null-terminating character at the end of C# string.
- This type is thread safe.

### Properties:
- `Length`
    - Length property represent the nubmer of `Char` object
        and not the number of unicode characters.
- `Chars`
    - Get the `Char` object at specified position in current String object.
- Examples:
```c#
string s = "hello world";
Console.WriteLine($"String Length: {s.Lenght}");
Console.WriteLine($"Chat at index 5: {s[5]}");
```

### Methods (To perform operations on string):

| Method                                  | Description                                                                                              |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------|
| Clone()                                 | Returns a reference to this instance of String.                                                          |
| Compare(String, ...)                    | Compares substrings of two specified String objects and returns an integer indicating their position.    |
| Concat(...)                             | Concatenates strings or string representations of objects.                                               |
| Contains(...)                           | Returns a value indicating whether a specified character or substring occurs within this string.         |
| Copy(...)                               | Creates a new instance of String with the same value as a specified String.                              |
| CopyTo(...)                             | Copies characters from this instance to an array or span.                                                |
| Create(...)                             | Creates a new string with specific formatting or length.                                                 |
| EndsWith(...)                           | Determines whether this string ends with a specified character or substring.                             |
| EnumerateRunes()                        | Returns an enumeration of Rune from this string.                                                         |
| Equals(...)                             | Determines whether this instance has the same value as another string.                                   |
| Format(...)                             | Replaces format items in a string with the string representation of objects.                             |
| GetEnumerator()                         | Retrieves an object to iterate through the characters in this string.                                    |
| GetHashCode()                           | Returns the hash code for this string.                                                                   |
| GetType()                               | Gets the Type of the current instance.                                                                   |
| IndexOf(...)                            | Reports the index of the first occurrence of a character or substring.                                   |
| IndexOfAny(...)                         | Reports the index position of the first occurrence of any character in a specified array.                |
| Insert(...)                             | Inserts a string at a specified index position.                                                          |
| Intern(...)                             | Retrieves the system's reference to the specified String.                                                |
| IsInterned(...)                         | Retrieves a reference to a specified String.                                                             |
| IsNullOrEmpty(...)                      | Indicates whether the specified string is null or empty.                                                 |
| IsNullOrWhiteSpace(...)                 | Indicates whether a specified string is null, empty, or consists only of white-space characters.         |
| Join(...)                               | Concatenates strings with specified separators.                                                          |
| LastIndexOf(...)                        | Reports the index position of the last occurrence of a character or substring.                           |
| LastIndexOfAny(...)                     | Reports the index position of the last occurrence of any character in a specified array.                 |
| Length                                  | Gets the number of characters in this string.                                                            |
| MemberwiseClone() 	                  | Creates a shallow copy of the current Object. (Inherited from object)                                    |
| Normalize(...)                          | Returns a new string with specified Unicode normalization.                                               |
| PadLeft(...)                            | Pads the left side of the string with spaces or specified characters.                                    |
| PadRight(...)                           | Pads the right side of the string with spaces or specified characters.                                   |
| Remove(...)                             | Removes characters from the string at specified positions.                                               |
| Replace(...)                            | Replaces occurrences of a specified character or substring with another string.                          |
| Split(...)                              | Splits the string into substrings based on specified delimiters.                                         |
| StartsWith(...)                         | Determines whether the string starts with a specified character or substring.                            |
| Substring(...)                          | Retrieves a substring from the string.                                                                   |
| ToCharArray()                           | Copies the characters in the string to a character array.                                                |
| ToLower()                               | Converts the string to lowercase.                                                                        |
| ToLowerInvariant()                      | Converts the string to lowercase using the invariant culture.                                            |
| ToUpper()                               | Converts the string to uppercase.                                                                        |
| ToUpperInvariant()                      | Converts the string to uppercase using the invariant culture.                                            |
| Trim()                                  | Removes leading and trailing white-space characters.                                                     |
| TrimEnd()                               | Removes trailing white-space characters.                                                                 |
| TrimStart()                             | Removes leading white-space characters.                                                                  |
| TryCopyTo(...)                          | Copies the contents of this string into a destination span.                                              |

