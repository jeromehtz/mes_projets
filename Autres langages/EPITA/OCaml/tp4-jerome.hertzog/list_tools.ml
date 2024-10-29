(* fonctions TP3 *)
let rec length list = match list with
    [] -> 0
  | e::l -> 1+length l ;;

let rec init_list n x = match n with
    0 -> []
  | n -> x::init_list (n-1) x ;;

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

let rec put_cell v (x,y) board = match (x,y,board) with
  | (0,0,[]) -> []
  | (_,_,[]) -> invalid_arg"..."
  | (0,y,e::b) -> (put_list v y e)::put_cell v (0,0) b
  | (x,y,e::b) -> e::put_cell v (x-1,y) b ;;


(* DEBUT TP 4 *)

(* EPITA *)
#use "topfind";;
#require "graphics";;

(* MAISON *)
#load "graphics.cma";;

open Graphics ;;
open_graph " 1200x800 " ;;

clear_graph() ;;

let draw_cell (x,y) size color =
  set_color color ;
  fill_rect x y size size ;;

let cell_color = function
  | 0 -> white
  | _ -> black ;;

let draw_board board cellsize =
  let rec draw_board_1 (x,y) board = match board with
    [] -> ()
  | e::b ->
     let rec draw_board_2 (x,y) list = match list with
         [] -> ()
       | elt::l -> draw_cell(x,y) cellsize (cell_color elt) ;
                   draw_board_2 (x,y+cellsize) l
     in draw_board_2 (x,y) e ; draw_board_1 (x+cellsize,y) b
  in draw_board_1 (1,1) board ;;

