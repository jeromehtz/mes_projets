
open Builtin;;

(** Naive power function. Linear complexity
    @param x base
    @param n exponent
 *)

(** gerer le signe et verifier dune runtest a epita **)
let rec pow x n =
    if n = 0 then 1
    else
      x*pow x (n-1) ;;

(** Fast integer exponentiation function. Logarithmic complexity.
    @param x base
    @param n exponent
 *)
let rec power x n = match n with
  | 0 -> 1
  | n ->
    let q,r = (n/2,n mod 2) in
    (if r=0 then
      power(x*x)(q)
    else
      x*power(x*x)(q)) ;;


(** Fast moduler exponentiation function. Logarithmic complexity.
    @param x base
    @param n exponent
    @param m modular base
 *)
let mod_power x n m =
  let rec mod_power_rec x n m =
    if n=0 then 1
    else
      if x<>0 then
        (let (q,r) = (n/2, n mod 2) in
        (if r=0 then mod_power_rec((m) mod (x*x))(q)(m)
        else
          x*mod_power_rec ((m) mod (x*x)) q m))
      else
        0
  in let res = mod_power_rec x n m in
     match (res,n) with
     | (res,n) when n mod 2 = 0 -> res * sign res
     | (res,n) -> if res<n then
                    (n - res) + res
                  else
                    res - n;;

(** Fast modular exponentiation function mod prime. Logarithmic complexity.
    It makes use of the Little Fermat Theorem.
    @param x base
    @param n exponent
    @param p prime modular base
 *)
let prime_mod_power x n p =
  if n = 0 then 1
  else
    let x1 = x mod p and n1 = n mod (p-1) in
    if x1 = 0 then 0
    else
      mod_power x1 n1 p;;
