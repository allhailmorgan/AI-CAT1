
% ==========================
% FACTS: Genders
% ======
male(charles). male(john). male(david). male(james). male(alex).
female(elizabeth). female(mary). female(lisa). female(emma). female(lily).

% ==============
% FACTS: Base Parent Relationships (parent(Parent, Child))
% ==================
% Grandparents to Parents
parent(charles, john).
parent(elizabeth, john).
parent(charles, mary).
parent(elizabeth, mary).

% Parents to Children
parent(john, david).
parent(lisa, david).
parent(john, emma).
parent(lisa, emma).

% Mary's children (David and Emma's cousins)
parent(james, alex).
parent(mary, alex).
parent(james, lily).
parent(mary, lily).


% ====================================================================
% RULES: Relationships
% ====================================================================

% A sibling shares at least one parent, and cannot be themselves
sibling(X, Y) :- 
    parent(P, X), 
    parent(P, Y), 
    X \= Y.

% Grandparent rule
grandparent(GP, GC) :- 
    parent(GP, P), 
    parent(P, GC).

% Grandchild rule
grandchild(GC, GP) :- 
    grandparent(GP, GC).

% Aunt or Uncle rule (Sibling of a parent)
uncle_or_aunt(UA, C) :- 
    parent(P, C), 
    sibling(UA, P).

% Specific Uncle (Male sibling of a parent)
uncle(U, C) :- 
    male(U), 
    uncle_or_aunt(U, C).

% Specific Aunt (Female sibling of a parent)
aunt(A, C) :- 
    female(A), 
    uncle_or_aunt(A, C).

% Cousin rule (Children of siblings)
cousin(X, Y) :- 
    parent(P1, X), 
    parent(P2, Y), 
    sibling(P1, P2).
