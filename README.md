## Analyzing-Interview-Transcripts
### Or: How to deal with big amounts of qualitative data?
---
**Project Description**
- I have the transcripts of several 90min interviews with students
- Not all the parts of the interview are relevant
- I want to identify the parts when students explain the given phenomena
- These explanations should be categorized into what we call "narrative mode" or "scientific mode"
- There a certain language features that indicate which "mode" the student is in
- In the end it would be valuable to know how long they are in each mode and how many switches occur
- We consider this useful, because depending on the mode the student is mainly in, he or she might prefer different instructional and informational material
- So far there are no consistent results for the benefit of using narrative texts in science education
- We assume that students in the narrative mode prefer texts with a narrative structure and students in the scientific mode prefer scientific texts

*Theoretical Background*

1. **The narrative mode** is active when individuals interpret events around them using a story-like pattern, in which characters and their actions shape the unfolding plot. It is characterized by agents that act in accordance with their intentions or motivation. If applied in a scientific context, misconception may arise. A Student in our interview said for example: "The bacteria eat the food, because they need food." The need for food is a human experience that was used to interpret an experiment that the students were conducting. 
2. **The scientific mode** in comparison is based on formal logical reasoning. It is also reflected in what we know today as the scientific method, where hypothesis are tested and accepted or rejected. It is applied when constructing arguments or theories. A student in the scientific mode would say "The bacteria process the food waste."

*Method*

In this exploratory study students were interviewed about the causes and effects of food waste. At each step of the activity they got more information and were asked to integrate this information into their explanations and their drawings. After each step the interviewer asked them about their drawings and their explanations. The aim was to see students pre-concepts, their thinking patterns and the way they explain causal relations.

*Language Features for the two modes of thought*

| Feature | Narrative Mode| Scientific Mode| 
| ---------------------- | ----------------------------------- |------------------------------ |
|Agents/characters    | Agents with intention "The bacteria eats food" | Entity interacting with environment or processes without human intention "The bacteria process food waste" | 
|Verbs| Action Verbs "The gases opened a hole in the atmosphere" | Verbs related to processes and interactions "Substances break down in water" |
|Tense| Past Tense "The gases left the garbage pile" | Present Tense "The garbage pile releases gases." |
|Pronouns & Voice | Personal Pronouns, Active Voice "We destroyed their homes" | Impersonal, Passive Voice "Their habitat was destroyed." |
|Structure | story-like: beginning, middle, end "Somebody throws away food, then the bacteria eat it, the gases get out and want to go up. They make a hole in the atmosphere and more light gets to the pole and then the polar bears die." | mechanistic: set-up, interaction between entities, final state "People throw away food. It ends up on landfills. Bacteria break down the food waste and release methane. Methane is a greehhouse gas and leads to increasing temperatures which is why the glaciers melt and the polar bears loose their habitat."|
| Metaphors | Based on embodied experiences "It's like when we drink cola, we don't need the gas. So the bacteria doesn't need the gas and it gets out."| Structural metaphors "The light is reflected back by the greenhouse gases like a mirror."| 

*Procedure*

The code is scanning the transcripts for words that were pre-defined as narrative or scientific. The second one doing basically the same, but based on the different word use due to the different semantics like active voice in the narrative mode in comparison to passive voice in the scientific mode. The results were not very good, because when a student uses a word in plural or in a slightly different expression, the code cannot identify the word and misses matches for each mode. That's why I tried to come up with a different code that integrates a large langual model (here chat gpt, and the open source version Ollama).

__Input File__

Excel File with two columns:
- one for the students utterances
- one for the two students (here: ב and ג)

__Output Files__

Two excel files: 
- one with the summarized results of the percentage of narrative and scientific mode for each student
- one with the classification for each mode

*How to run the code*

-> copy this respository
-> import the following modules: pandas, openpyxl, tqdm (the first two to process the excel file, the last one to show progress of the analysis)
-> run the code on pycharm


 *Data Source*
 1. The transcript contains dialogues between a pair of students and the interviews of the group with the researcher.
 3. The data are confidential so I need to make sure it's anonymized

 
:memo: **Technical Aspects**
- Right now transcrips appear in an excel file, maybe I have to transfer everything to a text file



---
This project is part of a [Python Course](https://github.com/Code-Maven/wis-python-course-2025-03) at Weizmann Institute
