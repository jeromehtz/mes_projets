(** Generating primes *)

(** open Basic_arithmetics;; **)

let is_prime n =
    let rec is_prime_rec i = match i with
          i when i=n -> true
        | i -> n mod i <> 0 && is_prime_rec(i+1) 
    in is_prime_rec 2 ;;

(** List composed of 2 and then odd integers starting at 3.
    @param n limit of list of odd integers, minimum value is 2.
 *)
let init_eratosthenes n =
  let i = 2 in
  let rec init_eratosthenes_rec i = match i with
    | i when i>n -> []
    | i when i=2 -> i::init_eratosthenes_rec (i+1)
    | i -> i::init_eratosthenes_rec (i+2)
  in init_eratosthenes_rec i;;



let eratosthenes n =
  let liste = init_eratosthenes(n)
  in let rec eratosthenes_rec n liste = match liste with
    | [] -> []
    | e::l when is_prime e -> e::eratosthenes_rec n l
    | e::l -> eratosthenes_rec n l
  in eratosthenes_rec n liste;;


let write_list li file =
  let liste_li = [1;2;3;4;5;6;7;8;9;10] in
  let oc = open_out file in
  let rec aux = function
    [] -> close_out oc
    |e::l -> Printf . fprintf oc "%s\n" (string_of_int e); aux l
  in aux liste_li ;;


(** Write a list of prime numbers up to limit into a txt file.
    @param n limit of prime numbers up to which to build up a list of primes.
    @param file path to write to.
*)
let write_list_primes n file =
  let liste_li = eratosthenes n in
  let oc = open_out file in
  let rec aux = function
    [] -> close_out oc
    |e::l -> Printf . fprintf oc "%s\n" (string_of_int e); aux l
  in aux liste_li ;;


(** Read file safely ; catch End_of_file exception.
    @param in_c input channel.
 *)
let input_line_opt in_c =
  try Some (input_line in_c)
  with End_of_file -> None;;

(** Create a list out of reading a line per line channel.
    @param in_c input channel.
 *)
let create_list in_c =
  let rec _create_list in_c =
    match input_line_opt in_c with
    | Some line -> (int_of_string line)::(_create_list in_c)
    | None -> []
  in _create_list in_c;;

(** Load list of primes into OCaml environment.
    @param file path to load from.
 *)
let read_list_primes file =
    let ic = open_in file in
    let try_read () =
    try Some ( input_line ic) with End_of_file -> None in
      let rec loop () = match try_read () with
        Some s -> (int_of_string s)::( loop ())
        | None -> close_in ic; []
    in loop () ;;

(** Get biggest prime.
    @param l list of prime numbers.
 *)
let rec last_element l = match l with
  | [] -> failwith "You're list is empty. "
  | e::[] -> e
  | h::t -> last_element t

(** Get two biggest primes.
    @param l list of prime numbers.
 *)
let rec last_two l = match l with
  | [] | [_] -> failwith "List has to have at least two prime numbers."
  | e::g::[] -> (e, g)
  | h::t -> last_two t

(** Finding couples of primes where second entry is twice the first
    plus 1.
    @param limit positive integer bounding searched for primes.
    @param isprime function testing for (pseudo)primality.
 *)
let double_primes limit isprime =
  let n = 1 and m = 3 and liste = [] in
  let rec double_primes_rec n m liste = match ((n,m),liste) with
  | ((_,m),l) when m>limit -> l
  | ((n,m),l) when is_prime(n) && is_prime(m) -> (n,m)::double_primes_rec (n+1) ((n+1)*2+1) l
  | ((n,m),l) -> double_primes_rec (n+1) ((n+1)*2+1) l
  in double_primes_rec n m liste;;

(** Finding twin primes.
    @param limit positive integer bounding searched for primes.
    @param isprime function testing for (pseudo)primality.
 *)
let twin_primes limit is_prime =
  let n = 1 and m = 3 and liste = [] in
  let rec twin_primes_rec n m liste = match ((n,m),liste) with
    | ((_,m),l) when m>limit -> l
    | ((n,m),l) when is_prime(n) && is_prime(m) -> (n,m)::twin_primes_rec (n+1) ((n+1)+2) l
    | ((n,m),l) -> twin_primes_rec (n+1) ((n+1)*2+1) l
  in twin_primes_rec n m liste;;



