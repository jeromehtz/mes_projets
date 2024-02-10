#use "list_tools.ml";;

(" 
nous allons repeter recursivement l'algorithme dinsertion d'une valeur
dans une liste triée en ordre croissant 
nous allons egalement verifier si la liste est triee sinon on 
ne peut pas inserer de valeur
")

let croissante liste = match liste with
    liste when length liste = 0 -> true
  | liste -> 
    let e1::rest = liste in
    let rec croiss elt li = match (elt,li) with
        (_,[]) -> true
      | (elt,e::l) -> e>elt && croiss e l
    in croiss e1 rest;;

let insert x list =
  let rec insert_rec list booleen = match (list,booleen) with
      ([],true) -> []
    | ([],false) -> x::[]
    | (e::l,b) when e>x && b=false -> x::e::insert_rec l (true)
    | (e::l,b) -> e::insert_rec l b 
  in insert_rec list false;;

let insertion_sort list = 
  let rec insertion_rec list res = match list with
      [] -> res
    | e::l -> let res = insert e res in insertion_rec l res 
  in insertion_rec list [];;

