---
markdown:
  image_dir: /assets
  path: file-operation.md
  ignore_from_front_matter: true
  absolute_image_path: false
export_on_save:
  markdown: true
---

# File Operation

## File

+ FIle is collection of related information.
+ Is used to store the data parmanently in file.
+ Can perform following list of operation:

  1. Open file
  2. Read or write
  3. Append
  4. Close

### 1. Opening a file

+ python has built-in function **open()** to open a file object
+ It return a file object.
+ >```python
  > #syntax
  >fileObjdect = open(fileName[,accessmode][,buffering]) 
  > ```

|Function|Dexcription|
|:---|:---|
|$open()$|opens a file and return an object|
|$close()$|used to close the file|

#### Different Modes

|Modes|Dexcription|
|:---|:---|
|$r$|Open for reading only|
|$rb$|reading in binary mode|
|$b$|open in binary mode|
|$r+$|open for reading and writing as well|
|$rb+$|reading and writing in binary mode|
|$W$|opens a file for writing only|
|$a$|opens a file for appending and reading|
|$t$|open in text mode(default)|
|$+$|open a file for updating (reading and writing)|

#### File object attribute

+ After opening a file object has following attribute

|Attribute|Description|
|:---|:----|
|Myfile$.closed$|Returns true if file is closed|
|Myfile$.mode$|Returns access Mode|
|Myfile$.name$|Returns name of the file.|

#### File object Methods

|Functions|Description|Syntax|
|:---|:---|:---|
|$read()$|It reads data depands up on size of character read(size). If size parameter read is not specified,it reads complete file.|FileObject.read([count])|
|$readline()$|To read individual line of a file.|FileObject.readline()|
|$tell()$|The tell() method tells you the current cusor position within a file.|FileObject.tell()|
|$seek()$|This method change the cursor position in the file.|seek(Offset[,]) <br>seek(0,0)|

#### Writing to  a file