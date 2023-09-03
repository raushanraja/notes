# 1.Canvas:
- HTML Element
- Provides an API to draw graphics using JS and HTML

## 2.Basic Usage
- Add an `<canvas></canvas>` element in HTML with id.
- Access the canvas element in js using `id` of above element
- Get the canvas context using `getContext('ContextType')` of the canvas element
- Start drawing using method provided by API such as `fillRect()` ... follow the docs for more. 

### 3.Canvas Coordinate System
- Canvas is two axis System (x , y)
- The Top-Left point of the canvas element is (0,0)
- And it increases as we move along x-axis or y-axis


#### 4. Porperties
|Property|Description|Values|
|-|-|-|
|`canvas` | HTMLCanvasElement | 
|`direction` | Current text direction | "ltr" , "rtl", "inherit"|
|`fillStyle` | The color, gradient, or pattern to use inside shapes |
|`filter` | Similar to the CSS filter property |
|`font` | Current text style for drawing text | 
|`fontkerning` | Specifies how fontkerning is user | "auto", "normal", "none"|
|`fontStretch` | How the font may be expanded or condensed | ultra-condensed, extra-condensed, condensed, semi-condensed, normal (default), semi-expanded, expanded, extra-expanded, ultra-expanded|
|`fontVariantCaps` | An alternative capitalization of the rendered text. | value CSS font-variant-caps property|
|`globalAlpha`| Alpha (transparency) value. | between 0 and 1.|
|`globalCompositeOperation` | Sets the type of compositing operation to apply | [Composite Operation](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Compositing/Example)|
|`imageSmoothEnabled` | Whether scaled images are smoothed. | true (default value), false. |
|`imageSmoothingQuality` | Set the quality of image smoothing. | "low", "medium", "high"|
|`letterSpacing` | Specifies the spacing between letters. | Corresponds to the CSS letter-spacing property.|
|`lineCap` | The shape used to draw the end points of lines. | "butt", "round", "square"|
|`lineDashOffset` | Sets the line dash offset, or "phase."  | Float value, default = 0.0|
|`lineJoin` | The shape used to join two line segments where they meet. | "round", "bevel", "miter" |
|`lineWidth` | Sets the thickness of lines. | A float, default = 1.0|
|`miterLimit` | Sets the miter limit ratio. | A float, default = 10.0|
|`shadowBlur` | The amount of blur applied to shadows.| Non-negative float, default = 0;|
|`shadowColor` | The color of shadows. |  A string parse as css color value.|
|`shadowOffsetX`  | The distance that shadows will be offset horizontally. | A float, default = 0 |
|`shadowOffsetY` | Specifies the distance that shadows will be offset vertically. | A float, default = 0|
|`strokeStyle` | The color, gradient, or pattern to use for the strokes. | A string parse css value, default = #000|
|`textAlign` | The current text alignment in use. | "left", "right", "center", "start", "end"|
|`textBaseLine` | The current text baseline in use | "top", "hanging", "middle", "alphabetic", "ideographic", "bottom"|
|`textRendering` | Inform the rendering engine about what to optimize for text rendering | "auto", "optimizeSpeed", "optimizeLegibility", "optimizePrecision"|
|`wordSpacing` | The spacing between words | Word spacing as a string in the CSS length data format , default = "0px" |

#### 5. CanvasRenderingContext2D Instance Methods:
|Method|Description|
|-|-|
|`arc(x, y, radius, startAngle, endAngle[, counterclockwise])`| Create circular arc|
|`arcTo(x1, y1, x2, y2, radius)`| Create circular arc based on control point (x1,y1) & (x2,y2)|
|`beginPath()`| Start a new path, clear old sub-path list.|
|`bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y)`| Create a cubic Bezier curve based on control paths(cp) and endpoint (x,y)|
|`clearRect(x, y, width, height)`| Set the pixel in reactangular area (x,y,w,h) to rgba(0,0,0,0) [black transparent]|
|`clip(path, fillRule)`| Turns the current or given path into the current clipping region. Both argument are optional|
|`closePath()`| Attempts to add a straight line from the current point to the start of the current sub-path. Needs stroke() and fill().|
|`createConicGradient(startAngle, x, y)`| It creates a gradient around a point with given coordinate. Needs addColorStop(stop, color)|
|`createImageData(width, height[, settings])`| Creates a new, blank(transparent) ImageData object.|
|`createLinearGradient(x1, y1, x2, y2)`| Creates a gradient along the line connecting two given coordinates. addColorStop(stop, color) Needed|
|`createPattern(image, repetition)`| Creates a pattern using the specified image and repetition.|
|`createRadialGradient(x0, y0, r0, x1, y1, r1)`| Creates a radial gradient using the size and coordinates of two circles. addColorStop(_,_) Needed.|
|`drawFocusIfNeeded([path,] element)`| Drwas a focus ring around the path if specified element is focused.|
|`drawImage(image, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight)`| Provides way to dram an image onto the canvas. 3 variants of this method exist based on arguments.|
|`ellipse(x, y, radiusX, radiusY, rotation, startAngle, endAngle[, counterclockwise])`| Creates an ellipse arc.|
|`fill(path, fillRule)`| Fills the current path with fillStyle. Both ars are optional.|
|`fillRect(x, y, width, height)`| Draws a rectangle that is filled according to the current fillStyle.|
|`fillText(text, x, y[, maxWidth])`| Draws a text string with filling character with current fillStyle.|
|`getContextAttributes()`| Returns an object that contains attributes used by the context (which were passed at time of initializing the context).|
|`getImageData(sx, sy, sw, sh[, settings])`| Returns an ImageData object representing the underlying pixel data for a specified portion of the canvas.|
|`getLineDash()`| Retuns the current line dash pattern. |
|`getTransform()`| Returns the current transformation matrix being applied to the context.|
|`isContextLost()`| Retuns bool value based on if rendering context is lost for some reason(Ran out of Memory etc). EXPERIMENTAL|
|`isPointInPath(path, x, y, fillRule)`| Returns whether or not the specified point is contained in the current path. 4 variants . see docs |
|`isPointInStroke([path,] x, y)`| Returns whether or not the specified point is inside the area contained by the stroking of a path. |
|`lineTo(x, y)`| Draws a straint line between current sub-path and to the point(x, y)|
|`measureText(text)`| Returns  a TextMetrics object that contains information about the measured text (such as its width, for example). |
|`moveTo(x, y)`| Start a new sub-path at given point(x, y). |
|`putImageData(imageData, dx, dy[, dirtyX, dirtyY, dirtyWidht, dirtyHeight])`| Paints data from the given ImageData object onto the canvas. |
|`quadraticCurveTo(cpx, cpy, x, y)`| Draws a quadratic Bezier cruve to current sub-path.|
|`rect(x, y, width, height)`|  Draws rectangle to the current path. |
|`reset()`| Resets the rendering context to its default state, allows it to be reused.|
|`resetTransform()`| Resets the current transform to the identity matrix.|
|`restore()`| Restores the most recently saved canvas state by popping the top entry in the drawing state stack.|
|`rotate(angle)`| Adds a rotation to the transformation matrix. |
|`roundRect(x, y, width, height, radii)`| Adds a rounded rectangle to the current path. Radii is a number or a list. Similar to border-radius.|
|`save()`| Saves the entire state of the canvas by pushing the current state onto a stack. |
|`scale(x, y)`| Adds a scaling transformation to the canvas units horizontally and/or vertically. |
|`scrollPathIntoView(path)`| Scrolls the current or given path into view. It is similar to Element.scrollIntoView(). Path is optional. EXPERIMENTAL|
|`setLineDash(segments)`| Sets the line dash pattern used when stroking lines. segments is array of number specifying distance.|
|`setTransform(matrix)`| Resets the current transformation to the identity matrix, and create a transformation described by the given arguments. 2 variants. |
|`stroke(path)`| Strokes (outlines) the current or given path with the current stroke style. Path is optional.|
|`strokeRect(x, y, width, height)`| Draws a stroked reactangle as per provided strokeStyle.|
|`strokeText(x, y[, maxWidth])`| Draws just outlines of the text (no fill).|
|`transform(a, b, c, d, e, f)`| Multiplies the current transformation with the given matrix. Heps in scale, rotate, translave(move) and skew the context.|
|`translate(x, y)`| Moves the current object by moving canvans origin by x and y units. setTransform() is called to reset the current transformation. |
