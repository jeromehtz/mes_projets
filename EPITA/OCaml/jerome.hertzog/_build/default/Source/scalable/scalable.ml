(** A naive implementation of big integers

This module aims at creating a set of big integers naively. Such data
types will be subsequently called bitarrays. A bitarray is a list of
zeros and ones ; first integer representing the sign bit. In this
contexte zero is reprensented by the empty list []. The list is to
be read from left to right ; this is the opposite convention to the
one you usually write binary decompositions with. After the sign bit
the first encountered bit is the coefficient in front of two to
the power zero. This convention has been chosen to ease writing
down code.

 *)

(** Creates a bitarray from a built-in integer.
    @param x built-in integer.
 *)


let rec power x n = match n with
  | 0 -> 1
  | n ->
    let q,r = (n/2,n mod 2) in
    (if r=0 then
      power(x*x)(q)
    else
      x*power(x*x)(q)) ;;

let rec length liste = match liste with
    [] -> 0
  | e::l -> 1+length l;;



let from_int x =
  let rec from_int_rec x list = match x with
    | 1 -> 1::list
    | x -> from_int_rec (x/2) ((x mod 2)::list)
  in from_int_rec x [] ;;

(** Transforms bitarray of built-in size to built-in integer.
    UNSAFE: possible integer overflow.
    @param bA bitarray object.
 *)
let to_int bA =
    let long_bA = length bA in
    let rec aux bA long_bA = match (bA,long_bA) with
        | ([],0) -> 0
        | ([],_) -> invalid_arg "on ne rentre pas dedans"
        | (e::b,l) when e=1 -> power 2 (l-1) + aux b (l-1)
        | (e::b,l) -> aux b (l-1)
    in aux bA (long_bA) ;;


(** Prints bitarray as binary number on standard output.
    @param bA a bitarray.
  *)
let rec print_b bA = match bA with
    | [] -> ()
    | e::b -> print_int e ; print_b b;;


(** Toplevel directive to use print_b as bitarray printer.
    CAREFUL: print_b is then list int printer.
    UNCOMMENT FOR TOPLEVEL USE.
*)
(* #install_printer print_b *)

(** Internal comparisons on bitarrays and naturals. Naturals in this
    context are understood as bitarrays missing a bit sign and thus
    assumed to be non-negative.
*)

(** Comparing naturals. Output is 1 if first argument is bigger than
    second -1 otherwise.
    @param nA A natural, a bitarray having no sign bit.
           Assumed non-negative.
    @param nB A natural.
 *)
let compare_n nA nB =
  let rec list_to_number x = match x with
      [] -> 0
    | e::[] -> e
    | e::l -> e*10 + list_to_number l
  in let n = list_to_number nB
     in let bB = from_int n in
        let rec compare nA bB = match (nA,bB) with
            ([],[]) -> 0
          | (_,[]) -> 1
          | ([],_) -> -1
          | (e1::l1,e2::l2) -> if e1>e2 then
                                 1
                               else
                                 if e1=e2 then
                                   compare l1 l2
                                 else
                                   -1
        in compare nA bB ;;

(** Bigger inorder comparison operator on naturals. Returns true if
    first argument is bigger than second and false otherwise.
    @param nA natural.
    @param nB natural.
 *)
let rec (>>!) nA nB =  match(nA,nB) with
    ([],[]) -> false
  | (_,[]) -> true
  | ([],_) -> false
  | (e1::l1,e2::l2) -> if e1>e2 then
                         true
                       else
                         if e1=e2 then
                           (>>!) l1 l2
                         else
                           false ;;

(** Smaller inorder comparison operator on naturals. Returns true if
    first argument is smaller than second and false otherwise.
    @param nA natural.
    @param nB natural.
 *)
let rec (<<!) nA nB = match(nA,nB) with
    ([],[]) -> false
  | (_,[]) -> false
  | ([],_) -> true
  | (e1::l1,e2::l2) -> if e1>e2 then
                         false
                       else
                         if e1=e2 then
                           (<<!) l1 l2
                         else
                           true ;;

(** Bigger or equal inorder comparison operator on naturals. Returns
    true if first argument is bigger or equal to second and false
    otherwise.
    @param nA natural.
    @param nB natural.
 *)
let rec (>=!) nA nB = match(nA,nB) with
    ([],[]) -> true
  | (_,[]) -> true
  | ([],_) -> false
  | (e1::l1,e2::l2) -> if e1>e2 then
                         true
                       else
                         if e1=e2 then
                           (>=!) l1 l2
                         else
                           false ;;

(** Smaller or equal inorder comparison operator on naturals. Returns
    true if first argument is smaller or equal to second and false
    otherwise.
    @param nA natural.
    @param nB natural.
 *)
let rec (<=!) nA nB = match(nA,nB) with
    ([],[]) -> true
  | (_,[]) -> false
  | ([],_) -> true
  | (e1::l1,e2::l2) -> if e1>e2 then
                         false
                       else
                         if e1=e2 then
                           (<=!) l1 l2
                         else
                           true ;;

(** Comparing two bitarrays. Output is 1 if first argument is bigger
    than second -1 otherwise.
    @param bA A bitarray.
    @param bB A bitarray.
*)
let rec compare_b bA bB = match (bA,bB) with
    ([],[]) -> 0
  | (_,[]) -> 1
  | ([],_) -> -1
  | (e1::l1,e2::l2) -> if e1>e2 then
                         1
                       else
                         if e1=e2 then
                           compare_b l1 l2
                         else
                           -1 ;;

(** Bigger inorder comparison operator on bitarrays. Returns true if
    first argument is bigger than second and false otherwise.
    @param nA natural.
    @param nB natural.
 *)
let (>>) bA bB = match(bA,bB) with
    ([],[]) -> false
  | (_,[]) -> true
  | ([],_) -> false
  | (e1::l1,e2::l2) -> if e1>e2 then
                         true
                       else
                         if e1=e2 then
                           (>>!) l1 l2
                         else
                           false ;;

(** Smaller inorder comparison operator on bitarrays. Returns true if
    first argument is smaller than second and false otherwise.
    @param nA natural.
    @param nB natural.
 *)
let (<<) bA bB = match(bA,bB) with
    ([],[]) -> false
  | (_,[]) -> false
  | ([],_) -> true
  | (e1::l1,e2::l2) -> if e1>e2 then
                         false
                       else
                         if e1=e2 then
                           (<<!) l1 l2
                         else
                           true ;;

(** Bigger or equal inorder comparison operator on bitarrays. Returns
    true if first argument is bigger or equal to second and false
    otherwise.
    @param nA natural.
    @param nB natural.
 *)
let (>>=) bA bB = match(bA,bB) with
    ([],[]) -> true
  | (_,[]) -> true
  | ([],_) -> false
  | (e1::l1,e2::l2) -> if e1>e2 then
                         true
                       else
                         if e1=e2 then
                           (>=!) l1 l2
                         else
                           false ;;

(** Smaller or equal inorder comparison operator on naturals. Returns
    true if first argument is smaller or equal to second and false
    otherwise.
    @param nA natural.
    @param nB natural.
 *)
let (<<=) bA bB = match(bA,bB) with
    ([],[]) -> true
  | (_,[]) -> false
  | ([],_) -> true
  | (e1::l1,e2::l2) -> if e1>e2 then
                         false
                       else
                         if e1=e2 then
                           (<=!) l1 l2
                         else
                           true ;;

(**################################################################**)


(** Sign of a bitarray.
    @param bA Bitarray.
*)
let sign_b bA = match bA with
    [] -> 1
  | e::b -> if e=1 then -1 else 1 ;;

(** Absolute value of bitarray.
    @param bA Bitarray.
*)
let abs_b bA = match bA with
    bA when sign_b bA = 1 -> bA
  | bA when length bA > 8 ->
     invalid_arg "non defini le complement a deux est defini seulement sur 8 bits"
  | bA -> let length = 8 - length bA in
          let rec zero length = match length with
            | 0 -> []
            | l -> 0::zero (l-1) in
          let liste = zero length in
          let rec return_bA liste bA = match bA with
            | [] -> liste
            | e::b -> return_bA (e::liste) b
          in let list = return_bA liste bA in
          let rec c2 bn booleen res = match (bn,booleen) with
            | ([],_) -> res
            | (e::b,false) when e=1 -> c2 b true (1::res)
            | (e::b,true) ->
                if e=1 then
                    c2 b true (0::res)
                else
                    c2 b true (1::res)
            | (e::b,bo) -> c2 b bo (e::res)
        in c2 list false [] ;;
(**
(** Quotient of integers smaller than 4 by 2.
    @param a Built-in integer smaller than 4.
*)
let _quot_t a = if a < 2 then 0 else 1

(** Modulo of integer smaller than 4 by 2.
    @param a Built-in integer smaller than 4.
*)
let _mod_t a = if a = 1 || a = 3 then 1 else 0

(** Division of integer smaller than 4 by 2.
    @param a Built-in integer smaller than 4.
*)
let _div_t a = (_quot_t a, _mod_t a)

(** Addition of two naturals.
    @param nA Natural.
    @param nB Natural.
*)**)
let add_n nA nB = 
  let rec rotate list1 list2 res1 res2  = match (list1,list2) with
      ([],[]) -> (res1,res2)
    | (e1::l1,[]) -> rotate l1 [] (e1::res1) res2
    | ([],e2::l2) -> rotate [] l2 res1 (e2::res2)
    | (e1::l1,e2::l2) -> rotate l1 l2 (e1::res1) (e2::res2) in
  let rec add_n_aux retenue l1 l2 res = match (retenue,l1,l2) with
      (0,[],[]) -> res
    | (r,[],[]) -> r::res
    | (r,[],e2::l2) -> 
      let add = r+e2 in
      (
        if add>=10 then
          add_n_aux 1 [] l2 ((add-10)::res)
        else
          add_n_aux 0 [] l2 (add::res)
      )
    | (r,e1::l1,[]) -> 
      let add = r+e1 in
      (
        if add>=10 then
          add_n_aux 1 l1 [] ((add-10)::res)
        else
          add_n_aux 0 l1 [] (add::res)
      )
    | (r,e1::l1,e2::l2) -> 
      let add = r+e1+e2 in
      (
        if add>=10 then
          add_n_aux 1 l1 l2 ((add-10)::res)
        else
          add_n_aux 0 l1 l2 (add::res)
      ) 
  in let (list1,list2) = rotate nA nB [] []
  in add_n_aux 0 list1 list2 [] ;;

(** Difference of two naturals.
    UNSAFE: First entry is assumed to be bigger than second.
    @param nA Natural.
    @param nB Natural.
*)
let diff_n nA nB = 
  let rec rotate list1 list2 res1 res2  = match (list1,list2) with
      ([],[]) -> (res1,res2)
    | (e1::l1,[]) -> rotate l1 [] (e1::res1) res2
    | ([],e2::l2) -> rotate [] l2 res1 (e2::res2)
    | (e1::l1,e2::l2) -> rotate l1 l2 (e1::res1) (e2::res2) in 
  let rec soustraction retenue list1 list2 res = match (retenue,list1,list2) with
      (0,[],[]) -> res
    | (_,[],_) -> invalid_arg"UNSAFE: First entry is assumed to be bigger than second."
    | (r,e1::l1,[]) -> let sous = e1-0-r in soustraction 0 l1 [] (sous::res)
    | (r,e1::l1,e2::l2) when e1<e2 -> 
        let sous = 10+e1-e2-r in soustraction 1 l1 l2 (sous::res)
    | (r,e1::l1,e2::l2) -> 
      let sous = e1-e2-r in soustraction 0 l1 l2 (sous::res) 
  in let (list1,list2) = rotate nA nB [] [] 
  in soustraction 0 list1 list2 [] ;;

(** Addition of two bitarrays.
    @param bA Bitarray.
    @param bB Bitarray.
 *)
let add_b bA bB = 
  let rec rotate list1 list2 res1 res2  = match (list1,list2) with
      ([],[]) -> (res1,res2)
    | (e1::l1,[]) -> rotate l1 [] (e1::res1) res2
    | ([],e2::l2) -> rotate [] l2 res1 (e2::res2)
    | (e1::l1,e2::l2) -> rotate l1 l2 (e1::res1) (e2::res2) in
  let rec addition retenue list1 list2 re = match (retenue,list1,list2) with
      (0,[],[]) -> re
    | (1,[],[]) -> 1::re
    | (r,e::l1,[]) -> 
      let res = r+e in 
      (if res = 2 then addition 1 l1 [] (0::re)
      else
          addition 0 l1 [] (res::re))
    | (r,[],e::l2) -> 
      let res = r+e in 
      (if res = 2 then addition 1 [] l2 (0::re)
      else
          addition 0 [] l2 (res::re))
    | (r,e1::l1,e2::l2) -> 
      let res = r + e1 + e2 in
      (if res = 2 then
        addition 1 l1 l2 (0::re)
      else
        if res = 3 then
          addition 1 l1 l2 (1::re)
        else
          addition 0 l1 l2 (res::re))
    | (_,_,_) -> invalid_arg"pour rendre la fonction exhaustive" 
  in let (list1,list2) = rotate bA bB [] [] in
  addition 0 list1 list2 [] ;;

(** Difference of two bitarrays.
    @param bA Bitarray.
    @param bB Bitarray.
*)
let diff_b bA bB = 
  let rec rotate list1 list2 res1 res2  = match (list1,list2) with
      ([],[]) -> (res1,res2)
    | (e1::l1,[]) -> rotate l1 [] (e1::res1) res2
    | ([],e2::l2) -> rotate [] l2 res1 (e2::res2)
    | (e1::l1,e2::l2) -> rotate l1 l2 (e1::res1) (e2::res2) in 
  let rec soustraction retenue list1 list2 res = match (retenue,list1,list2) with
      (0,[],[]) -> res
    | (_,[],_) -> invalid_arg"UNSAFE: First entry is assumed to be bigger than second."
    | (r,e1::l1,[]) -> let sous = e1-0-r in soustraction 0 l1 [] (sous::res)
    | (r,e1::l1,e2::l2) when e1<e2 -> 
        let sous = 10+e1-e2-r in 
        (
          if sous=9 then soustraction 1 l1 l2 (1::res)
          else
            soustraction 0 l1 l2 (1::res)
        )
    | (r,e1::l1,e2::l2) -> 
      let sous = e1-e2-r in soustraction 0 l1 l2 (sous::res) 
  in let (list1,list2) = rotate bA bB [] [] 
  in soustraction 0 list1 list2 [] ;;

(** Shifts bitarray to the left by a given natural number.
    @param bA Bitarray.
    @param d Non-negative integer.
*)
let rec shift bA d = []

(** Multiplication of two bitarrays.
    @param bA Bitarray.
    @param bB Bitarray.
*)
let mult_b bA bB = []

(** Quotient of two bitarrays.
    @param bA Bitarray you want to divide by second argument.
    @param bB Bitarray you divide by. Non-zero!
*)
let quot_b bA bB =  []

(** Modulo of a bitarray against a positive one.
    @param bA Bitarray the modulo of which you're computing.
    @param bB Bitarray which is modular base.
 *)
let mod_b bA bB = []

(** Integer division of two bitarrays.
    @param bA Bitarray you want to divide.
    @param bB Bitarray you wnat to divide by.
*)
let div_b bA bB = ([], [])
