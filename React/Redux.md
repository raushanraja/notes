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
1. create an action with `createAction(type,playloadCreator,metaCreator)`
    + contains type to identify the action andn what the payload be.
        |parameter 1| isRequired|datatype|
        |--|--|--|
        |tpye|required|str|
        |payloadCreator|required|function| 
        |metaCreator|optional|function| 

2. Create a reducer using `createReducer(handler,[defaultState])`
    + handler: object or function 
    + [defaultState]: a default state

3. Create a method in Selector 

4. Add to Container pages
    + Add mapStateToProps for allowing access
    + Add mapDispatchToProps for dispatching action