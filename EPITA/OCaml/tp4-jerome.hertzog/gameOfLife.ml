(* commentaire *)
#use "list_tools.ml";;

let rules0 cell near = match (cell,near) with
    (0,3) -> 1
  | (1,n) when n=2 || n=3 -> 1
  | (_,_) -> 0;;

let rec game_ y u c list = match (u,list) with
    (u,[]) -> c 
  | (u,e1::l) when (u=y-1 || u=y) && e1=1 -> game_ y (u+1) (c+1) l
  | (u,e1::l) when u=y+1 -> if e1=1 then c+1 else c
  | (u,e1::l) -> game_ y (u+1) c l;;

let rec game1 y t x u c booleen list = match (u,list,booleen) with
    (u,[],b) -> (c,b)
  | (u,e1::l,b) when u=y && t=x && e1=1 -> game1 y t x (u+1) c true l  
  | (u,e1::l,b) when u=y-1 && e1=1 -> game1 y t x (u+1) (c+1) b l
  | (u,e1::l,b) when u=y+1 -> if e1=1 then (c+1,b) else (c,b)
  | (u,e1::l,b) -> game1 y t x (u+1) c b l;;
  


let count_neighbours_bonus (x,y) board size =  
  let rec aux v compteur booleen list = match (v,list,booleen) with
    | (t,[],_) -> invalid_arg "on ne rentrera presque jamais dans ce cas"
    | (t,e::l,b) when t=x-1 ->
        let compt = (game_ y 0 compteur e) in aux (t+1) compt b l
    | (t,e::l,b) when t=x ->
        let (compteur, b) = (game1 y t x 0 compteur false e) in aux (t+1) compteur b l
    | (t,e::l,b) when t=x+1 ->
        let compt = (game_ y 0 compteur e)
        in (b = false && compt = 3) || (b = true && (compt = 2 || compt = 3))
    | (t,e::l,b) -> aux (t+1) (compteur) (b) (l)
  in aux 0 0 false board ;;

let rec seed_life board size nb_cell = match 

(* faisons count_neighbours avec get_cell *)
let test predicat = match predicat with
    0 -> 0
  | _ -> 1 ;;

let count_neighbours (x,y) board =
  let booleen = (get_cell (x,y) board = 1 ) in
  let compter (x,y) c = 
    let c = c + test(get_cell (x-1,y+1) board) in
    let c = c + test(get_cell (x,y+1) board) in
    let c = c + test(get_cell (x+1,y+1) board) in
    let c = c + test(get_cell (x-1,y) board) in
    let c = c + test(get_cell (x+1,y) board) in
    let c = c + test(get_cell (x-1,y-1) board) in
    let c = c + test(get_cell (x,y-1) board) in
    let c = c + test(get_cell (x+1,y-1) board) in
    c 
  in let compt = compter (x,y) 0 in 
  (booleen = false && compt = 3) || (booleen = true && (compt = 2 || compt = 3)) ;;

let rec insert_nth (x,y) v list = match (x,list) with
    (x,_) when x<0 -> invalid_arg "insert_nth : invalid index"
  | (0,[]) -> []
  | (x,[]) -> [v]::[]
  | (0,e::li) -> let rec insert y liste = match (y,liste) with
              (0,l) -> v::l
            | (y,[]) -> v::[]
            | (y,e::l) -> e::insert(y-1) l 
          in insert y e :: insert_nth (0,y) v li 
  | (x,e::li) -> e::insert_nth (x-1,y) v li;;

let seed_life_ board size nb_cell =  
  let rec seed_life_rec board nb_cell = match (nb_cell,board) with
      (0,b) -> b
    | (n,b) -> let v = 1 in
        let x=Random.int(size) and y=Random.int(size) in
        let b = insert_nth (x,y) v b in
        seed_life_rec b (n-1) 
  in seed_life_rec board nb_cell;;
(*
let seed_life board size nb_cell = 
  let rec aux board nb_cell test = match (board,nb_cell,test) with
      ([],0,_) -> []
    | *)

let new_board size nb_cell =
  let board = init_board (size,size) 0 in
  seed_life_ board size nb_cell;;



  
