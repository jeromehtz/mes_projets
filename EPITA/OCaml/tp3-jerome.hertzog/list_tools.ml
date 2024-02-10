(* debut TP *)

let rec length list = match list with
    [] -> 0
  | e::l -> 1+length l ;;

let get_min list = match list with
     [] -> invalid_arg"get_min : empty list"
   | _ -> let e::rest = list in
     let rec min elt liste = match liste with
         []-> elt
       | e::l when e<elt -> min e l
       | e::l -> min elt l
     in min e rest ;;

let nth n list = match n with
    n when n<0 -> invalid_arg"nth : index must be a natural"
  | n -> let rec find n liste = match (n,liste) with
             (0,e::l) -> e
           | (_,[]) -> failwith"nth : list too short"
           | (i,e::l) -> find (n-1) l
         in find n list ;;

let insert x list = match list with
    [] -> x::[]
  | _ -> let rec insert_ x liste booleen = match liste with
             [] -> []
           | e::l when e>x && booleen = false -> x::e::insert_ x l (true)
           | e::l when booleen = true -> e::insert_ x l (true)
           | e::l -> e:: insert_ x l booleen
         in insert_ x list false ;;

let remove x list = match list with
    [] -> x::[]
  | _ -> let rec remove_ x liste booleen = match liste with
             [] -> []
           | e::l when e=x && booleen = false -> remove_ x l (true)
           | e::l when booleen = true -> e::remove_ x l (true)
           | e::l -> e::remove_ x l booleen
         in remove_ x list false ;;

let rec init_list n x = match n with
    0 -> []
  | n -> x::init_list (n-1) x ;;

let put_list x i liste =
    if (length liste <> 0 && i=0) || (liste = [] && i<>0) then liste
    else
      let rec replace_ i liste booleen = match (i,liste) with
        | (0,[]) -> []
        | (_,[]) -> invalid_arg "list too short"
        | (i,e::l1) when i=0 && booleen = false -> x::replace_ (0) l1 (true)
        | (0,e::l) when booleen = true -> e::replace_ 0 l (true)
        | (i,e::l1) -> e::replace_ (i-1) l1 booleen
      in replace_ i liste false ;;

let rec init_board (l,c) x = match l with
  | 0 -> []
  | l -> init_list c x :: init_board (l-1,c) x ;;

let rec get_cell (x,y) board = match (x,board) with
  | (0,e::b) -> (let rec find y liste = match (y,liste) with
                   | (0,e::l) -> e
                   | (_,[]) -> invalid_arg"get_cell : list too short"
                   | (y,e::l) -> find (y-1) l
                 in find y e)
  | (_,[]) -> invalid_arg"get_cell : board too short"
  | (x,e::b) -> get_cell (x-1,y) b ;;

let rec put_cell v (x,y) board = match (x,y,board) with
  | (0,0,[]) -> []
  | (_,_,[]) -> invalid_arg"..."
  | (0,y,e::b) -> (put_list v y e)::put_cell v (0,0) b
  | (x,y,e::b) -> e::put_cell v (x-1,y) b ;;
