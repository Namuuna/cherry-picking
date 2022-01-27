1. Have priority map processing function in case the mapping changes. 
2. Create a dictionary of possible combination of types and subtype relationships with their respective weights calculated from the priority map.
3. Process the input alerts, while saving the id and respective weights depending on the weight dict created in previous step. Order the output.
4. For the first 4 ids, get their title and get cosine similarity points between their title the priority maps' title_identifier. 
5. Get score(sum) depending on how many occurences happen. 

(Will probably change the algorithm again)
