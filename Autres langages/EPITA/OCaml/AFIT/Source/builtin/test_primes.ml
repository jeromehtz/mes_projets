(** Testing for primality *)

(**open Basic_arithmetics ;;
open Power;;**)

(** #use "basic_arithmetics.ml" ;; **)
(**#use "power.ml" ;;**)





(** Deterministic primality test *)
let is_prime n =
    let rec is_prime_rec i = match i with
          i when i=n -> true
        | i -> n mod i <> 0 && is_prime_rec(i+1) 
    in is_prime_rec 2 ;;



(** Primality test based on small Fermat theorem
    @param p tested integer
    @param testSeq sequence of integers against which to test
 *)
let is_pseudo_prime p test_seq = true ;;
