## StringBuilder
- StringBuilder class Provides a mechanism for efficient string manipulation, especially when you need to concatenate a large number of strings.
- The StringBuilder class in C# is a part of the System.Text namespace, and allows creation of dynamic objects.

### Why StringBuilder
In C#, strings are immutable, meaning they cannot be changed after creation. 
Modifying a string creates a new one, consuming memory unnecessarily. 
StringBuilder, however, offers a mutable buffer for efficient string manipulation by directly modifying the existing string, avoiding excessive memory allocations and copying.


### Common Methods
| Property/Method                        | Description                                                                                                  | Example Use                                                                                         |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Capacity                               | Gets or sets the maximum number of characters that can be contained in the memory allocated by the current instance. | `StringBuilder sb = new StringBuilder(); sb.Capacity = 1000;`                                    |
| Chars[Int32]                           | Gets or sets the character at the specified character position in this instance.                              | `char myChar = sb.Chars[0];`                                                                       |
| Length                                 | Gets or sets the length of the current StringBuilder object.                                                  | `sb.Length = 10;`                                                                                   |
| MaxCapacity                            | Gets the maximum capacity of this instance.                                                                   | `int maxCap = sb.MaxCapacity;`                                                                     |
| Append(),                              | Appends the string representation of specified values to this instance.                                       | `sb.Append(true); sb.Append(42);`                                                              |
| AppendFormat(),                        | Appends the string returned by processing a composite format string                                           | `sb.AppendFormat("GHI{0}{1}", 'J', 'k');`|
| Insert()                               | Inserts the string representation of specified values into this instance at the specified character position. | `sb.Insert(0, true); sb.Insert(5, 'X'); `|
| Remove(Int32, Int32)                   | Removes the specified range of characters from this instance.                                                  | `sb.Remove(0, 5);`|
| Replace()                              | Replaces specified characters or strings in this instance with other specified characters or strings.          | `sb.Replace('a', 'b'); sb.Replace("Hello", "Hi");`                                            |
| ToString()                             | Converts the value of this instance to a String.                                                              | `string result = sb.ToString();`                                                                   |
| EnsureCapacity(Int32)                  | Ensures that the capacity of this instance of StringBuilder is at least the specified value.                 | `sb.EnsureCapacity(1000);`                                                                          |
| Clear()                                | Removes all characters from the current StringBuilder instance.                                               | `sb.Clear();`                                                                                       |
| AppendLine()                           | Appends specified strings, or a default line terminator, to the end of the current StringBuilder object.      | `sb.AppendLine(); sb.AppendLine("Hello");`                                                     |
| CopyTo()                               | Copies characters from this instance to a destination Char array or Span<Char>.                            | `char[] dest = new char[10]; sb.CopyTo(0, dest, 0, 5);`                                            |
| GetChunks()                            | Returns an object that can be used to iterate through the chunks of characters represented in a ReadOnlyMemory<Char> created from this StringBuilder instance. | `var chunks = sb.GetChunks();`                                                                   |
| Equals(Object), GetHashCode(), GetType(), ... | Common Object methods and properties inherited by StringBuilder.                                          | `bool areEqual = sb.Equals(otherStringBuilder); int hashCode = sb.GetHashCode();`              |


### StringBuilder vs String concatenattion Comparision
| Aspect         | StringBuilder | Regular String concatenattion         |
|----------------|----------------|--------------------------------------|
| Performance    | More efficient | Less efficient                       |
| Memory Usage   | Less memory    | More memory                          |
| Readability    | More control   | Easier to read                       |
| Mutability     | Mutable        | Immutable                            |

