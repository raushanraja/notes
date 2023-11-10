### React Component:
- React components are javascript function that return markup.
- Each component must start with Capital Letter.
- Declaring a component
```js
function MyButton(){
    return <button> I am a button</button>
}
```
- Nesting a component is just putting one component inside another one
```js
function My App(){
    return (
        <div>
            <h1> Welcom to my app</h1>
            <MyButton/>
        </div>
    );
};
```
- All of the  syntax seen above is called a JSX. It's optional but mostly used in react projects.
- There are some basic rules for JSX
    - Each component can return only one top level tag.
    - All tags should be closed.

### Adding Style to React
- React allows adding styles in two ways:
    1. Using `className` attribute
        - Which is similar to `class` in HTML.
        - And takes space separated class name as input.
    2. Using `style` attribute
        - which takes Object of k-v pair as input.
        - example: style={ {color:'red', fontWeight:'bold'} }
```js
import './App.css'
import MyButton from './button';

function App() {
  const [count, setCount ] = useState(0);

  return (
    <div className='medium'>
        <div className='bold'>Welcom to my counter app, current count:
            <span className='bolditalic' style={{color:'whitesmoke'}}>
                {count}
            </span>
        </div>
        <MyButton setCount={setCount}/>
    </div>
  )
}

export default App
```

### Displaying Data
- JSX allows putting markup into JavaScript.
- To do this we use curly braces `{}` which let's escape back into JS
so we can embed some variable into code and display to user.
```js
function UserInfo(){
    const details = {
        "name": "Jonh",
        "phone" : "1234567"
    }

    return (
        <>
            <h4> Name: {details.name} </h4>
            <h4> Phone: {details.phone} </h4>
        </>
    )
}
```

### Conditional Rendering
- Conditional Statment in reacts as same as in regular Javascript.
- So they can be used as is, for rendering purpose
- Using `if-else`
```js
if(loggedIn){
    content = <AdminPanel/>;
}
else {
    content = <LoginForm>;
}

return (
    { div>
        {content}
    </div> }
)
```

- Using Conditional `?` operator
```js
return (
    <div>
        {isloggedIn? <AdminPanel/> : <LoginForm/>}
    </div>
)
```

- Using `&&` Operator, when there is no else
```js
return (
    <div>
        {isloggedIn && <AdminPanel/>}
    </div>
)
```

### Rendering List
- Mostly `for loop` and `map` are used to render list of components
```js
const products = [
    {title:"Apple", isFruit: true, id:1},
    {title:"Garlic", isFruit:false, id:2}
];

export default function IsFruit(){
    const listItems = products.map((item,_)=>{
        return(
         <li key={item.id}>
           Is {item.title} a fruit? : {item.isFruit ? 'Yes' : 'No'}
        </li>    
        )
});


    return (
        <ul>
            {listItems}
        </ul>
    );
}

```


### Responding to Event
- Reponse to event form a React Component is done by declaring an event handle method and attaching that method to specific event.
```js
function SayHello(){

    function alertHello(){
        alert("Hello, You clicked Me")
    }

    return <button onClick={alertHello}> Click Me</button>
}

``` 

### Updating the Screen
- When we want to remeber some information, display it and  update is later.
- For this we now use  hook `useState`
- `useState` return two things: 
    1. The current value
    2. The method to update the value
```js
function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      Clicked {count} times
    </button>
  );
}
```

### Using Hooks
- All the function in ReactJS library starting with `use` are hooks, such as `useState`, `useMemo`, `useRef`, `useEffect`
- These are function which allows use to use React's State and LifeCycle methods inside a functional component.
- An example is already given above, that show the use of `useState` hook.

### Sharing Data between componenets
- To share the data between two component, the data is moved from individual component "upwards" to the closest parent compnent of all the.
- In the example given below
    - The `count` state and `handleClick` is moved from individual `Button` component "upward" to `MyApp` component
    - Which (MyApp) is the closest parent componenet of both `Button`.
```js 
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}

```