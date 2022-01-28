Notes:
1. Function process_map() processes priority_map in case the mapping changes. 
1.1. Creates a dictionary of possible combination of types and subtype relationships with their respective weights calculated from the priority map.
1.2. Creates title weights. If word is repeated, then its weight will be: from weight coefficient(derived from the length of priority map) subtract the average of title weights.

2. Cherry_Pick(): Calculate weights for each input alert object based on the dictionary of types weights created in previous step. Also, gets cosine similarity value between input alert title and priority map title, which then added to the overall score/weight. 


Run Time Complexity:

Process_map(): O(ab) 
    a => number of priority map objects
    b => number of keys in priority map (4)

Cherry_pick(): O(nxm) 
    n => number of inputs 
    m => vector of input title and title identifier from the map 

Output example: 
[('000000002', 12.0), ('000000004', 11.142857142857142), ('000000001', 6.0), ('000000003', 5.0)]
Execution time: 0.005081299999999955



