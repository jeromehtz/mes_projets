(** Basic arithmetics with builtin integers *)

open Builtin;; 


let gcd x y =
  let rec aux x x1 y r = match r with
      0 -> x1
    | r ->
       let (_,r) = div x y in
       aux r x x r
  in aux x 0 y 1 ;;

(** Extended euclidean division of two integers NOT OCAML DEFAULT.
    Given non-zero entries a b computes triple (u, v, d) such that
    a*u + b*v = d and d is gcd of a and b.
    @param a non-zero integer
    @param b non-zero integer.
*)
let rec bezout a b = match b with
    0 -> (1,0,a)
  | b ->
    let (u,v,d) = bezout(b)(a mod b) in
    (v,u-(quot b a)*v,d);;
