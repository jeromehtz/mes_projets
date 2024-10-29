#use "list_tools.ml";;

let queue = 
  let rec build_list value taille = match (taille,value) with
      (0,_) -> []
    | (t,v) -> v::build_list (Random.int(11))(t-1) 
  in build_list (Random.int(11))(Random.int(11));;

let head queue = match queue with
    [] -> invalid_arg "head : queue is empty"
  | e::l -> e;;

let dequeue queue = match queue with
    [] -> invalid_arg "head : queue is empty"
  | e::rest -> (e,rest);;

let rec insert_end x liste = match liste with
    [] -> x::[]
  | e::[] -> e::x::[]
  | e::l -> e::insert_end x l;;

let enqueue v list = 
  let rec insert_end x liste = match liste with
      [] -> x::[]
    | e::[] -> e::x::[]
    | e::l -> e::insert_end x l 
  in insert_end v list;;

let rec enqueue_list list queue = match (list,queue) with
    ([],q) -> q
  | (e::l,q) -> enqueue_list l (enqueue e q);;  

let insert_nth i x list = match i with
    i when i<0 -> invalid_arg "insert_nth : invalid index"
  | i -> let rec insert i liste = match (i,liste) with
              (0,l) -> x::l
            | (_,[]) -> failwith "insert_nth : list too short"
            | (i,e::l) -> e::insert(i-1) l 
          in insert i list;;

let put_first list queue = 
  let rec put_ind i list queue = match (list,i) with
    ([],i) -> queue
  | (e::l,i) -> let queue = insert_nth i e queue in put_ind (i+1) l queue 
  in put_ind 0 list queue;;

let sub_queues i j queue = match (i,j) with
    (i,j) when i<0 || j<0 || i>j -> invalid_arg "sub_queues : invalid ranks"
  | (i,j) when j>length queue-1 -> failwith "sub_queues : list too short"
  | _ ->
    let rec sub_queues_1 t queue = match (t,queue) with
        (t,_) when t=i -> []
      | (t,e::q) -> e::sub_queues_1 (t+1) q 
      | (_, []) -> failwith "faisons plaisir a ocaml"
    in 
    let rec sub_queues_2 t queue = match (t,queue) with
        (t,_) when t>j -> []
      | (t,e::q) when t>=i && t<=j -> e::sub_queues_2 (t+1) q
      | (t,e::q) -> sub_queues_2 (t+1) q
      | (_, []) -> failwith "faisons plaisir a ocaml" 
    in
    let rec sub_queues_3 t qu1 queue = match (t,qu1,queue) with
        (_,[],[]) -> []
      | (t,[],e::q) when t>j+2 -> e::sub_queues_3 (t+1) [] q
      | (t,e::q1,q) when t<j-1 -> e::sub_queues_3 (t+1) q1 q
      | (t,[],e::q) -> sub_queues_3 (t+1) [] q
      | (_, _::_, _) -> failwith "faisons plaisir a ocaml"
    in let res = sub_queues_1 0 queue in 
    let res_1 = sub_queues_2 0 queue in 
    let res_2 = sub_queues_3 0 res queue  in (res_1,res_2) ;; 


let half_queues queue = 
  let rec sub_queues_rec t queue = match (t,queue) with
    | (t,q) when t>length queue / 2 -> []
    | (_,[]) -> failwith "pour faire plaisir a caml"
    | (t,e::q) -> e::sub_queues_rec (t+1) q  
  in
  let rec sub_queues_ t queue = match (t,queue) with
      (_,[]) -> []
    | (t,e::q) when t> length queue / 2 -> e::sub_queues_ (t+1) q
    | (t,e::q) -> sub_queues_ (t+1) q
  in (sub_queues_rec 0 queue, sub_queues_ 0 queue) ;;

let change i v1 queue = 
  put_list v1 i queue;;

let swap i j queue =
  change j (nth i queue) (change i (nth j queue) queue);;