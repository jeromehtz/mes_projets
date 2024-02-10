("
nous avons besoin de deux fonctions. La premiere aura comme role de selectionner le max
dans la liste de depart. il faut aussi trouver comment supprimer le max.
la deuxieme appelle ce principe recursivement. et on va cons a chaque fois les valeurs
")

#use "list_tools.ml";;

let get_max list =
  let e::rest = list in
    let rec max elt liste = match liste with
        [] -> elt
      | e::l when e>elt -> max e l
      | e::l -> max elt l
     in max e rest ;;

let remove x liste = 
  let rec remove_rec liste res booleen = match (liste,res,booleen) with
      ([],_,false) -> invalid_arg "remove : impossible de supprimer"
    | ([],r,true) -> r
    | (e::l,r,b) when x=e -> remove_rec l r (true)
    | (e::l,r,b) -> e::remove_rec l r b 
  in remove_rec liste [] false;;

let selection_sort list = 
  let rec selection_sort_rec liste res = match liste with
      [] -> res
    | liste -> let max = get_max liste in selection_sort_rec (remove max liste)(max::res)
  in selection_sort_rec list [];;