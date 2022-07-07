---
markdown:
  image_dir: /assets
  path: data_structure.md
  ignore_from_front_matter: true
  absolute_image_path: false
export_on_save:
  markdown: true
---
# 1. Data Structure

## Definition

+ It way is a of storing and organising data.
+ Allow performing operatios on data easily.
  
## Types of Data Structure

+ Primitive (built-in)
  + Integer
  + Float
  + Character
  + Pointer
+ Non-Primitive
  + Files
  + Lists
    + Linear
      + Arrays
      + Stack
      + Linked List
      + Queues
    + Non-Linear
      + Graphs
      + Trees

```dot
digraph typesOfDS{
     a[label="Data Structure", shape="Box"];
     b[label="Primitive", shape="Box"];
     c[label="Integer", shape="Box"];
     d[label="Float", shape="Box"];
     e[label="Character", shape="Box"];
     f[label="Pointer", shape="Box"];
     g[label="Non-Primitive", shape="Box"];
     h[label="Files", shape="Box"];
     i[label="Lists", shape="Box"];
     j[label="Linear", shape="Box"];
     k[label="Non-Lienar", shape="Box"];
     l[label="Arrays", shape="Box"];
     m[label="Stack", shape="Box"];
     n[label="Linked List", shape="Box"];
     o[label="Queues", shape="Box"];
     p[label="Graphs", shape="Box"];
     q[label="Trees", shape="Box"];
     r[label="Binary Trees", shape="Box"];
     s[label="B-Trees", shape="Box"];
     t[label="Heaps", shape="Box"];
     hash[label="Hash Table",shape="Box"];

    a -> b
    b -> c
    b -> d
    b -> e
    b -> f

    a -> g
    g -> h
    g -> i

    i -> j
    i -> k

    j -> l
    j -> m
    j -> n
    j -> o

    k -> p
    k -> q

    l -> hash

    q -> r
    q -> s
    q -> t

}
```

## Operations

|Operation| What does it means? |
|:---|:---|
| Creation  | Allocation of memory space for data elements.|
| Deletion  | Deallocation of memory space assigned to a specific data structure.|
| Selection | Accessing a particular data item in a data structure.|
| Insertion | Inserting data item in a data structure.|
| Updation  | Updating a data item by re-insertion at same place or deletion.|
| Sorting   | Arranging all the data items in a specific order.|
| Merging   | Combining tow or more data items in a single unit.|
| Traversing| Accessing all the data items at least once in a data structure.|