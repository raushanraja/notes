#### Solid JS Primitives:
1. Signal : `createSignal`
2. Memo: `createMemo`
3. Effect: `createEffect`

##### 1. Signals
+ Simplest primitive, it contains a value and get/set function
+ Eg: `const [count, setCount] = createSignal(0)`
  
##### 2. Effects
+ Effects are functions
+ It wraps & reads the `Signal` value and re-executes whenever a `Signal's` value changes
+ Useful for creating side effects, like rendering.
+ Eg: `createEffect(()=>console.log("The count is ",count()))`
##### 3. Memo
+ Memos are cached derived values.
+ Shares the properties of both `Signals` and `Effects`.
+ Memos have their own dependent singal and
+ Memos values changes when their Signal changes.
+ Eg: ``const fullName = createMemo(() => `${firstName()} ${lastName()}`);``