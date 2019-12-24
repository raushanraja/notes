## Redux

+ Store
+ Reducer
+ Action
+ View
+ Container
+ Selector
+ Component


### PR.1.0
#### redux-act, react-
+ create an action with `createAction(type,playloadCreator,metaCreator)`
    + contains type to identify the action andn what the payload be.
|:--|:--| :--|
|tpye|required|str|
|payloadCreator|required|function| 
|metaCreator|optional|function| 

+ Create a reducer using `createReducer(handler,[defaultState])`
    + handler: object or function 
    + [defaultState]: a default state

+ Create a method in selector 

+ Add to Container pages
    + Add mapStateToProps for allowing access
    + Add mapDispatchToProps for dispatching action