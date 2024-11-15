#### Commnets in C#
- Single Line
    - Starts with `//` to forward slashes
- Multi Line
    - Starts with `/*` and continues till next `*/`
- XML Documentation Comment
    - Start with `///` and then xml content
    - Mainly used to describe the code with predefined set of xml tags.
    - Then a build process can be run to generate Documentation, there are multiple ways
    but easiest is to update the `.csproj` file by adding following to `<PropertyGroup>`
        - `<GenerateDocumentationFile>true</GenerateDocumentationFile>` : Specifies that we want the Documentation to be generated
        - `<DocumentationFile>DocumentationFileName.xml</DocumentationFile>` : Specifies location and filename to be generated
        - Run : `dotnet build` 
