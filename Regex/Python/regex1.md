# Regex: Regular Expression
+ Import package `re`
+ Compile / Without compiling
+ Perform match


## Methods for matching
|Pattern Compile| Without Compile|
|-|-|
|pattern.search|re.search|
|pattern.match|re.match|
|pattern.fullmatch|re.fullmatch|
|pattern.split|re.split|
|pattern.findall|re.findall|
|pattern.finditer|re.finditer|
|pattern.sub|re.sub|
|pattern.subn|re.subn|
|pattern.flags|re.escape|
|pattern.groups|re.purge|
|pattern.groupindex|re.|
|pattern.pattern|re.|

## Match objects
||
|-|
|Match.expand(template)|
|Match.group([group1, ...])|
|Match.\_\_getitem\_\_(g)|
|Match.groups(default=None)|
|Match.groupdict(default=None)|
|Match.start([group])|
|Match.end([group])|
|Match.span([group])|
|Match.pos|
|Match.endpos|
|Match.lastindex|
|Match.lastgroup|
|Match.re|
|Match.string|

### 1. First step is to import package
+ `import re`

### 2. Then Compiling the expressions into patterns
+ ```python 
  import re
  pattern = re.compile('ab*')
  ```
> `\` : Backslash matching
> > We use raw string, that is string pre-fixed with `r` to remove the complexities when matching characters such as backslash(`\`).
<br/>
> > For example:  
Regular String : `"\\\\section" `
<br>
Raw String: `r"\\section"`


### 3. Performing matches Using pattern

#### 3.1 Pattern.search(string[, pos[, endpos]])

+ Scan and finds first match
+ Return a corresponding match object or  None
+ `string` : String to search from
+ `pos` : Integer starting point (Optional)
+ `endpos` : Integer ending point (Optional)


#### 3.2 Pattern.match(string[, pos[, endpos]])
+ Mataches at beginning of string
+ The optional pos and endpos parameters have the same meaning as for the search() method.


#### 3.3 Pattern.fullmatch(string[, pos[, endpos]])

+ Matches whole string at beginning
+ The optional pos and endpos parameters have the same meaning as for the search() method.


#### 3.4 Pattern.split(string, maxsplit=0)
#### 3.5 Pattern.findall(string[, pos[, endpos]])
#### 3.6 Pattern.finditer(string[, pos[, endpos]])
#### 3.7 Pattern.sub(repl, string, count=0)
#### 3.8 Pattern.subn(repl, string, count=0)
#### 3.9 Pattern.flags
#### 3.10 Pattern.groups : The number of capturing groups in the pattern.
#### 3.11 Pattern.groupindex :A dictionary mapping any symbolic group names defined by (?P<id>) to group numbers.
#### 3.12 Pattern.pattern : The pattern string from which the pattern object was compiled.






